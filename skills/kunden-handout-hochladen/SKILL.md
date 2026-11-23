---
name: kunden-handout-hochladen
description: Baut den Leitfaden (das Handout) zur Setup-Session eines Kunden aus der einzigen zentralen Vorlage (Zeitstrahl, Inhaltsverzeichnis, Fassung VS Code oder Claude-App) und veröffentlicht ihn auf lehrconsult.de/<vorname>/ mit Passwort, . Trigger "Handout für [Kunde] bauen", "Leitfaden für [Kunde]", "Handout für [Kunde] hochladen", "Handout auf lehrconsult", ""Kunden-Handout online stellen", "Seite für die Setup-Session veröffentlichen", "Zeitstrahl ins Handout". Nicht für Landingpages (landingpage-viktor), nicht für die Setup-Datei allein (setup-session-kunde), nicht für Anleitungen ohne Setup (kundenanleitung).
---

# Leitfaden bauen und hochladen

Seit 29.10.2026 gibt es **eine** Handout-Vorlage (Single Source of Truth). Der Leitfaden begleitet die Setup-Session, liegt auf `lehrconsult.de/<vorname>/` hinter einem Passwort-Gate im Browser und trägt `noindex`. Oben steht der Zeitstrahl „Ablauf“ , links das Inhaltsverzeichnis, am Ende der Spicker.

**Vorlage und Bauskript** (Pfade relativ zu `/Users/viktorlehr/Library/CloudStorage/OneDrive-TheNomadSpirit/Second Brain/1. LEHRCONSULT/`):

| Datei | Zweck |
|---|---|
| `03-resources/templates/setup-second-brain-kunde/HANDOUT.html` | einzige Vorlage, beide Fassungen |
| `03-resources/templates/setup-second-brain-kunde/handout-bauen.py` | baut daraus die Kundenfassung |
| `03-resources/templates/setup-second-brain-kunde/SETUP.md` | zugehörige Setup-Datei (Skill `setup-session-kunde`) |
| `03-resources/templates/setup-second-brain-kunde/LIESMICH.md` | Pflegehinweise, Nachträge |

Eine Verbesserung am Handout gehört **in die Vorlage** (mit Nachtrag in `LIESMICH.md`), nie nur in die Kundendatei. Alte Einzelfassungen (`HANDOUT-claude-app.html` und die VS-Code-Fassung vor dem 29.10.2026) liegen unter `04-archive/2026/system/setup-second-brain-kunde-legacy/` und werden nicht mehr benutzt.

## Vorher

1. **Setup-Datei steht schon** (`setup-<vorname>.md`, Skill `setup-session-kunde`), im Lead-Ordner unter `materialien/handout-claude-setup/`. Das Vorwissen zum Kunden steht dort im Abschnitt „Was Viktor schon weiß“ (`{{BEKANNT}}`). Frisch von der Platte lesen.
2. **Fassung wählen, ohne zu fragen:** Das Werkzeug steht in `status.md` des Leads.
   - `--tool app`: Claude-App, Reiter Code (kompakt, Windows, ohne Bilder, keine optionalen Blöcke). 
   - `--tool code`: VS Code (lang, Bilder, Schalter Windows/Mac, Blöcke `einleitung`, `prompts`, `skills`).  Der Ordner `bilder/` der Vorlage (ohne `markieren.py`) muss mit hochgeladen werden.
3. **Textbausteine aus dem Vorwissen schreiben** (Beleg-Pflicht: nichts erfinden, nur was belegt ist):
   - `VORWISSEN_HANDBUCH`: ein bis zwei Sätze, wer der Kunde ist und woran er baut, für „Dein Handbuch“.
   - `SPICKER_TITEL`, `SPICKER_BEISPIELSATZ` und die Tabellenzeilen `SPICKER_ZEILEN` (Datei mit `<tr><td>Du willst</td><td>„Du schreibst“</td></tr>` je Zeile): Beispielaufträge aus dem Vorwissen.
   - `HEIKLE_DATEN_TITEL` und `HEIKLE_DATEN_TEXT`: die heiklen Daten seiner Branche (fehlt etwas Belegtes, benenne sie allgemein).
   - Nur bei `code` mit Einleitung: `WOFUER_EINSTIEG` (zwei bis drei Sätze in seinen Worten) und `BEISPIEL_AUFGABEN` (zwei bis drei echte Aufgaben im Akkusativ).
   - Optional: `PROJEKT_ZUSATZ` und `BEREICH_ZUSATZ` (Beispielordner im Ordnerabschnitt), `PROJEKTE`, `BEREICHE`, `RESSOURCEN`, `ARCHIV` (Standard `01.projects`, `02.areas`, `03.ressources`, `04.archiv`; bei anderen Namen im Kunden-Setup überschreiben).

## Bauen

```bash
V="/Users/viktorlehr/Library/CloudStorage/OneDrive-TheNomadSpirit/Second Brain/1. LEHRCONSULT/03-resources/templates/setup-second-brain-kunde"
python3 "$V/handout-bauen.py" --tool app --vorname <vorname> --kunde "<Anzeigename>" \
  --termin TT.MM.JJJJ --start HH:MM \
  --set VORWISSEN_HANDBUCH="..." --set SPICKER_TITEL="..." --set SPICKER_BEISPIELSATZ="..." \
  --set-datei SPICKER_ZEILEN=zeilen.html \
  --set HEIKLE_DATEN_TITEL="..." --set HEIKLE_DATEN_TEXT="..." \
  --out "<lead>/materialien/handout-claude-setup/index.html"
```

- `--start` ist der Beginn der Session in **deutscher Zeit** und füllt den Zeitstrahl (Abstände 0/10/20/30/55/70/80 Minuten). Fehlt er, bleiben `{{ZEIT_1}}` bis `{{ZEIT_7}}` offen.
- Passwort: Standard ist ein zufälliges Passwort (10 Zeichen, klein), das Skript gibt es beim Bauen aus. Im Lead-Ordner notieren und dem Kunden mitschicken. Ein eigenes nur mit `--passwort` (wird kleingeschrieben, das Gate vergleicht klein). Nie ein Muster aus Vorname und Jahr (seit 23.11.2026, das Repo ist öffentlich).
- Das Skript meldet offene Platzhalter (Exit 1) und Em-Dashes. Beides muss leer sein.
- Abschnittsnummern, Seitenleiste und Inhaltsverzeichnis entstehen beim Bauen. Zusätze, die nicht in der Vorlage stehen, kommen als eigener Abschnitt vor „Wenn etwas hakt“ in die gebaute Datei, mit Nummern und Seitenleiste nachgezogen und mit Primärquelle samt Prüfdatum.
- Kopie von `setup-<vorname>.md` liegt im selben Ordner (Download-Knopf im Handout verweist darauf, Name `setup-<vorname>.md`).

## Prüfen

1. `grep -c '{{' index.html` ergibt 0, `grep -c '—' index.html` ebenfalls.
2. `grep -niwE '<Namen früherer Kunden>' index.html`: Vornamen aus den Ordnern unter `02-areas/crm/leads/` lesen, jeden Treffer prüfen.
3. Sicht-Check: Headless-Chrome-Screenshot (mit echtem `HOME` und eigenem `--user-data-dir`, nie mit umgebogenem `HOME`). Um das Gate zu umgehen, in einer Testkopie `<body class="` zu `<body class="unlocked ` machen. Zeitstrahl, Seitenleiste (zweistellige Nummern ohne Umbruch), Spicker ansehen.
4. Stil: Du, echte Umlaute, keine Em-Dashes, keine „Nicht X, sondern Y“-Sätze. **Preise und Angebotsdetails gehören nie ins Handout.** Das Gate ist eine Hürde, kein Tresor: keine vertraulichen Inhalte.
5. Schritte zur Oberfläche (Code-Tab) nur beschreiben, was belegt ist. Offenes vermerkst du in `status.md`.

## Hochladen

Ausdrückliche Freigabe von Viktor einholen (außenwirksam), wenn er nicht schon „lade hoch“ gesagt hat. Dann nach Skill `webgo-upload`, ein Lauf (Passwort nie in Chat oder Log schreiben):

```bash
export PW="$(security find-generic-password -a <webgo-benutzer> -s webgo-sftp -w)"
for f in index.html setup-<vorname>.md; do
  curl -sS --ftp-pasv --ftp-create-dirs --user "<webgo-benutzer>:$PW" -T "$f" \
    "ftp://<webgo-host>/lehrconsult.de/<vorname>/$f" -w "$f: %{http_code} · %{size_upload} B\n"
done
```

Fassung `code`: Ordner `bilder/` mit hochladen (`lehrconsult.de/<vorname>/bilder/`), danach jedes Bild per HTTP prüfen. Bei `530` gilt der SFTP-Weg aus dem Skill `webgo-upload`.

## Festhalten

1. HTTP 200 für `/<vorname>/` und `/<vorname>/setup-<vorname>.md`, `diff` gegen die lokalen Dateien: byte-gleich.
2. Seite im Chrome öffnen (`open -a "Google Chrome" URL`).
3. In `<lead>/status.md` eintragen: Link, Passwort, Größen, was ungeprüft ist.
4. Viktor melden: Link und Passwort zum Weitergeben an den Kunden.

## Spiegel auf GitHub

Vorlage, Bauskript und Skills spiegeln im privaten Repo `viktor-lab-026/setup-second-brain-kunde`. Die Quelle der Wahrheit bleibt der Workspace-Ordner. Ins Repo kommen nur `SETUP.md`, `HANDOUT.html`, `handout-bauen.py`, `LIESMICH.md`, `bilder/` und die Skills, nie Lead-Ordner, Kundenhandouts, Passwörter oder Zugangsdaten. Pushen nur nach Freigabe.
