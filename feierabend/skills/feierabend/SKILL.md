---
name: feierabend
description: Tagesabschluss für mein Second Brain. Liest den Eingang aller heutigen Sitzungen, legt Entscheidungen mit Begründung ab, schickt neues Sachwissen in den Eingangskorb, zieht die Startseite 3-ressourcen/wissen/start.md nach und macht ein Backup mit Cloud-Kopie. Nutzen, wenn ich /feierabend tippe oder sage, dass der Tag abgeschlossen werden soll. Schreibt ins Second Brain erst nach meinem Okay.
---

# /feierabend: Tagesabschluss

Alle Pfade gehen vom Arbeitsordner aus. Mein Second Brain liegt in `3-ressourcen/wissen/`, der Eingangskorb für neues
Wissen in `3-ressourcen/raw/inbox/`, der Eingang der Sitzungen in `3-ressourcen/raw/sitzungen/`. Der Befehl startet nur,
wenn ich ihn tippe oder ausdrücklich sage, dass der Tag abgeschlossen werden soll. Nur die Erfassung der Sitzungen läuft
von selbst: Ein Hook schreibt nach jeder beendeten Sitzung einen Entwurf in den Eingang. Ins Second Brain kommt davon
nichts, bevor ich hier Ja sage.

## Drei Grundsätze

- **Du kennst zwei Quellen:** den Eingang der Sitzungen (Hook) und dieses Gespräch samt den heute geänderten Dateien.
  Gespräche in anderen Arbeitsordnern kennst du nicht. Frag mich dazu am Ende von Schritt 1 einmal.
- **Nur Belegtes kommt hinein.** Du nimmst auf, was ich gesagt, entschieden oder bestätigt habe, oder was in einer Datei
  steht. Du ergänzt nichts und erfindest keine Gründe. Ist etwas unsicher, stell es mir als Frage. Steht in einem
  Eingangsentwurf „nicht wörtlich im Protokoll gefunden“, ist das immer eine Frage an mich.
- **Datenschutz wie im Handbuch:** keine echten Namen von Kundinnen und Kunden, keine Gesundheits-, Bank- oder
  Zugangsdaten. Kürzel statt Namen. Findest du so etwas, übernimm es nicht und nenn mir nur die Art der Angabe.

## Ablauf

### 1. Den Tag ansehen

1. **Fehlende Sitzungen nachholen.** Gibt es `.claude/hooks/sitzung-eingang.py`, führ es einmal aus:
   `python3 .claude/hooks/sitzung-eingang.py --nachholen heute` (auf Windows `python` oder `py`). Der Lauf erfasst
   Sitzungen, die der Hook nicht erwischt hat, und kann bis zu zehn Minuten dauern. Gibt das Skript einen Fehler aus,
   nenn ihn mir und mach weiter. Gibt es das Skript nicht, überspring den Schritt.
2. **Eingang lesen.** Lies alle Dateien in `3-ressourcen/raw/sitzungen/`, bei denen oben `status: offen` steht, auch von
   älteren Tagen.
3. **Dieses Gespräch und die Dateien von heute.** Lies dieses Gespräch von Anfang an. Sieh dazu nach, welche Dateien im
   Arbeitsordner heute geändert wurden, nur Namen, ohne sie zu öffnen. Auf dem Mac mit
   `find . -type f -newermt "$(date +%Y-%m-%d)" -not -path "./.git/*" -not -path "./.claude/*"`, auf Windows mit
   `Get-ChildItem -Recurse -File | Where-Object { $_.LastWriteTime.Date -eq (Get-Date).Date }`. Geh nur in Dateien
   hinein, wenn ich sie im Gespräch erwähnt habe.
4. **Eine Frage.** Gibt es `.claude/hooks/sitzung-eingang.py` nicht, frag mich: „Gab es heute andere Gespräche mit
   Entscheidungen oder Ergebnissen, die ich kennen soll?“ Gibt es den Hook, frag nur: „Gab es heute Gespräche in anderen
   Arbeitsordnern mit Entscheidungen, die ich kennen soll?“

### 2. Sortieren

Sortier alles Belegte in vier Listen. Jeder Punkt aus dem Eingang trägt seine Herkunft in Klammern, etwa
„(Sitzung 30.10. 13:33)“.

- **Entscheidungen:** Was stand zur Wahl, was habe ich gewählt, warum, was habe ich verworfen, was betrifft es.
- **Stände:** Wo steht jedes Projekt oder Thema jetzt, in ein bis zwei Sätzen.
- **Neues Wissen:** Dauerhaftes, also Abläufe, Fachwissen, Vorlagen. Termine und Aufgaben, die in einer Woche überholt
  sind, kommen unter „Als Nächstes“.
- **Als Nächstes:** offene Punkte, mit Frist nur dann, wenn ich sie genannt habe.

Steht dieselbe Sache in mehreren Sitzungen, führ sie einmal auf. Die jüngste Aussage gilt, die ältere nennst du in
einem Halbsatz.

### 3. Entwurf zeigen und auf mein Okay warten

Zeig mir die vier Listen kurz. Jeder Punkt trägt einen Halbsatz dazu, woran du ihn festmachst („du hast gesagt …“, die
Belegzeile aus dem Eingang oder der Dateiname). Unsicheres stellst du mit AskUserQuestion, die empfohlene Antwort steht
vorn und trägt „(Empfohlen)“. Ich darf Punkte streichen. Du schreibst nichts ins Second Brain, bevor ich Ja gesagt habe.

### 4. Schreiben (nach meinem Okay)

- **Entscheidungen:** Je Entscheidung eine Seite `3-ressourcen/wissen/entscheidungen/JJJJ-MM-TT-thema.md` mit den Zeilen
  Datum, Frage, Wahl, Warum, Verworfen, Betrifft und unten `Quelle: aus dem Gespräch vom JJJJ-MM-TT`. Was nicht gesagt
  wurde, bleibt leer oder steht als „offen“ da. Gibt es zum Thema schon eine Seite, ergänzt du sie, statt eine zweite
  anzulegen. Ändert sich eine frühere Entscheidung, bleibt die alte Seite stehen und bekommt oben einen Satz mit
  Verweis auf die neue. Trag jede neue Seite in die `index.md` der Ablage `entscheidungen` ein und setz den Rückverweis.
- **Neues Wissen:** Das sortierst du nicht selbst ein. Leg je Punkt eine Datei
  `3-ressourcen/raw/inbox/JJJJ-MM-TT-thema.md` an, erste Zeile `Quelle: aus dem Gespräch vom JJJJ-MM-TT`. Einsortiert
  wird mit `/verarbeiten`.
- **Startseite `3-ressourcen/wissen/start.md`:** Fehlt die Datei, hör hier auf und sag mir: „Dafür fehlt noch das Setup
  aus Lektion 3.1.“ Sonst pflegst du die drei Abschnitte:
  - „Was zuletzt passiert ist“: eine Zeile je wichtigem Ergebnis, mit Datum, das Neueste oben, bei Entscheidungen mit
    Verweis auf die Seite.
  - „Was gerade läuft“: die Stände aus Schritt 2 eintragen oder aktualisieren. Ist etwas erledigt, löschst du es nicht,
    sondern setzt es mit Datum nach „Was zuletzt passiert ist“.
  - „Was als Nächstes ansteht“: die offenen Punkte aus Schritt 2.
  - Alles andere in der Datei bleibt, wie es ist. Hat „Was zuletzt passiert ist“ mehr als 15 Zeilen, sag es mir und
    schlag vor, die ältesten nach `4-archiv/` zu legen. Tu es erst nach meinem Ja.
- **Geschützte Seiten:** Steht oben in einer Seite `gepflegt_von: ich`, formulierst du dort nichts um.
- **Eingang abschließen:** Jede Eingangsdatei, die du ganz abgearbeitet hast (übernommen oder von mir gestrichen), setzt
  du oben auf `status: erledigt TT.MM.` und verschiebst sie nach `3-ressourcen/raw/sitzungen/erledigt/`. Das ist die
  einzige Verschiebung, die du hier machst. Bleibt in einer Datei etwas offen, lass sie liegen.
- Du löschst nichts.

### 5. Verweise prüfen

Prüf jeden neuen Verweis in doppelten eckigen Klammern mit `ls "<Verweis>.md"`.

### 6. Backup

Gibt es `.claude/feierabend-backup.txt` nicht, überspring den Schritt und sag in der Schlussmeldung: „Backup ist nicht
eingerichtet, siehe Abschnitt Backup in EINRICHTEN.md.“ Sonst steht dort eine Zeile `CLOUD=<Pfad>`, bei „keine Cloud“
eine leere Angabe. Ruf das Skript mit dem Pfad des Arbeitsordners (`pwd`) und dem Cloud-Pfad auf:

- Mac: `bash .claude/scripts/feierabend-backup.sh "<Arbeitsordner>" "<Cloud-Pfad>"`
- Windows: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .claude/scripts/feierabend-backup.ps1 "<Arbeitsordner>" "<Cloud-Pfad>"`

Das Skript legt ein datiertes Zip an, eine Kopie auf diesem Rechner unter `Claude-Backup` im Benutzerordner und eine in
der Cloud unter `Claude-Backup`. Die letzten sieben Stände bleiben, die Anmeldedaten von Claude und Videodateien bleiben
draußen. Meldet das Skript einen Fehler, nenn ihn wörtlich. Der Feierabend gilt trotzdem als abgeschlossen.

### 7. Bericht

Fass in höchstens fünf Zeilen zusammen: wie viele Sitzungen aus dem Eingang kamen, wie viele Entscheidungen angelegt
wurden, was in den Eingangskorb ging, was in `start.md` steht und wie viele Dateien jetzt im Eingangskorb auf
`/verarbeiten` warten (Zahl aus `3-ressourcen/raw/inbox/`). In der letzten Zeile steht das Backup mit dem **vollen Pfad**
der Cloud-Kopie, genau so, wie das Skript ihn ausgibt.
