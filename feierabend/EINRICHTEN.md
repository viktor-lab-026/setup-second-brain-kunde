# Feierabend einrichten

Diese Datei richtet den Befehl `/feierabend` ein. Er gehört zu deinem Second Brain aus Lektion 3.1. Lies sie ganz und
arbeite sie der Reihe nach ab. Zeig mir zuerst den Plan und warte auf mein Ja.

Das Paket hat drei Teile: den Befehl selbst, einen Hook, der nach jeder beendeten Sitzung einen Entwurf in einen Eingang
schreibt, und ein Backup mit Kopie in meiner Cloud.

## Voraussetzung prüfen

Prüf mit `ls`, ob es `3-ressourcen/wissen/start.md`, `3-ressourcen/wissen/index.md`, die Ablage
`3-ressourcen/wissen/entscheidungen/` und den Ordner `3-ressourcen/raw/inbox/` gibt. Fehlt etwas davon, hör auf und sag
mir: „Dafür fehlt noch das Setup aus Lektion 3.1.“ Leg nichts selbst an.

## Schritt 1: Den Befehl einrichten

Kopier den Ordner `feierabend-paket/skills/feierabend/` nach `.claude/skills/feierabend/`.

Sag mir vorher: „Gleich schreibe ich in den Ordner .claude. Dafür kommt eine Rückfrage. Klick auf Yes.“ Wird der Zugriff
abgelehnt, sag das und versuch es genau einmal neu. Gibt es dort schon einen Skill `feierabend`, überschreib ihn nicht.
Zeig mir den Unterschied und frag, ob der alte ins Archiv `4-archiv` soll.

Prüf danach mit `ls`, dass `.claude/skills/feierabend/SKILL.md` an seinem Platz liegt.

## Schritt 2: Den Hook einrichten (erfasst jede Sitzung)

Der Hook läuft, wenn ich ein Gespräch beende. Er liest das Protokoll und legt unter `3-ressourcen/raw/sitzungen/` einen
Entwurf mit Entscheidungen, Ständen und neuem Wissen ab. Dafür schickt er den Text des Gesprächs, wie jedes Gespräch mit
Claude, an mein Claude-Konto. Der Eingang bleibt auf meinem Rechner. Ins Second Brain kommt daraus nichts, bevor ich bei
`/feierabend` Ja sage.

1. **Python prüfen.** Führ `python3 --version` aus (auf Windows `python --version` oder `py --version`). Auf dem Mac kann
   dabei ein Fenster „Entwicklertools installieren“ erscheinen. Sag mir dann, dass ich es schließen darf. Findest du kein
   Python, überspring Schritt 2 und sag mir: „Ohne Python läuft kein Hook. /feierabend funktioniert trotzdem, es liest
   dann nur das aktuelle Gespräch.“ Mach mit Schritt 3 weiter.
2. **Dateien anlegen.** Kopier `feierabend-paket/hooks/sitzung-eingang.py` nach `.claude/hooks/sitzung-eingang.py`. Leg
   die Ordner `3-ressourcen/raw/sitzungen/` und `3-ressourcen/raw/sitzungen/erledigt/` an. Auch dafür kommt eine
   Rückfrage, ich klicke auf Yes.
3. **Hook eintragen.** Lies `.claude/settings.json`. Gibt es die Datei nicht, leg sie mit dem Inhalt unten an. Gibt es sie
   schon, ergänz den Block `SessionEnd` mit dem Edit-Werkzeug und lass alles andere stehen. Schreib die Datei nie
   komplett neu. Gibt es schon einen Eintrag `SessionEnd`, häng den neuen Hook dort an. Steht `sitzung-eingang.py` schon
   drin, trag ihn nicht noch einmal ein.

   ```json
   {
     "hooks": {
       "SessionEnd": [
         {
           "hooks": [
             { "type": "command", "command": "python3 \"${CLAUDE_PROJECT_DIR}/.claude/hooks/sitzung-eingang.py\"", "timeout": 5 }
           ]
         }
       ]
     }
   }
   ```

   Auf Windows steht statt `python3` das Wort `python`. Der Windows-Weg ist ungetestet. Läuft der Hook dort nicht, bleibt
   `/feierabend` mit `--nachholen` nutzbar.
4. **JSON prüfen.** Lies die Datei danach noch einmal und prüf, dass sie gültiges JSON ist (zum Beispiel mit
   `python3 -c "import json; json.load(open('.claude/settings.json'))"`). Ist sie kaputt, stell den alten Stand wieder
   her und sag es mir.
5. Sag mir: „Beim nächsten Start fragt Claude Code eventuell, ob du dem neuen Hook vertraust. Klick auf Yes.“

## Schritt 3: Das Backup einrichten (mit Kopie in der Cloud)

Das Backup legt am Ende von `/feierabend` ein datiertes Zip von meinem Arbeitsordner und meinen Claude-Einstellungen an,
einmal auf diesem Rechner und einmal in einem Cloud-Ordner. Die Anmeldedaten von Claude und Videodateien bleiben draußen.
Welche Cloud, entscheide ich per Klick.

1. **Cloud-Ordner suchen** mit `ls`, nur lesend. Mac: `~/Library/Mobile Documents/com~apple~CloudDocs` (iCloud Drive),
   `~/Library/CloudStorage/` (dort liegen OneDrive, Dropbox und Google Drive als Ordner), `~/Dropbox`. Windows:
   `$env:USERPROFILE`, dort Ordner `OneDrive*` und `Dropbox`, dazu Laufwerk `G:` (Google Drive). Notier dir jeden Treffer
   mit vollem Pfad.
2. **Frag mich mit AskUserQuestion** („Wohin soll die Cloud-Kopie des Backups?“). Die Optionen sind die gefundenen
   Ordner, bis zu drei, mit Namen des Dienstes. Die erste Option trägt „(Empfohlen)“ und ist bei Mac iCloud Drive, sonst
   der erste Treffer. Die letzte Option heißt „Keine Cloud, nur dieser Rechner“. Einen eigenen Ordner nenne ich über
   „Other“. Gibt es keinen Treffer, nenn mir das und lass mich einen Ordner angeben oder „Keine Cloud“ wählen.
3. **Auswahl speichern.** Leg `.claude/feierabend-backup.txt` mit einer Zeile an: `CLOUD=<voller Pfad>`, bei „Keine
   Cloud“ `CLOUD=`.
4. **Skript kopieren.** Mac: `feierabend-paket/scripts/feierabend-backup.sh` nach `.claude/scripts/feierabend-backup.sh`.
   Windows: `feierabend-backup.ps1` nach `.claude/scripts/feierabend-backup.ps1`. Auch dafür kommt eine Rückfrage, ich
   klicke auf Yes.
5. **Einmal ausprobieren.** Ruf das Skript mit dem Pfad des Arbeitsordners (`pwd`) und dem gewählten Cloud-Pfad auf, wie in
   `.claude/skills/feierabend/SKILL.md` unter „Backup“. Es kann bei großen Ordnern ein paar Minuten dauern. Zeig mir die
   Ausgabe, besonders die Zeile „In der Cloud:“ mit dem vollen Pfad. Prüf mit `ls`, dass die Datei dort liegt. Auf dem Mac
   heißt „Cloud-Ordner nicht gefunden“, dass der Dienst nicht eingeschaltet ist, bei iCloud Drive in den
   Systemeinstellungen unter meinem Namen. „Einzelne Dateien nicht gesichert“ heißt, dass eine Datei gerade geöffnet war.
   Das Zip ist trotzdem da.

## Schritt 4: Eine Zeile ins Handbuch

Häng diese eine Zeile mit dem Edit-Werkzeug an das Ende des Abschnitts „Mein Second Brain“ in `CLAUDE.md`. Alles andere
in der Datei bleibt, wie es ist. Schreib die Datei nie komplett neu. Gibt es den Abschnitt nicht, hör auf und sag mir:
„Dafür fehlt noch das Setup aus Lektion 3.1.“

```markdown
- Jede beendete Sitzung landet als Entwurf in 3-ressourcen/raw/sitzungen/. Am Ende eines Arbeitstags halte ich mit /feierabend Entscheidungen und Stand fest und sichere alles in einem Backup. Du schreibst dabei erst nach meinem Okay ins Second Brain.
```

Steht die Zeile schon da, häng sie nicht noch einmal an.

## Schritt 5: Abschluss

1. Verschieb den Ordner `feierabend-paket` nach `4-archiv/feierabend-paket`. Er wird nicht mehr gebraucht.
2. Zeig mir kurz, was neu ist: der Befehl, der Hook, das Backup mit dem Pfad der Cloud-Kopie und die Zeile im Handbuch.
3. Bitte mich, ein neues Gespräch zu starten, weil Claude Befehle und Hooks beim Start lädt. Schlag mir für das neue
   Gespräch diesen Test vor: `/` tippen und nachsehen, ob `feierabend` in der Liste steht. Der Hook zeigt sich danach
   daran, dass nach einem Gespräch mit mindestens zwei Runden eine Datei unter `3-ressourcen/raw/sitzungen/` liegt.
