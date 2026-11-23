#!/usr/bin/env python3
"""sitzung-eingang.py: erfasst jede beendete Claude-Sitzung für /feierabend.

Drei Aufrufarten:

  (ohne Argumente)         SessionEnd-Hook. Liest das Hook-JSON von stdin, startet den
                           Worker abgekoppelt und kehrt sofort zurück.
  --worker <mitschrift>    Zieht aus einer Sitzung Entscheidungen, Stände und neues Wissen
                           und legt sie als Entwurf in 3-ressourcen/raw/sitzungen/ ab.
  --nachholen <JJJJ-MM-TT> Holt alle Sitzungen dieses Arbeitsordners seit dem Datum nach,
                           die noch nicht erfasst sind ("heute" geht auch). /feierabend
                           ruft das zuerst auf.

Der Hook schreibt nur Entwürfe in den Eingang. Ins Second Brain kommt davon nichts, bevor
du bei /feierabend Ja gesagt hast. Die Sitzungsprotokolle liegen in ~/.claude/projects/.
"""
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

PROJEKT = Path(__file__).resolve().parents[2]
EINGANG = PROJEKT / "3-ressourcen" / "raw" / "sitzungen"
ENTSCHEIDUNGEN = PROJEKT / "3-ressourcen" / "wissen" / "entscheidungen"
TECHNIK = PROJEKT / ".claude" / "sitzung-eingang"
STAND = TECHNIK / "erfasst.json"
PROTOKOLL = TECHNIK / "protokoll.log"
SPERRE = TECHNIK / "sperre"
MODELL = "sonnet"
MAX_DIGEST = 14000
MIN_RUNDEN = 2

PROMPT = """Unten steht der Auszug einer Arbeitssitzung zwischen einer Person und Claude Code. \
ICH sind die Nachrichten der Person, AUSWAHL sind Antworten, die sie in einer Rückfrage \
angeklickt hat, CLAUDE sind Claudes Abschlussmeldungen.

Zieh drei Dinge heraus, aber nur, was die Person selbst gesagt, ausgewählt oder \
ausdrücklich bestätigt hat. Vorschläge von Claude ohne Zustimmung zählen nicht. \
Nichts erfinden, nichts ergänzen, was nicht im Auszug steht.

1. "entscheidungen": Richtungs-Entscheidungen, also Preise, Angebote, Zielgruppe, \
Zusammenarbeit, Tool- und Systemwahl, Aufbau der Ordner, Rechts- und Datenschutzfragen. \
Nicht dazu gehören Tagesgeschäft, Termine, Aufgaben, einzelne Formulierungen in einem \
Text und technische Kleinigkeiten.
2. "stand": fachliche Projekt- oder Statusänderungen (etwas fertig, verschoben, zugesagt, \
abgesagt, eine Zahl geändert). Nicht dazu gehören Dateien, die Claude gebaut oder \
geändert hat, die stehen schon auf der Platte.
3. "wissen": dauerhaftes Sachwissen, das die Person selbst genannt oder bestätigt hat \
(Abläufe, Fachwissen, Vorlagen). Nicht dazu gehören Termine und Aufgaben, die in einer \
Woche überholt sind.

Datenschutz: keine Klarnamen von Kundinnen und Kunden (nimm ein Kürzel oder lass es weg), \
keine Gesundheits-, Bank- oder Zugangsdaten. Enthält ein Zitat so etwas, lass das Feld \
"beleg" leer.

Was unter BEREITS ERFASST steht, nicht noch einmal aufnehmen. Meistens sind alle drei \
Listen leer, das ist richtig so.

Antworte NUR mit JSON in genau dieser Form, ohne Vorrede, ohne Codeblock:
{{"entscheidungen": [{{"titel": "Satz, der die Wahl nennt", "frage": "was stand zur Wahl", \
"wahl": "wofür sich die Person entschieden hat", \
"warum": "der Grund, so wie die Person ihn genannt hat, sonst leer", \
"verworfen": "Alternativen und warum nicht, sonst leer", \
"betrifft": "Projekt, Ordner oder Datei, sonst leer", \
"beleg": "wörtliches Zitat aus ICH oder AUSWAHL, höchstens 200 Zeichen"}}], \
"stand": [{{"was": "ein Satz", "wo": "Projekt oder Datei, in die es gehört", \
"beleg": "wörtliches Zitat aus ICH oder AUSWAHL, höchstens 200 Zeichen"}}], \
"wissen": [{{"titel": "kurzer Titel", "inhalt": "zwei bis vier Sätze in einfachen Worten", \
"beleg": "wörtliches Zitat aus ICH oder AUSWAHL, höchstens 200 Zeichen"}}]}}

Deutsch mit echten Umlauten, keine Gedankenstriche.

BEREITS ERFASST (letzte 21 Tage):
{bekannt}

SITZUNG:
{digest}
"""


def notiere(text):
    TECHNIK.mkdir(parents=True, exist_ok=True)
    with open(PROTOKOLL, "a", encoding="utf-8") as f:
        f.write(f"{dt.datetime.now():%Y-%m-%d %H:%M:%S} {text}\n")


def saeubern(text):
    text = re.sub(r"<system-reminder>.*?</system-reminder>", "", text, flags=re.S)
    text = re.sub(r"<(command-message|command-args|local-command-stdout)>.*?</\1>", "", text, flags=re.S)
    text = re.sub(r"</?command-name>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def schwaerzen(text):
    """Nimmt offensichtliche Zugangs- und Kontodaten raus, bevor Text weitergegeben wird."""
    text = re.sub(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", "[E-Mail]", text)
    text = re.sub(r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,7}(?: ?[A-Z0-9]{1,4})?\b", "[IBAN]", text)
    text = re.sub(r"\b(?:sk|pk|ghp|xox[bp])[-_][A-Za-z0-9_-]{16,}", "[Schlüssel]", text)
    text = re.sub(r"\b(?=[A-Za-z0-9]*\d)(?=[A-Za-z0-9]*[A-Za-z])[A-Za-z0-9]{32,}\b", "[Schlüssel]", text)
    return re.sub(r"(?<!\d)(?:\+\d{1,3}|0)[\d /()-]{8,}\d", "[Telefon]", text)


def lies_mitschrift(pfad, ab_zeile):
    """Gibt (digest, zeilenzahl, letzter_zeitpunkt, anzahl_runden) zurück."""
    titel, runden, dateien = "", [], []
    letzte_antwort, zeitpunkt, n = "", None, 0
    fragen = set()
    with open(pfad, encoding="utf-8", errors="replace") as f:
        for n, roh in enumerate(f, 1):
            try:
                e = json.loads(roh)
            except ValueError:
                continue
            typ = e.get("type")
            if typ == "ai-title":
                titel = e.get("title") or e.get("aiTitle") or titel
                continue
            if n <= ab_zeile or e.get("isSidechain"):
                continue
            if e.get("timestamp"):
                zeitpunkt = e["timestamp"]
            inhalt = (e.get("message") or {}).get("content")
            if typ == "user" and isinstance(inhalt, list):
                # Klicks in AskUserQuestion stehen nur als tool_result im Protokoll
                for b in inhalt:
                    if b.get("type") != "tool_result" or b.get("tool_use_id") not in fragen:
                        continue
                    roh_text = b.get("content")
                    if isinstance(roh_text, list):
                        roh_text = " ".join(x.get("text", "") for x in roh_text if isinstance(x, dict))
                    if isinstance(roh_text, str):
                        text = saeubern(roh_text).replace("Your questions have been answered: ", "")
                        text = text.replace(" You can now continue with these answers in mind.", "")
                        if letzte_antwort and runden:
                            runden[-1]["claude"] = letzte_antwort[-700:]
                        runden.append({"ich": "AUSWAHL: " + text[:600], "claude": ""})
                        letzte_antwort = ""
            if typ == "user" and not e.get("isMeta"):
                if isinstance(inhalt, str):
                    text = saeubern(inhalt)
                elif isinstance(inhalt, list) and all(b.get("type") == "text" for b in inhalt):
                    text = saeubern(" ".join(b.get("text", "") for b in inhalt))
                else:
                    text = ""
                if text and not text.startswith("Base directory for this skill"):
                    if letzte_antwort and runden:
                        runden[-1]["claude"] = letzte_antwort[-700:]
                    runden.append({"ich": text[:600], "claude": ""})
                    letzte_antwort = ""
            elif typ == "assistant" and isinstance(inhalt, list):
                for b in inhalt:
                    if b.get("type") == "text" and b.get("text", "").strip():
                        letzte_antwort = saeubern(b["text"])
                    elif b.get("type") == "tool_use" and b.get("name") == "AskUserQuestion":
                        fragen.add(b.get("id"))
                    elif b.get("type") == "tool_use" and b.get("name") in ("Write", "Edit"):
                        p = (b.get("input") or {}).get("file_path", "")
                        p = p.replace(str(PROJEKT) + os.sep, "")
                        if p and p not in dateien:
                            dateien.append(p)
    if letzte_antwort and runden:
        runden[-1]["claude"] = letzte_antwort[-900:]

    def baue(auswahl):
        teile = [f"TITEL: {titel}"] if titel else []
        for r in auswahl:
            teile.append(f"ICH: {r['ich']}")
            if r["claude"]:
                teile.append(f"CLAUDE: {r['claude']}")
        if dateien:
            teile.append("GESCHRIEBENE DATEIEN: " + ", ".join(dateien[:25]))
        return "\n".join(teile)

    digest = baue(runden)
    while len(digest) > MAX_DIGEST and len(runden) > 6:
        del runden[3]
        digest = baue(runden)
    return schwaerzen(digest[:MAX_DIGEST]), n, zeitpunkt, len(runden)


def lokale_zeit(iso):
    if not iso:
        return dt.datetime.now()
    try:
        return dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone().replace(tzinfo=None)
    except ValueError:
        return dt.datetime.now()


def frage_claude(prompt):
    claude = shutil.which("claude") or str(Path.home() / ".local" / "bin" / "claude")
    lauf = subprocess.run(
        [claude, "-p", "--model", MODELL, "--tools", "", "--no-session-persistence",
         "--strict-mcp-config", "--disable-slash-commands", "--output-format", "text"],
        input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=240,
        env=dict(os.environ, SITZUNG_EINGANG_WORKER="1"), cwd=str(Path.home() / ".claude"),
    )
    if lauf.returncode != 0:
        raise RuntimeError(f"claude exit {lauf.returncode}: {lauf.stderr.strip()[:300]}")
    return lauf.stdout.strip()


def flach(text):
    return re.sub(r"\s+", " ", re.sub(r"[„“\"'‚‘’«»]", "", text or "")).strip().lower()


def bekannte_eintraege():
    ab = f"{dt.date.today() - dt.timedelta(days=21):%Y-%m-%d}"
    zeilen = []
    if ENTSCHEIDUNGEN.exists():
        zeilen += [f"- {p.stem}" for p in sorted(ENTSCHEIDUNGEN.glob("*.md")) if p.name[:10] >= ab]
    if EINGANG.exists():
        for p in sorted(EINGANG.glob("*.md")):
            zeilen += [z[4:].strip() and f"- (Eingang) {z[4:].strip()}"
                       for z in p.read_text(encoding="utf-8").splitlines() if z.startswith("### ")]
    return "\n".join(zeilen) or "(nichts)"


def schreibe_eingang(sitzung, wann, digest):
    """Legt Entwürfe in den Eingang. Gibt die Zahl der Einträge zurück."""
    antwort = frage_claude(PROMPT.format(bekannt=bekannte_eintraege(), digest=digest))
    treffer = re.search(r"\{.*\}", antwort, flags=re.S)
    if not treffer:
        raise RuntimeError(f"kein JSON: {antwort[:200]}")
    daten = json.loads(treffer.group(0))
    entsch = [e for e in daten.get("entscheidungen") or [] if e.get("titel") and e.get("wahl")]
    stand = [s for s in daten.get("stand") or [] if s.get("was")]
    wissen = [w for w in daten.get("wissen") or [] if w.get("titel") and w.get("inhalt")]
    if not (entsch or stand or wissen):
        return 0
    titel = digest.split("\n", 1)[0].replace("TITEL: ", "") if digest.startswith("TITEL: ") else sitzung[:8]
    roh = flach(digest)

    def beleg(text):
        text = schwaerzen((text or "").strip())
        if not text:
            return "(kein Zitat)"
        gefunden = flach(text)[:80] in roh
        return f"„{text}“" + ("" if gefunden else " (nicht wörtlich im Protokoll gefunden, prüfen)")

    teile = ["---", f"sitzung: {sitzung}", f"zeit: {wann:%Y-%m-%d %H:%M}", "status: offen", "---", "",
             f"# Eingang aus „{titel}“, {wann:%d.%m.%Y %H:%M}", "",
             "Entwurf aus der Sitzung. Ins Second Brain kommt davon erst etwas, wenn ich bei /feierabend Ja sage.", ""]
    if entsch:
        teile += ["## Entscheidungen", ""]
        for e in entsch:
            teile += [f"### {e['titel'].strip()}", "",
                      f"- **Frage:** {e.get('frage', '').strip()}",
                      f"- **Wahl:** {e['wahl'].strip()}",
                      f"- **Warum:** {e.get('warum', '').strip() or '(nicht genannt)'}",
                      f"- **Verworfen:** {e.get('verworfen', '').strip() or '(nicht genannt)'}",
                      f"- **Betrifft:** {e.get('betrifft', '').strip()}",
                      f"- **Beleg:** {beleg(e.get('beleg'))}", ""]
    if stand:
        teile += ["## Stände", ""]
        for s in stand:
            teile.append(f"- {s['was'].strip()} → {s.get('wo', '').strip() or '?'} · Beleg: {beleg(s.get('beleg'))}")
        teile.append("")
    if wissen:
        teile += ["## Neues Wissen", ""]
        for w in wissen:
            teile += [f"### {w['titel'].strip()}", "", w["inhalt"].strip(), "", f"Beleg: {beleg(w.get('beleg'))}", ""]
    EINGANG.mkdir(parents=True, exist_ok=True)
    (EINGANG / "erledigt").mkdir(exist_ok=True)
    (EINGANG / f"{wann:%Y-%m-%d_%H%M}_{sitzung[:8]}.md").write_text("\n".join(teile), encoding="utf-8")
    return len(entsch) + len(stand) + len(wissen)


def sperre_holen():
    """Einfache Sperre, damit Hook und /feierabend dieselbe Sitzung nicht doppelt erfassen."""
    TECHNIK.mkdir(parents=True, exist_ok=True)
    ende = time.time() + 300
    while True:
        try:
            os.close(os.open(SPERRE, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            return
        except FileExistsError:
            if time.time() > ende or time.time() - SPERRE.stat().st_mtime > 600:
                return
            time.sleep(2)


def sperre_loesen():
    try:
        SPERRE.unlink()
    except FileNotFoundError:
        pass


def verarbeite(pfad):
    pfad = Path(pfad)
    sitzung = pfad.stem
    sperre_holen()
    try:
        stand = json.loads(STAND.read_text(encoding="utf-8")) if STAND.exists() else {}
        ab = stand.get(sitzung, 0)
        digest, zeilenzahl, zeitpunkt, runden = lies_mitschrift(pfad, ab)
        if runden < MIN_RUNDEN or zeilenzahl <= ab:
            if runden == 0:
                stand[sitzung] = max(ab, zeilenzahl)
                STAND.write_text(json.dumps(stand, indent=1), encoding="utf-8")
            notiere(f"{sitzung}: zu kurz oder nichts Neues")
            return
        wann = lokale_zeit(zeitpunkt)
        try:
            n = schreibe_eingang(sitzung, wann, digest)
            notiere(f"{sitzung}: {n} Einträge" if n else f"{sitzung}: nichts Festhaltenswertes")
        except Exception as fehler:
            notiere(f"FEHLER {sitzung}: {fehler}")
            return
        stand[sitzung] = zeilenzahl
        STAND.write_text(json.dumps(stand, indent=1), encoding="utf-8")
    finally:
        sperre_loesen()


def mitschriften_ordner():
    name = re.sub(r"[^A-Za-z0-9]", "-", str(PROJEKT))
    return Path.home() / ".claude" / "projects" / name


def main():
    if len(sys.argv) == 1:
        if os.environ.get("SITZUNG_EINGANG_WORKER") == "1":
            return 0
        try:
            daten = json.load(sys.stdin)
        except ValueError:
            return 0
        pfad = daten.get("transcript_path")
        if pfad and os.path.exists(pfad):
            TECHNIK.mkdir(parents=True, exist_ok=True)
            optionen = {"start_new_session": True} if os.name != "nt" else {
                "creationflags": subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP}
            with open(PROTOKOLL, "a") as log:
                subprocess.Popen([sys.executable, __file__, "--worker", pfad],
                                 stdin=subprocess.DEVNULL, stdout=log, stderr=log, **optionen)
        return 0
    if sys.argv[1] == "--worker" and len(sys.argv) > 2:
        try:
            verarbeite(sys.argv[2])
        except Exception as fehler:  # nie laut scheitern, nur notieren
            notiere(f"FEHLER {Path(sys.argv[2]).stem}: {fehler}")
        return 0
    if sys.argv[1] == "--nachholen" and len(sys.argv) > 2:
        tag = dt.date.today().isoformat() if sys.argv[2] == "heute" else sys.argv[2]
        seit = dt.datetime.strptime(tag, "%Y-%m-%d").timestamp()
        dateien = [p for p in mitschriften_ordner().glob("*.jsonl")
                   if seit <= p.stat().st_mtime < time.time() - 900]
        dateien.sort(key=lambda p: p.stat().st_mtime)
        for i, p in enumerate(dateien, 1):
            print(f"[{i}/{len(dateien)}] {p.stem}", flush=True)
            try:
                verarbeite(p)
            except Exception as fehler:
                notiere(f"FEHLER {p.stem}: {fehler}")
                print(f"  FEHLER: {fehler}", flush=True)
        print(f"Eingang: {len(list(EINGANG.glob('*.md'))) if EINGANG.exists() else 0} offene Dateien", flush=True)
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
