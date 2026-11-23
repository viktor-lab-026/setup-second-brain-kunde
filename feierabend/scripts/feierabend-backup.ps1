# Backup fuer /feierabend (Windows): Arbeitsordner und Claude-Einstellungen als datiertes Zip.
# Eine Kopie bleibt unter Benutzerordner\Claude-Backup, eine zweite liegt im gewaehlten Cloud-Ordner unter Claude-Backup.
# Von beiden bleiben die letzten 7 Staende. Die Anmeldedaten von Claude und Videodateien bleiben draussen.
#   powershell.exe -NoProfile -ExecutionPolicy Bypass -File feierabend-backup.ps1 "C:/Users/name/KI-System" "C:/Users/name/OneDrive"
param([string]$Arbeit, [string]$Cloud)
$ErrorActionPreference = 'Stop'
if (-not $Arbeit -or -not (Test-Path -LiteralPath $Arbeit -PathType Container)) { 'Aufruf: powershell.exe -NoProfile -ExecutionPolicy Bypass -File feierabend-backup.ps1 C:/pfad/zum/arbeitsordner C:/pfad/zum/cloud-ordner'; exit 1 }
$Arbeit = (Get-Item -LiteralPath $Arbeit).FullName.TrimEnd('\', '/')
$Lokal = Join-Path $env:USERPROFILE 'Claude-Backup'
$Behalten = 7
$Name = 'claude-backup_' + (Get-Date -Format 'yyyy-MM-dd') + '.zip'
$Tar = Join-Path $env:SystemRoot 'System32\tar.exe'
$Tmp = Join-Path $env:TEMP ('claude-backup-' + [guid]::NewGuid().ToString())
New-Item -ItemType Directory -Force -Path $Tmp | Out-Null
New-Item -ItemType Directory -Force -Path $Lokal | Out-Null
$Zip = Join-Path $Tmp $Name
$Weg = @('--exclude=*.mp4', '--exclude=*.MP4', '--exclude=*.mov', '--exclude=*.MOV', '--exclude=*.mkv', '--exclude=*/.obsidian/workspace*',
  '--exclude=.claude/projects', '--exclude=.claude/shell-snapshots', '--exclude=.claude/statsig', '--exclude=.claude/todos',
  '--exclude=.claude/cache', '--exclude=.claude/plugins', '--exclude=.claude/debug', '--exclude=.claude/.credentials.json')
$Teile = @('-C', (Split-Path -Parent $Arbeit), (Split-Path -Leaf $Arbeit))
if (Test-Path -LiteralPath (Join-Path $env:USERPROFILE '.claude')) { $Teile += @('-C', $env:USERPROFILE, '.claude') }
$ErrorActionPreference = 'Continue'
& $Tar -a -c -f $Zip @Weg @Teile 2>$null
$Code = $LASTEXITCODE
$ErrorActionPreference = 'Stop'
if (-not (Test-Path -LiteralPath $Zip)) { Remove-Item -Recurse -Force $Tmp; "Backup fehlgeschlagen: tar hat kein Zip erzeugt (Code $Code)"; exit 1 }

function Alte-Weg([string]$Ordner) {
  Get-ChildItem -LiteralPath $Ordner -Filter 'claude-backup_*.zip' | Sort-Object Name -Descending | Select-Object -Skip $Behalten | Remove-Item -Force
}
Copy-Item -LiteralPath $Zip -Destination (Join-Path $Lokal $Name) -Force
Alte-Weg $Lokal

$Wolke = 'keine Cloud gewaehlt, nur auf diesem Rechner gesichert'
if ($Cloud -and (Test-Path -LiteralPath $Cloud -PathType Container)) {
  $Ziel = Join-Path $Cloud 'Claude-Backup'
  New-Item -ItemType Directory -Force -Path $Ziel | Out-Null
  Copy-Item -LiteralPath $Zip -Destination (Join-Path $Ziel $Name) -Force
  Alte-Weg $Ziel
  $Wolke = Join-Path $Ziel $Name
} elseif ($Cloud) {
  $Wolke = "Cloud-Ordner nicht gefunden ($Cloud), nur auf diesem Rechner gesichert"
}
Remove-Item -Recurse -Force $Tmp
$Groesse = '{0:N1} MB' -f ((Get-Item -LiteralPath (Join-Path $Lokal $Name)).Length / 1MB)
$Hinweis = ''
if ($Code -ne 0) { $Hinweis = ', einzelne Dateien nicht gesichert' }
"Backup $Name ($Groesse$Hinweis)"
"Auf diesem Rechner: $(Join-Path $Lokal $Name)"
"In der Cloud: $Wolke"
