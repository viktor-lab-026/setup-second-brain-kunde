*Gekürzte Fassung für das Repo, ohne Kundenverlauf. Die vollständige LIESMICH mit allen Nachträgen liegt im Workspace.*

# Setup-Session Second Brain: aktuelle Vorlage

Dieser Ordner ist die zentrale Fassung für neue Kunden-Setups. Historische Versionen liegen im Archiv des Workspaces und nicht in diesem Repo.

## Dateien

| Datei | Zweck |
|---|---|
| `SETUP.md` | Arbeitsanweisung an Claude; vor der Session personalisieren |
| `HANDOUT.html` | Handout-Vorlage, einzige Quelle für beide Fassungen (VS Code und Claude-App), mit Zeitstrahl, Inhaltsverzeichnis und Platzhaltern |
| `handout-bauen.py` | Baut aus `HANDOUT.html` das Kundenhandout (`--tool code` oder `--tool app`), siehe Abschnitt „Handout bauen“ |
| `bilder/` | Screenshots, nur für die Fassung `code` |
| `LIESMICH.md` | Interne Pflegehinweise; nicht an Kunden weitergeben |

## Aktuelle Architektur

- Das eingebaute Auto-Memory merkt sich Präferenzen und Zusammenarbeit. Seit 05.10.2026 liegt es über `autoMemoryDirectory` in `~/.claude/settings.json` unter `<RESSOURCEN>/memory/`, neben dem Wissensordner und nicht darin (Etappe 4, Abschnitt „Das Gedächtnis ins Second Brain legen“).
- Fachwissen kommt auf ausdrücklichen Wunsch, über Dateien im Eingangskorb oder per Übertrag aus dem Gedächtnis ins Second Brain. Das Gedächtnis sammelt, das Second Brain behält: `/verarbeiten` überträgt Sachwissen aus `memory/` und lässt dort einen Verweis (seit 06.10.2026).
- Vor jeder inhaltlichen Aufgabe liest Claude die passenden Seiten und nennt sie. Seiten sind in beide Richtungen verlinkt, Verweise stehen als Pfad ab dem Arbeitsordner.
- Fragen werden in normaler Sprache gestellt. Dafür ist kein eigener Befehl nötig.
- `/verarbeiten` überträgt zuerst Sachwissen aus dem Gedächtnis und nimmt dann Quellen aus dem Eingangskorb oder ausdrücklich bestätigte Gesprächsinhalte auf.
- `/pruefung` kontrolliert Second Brain und Gedächtnis zusammen (seit 27.10.2026, vorher zwei Befehle) und läuft als lokale geplante Aufgabe am 1. jedes Monats.
- `/feierabend` legt fertige Stücke ab, fragt einmal nach dem Second Brain, misst das Gedächtnis und macht ein Backup (Mac `ki-system-backup.sh` nach iCloud, Windows `ki-system-backup.ps1` nach OneDrive).
- Es gibt keinen eigenen `/log`-Befehl, keinen `/fragen`-Befehl und keinen Autolink-Hook im Kunden-Setup. Behält ein Kunde einen eigenen Abschlussbefehl, bekommt er einen Schlusspunkt, der Sitzungswissen ins Second Brain anbietet.

## Personalisieren

1. `SETUP.md` als `setup-<vorname>.md` in den Lead-Ordner kopieren (`02-areas/crm/leads/<Vorname Nachname>/materialien/handout-claude-setup/`).
2. Die Kunden-Platzhalter ersetzen: `{{VORNAME}}`, `{{BEKANNT}}` (Spiegelstriche: was Viktor vorab weiß, welche Interviewfragen damit beantwortet sind, Regeln für „Wie ich arbeiten soll“ zum wörtlichen Übernehmen; weiß er nichts, steht dort „Noch nichts, stell alle fünf Fragen.“), `{{ABLAGEN_VORSCHLAG}}` (Tabelle mit drei bis fünf Ablagen oder „Keiner, leite die Ablagen allein aus den Antworten ab.“), `{{FRAGERUNDE}}` (null bis drei Auswahlfragen mit Empfehlung vorn, gestellt zusammen mit dem Ablagen-Okay; sonst „Keine weiteren Fragen.“). Danach mit `grep -n '{{' setup-<vorname>.md` prüfen: kein Treffer.
3. Die Vorlage schreibt in der er-Form. Bei einer Kundin die Pronomen in der Kopie anpassen (`grep -n -w -e er -e ihm -e ihn -e sein -e seine -e seinen -e seiner -e seinem`).
4. `<PFAD>`, `<RESSOURCEN>`, `<ARCHIV>`, `<HOME>`, `BACKUP-AUFRUF` und `BACKUP-WOLKE` bleiben stehen; Claude ersetzt sie erst während der Session.
5. Die personalisierte Setup-Datei in einem Testordner vollständig durchspielen (Subagent mit FAKE-HOME im Scratchpad), bevor sie ausgegeben wird.
6. **Einrichtung mit einem Prompt:** Die Datei liegt im Arbeitsordner des Kunden. Im Code-Tab der Claude-App (oder in VS Code) diesen Ordner öffnen und schreiben: „Lies setup-<vorname>.md und arbeite sie Etappe für Etappe ab.“

## Bausteine

| Baustein | Wann | Richtwert |
|---|---|---:|
| Grundsetup, Etappen 0 bis 6, mit Interview | immer | 45 bis 75 Minuten, je nachdem, wie viel Viktor vorab weiß |
| A: Marke und Stilguide · B: Obsidian · D: geteilter Wissensordner | nur bei Bedarf | je 20 Minuten |
| CI und Output (Startpaket, CI-Skill, `/ablegen`) | bei fertiger CI | etwa 20 Minuten |

Die Bausteine A, B und D stehen seit 27.10.2026 nicht mehr in `SETUP.md`. Wer sie braucht, nimmt sie aus `04-archive/2026/system/setup-second-brain-kunde-legacy/SETUP-2026-10-27-vor-grundsetup.md`, „CI und Output“ aus einer früheren Kundendatei, und gleicht sie an die neuen Befehle an (`/gedaechtnis-aufraeumen` heißt jetzt `/pruefung`). Zwei Stunden sind die Obergrenze.

## Vor der Ausgabe prüfen

- Keine offenen `{{…}}`-Platzhalter.
- Keine Hinweise auf `/fragen` oder einen Autolink-Hook, und `/log` nur als vorhandener Abschlussbefehl des Kunden. `autoMemoryDirectory` und der Ordner `memory/` gehören seit 05.10.2026 dazu.
- `SETUP.md` nennt genau vier Befehle: `/verarbeiten`, `/pruefung`, `/feierabend` und `/interview` (seit 29.10.2026), dazu das Backup-Skript für das System des Kunden und die Monatsprüfung als lokale geplante Aufgabe.
- Das Handout erklärt natürliche Fragen und den Satz „Nimm das in mein Second Brain auf“.
- Der Root des Kunden-Workspaces bleibt frei von Skills, Agenten und Werkzeug-Konfiguration.
- Keine personenbezogenen Daten in Beispielen oder Testmaterial.

## Abgrenzung

`../second-brain-os-setup.md` bildet ein umfangreiches persönliches Betriebssystem mit zusätzlichen Routinen ab. Das ist ein anderes Produkt und darf nicht mit dieser einfachen Kundenfassung vermischt werden.

## Nachtrag 29.10.2026: Eine Vorlage, zwei Fassungen (Single Source of Truth)

Anlass: ein Setup am 29.10.2026 (Claude-App, Windows). Dort entstanden Bausteine, die in der Vorlage fehlten. Viktor wollte „einen Single Source of Truth“ und den Zeitstrahl oben.

- **`SETUP.md`:** Etappe 0b (CLAUDE.md zuerst, Grundstock aus dem Vorwissen, Projekt- und Bereichsordner nur bei belegtem Vorwissen), Interviewprompt vor „Die Fragen“, Etappe 4 „Das Briefing vervollständigen und das Gedächtnis“, vierter Befehl `/interview`, voller PARA-Aufbau, Regel „Fast alles läuft automatisch“ und die Monatsprüfung als Automation ohne Rückfrage (Schritt 9, `{{VORNAME}}`). Fassung davor liegt nur im Scratchpad der Sitzung, Die Kundenfassung liegt im Lead-Ordner.
- **`HANDOUT.html`:** ersetzt `HANDOUT.html` (VS Code) und `HANDOUT-claude-app.html`, beide archiviert unter `04-archive/2026/system/setup-second-brain-kunde-legacy/`. Der Zeitstrahl `nav.plan` steht oben , das Inhaltsverzeichnis links (`#sidenav`, ab 1240 px), ein Gate mit Passwort. Der Begriff heißt überall „Session“.
- **`handout-bauen.py`** erzeugt die Kundenfassung. Pflicht: `--tool code|app`, `--vorname`, `--termin`, `--out`. Dazu `--kunde`, `--passwort` (Standard: zufällig erzeugt und beim Bauen ausgegeben, kleingeschrieben), `--stand`, `--start HH:MM` (füllt den Zeitstrahl mit den Abständen 0/10/20/30/55/70/80 Minuten), `--mit/--ohne` für optionale Blöcke, `--set SCHLÜSSEL=WERT`, `--set-datei SCHLÜSSEL=DATEI`. Das Skript meldet offene Platzhalter (Ausgabe 1) und Em-Dashes. Abschnittsnummern, Seitenleiste und Inhaltsverzeichnis entstehen beim Bauen.
- **Fassungen:** `code` = VS Code mit Bildern, Schalter Windows/Mac, standardmäßig mit den Blöcken `einleitung`, `prompts`, `skills`. `app` = Claude-App (Reiter Code), Windows, ohne Bilder, kompakt, ohne optionale Blöcke. Weitere optionale Blöcke: `obsidian`.
- **Platzhalter, die der Kunde braucht:** `VORWISSEN_HANDBUCH`, `SPICKER_TITEL`, `SPICKER_ZEILEN` (HTML-Tabellenzeilen), `SPICKER_BEISPIELSATZ`, `HEIKLE_DATEN_TITEL`, `HEIKLE_DATEN_TEXT`, bei `einleitung` zusätzlich `WOFUER_EINSTIEG` und `BEISPIEL_AUFGABEN`. Die Ordnernamen stehen als Standard (`01.projects` bis `04.archiv`) und lassen sich mit `--set PROJEKTE=…` überschreiben. Beispiele und Vorwissen nur aus belegtem Vorwissen (Beleg-Pflicht).
- **Gebaut und getestet:** beide Fassungen mit Testwerten, keine offenen Platzhalter, keine doppelten IDs, keine toten Anker, Screenshot-Sichtprüfung. Auf einem Windows-Rechner im Termin noch nicht gesehen.
- **Bilder:** Die Fassung `code` verweist auf `bilder/`, der Ordner muss mit hochgeladen werden (siehe Nachtrag 02.10.2026).
- **Skill:** `kunden-handout-hochladen` baut und veröffentlicht das Handout aus dieser Vorlage. Die Vorlage liegt zusätzlich im privaten GitHub-Repo `viktor-lab-026/setup-second-brain-kunde` (Spiegel, keine Kundendaten). Quelle der Wahrheit bleibt dieser Ordner.
