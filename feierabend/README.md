Quelle: `01-projects/ki-akademie/05-e-learning/demo-material/modul-3/feierabend-paket/` (Lektion 3.8 der Akademie). Diese Kopie ist die Fassung für die Setup-Session.

# Feierabend-Paket

Der Standard-Befehl `/feierabend` für Kunden-Setups. Er hält am Ende des Arbeitstags Entscheidungen und Stände im Second Brain fest, liest dafür den Eingang aller Sitzungen und sichert alles in einem Backup mit Kopie in der Cloud.

| Pfad | Inhalt |
|---|---|
| `EINRICHTEN.md` | Arbeitsanweisung an Claude: Befehl, Hook und Backup einrichten (Cloud-Ziel per AskUserQuestion) |
| `skills/feierabend/SKILL.md` | der Befehl `/feierabend` (7 Schritte, schreibt erst nach dem Okay) |
| `hooks/sitzung-eingang.py` | SessionEnd-Hook: legt nach jeder beendeten Sitzung einen Entwurf in `3-ressourcen/raw/sitzungen/` ab, nachholen mit `--nachholen heute` |
| `scripts/feierabend-backup.sh` | Backup für den Mac (Zip lokal und in der gewählten Cloud, letzte 7 Stände) |
| `scripts/feierabend-backup.ps1` | dasselbe für Windows (auf echtem Windows ungetestet) |

Voraussetzung: das Second Brain aus dem Grundsetup (`3-ressourcen/wissen/start.md`, `index.md`, `entscheidungen/`, `raw/inbox/`) und Python 3 für den Hook. Ohne Python läuft `/feierabend` trotzdem, liest dann aber nur das aktuelle Gespräch. Der Sitzungstext geht für den Entwurf wie jedes Gespräch an das Claude-Konto des Kunden, der Eingang bleibt lokal. Stand: 30.10.2026, Hook-Worker und Mac-Backup einzeln getestet, der ganze Ablauf noch nicht im Probelauf.

Einrichten: den Ordner in den Arbeitsordner des Kunden legen und Claude sagen: „Lies die Datei feierabend/EINRICHTEN.md und richte den Feierabend danach ein. Zeig mir zuerst den Plan.“ (In `EINRICHTEN.md` steht der Ordnername `feierabend-paket`, beim Ablegen entsprechend umbenennen oder den Pfad anpassen.)
