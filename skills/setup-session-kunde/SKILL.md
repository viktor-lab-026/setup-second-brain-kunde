---
name: setup-session-kunde
description: Nutzen, wenn Viktor eine 1:1-Setup-Session (Claude Code einrichten, Second Brain, Briefing, Befehle) für einen Kunden oder eine Kundin vorbereiten will. Trigger "Setup-Session für [Name] vorbereiten", ""Setup-Datei und Handout für [Kunde]", "neuer Kunde fürs Claude-Setup", "/setup-session-kunde". NICHT für KI-Werkstatt-Sessions (werkstatt), Hilker-Trainingstage (hilker-trainingstag), allgemeine Anleitungen ohne Setup (kundenanleitung).
---

# Setup-Session für einen Kunden vorbereiten

**Kernprinzip:** Die Setup-Datei läuft bei jedem Kunden gleich, sie kommt aus der zentralen Vorlage. Den Kunden tragen das Handout und der Use-Case-Plan. Deshalb steht das Kundenprofil am Anfang, und alles Persönliche fließt aus ihm.

**Quellen, vor jedem Lauf frisch lesen:**

| Datei | Wofür |
|---|---|
| `03-resources/templates/setup-second-brain-kunde/SETUP.md` | Setup-Datei, Grundsetup (Etappen 0 bis 6, mit CLAUDE.md zuerst, `/interview`, vier Befehlen, Monatsprüfung als Automation). Die Bausteine A bis D stehen seit 27.10.2026 im Archiv (`LIESMICH.md`) |
| `03-resources/templates/setup-second-brain-kunde/HANDOUT.html` + `handout-bauen.py` | Einzige Handout-Vorlage (Single Source of Truth, seit 29.10.2026): beide Fassungen VS Code und Claude-App, Zeitstrahl, Inhaltsverzeichnis. Gebaut und veröffentlicht wird sie über den Skill `kunden-handout-hochladen` |
| `03-resources/templates/setup-second-brain-kunde/LIESMICH.md` | Zeiten, Reibungspunkte, Testauftrag |
| `03-resources/templates/setup-second-brain-kunde/bilder/` | sieben Screenshots mit Markierungen für die Schritte 1 bis 5 (seit 02.10.2026) |
| `module.md` (dieser Ordner) | Welcher Kundenwunsch wohin gehört, mit Zeitbedarf |
| `kundenprofil-vorlage.md` (dieser Ordner) | Gerüst für Phase 1 |

Pfade relativ zu `/Users/viktorlehr/Library/CloudStorage/OneDrive-TheNomadSpirit/Second Brain/1. LEHRCONSULT/`. Alles zum Kunden liegt in `02-areas/crm/leads/<Vorname Nachname>/`. Frühere Leadordner dienen nur als Anschauung, sie werden nie kopiert.

**Standard-Lieferung:** Kundenprofil, Setup-Datei, Handout, Use-Case-Plan, Testlauf, Upload. Trainingsleitfaden, Demo-Menü und Vorab-Mail entstehen nur, wenn Viktor sie ausdrücklich nennt. „das übliche Paket“ meint die Standard-Lieferung, dafür fragst du nicht nach. Die drei Extras bietest du am Ende einmal an.

**Dateidatum:** `<JJJJ-MM-TT>` in Dateinamen ist immer das Termindatum.

**Der Haltepunkt nach Phase 2 gilt auch gegen die Workspace-Regel „nie nach Bestätigung fragen“.** Die Modulwahl ist Viktors Entscheidung und kein Vollzug eines Auftrags.

---

## Phase 1: Kundenprofil

Nichts bauen, bevor das Profil steht und Viktor es freigegeben hat.

1. **Vorhandenes suchen:** Leadordner, lokales CRM (Skill `crm-status`), Notion CRM, Mail.app nach dem Namen. Dazu den Apple-Kalender rund um den Termin: Steht er schon drin, gibt es Überschneidungen?
2. **Viktor fragen, in einer einzigen Nachricht**, alles, was nach Schritt 1 fehlt. Die Punkte stehen in `kundenprofil-vorlage.md`. Frag dabei immer nach Website und Kanälen und, falls der Kunde geschrieben hat, nach dem Wortlaut seiner Mail. Liefert Schritt 1 schon Links, startest du Schritt 3 sofort und fragst parallel.
3. **Web-Recherche**, sobald Links oder Firmenname da sind: `recherche-agent` im Hintergrund zu Angebot, Ton (Kernsätze wörtlich), Kanälen und Vorgaben einer Dachmarke. Jede Aussage mit URL. Bis zur Bestätigung gilt alles als **Vermutung**. Neue Lücken aus der Recherche kommen als offene Fragen ins Profil, eine zweite Rückfrage an Viktor gibt es dafür nicht.
4. **Profil schreiben** nach `gespraechsvorbereitung/kundenprofil-<JJJJ-MM-TT>.md`, Gerüst aus der Vorlage. Wünsche und Kernproblem **wörtlich** übernehmen, sie landen später im Handout.

## Phase 2: Module wählen

1. Jeden Wunsch und jede Frage aus dem Profil **genau einem Ziel** zuordnen, nach `module.md`: Setup-Baustein, Handout-Zusatz, Use-Case-Plan oder Folgetermin. Kein Wunsch fällt still weg.
2. Zeit rechnen: Kern plus gewählte Bausteine plus Use Case gegen die Termindauer. Reicht sie nicht, Kürzung vorschlagen, nach der Reihenfolge in `module.md`. „Kern Wort für Wort“ betrifft den Text der Setup-Datei, im Termin darf der Kern trotzdem schneller laufen (Kundenmail in Etappe 2 einfügen lassen, `/fragen` und `/pruefung` nur benennen).
3. **Haltepunkt:** Profil in fünf Zeilen, Zuordnungstabelle, Zeitsumme, offene Fragen. Auf Viktors Okay warten.

## Phase 3: Setup-Datei

Vorlage kopieren nach `materialien/handout-claude-setup/setup-<kunde>.md`. `<kunde>` ist der Vorname klein, ohne Umlaute.

Ändern darfst du nur das hier:
- Titelzeile `# Setup: Dein eigenes KI-System · für <Vorname>`. Dazu `{{VORNAME}}` im Kopf und bei Baustein C `{{HANDOUT-URL}}` (`https://lehrconsult.de/<kunde>/` mit Schrägstrich am Ende)
- Pronomen und Anrede bei einer Kundin: er/ihn/ihm/sein auf sie/ihr, „der Kunde“ und „dem Kunden“ auf „die Kundin“ und „der Kundin“. Jede Stelle von Hand prüfen, weil „er“ auch Claude, Ordner und Eingangskorb meint. Die Mehrzahl „Kunden“ bleibt, wo sie die Kundschaft meint
- Frage 5 in Etappe 3 an den Beruf anpassen: die heiklen Daten der Branche ergänzen, bei Selbstständigen den Teil über den Arbeitgeber streichen
- Nicht gewählte Bausteine **ganz** löschen, auch ihre Zeilen in Etappe 6 (Übersicht, Kontrollen)
- Verweise auf gelöschte Bausteine überall glätten, auch im Kern: etwa „Graph-Gruppe aus B3“ in Etappe 1, „Position: nach Baustein B“ oder „Vorweg für C und D“. Suche mit `grep -nE 'Baustein [A-D]|B[1-3]|C und D' setup-<kunde>.md` und lies jeden Treffer. Das zählt nicht als Änderung am Kern
- Die Trainer-Notiz unter `# Bausteine` („Die folgenden Bausteine sind optional …“) löschen, sie ist nicht für den Kunden bestimmt
- Gewählte Bausteine an ihre Stelle im Ablauf verschieben: A zwischen Etappe 3 und 4, B, C und D in dieser Reihenfolge zwischen Etappe 5 und 6. Die Überschrift `# Bausteine` fällt dann weg. Die kursiven Trainer-Zeilen am Anfang jedes gewählten Bausteins (für wen, „im Zweifel weglassen“, Position) ersetzt du durch eine Zeile nach dem Muster *Läuft direkt nach Etappe 5 und vor Etappe 6. Rechne mit 25 bis 30 Minuten.* So überspringt Claude keinen gebuchten Baustein

Der Kern, also Etappen 0 bis 6, bleibt Wort für Wort. Findest du eine Verbesserung, gehört sie in die Vorlage mit Nachtrag in `LIESMICH.md`, nie nur in die Kundendatei.

## Phase 4: Handout

Seit 29.10.2026 gibt es nur noch **eine** Handout-Vorlage (`HANDOUT.html` mit `handout-bauen.py`). Das Handout baust du mit dem Skill `kunden-handout-hochladen`, Schritt „Bauen“. Er wählt die Fassung nach dem Werkzeug des Kunden (VS Code oder Claude-App), füllt den Zeitstrahl und das Inhaltsverzeichnis und prüft Platzhalter, Em-Dashes und Anker.

Aus Phase 1 und 2 lieferst du ihm: Werkzeug und Betriebssystem, Vorwissen für „Dein Handbuch“ (belegt, wörtlich aus dem Profil), Beispielaufträge für den Spicker, die heiklen Daten der Branche und die Uhrzeit des Termins. Zusätze aus Phase 2, die nicht in der Vorlage stehen (zum Beispiel Werkzeuge verbinden, Memory in claude.ai), kommen als eigener Abschnitt vor „Wenn etwas hakt“ in die gebaute `index.html`, mit Primärquelle und Prüfdatum. Sprachniveau und Stil wie bisher: `_system/context/about-me/files/anti-ai-writing-style.md` lesen, Pre-Submit-Check auf jeden neuen Satz.

Zusätzlich prüfst du den Namen eines früheren Kunden: Die Vornamen von Personen liest du von Hand aus den Ordnernamen in `02-areas/crm/leads/`. Firmen- und Programmteile wie „Private“, „BVS“ oder „KI-Werkstatt“ lässt du weg. Dann `grep -niwE 'name1|name2|…' index.html setup-<kunde>.md` und jeden Treffer lesen. CSS, Code und feste Begriffe wie „Command Line“ sind Fehlalarm.

## Phase 5: Use-Case-Plan

`gespraechsvorbereitung/use-case-plan-<JJJJ-MM-TT>.md`, sachlich formuliert, in dieser Reihenfolge:

1. **Was er will:** im Wortlaut aus dem Profil
2. **Oberflächen trennen**, wenn Fragen claude.ai statt Claude Code meinen (Memory, Projekte, Connectoren)
3. **Antworten auf seine Fragen:** je Antwort Klickpfad, Quelle, Prüfdatum. Nicht Belegtes steht als „nicht belegt“ drin. Die Recherche übernimmt `recherche-agent`, nur mit Primärquellen
4. **Der echte Use Case nach dem Setup:** zwei bis drei kopierfertige Prompts, jeweils mit Sätzen gegen erfundene Zahlen, gegen Versprechen und gegen Personendaten, dazu Wow-Moment und eine Korrektur per Satz
5. **Zeitrechnung und Kürzungsreihenfolge.** Nie gekürzt werden Datenschutz-Satz, Etappe 6 mit Neustart und der Use Case
6. **Folgetermin-Themen**

## Phase 6: Testlauf (Pflicht)

1. **Fable spielt die Setup-Datei durch:** Agent `general-purpose` mit `model: fable`, im Hintergrund. Der Testauftrag steht wörtlich in `LIESMICH.md`.
   - Szenario 1 nimmt Betriebssystem und Technikstand aus dem Profil, Szenario 2 die gewählten Bausteine oder das andere Betriebssystem
   - Im Prompt steht: Schreibpfade nur `/tmp/FAKE-HOME/`, echte Umlaute, die Datei nicht ändern
2. **Blocker einarbeiten.** Steckt einer in der Vorlage, dort beheben und in `LIESMICH.md` nachtragen.
3. **Nach Korrekturen ein zweiter Lauf.**

## Phase 7: Upload

Skill `webgo-upload`, Ziel `lehrconsult.de/<kunde>/`.

1. **Vorher prüfen, ob der Pfad frei ist:** `https://lehrconsult.de/<kunde>/` muss 404 liefern. Liefert er 200, Viktor fragen.
2. **Hochladen:** `index.html`, `setup-<kunde>.md`, die sieben PNGs nach `bilder/` und bei Baustein C das Skript als `vault-autolink.txt`. **Nie eine `.py`**, der Server antwortet darauf mit 500.
3. **Live prüfen:**
   - Handout über die Ordner-URL: 200 und byte-gleich. `index.html` direkt leitet nur mit 301 um
   - Setup-Datei: 200 und byte-gleich
   - `.txt`: 200 mit `text/plain`
   - Jedes Bild unter `bilder/`: 200 mit `image/png` und byte-gleich

## Phase 8: Übergabe

1. **`status.md` im Leadordner** anlegen oder aktualisieren: Termin, Link, Passwort, Module, Testergebnis, Offenes.
2. **Viktor melden:** Link und Passwort, Module mit Zeitsumme, Befunde aus dem Testlauf, offene Punkte. Trainingsleitfaden, Demo-Menü und Vorab-Mail einmal anbieten.

## Phase 9: Nachbereitung (nach dem Termin, auf Viktors Zuruf)

Standard seit 26.10.2026: Transkript, Zusammenfassung als PDF und Mail-Entwurf.

1. **Aufnahme:** `~/Documents/Zoom/<Datum Titel>/audio*.m4a`. Mit ffmpeg in Stücke zu 1500 s zerlegen (mono, 32k, mp3), wegen der 25-MB-Grenze der API.
2. **Whisper-API** (`whisper-1`, `language=de`, `verbose_json`), Stücke **nacheinander** mit `curl --http1.1`. Parallel gab es HTTP2-Fehler. Bei „Empty reply“ das Stück halbieren. Segmente mit Offset zusammenführen, Zeitmarken `[h:mm:ss]`, nach `gespraechsvorbereitung/<Datum>_transkript-session-<N>.md`.
3. **Video** nur auf ausdrücklichen Auftrag und nur per `mv` in den Papierkorb. Audio und Chat bleiben.
4. **PDF im Viktor-CI** (Logo aus `03-resources/ci-assets/logo/`): kurz „Das haben wir geschafft“, „Deine nächsten Schritte“ zum Abhaken, die Session zum Nachlesen nach Themen, Befehle auf einen Blick. Nur Belegtes aus dem Transkript, Unsicheres als „laut …“. Rendern mit Headless-Chrome (`--print-to-pdf --no-pdf-header-footer`), Vorschau über `pdftoppm` (PIL fehlt). Danach Pre-Submit-Check, Text mit `pdftotext` prüfen.
5. **Mail-Entwurf** an den Kunden mit PDF und Transkript als `.txt`, Stil nach `feedback-mail-stil-locker-nummeriert`, danach Entwürfe auf Dubletten prüfen (`reference-apple-mail-applescript`).
6. **`status.md`** um Stand und offene Punkte des Kunden ergänzen.

---

## Häufige Fehler

| Fehler | Richtig |
|---|---|
| Setup-Datei oder Handout entstehen vor dem Profil | Phase 1 und der Haltepunkt nach Phase 2 zuerst |
| Paket des letzten Kunden als Basis | immer `SETUP.md` und `HANDOUT.html` |
| Ein Wunsch taucht nirgends auf, zum Beispiel Outlook | jeder Wunsch hat ein Ziel aus `module.md` |
| Trainingsleitfaden, Demo-Menü, Vorab-Mail ungefragt | nur auf Wunsch |
| Web-Recherche steht als Tatsache im Handout | im Profil als Vermutung, das Handout behauptet nur Bestätigtes |
| Kern-Etappen für den Kunden umformuliert | Kern bleibt, Verbesserungen gehen in die Vorlage |
| Klickpfade aus dem Gedächtnis | Primärquelle mit Prüfdatum |
| Nach Korrekturen kein zweiter Testlauf | zweiter Lauf ist Pflicht |
| `.py` auf den Server | `vault-autolink.txt` |
| Plugin oder `claude mcp add` im Termin, ohne dass `claude` im Terminal läuft | Handout-Schritt 5 zuerst: Installation, PATH-Befehl aus der Ausgabe, ein vollständiger `claude`-Start. Die Erweiterung legt `claude` nicht ins Terminal |
| Großer Import oder Ordner-Migration live im Termin | kleine Auswahl live, den Rest als Hausaufgabe mit Prompt. iCloud-Ordner vorher auf „Immer auf dem Rechner behalten“ |
| Mail-Agent oder Notizen-Zugriff ungefragt im Paket | vorher fragen, Notizen nur auf einen Ordner „Claude Inbox“ |
| Kein fester Ausgabeordner | `outputs` in Ressourcen anlegen und in der CLAUDE.md eintragen |
| Handout-Schritt 5 aus dem Kundenhandout gelöscht | bleibt stehen, auch wenn der Use Case ohne Terminal auskommt. Kunden wollen später fast immer ein Plugin oder eine Verbindung |
