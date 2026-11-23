# setup-second-brain-kunde

Vorlage für die 1:1-Setup-Session von LEHRCONSULT (Claude einrichten, Second Brain, Briefing, vier Befehle) samt Handout-Bauskript, einem echten Beispiel und den zwei zugehörigen Skills für Claude Code.

Dieses Repo ist ein Spiegel. Die Quelle der Wahrheit liegt im Workspace unter `03-resources/templates/setup-second-brain-kunde/`. Hier liegen keine Kundendaten, keine Lead-Ordner und keine Passwörter. Das Beispiel ist anonymisiert.

| Pfad | Inhalt |
|---|---|
| `vorlage/SETUP.md` | Arbeitsanweisung an Claude (Grundsetup, Etappen 0 bis 6) |
| `vorlage/HANDOUT.html` | einzige Handout-Vorlage, Fassungen VS Code und Claude-App, Zeitstrahl, Inhaltsverzeichnis |
| `vorlage/handout-bauen.py` | baut das Kundenhandout: `python3 handout-bauen.py --tool app\|code --vorname … --termin … --start HH:MM --out index.html`. Ohne `--passwort` entsteht ein zufälliges Passwort, das Skript gibt es aus |
| `vorlage/bilder/` | Screenshots für die Fassung `code` |
| `vorlage/LIESMICH.md` | Pflegehinweise (gekürzt) |
| `beispiel/` | eine echte Session (Claude-App, Windows, 29.10.2026), anonymisiert: das Handout (`index.html`, Passwort `beispiel`) und die Setup-Datei dazu (`setup-max.md`) |
| `skills/kunden-handout-hochladen/` | Skill: Handout bauen und auf lehrconsult.de veröffentlichen |
| `skills/setup-session-kunde/` | Skill: Setup-Session für einen Kunden vorbereiten |
| `feierabend/` | Standard-Befehl `/feierabend` mit SessionEnd-Hook und Backup mit Cloud-Kopie (Skill, Hook, Skripte, `EINRICHTEN.md`) |

Die Skills gehören nach `~/.claude/skills/`.

## So läuft eine Session

1. **Vorher:** Aus dem Vorgespräch die `vorlage/SETUP.md` für die Person füllen (alle `{{…}}`-Platzhalter, vor allem „Was Viktor schon weiß“) und als `setup-<vorname>.md` speichern. Dazu mit `handout-bauen.py` das Handout bauen. Wie das fertig aussieht, zeigt `beispiel/`.
2. **In der Session:** Die Person lädt die Setup-Datei über das Handout herunter, legt sie in ihren Arbeitsordner und gibt Claude den Einzeiler aus dem Handout. Claude arbeitet die Etappen ab und wartet an den Haltepunkten. Du begleitest, klickst mit und beantwortest Fragen.
3. **Danach:** Das Handout bleibt der Spicker für den Alltag.

Fragen an kontakt@lehrconsult.de.
