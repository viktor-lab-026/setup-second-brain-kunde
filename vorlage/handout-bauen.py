#!/usr/bin/env python3
"""Baut aus HANDOUT.html (einzige Vorlage) das Handout für einen Kunden.

Beispiel (Claude-App, Windows):
  python3 handout-bauen.py --tool app --vorname anna --kunde Anna --termin 29.10.2026 --start 17:00 \
    --set VORWISSEN_HANDBUCH="Du bist ..." --set SPICKER_TITEL="Beispiele für ..." \
    --set SPICKER_BEISPIELSATZ="die Checkliste" --set-datei SPICKER_ZEILEN=zeilen.html \
    --set HEIKLE_DATEN_TITEL="..." --set HEIKLE_DATEN_TEXT="..." --out index.html

Die Vorlage kennt zwei Fassungen:
  --tool code   VS Code mit Bildern, Schalter Windows/Mac, Prompt-Spickzettel und Skills
  --tool app    Claude-App (Reiter Code), Windows, ohne Bilder, kompakt
Optionale Blöcke (einleitung, prompts, skills, obsidian) schaltest du mit --mit / --ohne.
Nummern der Abschnitte, Seitenleiste und Inhaltsverzeichnis entstehen beim Bauen.
"""
import argparse, datetime, os, re, secrets, string, sys

HIER = os.path.dirname(os.path.abspath(__file__))
STANDARD_OPT = {"code": {"einleitung", "prompts", "skills"}, "app": set()}
ABSTAENDE = [0, 10, 20, 30, 55, 70, 80]  # Minuten ab Start für den Zeitstrahl
STANDARDWERTE = {
    "PROJEKTE": "01.projects", "BEREICHE": "02.areas", "RESSOURCEN": "03.ressources", "ARCHIV": "04.archiv",
    "PROJEKT_ZUSATZ": "", "BEREICH_ZUSATZ": "",
    "ZEITHINWEIS": "Uhrzeiten in deutscher Zeit, als Richtwerte.",
}

def kommagetrennt(s):
    return {x.strip() for x in s.split(",") if x.strip()}

def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--tool", choices=["code", "app"], required=True)
    a.add_argument("--vorname", required=True, help="kleingeschrieben, wird zu setup-<vorname>.md")
    a.add_argument("--kunde", help="Anzeigename in der Überschrift (Standard: Vorname großgeschrieben)")
    a.add_argument("--passwort", help="Standard: zufällig erzeugt (10 Zeichen, klein), wird beim Bauen ausgegeben")
    a.add_argument("--stand", help="Standard: heute")
    a.add_argument("--termin", required=True, help="z. B. 29.10.2026")
    a.add_argument("--start", help="Beginn der Session, z. B. 17:00. Füllt den Zeitstrahl")
    a.add_argument("--mit", default="", help="optionale Blöcke zusätzlich, kommagetrennt")
    a.add_argument("--ohne", default="", help="optionale Blöcke weglassen, kommagetrennt")
    a.add_argument("--set", action="append", default=[], metavar="SCHLÜSSEL=WERT")
    a.add_argument("--set-datei", action="append", default=[], metavar="SCHLÜSSEL=DATEI", help="Wert aus einer Datei")
    a.add_argument("--vorlage", default=os.path.join(HIER, "HANDOUT.html"))
    a.add_argument("--out", required=True)
    args = a.parse_args()

    t = open(args.vorlage, encoding="utf-8").read()

    # 1. Fassung wählen
    for name in ("code", "app"):
        pat = re.compile(r"<!--TOOL:%s-->\n?(.*?)\n?<!--/TOOL-->" % name, re.S)
        t = pat.sub(lambda m: m.group(1) if name == args.tool else "", t)
    if args.tool == "app":
        t = re.sub(r"/\*OSAUTO\*/.*?/\*/OSAUTO\*/", "", t, flags=re.S)
    else:
        t = t.replace("/*OSAUTO*/", "").replace("/*/OSAUTO*/", "")

    # 2. optionale Blöcke
    aktiv = (STANDARD_OPT[args.tool] | kommagetrennt(args.mit)) - kommagetrennt(args.ohne)
    def opt(m):
        return m.group(2) if m.group(1) in aktiv else ""
    t = re.sub(r"<!--OPT:(\w+)-->\n?(.*?)\n?<!--/OPT-->", opt, t, flags=re.S)

    # 3. Abschnitte nummerieren, Seitenleiste und Inhaltsverzeichnis bauen
    nav, toc, n = [], [], 0
    def h2(m):
        nonlocal n
        n += 1
        attrs, text = m.group(1), m.group(2)
        ziel = re.search(r'id="([\w-]+)"', attrs) or re.search(r'data-href="([\w-]+)"', attrs)
        kurz = re.search(r'data-nav="([^"]+)"', attrs).group(1)
        text = text.replace("{{N}}", str(n))
        nav.append('    <li><a href="#%s"><span class="n">%d</span>%s</a></li>' % (ziel.group(1), n, kurz))
        toc.append('<li><a href="#%s">%s</a></li>' % (ziel.group(1), re.sub(r"^\d+ · ", "", text)))
        attrs = re.sub(r'\s*data-nav="[^"]*"', "", attrs)
        attrs = re.sub(r'\s*data-href="[^"]*"', "", attrs)
        return "<h2%s>%s</h2>" % (attrs, text)
    t = re.sub(r"<h2([^>]*data-nav=[^>]*)>(.*?)</h2>", h2, t)
    t = t.replace("<!--NAV-->", "\n".join(nav)).replace("<!--TOC-->", "\n".join(toc))

    # 4. Werte
    kunde = args.kunde or args.vorname.capitalize()
    passwort = (args.passwort or "".join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(10))).lower()
    werte = dict(STANDARDWERTE)
    werte.update({
        "TOOL": args.tool, "VORNAME": args.vorname, "KUNDE": kunde,
        "PASSWORT": passwort,
        "STAND": args.stand or datetime.date.today().strftime("%d.%m.%Y"),
        "TERMIN_DATUM": args.termin,
    })
    if args.start:
        h, m = map(int, args.start.split(":"))
        basis = datetime.datetime(2000, 1, 1, h, m)
        for i, d in enumerate(ABSTAENDE, 1):
            werte["ZEIT_%d" % i] = (basis + datetime.timedelta(minutes=d)).strftime("%H:%M")
    for s in args.set:
        k, _, v = s.partition("=")
        werte[k.strip()] = v
    for s in args.set_datei:
        k, _, pfad = s.partition("=")
        werte[k.strip()] = open(pfad, encoding="utf-8").read().strip("\n")
    for k, v in werte.items():
        t = t.replace("{{%s}}" % k, v)

    # 5. PERSONALISIEREN-Kommentare der Vorlage entfernen
    t = re.sub(r"<!-- PERSONALISIEREN:[^>]*?-->\n?", "", t, flags=re.S)

    offen = sorted(set(re.findall(r"\{\{[A-Z_0-9]+\}\}", t)))
    open(args.out, "w", encoding="utf-8").write(t)
    print("geschrieben: %s (%d Byte), Fassung %s, Blöcke: %s" % (args.out, len(t.encode("utf-8")), args.tool, ", ".join(sorted(aktiv)) or "keine"))
    print("Passwort: %s%s" % (passwort, "" if args.passwort else " (zufällig erzeugt, im Lead-Ordner notieren)"))
    if t.count("—"):
        print("WARNUNG: %d Em-Dashes" % t.count("—"))
    if offen:
        print("OFFEN, noch zu füllen: " + ", ".join(offen))
        return 1
    print("keine offenen Platzhalter")
    return 0

if __name__ == "__main__":
    sys.exit(main())
