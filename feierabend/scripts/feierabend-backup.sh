#!/bin/bash
# Backup für /feierabend: Arbeitsordner und Claude-Einstellungen als datiertes Zip.
# Eine Kopie bleibt auf dem Mac (~/Claude-Backup), eine zweite liegt im gewählten Cloud-Ordner unter Claude-Backup.
# Von beiden bleiben die letzten 7 Stände. Die Anmeldedaten von Claude und Videodateien bleiben draußen.
#   bash feierabend-backup.sh "/Users/name/Desktop/KI-System" "/Users/name/Library/Mobile Documents/com~apple~CloudDocs"
set -e
ARBEIT="$1"
CLOUD="$2"
if [ -z "$ARBEIT" ] || [ ! -d "$ARBEIT" ]; then echo "Aufruf: bash feierabend-backup.sh /pfad/zum/arbeitsordner /pfad/zum/cloud-ordner"; exit 1; fi
LOKAL="$HOME/Claude-Backup"
BEHALTEN=7
NAME="claude-backup_$(date +%Y-%m-%d).zip"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$LOKAL"
HINWEIS=""
# zip meldet Code 12 oder 18, wenn einzelne Dateien fehlen oder gerade geöffnet sind. Das Zip ist dann trotzdem da.
tolerant() { "$@" || { c=$?; if [ "$c" -eq 12 ] || [ "$c" -eq 18 ]; then HINWEIS=", einzelne Dateien nicht gesichert"; else return "$c"; fi; }; }
cd "$(dirname "$ARBEIT")"
tolerant zip -rqy "$TMP/$NAME" "$(basename "$ARBEIT")" \
  -x "*.DS_Store" "*.mp4" "*.MP4" "*.mov" "*.MOV" "*.mkv" "*/.obsidian/workspace*"
cd "$HOME"
[ -d .claude ] && tolerant zip -rqy "$TMP/$NAME" .claude -x ".claude/projects/*" ".claude/shell-snapshots/*" ".claude/statsig/*" ".claude/todos/*" ".claude/cache/*" ".claude/plugins/*" ".claude/debug/*" ".claude/.credentials.json"
cp "$TMP/$NAME" "$LOKAL/$NAME"

aufraeumen() { ls -1 "$1"/claude-backup_*.zip 2>/dev/null | sort -r | tail -n +$((BEHALTEN+1)) | while read -r alt; do mv "$alt" "$HOME/.Trash/" 2>/dev/null || true; done; }
aufraeumen "$LOKAL"

WOLKE="keine Cloud gewählt, nur auf diesem Mac gesichert"
if [ -n "$CLOUD" ] && [ -d "$CLOUD" ]; then
  mkdir -p "$CLOUD/Claude-Backup"
  cp "$TMP/$NAME" "$CLOUD/Claude-Backup/$NAME"
  aufraeumen "$CLOUD/Claude-Backup"
  WOLKE="$CLOUD/Claude-Backup/$NAME"
elif [ -n "$CLOUD" ]; then
  WOLKE="Cloud-Ordner nicht gefunden ($CLOUD), nur auf diesem Mac gesichert"
fi
GROESSE=$(du -h "$LOKAL/$NAME" | cut -f1)
echo "Backup $NAME ($GROESSE$HINWEIS)"
echo "Auf diesem Mac: $LOKAL/$NAME"
echo "In der Cloud: $WOLKE"
