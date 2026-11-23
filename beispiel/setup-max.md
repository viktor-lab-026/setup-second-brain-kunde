# Setup: Dein eigenes KI-System · für Max

**An Claude:** Diese Datei ist lang. Lies sie vollständig (die eine Ausnahme steht zwei Absätze weiter unten), notfalls in mehreren Teilen (etwa Zeile 1 bis 300 und 301 bis Ende), und fang erst an, wenn du sie ganz gelesen hast. Sie ist deine Arbeitsanweisung. Arbeite die Etappen der Reihe nach ab, im Ordner, der gerade geöffnet ist. Melde nach jeder Etappe in zwei, drei Sätzen, was du getan hast, und mach dann direkt weiter. Sprich Deutsch und duze. Die Person vor dem Bildschirm heißt Max.

**Bevor du anfängst:** Stehen irgendwo in dieser Datei noch zwei öffnende geschweifte Klammern direkt hintereinander, ist sie nicht fertig vorbereitet. Dann stopp, sag Max, dass Viktor die Datei noch ergänzen muss, und leg nichts an. Spitze Klammern wie `<PFAD>` sind dagegen gewollt, die setzt du im Lauf selbst ein.

**Eine Ausnahme von der Reihenfolge, und nur diese:** Sagt die erste Nachricht der Unterhaltung, der Neustart sei schon passiert und das Setup sei gelaufen, dann arbeitest du die Datei nicht von vorn ab. Du liest nur Etappe 6 und den Absatz „JSON prüfen“ in Etappe 0, steigst in Schritt 7 beim Satz „Bitte ihn danach, diese Kontrollen nacheinander selbst einzutippen“ ein (Neustart und Übergabe sind schon passiert, schick ihn nicht noch einmal in eine neue Unterhaltung), fragst vorher, ob der Modus noch auf Manual steht (dann darf er jetzt zurück auf Auto: unten im Eingabefeld auf die Modus-Anzeige klicken), machst mit den Kontrollen und danach mit Schritt 8 bis 10 weiter und legst nichts neu an, was schon existiert. Was eine Kontrolle in Etappe 6 ausdrücklich als Reparatur verlangt, führst du aus.

**Fünf Regeln für den ganzen Ablauf:**

1. Du legst nichts doppelt an, und du benennst nichts um, außer er erlaubt es ausdrücklich. Was schon da ist, bleibt genau so, wie es heißt. Du ergänzt nur, was fehlt.
2. **Fast alles läuft automatisch.** Was Viktor über Max schon weiß, steht in Etappe 3 unter „Was Viktor schon weiß“, danach fragst du nicht noch einmal. Gefragt wird nur an drei Stellen: im Interview in Etappe 3 samt der Freigabe der Ablagen, wenn ein vorhandener Ordner nicht eindeutig zuzuordnen ist oder umbenannt werden müsste, und wenn eine Datei, die du schreiben willst, schon existiert. Dazu kommen nur die Okays, die unten ausdrücklich verlangt sind (Setup heute schon gelaufen, vorhandenes `autoMemoryDirectory`, Löschen oder Verschieben von Dateien). Alles andere legst du direkt an und meldest es danach in einem Satz.
3. Wird ein Dialog weggeklickt oder ein Zugriff abgelehnt, sagst du das und wiederholst den Vorgang genau einmal. Erst wenn auch der zweite Versuch scheitert, gilt der Zugriff als gescheitert. Die eine Ausnahme ist die Meldung „Blocked by classifier“: Dort gilt der Weg aus Etappe 2, also zuerst der Moduswechsel.
4. **Fragen stellst du mit dem Werkzeug AskUserQuestion**, also als Auswahl zum Anklicken. Die empfohlene Antwort steht als erste Option und trägt „(Empfohlen)“. Bis zu vier voneinander unabhängige Fragen packst du in einen einzigen Aufruf. Eigener Text bleibt über das freie Feld immer möglich. Gibt es das Werkzeug bei ihm nicht, stellst du dieselben Fragen nummeriert in einer einzigen Nachricht. Die eine Ausnahme sind die offenen Interviewfragen in Etappe 3: Die stellst du immer als normale Nachricht, weil er dort frei erzählt.
5. Frag nichts, was du schon weißt oder selbst nachsehen kannst. Was Etappe 0 gefunden hat oder was in dieser Datei steht, setzt du voraus und nennst es nur.

**Der Ablauf auf einen Blick:** Etappe 0 Bestandsaufnahme · Etappe 0b die CLAUDE.md zuerst · Etappe 1 Second Brain anlegen · Etappe 2 Ausgabe-Ordner und persönlicher Ordner · Etappe 3 Interview und Ablagen · Etappe 4 Briefing und Gedächtnis · Etappe 5 die Befehle für den Alltag · Etappe 6 Neustart und Kontrolle.

---

## Etappe 0: Bestandsaufnahme und der absolute Pfad

Bevor du irgendetwas anlegst, sieh dir an, was da ist.

1. **Stell fest, auf welchem System du läufst.** Liefert `uname -s` `Darwin`, ist es ein Mac. Beginnt die Ausgabe mit `MINGW`, `MSYS` oder `CYGWIN`, oder gibt es den Befehl nicht, ist es Windows. Merk dir das als SYSTEM (Mac oder Windows). An einigen Stellen unten gibt es zwei Wege, du nimmst immer nur den für SYSTEM.
2. **Ermittle den absoluten Pfad des geöffneten Ordners**, also den vollständigen Pfad ab der Festplatte, zum Beispiel `/Users/name/KI-System`. Auf Windows schreibst du ihn mit Laufwerksbuchstaben und normalen Schrägstrichen, also `C:/Users/name/KI-System`, auch wenn Windows selbst Backslashes anzeigt. Windows versteht diese Schreibweise, und sie passt zu allen Pfaden unten. Die Git-Bash-Form `/c/Users/...` nimmst du nie. Auf Windows liefert `cygpath -m "$(pwd)"` den Pfad direkt in dieser Form. Liefert ein Befehl die andere Form oder Backslashes, schreibst du sie selbst um: Aus `/c/Users/name` und aus `C:\Users\name` wird `C:/Users/name`. Diesen Pfad nennst du ab jetzt PFAD. Enthält er Leerzeichen, setzt du ihn in jedem Shell-Befehl in Anführungszeichen, auch bei `ls`, sonst meldet der Befehl einen gesunden Pfad als fehlend. Überall dort, wo unten `<PFAD>` steht, setzt du ihn ein. Ausgeschrieben, nie abgekürzt, nie als `.` oder `./`.
   **Das gilt ausnahmslos auch in JSON-Dateien:** Dort schreibst du Windows-Pfade mit Schrägstrichen, also `C:/Users/name/KI-System`. Ein einzelner Backslash macht die ganze Datei ungültig, und Claude Code kann sie dann nicht mehr laden, samt aller bestehenden Rechte.
3. Liste die Ordner im geöffneten Ordner auf. Gesucht sind vier Bereiche, **egal wie sie heißen und wie sie geschrieben sind**: Projekte, Bereiche (Areas), Ressourcen, Archiv. Ein Ordner erfüllt einen dieser Zwecke auch dann, wenn er ganz anders heißt. `03-material`, `Ablage` oder `Unterlagen` sind der Ressourcen-Ordner. Leg niemals einen zweiten Ordner für einen Zweck an, den ein vorhandener schon erfüllt.
4. **Den Namen des Archiv-Ordners nennst du ab jetzt ARCHIV.** Wo unten `<ARCHIV>` steht, setzt du ihn ein. Gibt es keinen, legst du ihn ohne Rückfrage als `04.archiv` an, mit dem Trenner der vorhandenen Ordner (heißen sie `01-projekte`, dann `04-archiv`).
   **Den Namen des Ressourcen-Ordners nennst du ab jetzt RESSOURCEN.** Überall dort, wo unten `<RESSOURCEN>` steht, setzt du ihn ein, genau wie PFAD, in seiner gefundenen Schreibweise. Heißt der Ordner bei ihm `03-material`, steht ab jetzt überall `03-material`. Gibt es keinen, legst du ihn ohne Rückfrage als `03.ressources` an, und RESSOURCEN ist dann `03.ressources`.
5. Schau nach, ob es unter dem Ressourcen-Ordner schon einen Eingangskorb (`raw`, `inbox`) oder einen Wissensbereich (`wissen`, `knowledge`, `vault`) gibt. Ein Ordner `.obsidian` zählt nicht dazu, er gehört zum Programm Obsidian. **Liegen dort schon `wissen/index.md` und `wissen/start.md`, frag zuerst, ob dieses Setup heute schon gelaufen ist.** Wenn ja, gilt die Ausnahme aus dem Kopf dieser Datei: Spring direkt zu den Kontrollen in Etappe 6.

**Bevor du weitersuchst, sag das hier an. Danach suchst du direkt weiter, ohne auf eine Antwort zu warten:**

> Gleich schaue ich außerhalb dieses Ordners nach, ob dort schon Einstellungen von dir liegen. Dabei kann eine Systemfrage erscheinen, ob ich das darf. Bitte klick auf **„Keep allowing“** (weiterhin erlauben) oder den gleichbedeutenden Knopf und niemals auf **„Block from now on“** (ab jetzt blockieren) oder ein anderes dauerhaftes Blockieren. Ein Blockieren merkt sich das Programm dauerhaft, und danach komme ich in keiner Sitzung mehr an Dateien außerhalb dieses Ordners, auch nicht an deine alten Anweisungen.

6. **Suche jetzt nach vorhandenen Briefing-Dateien.** Schau an vier Stellen nach und lies, was du findest, ohne etwas zu ändern:
   - `CLAUDE.md` im geöffneten Ordner und in seinen Unterordnern
   - jede andere Textdatei im geöffneten Ordner, die wie eine Anweisung an dich aussieht (etwa `anweisungen.md`, `briefing.md`, `instructions.txt`). Diese Setup-Datei selbst zählt nicht dazu
   - `~/.claude/CLAUDE.md`, also die persönliche Datei im Benutzerverzeichnis
   - `~/.claude/commands/`, ob dort schon Befehle liegen

   **Fehlen in `~/.claude/` die Datei `CLAUDE.md`, der Ordner `commands/` oder die Datei `settings.json`, ist das kein Fehler.** Den Ordner `~/.claude/` selbst gibt es in einer laufenden Sitzung fast immer. Auf einem frischen Rechner ist das der Normalfall. Du meldest es als „noch nicht angelegt“, suchst nicht an anderen Orten weiter und legst das Fehlende in Etappe 4 und 5 an. Ermittle dafür jetzt mit `echo $HOME` den vollen Pfad des Benutzerordners, etwa `/Users/name`. Auf Windows nimmst du `cygpath -m "$HOME"` und bekommst ihn mit Laufwerksbuchstaben, also `C:/Users/name`. Diesen Pfad nennst du HOME. Wo unten `~/.claude/` steht, schreibst du beim Anlegen den vollen Pfad aus, also `/Users/name/.claude/`, damit keine Datei in einem Ordner namens `~` im Arbeitsordner landet.

**JSON prüfen, gilt für jede `settings.json` in diesem Ablauf.** Auf dem Mac mit `osascript -l JavaScript -e 'ObjC.import("Foundation"); JSON.parse(ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError("<voller Pfad>",4,null))); "OK"'`. Das läuft auf jedem Mac ohne Installation. Kommt `OK`, ist die Datei gültig, bei `SyntaxError` nicht. Auf Windows mit `powershell -NoProfile -Command "try { Get-Content -Raw -ErrorAction Stop -LiteralPath '<voller Pfad>' | ConvertFrom-Json | Out-Null; 'OK' } catch { 'FEHLER' }"`. Der Befehl enthält absichtlich kein Dollarzeichen, weil die Bash es sonst vorher ersetzt. Kommt `OK`, ist die Datei gültig, kommt `FEHLER`, ist sie ungültig. Meldet PowerShell stattdessen einen eigenen Fehler (etwa „ParserError“ oder „nicht erkannt“), liegt es am Befehl und nicht an der Datei: Du prüfst den Befehl und wiederholst ihn, du stellst deshalb nie eine Datei wieder her.

**Dann berichte in einer kurzen Liste:** SYSTEM, was da ist, wie es genau heißt, was fehlt, wie PFAD, RESSOURCEN, ARCHIV und HOME lauten, und welche Briefing-Dateien du gefunden hast. Eine gefundene Briefing-Datei im Arbeitsordner änderst du nicht, ihre Regeln übernimmst du nur, wenn Max das in Etappe 3 bestätigt. Eine vorhandene `~/.claude/CLAUDE.md` bekommt in Etappe 0b und 4 nur Neues angehängt, dazu fragst du nicht.

**Ab hier gilt:** Du übernimmst die gefundene Schreibweise. Findest du `01-projects` mit Bindestrich, arbeitest du mit Bindestrich weiter. Du korrigierst das nicht und legst keine zweite Variante daneben.

**Ist eine Zuordnung unklar** (ein Ordner passt zu keinem Bereich oder zu zweien, ein Bereich liegt doppelt vor), fragst du das jetzt ab, alle offenen Punkte in einem einzigen AskUserQuestion-Aufruf, und legst erst nach der Antwort etwas an. Das ist die einzige Frage vor Etappe 3. **Ist alles eindeutig, fragst du nicht.** Du legst das Fehlende an, meldest es und gehst direkt in Etappe 1, auch dort ohne Rückfrage. Fehlt die Grundstruktur ganz oder fehlen einzelne Bereiche, legst du nur das Fehlende an, in dieser Schreibweise, auch wenn ein vorhandener Ordner anders geschrieben ist:

```
01.projects/
02.areas/
03.ressources/
04.archiv/
```

Sag ihm dazu in einem Satz, wofür die vier da sind: Projekte haben ein Ende, Bereiche laufen dauerhaft, Ressourcen sind Material und Wissen, ins Archiv kommt Abgeschlossenes.

---

## Etappe 0b: Zuerst die CLAUDE.md

Das Erste, was entsteht, ist die Datei, die Claude bei jedem Start von selbst liest: `~/.claude/CLAUDE.md` (voller Pfad mit HOME, siehe Etappe 0). Du schreibst sie jetzt als Grundstock aus dem, was Viktor schon weiß. Das Interview in Etappe 3 und das Second Brain in Etappe 4 vervollständigen sie, indem du mit dem Edit-Werkzeug ergänzt. Hier fragst du nichts.

**Vorher legst du die Projekt- und Bereichsordner an, die aus „Was Viktor schon weiß“ belegt sind** (nur, was fehlt, mit den echten Namen aus Etappe 0, hier als Beispiel mit `01.projects` und `02.areas`):

- `<PFAD>/<PROJEKTE>/ratgeber-wohnungsuebergabe/project.md` mit den Überschriften **Ziel** (ein Ratgeber zur Wohnungsübergabe), **Bausteine** (Video, kostenlose Checkliste, Landingpage, Ratgeber für rund 29 €, verkauft über Digistore24, Nachrichten über ManyChat), **Stand** (noch leer) und **Nächste Schritte** (noch leer). Mehr schreibst du nicht hinein.
- `<PFAD>/<BEREICHE>/farbwerk-beispiel-gmbh/area.md` mit den Überschriften **Zweck** (die Farbwerk Beispiel GmbH in Musterstadt: Leistungen, Preise, Angebote, Baustellenalltag) und **Laufende Aufgaben** (noch leer).

**Dann schreibst du die CLAUDE.md.** Sag vorher den Hinweis aus Etappe 2 an („Bevor du in den persönlichen Ordner schreibst“). Bei einer Blockade gilt dort der Weg über den Moduswechsel auf Manual. Prüf mit `ls ~/.claude/CLAUDE.md` (voller Pfad), ob die Datei schon existiert. Existiert sie, gelten die Regeln aus Etappe 4, Abschnitt „Erst klären, was mit dem Vorhandenen passiert“: Du hängst nur mit dem Edit-Werkzeug an und lässt jede vorhandene Zeile stehen. Sonst legst du sie so an, mit echten Werten statt der spitzen Klammern:

```markdown
# CLAUDE.md

## Wer ich bin

Ich bin Max Beispiel, Malermeister und Inhaber der Farbwerk Beispiel GmbH in Musterstadt. Ich baue gerade einen Ratgeber zur Wohnungsübergabe: Ein Video führt zu einer kostenlosen Checkliste, von dort geht es auf eine Landingpage und zum Ratgeber für rund 29 €. Verkauft wird über Digistore24, die Nachrichten laufen über ManyChat. Bisher habe ich ChatGPT genutzt, Claude ist neu für mich.

## Wie ich arbeiten soll

- Du duzt mich und schreibst locker wie auf der Baustelle.
- Kurz und konkret. Ein Schritt nach dem anderen, keine langen Erklärungen.
- Was du selbst erledigen kannst, erledigst du. Ich klicke nur, wo es nicht anders geht, und dann sagst du mir genau, wo.
- Schreib so, wie ein Handwerksmeister mit Kunden redet: klar, ehrlich, ohne Fachchinesisch.
- In Videos zeige ich mein Gesicht nicht. Schlag nie Formate vor, bei denen ich vor die Kamera muss.
- Fakten zu Mietrecht, Schönheitsreparaturen und Schäden nie erfinden. Stehen sie nicht im Second Brain oder in meinem Material, frag nach.
- Fehlt dir etwas über mich oder meine Arbeit, frag nach, statt zu raten. Mit `/interview` schärfe ich dieses Briefing jederzeit nach.

## Meine Ordner

Mein Arbeitsordner ist `<PFAD>`, aufgeteilt in vier Bereiche:

- `<PFAD>/<PROJEKTE>/`: Projekte mit einem Ende, ein Unterordner pro Projekt mit einer `project.md` (Ziel, Stand, nächste Schritte). Aktuell: `ratgeber-wohnungsuebergabe`.
- `<PFAD>/<BEREICHE>/`: Bereiche, die dauerhaft laufen, ein Unterordner pro Bereich mit einer `area.md`. Aktuell: `farbwerk-beispiel-gmbh`.
- `<PFAD>/<RESSOURCEN>/`: Material und Wissen, darin Eingangskorb, Second Brain, Gedächtnis und deine Ausgaben.
- `<PFAD>/<ARCHIV>/`: Abgeschlossenes.

Verzeichnisse (`index.md`) gibt es nur im Second Brain: die Landkarte `<PFAD>/<RESSOURCEN>/wissen/index.md` und je eins in jeder Ablage. Archiv und Eingangskorb haben bewusst keins. Was dort liegt, siehst du mit `ls` nach, bevor du etwas darüber sagst oder dort etwas anlegst.

## Arbeitsregeln

- Sag mir immer, in welchen Ordner du etwas geschrieben hast, mit vollem Pfad.
- Wenn ich dir eine Datei nenne, sage ich dir dazu, in welchem Ordner sie liegt. Wenn ich es vergesse, frag nach, statt im ganzen Ordner zu suchen.
- Fachliche Aussagen über Zahlen, Termine, Preise und Zusagen nie erfinden. Stehen sie nicht im Second Brain oder in meinem Material, frag nach.
- Passwörter, Zugangsdaten und API-Schlüssel tippe ich nie in den Chat. Brauchst du einen, sag mir, wo ich ihn selbst eintrage.
```

Zeig ihm danach den Pfad der Datei und sag in einem Satz: Das ist das Gedächtnis fürs Arbeiten, Claude liest es ab jetzt bei jedem Start. Gleich im Interview schärft sie sich weiter. Dann geht es mit Etappe 1 weiter.

---


## Etappe 1: Eingangskorb und Second Brain anlegen

Lege im Ressourcen-Ordner an, was fehlt (Schreibweise aus Etappe 0, hier als Beispiel mit `03.ressources`):

```
03.ressources/
  raw/
    inbox/
  wissen/
  claude-output/
```

`raw/inbox/` ist der Eingangskorb: Dort landet alles Neue, bevor es einsortiert wird. `raw/` selbst ist das Quellen-Archiv für alles, was schon verarbeitet wurde. `claude-output/` ist der Ort für alles, was Claude für ihn baut (Etappe 2).

**Die Ablagen im Second Brain** (die Schubladen unter `wissen/`) legst du hier noch nicht an. Sie entstehen in Etappe 3 aus dem Interview.

**Hat Etappe 0 schon einen Eingangskorb an anderer Stelle gefunden**, etwa `03.ressources/inbox/`: leg keinen zweiten an. Die Frage, ob er nach `raw/inbox/` umziehen darf, kommt in Etappe 3 mit in die Fragen nach dem Interview. Bis dahin arbeitest du mit seinem echten Pfad. Bleibt er, wo er ist, setzt du seinen echten Pfad in das Briefing aus Etappe 4 und in die Befehle aus Etappe 5 ein und ersetzt dort die Formulierung „eine Ebene höher nach `raw/`" durch den Ordner, in den verarbeitetes Material bei ihm wandert. Gibt es noch keinen Ordner für verarbeitetes Material, leg `raw/` im Ressourcen-Ordner direkt an und melde es. Liegen im vorhandenen Eingangskorb schon Dateien, nenn sie jetzt, verarbeitet werden sie erst nach dem Setup.

**Hat Etappe 0 einen Wissensbereich unter anderem Namen gefunden**, etwa `knowledge/` oder `vault/`: leg kein `wissen/` daneben an. Die Frage nach dem Umbenennen kommt ebenfalls in Etappe 3. Bleibt der Name, setzt du ihn überall dort ein, wo unten `wissen` in einem Pfad steht.

Danach legst du `wissen/start.md` an, mit genau drei Abschnitten und leeren Platzhaltern: Was gerade läuft · Was zuletzt passiert ist · Was als Nächstes ansteht. Diese Startseite ist der Wiedereinstieg für jede neue Sitzung. Landkarte und Verzeichnisse folgen in Etappe 3 mit den Ablagen.

---

## Etappe 2: Ausgabe-Ordner und persönlicher Ordner

### Der Ausgabe-Ordner

Alles, was Claude für Max baut (ein Text als Datei, eine Grafik, eine Präsentation, eine Checkliste), bekommt eine eigene Mappe unter `<PFAD>/<RESSOURCEN>/claude-output/`, benannt nach dem Muster `JJJJ-MM-TT_art_thema`. Den Ordner hast du in Etappe 1 angelegt. Die Regel dazu kommt in Etappe 4 ins Briefing. Sag ihm das in einem Satz: So findet er jedes Ergebnis wieder, sortiert nach Datum.

### Bevor du in den persönlichen Ordner schreibst

In den Etappen 0b, 4 und 5 schreibst du auch außerhalb des Arbeitsordners, nach `~/.claude/`. Dafür gilt:

**Sag vorher an:** Ab jetzt schreibst du an einigen Stellen in den persönlichen Ordner außerhalb des Arbeitsordners. Dabei kommen Rückfragen, ob das erlaubt ist. Bitte um Zustimmung, wenn sie erscheinen.

**Wenn ein Schreibzugriff dorthin abgelehnt oder blockiert wird:** Brich nicht ab. In den Plänen Pro und Max läuft Claude Code im Auto-Modus, und der kann Schreibzugriffe unter `~/.claude/` blocken, mit der Meldung „Blocked by classifier", ohne den Pfad zu nennen.

**Der erste Weg ist der Moduswechsel, nicht der Umzug.** Lass ihn unten im Eingabefeld auf die Modus-Anzeige klicken und dort **Manual** wählen. Im Terminal geht das mit `Shift` und `Tab`, bis unten „manual mode on“ steht. Den Weg über `/permissions` nimmst du nicht. Dort steht die Blockade zwar unter „Recently denied“ und lässt sich mit `r` freigeben, für Einsteiger ist das aber zu unübersichtlich. Wiederhol dann den Schreibvorgang. Statt der Blockade kommt jetzt ein Dialog, und er klickt auf **„Yes, and allow Claude to edit its own settings for this session“**. Sag ihm dazu: Ab jetzt kommen öfter Rückfragen, auch beim Lesen, und vor jedem Schreiben ein Vergleichsfenster. Dort reicht jeweils **Yes**. Etappe 6 sagt ihm, wann er zurück auf Auto darf.

**Klickt er den Dialog versehentlich weg**, sag das und wiederhol den Schreibvorgang genau einmal. **Erst wenn auch der zweite Versuch scheitert**, legst du Briefing und Befehle im Arbeitsordner an, also `CLAUDE.md` im Wurzelordner und die Befehle unter `.claude/commands/`. Rechne dabei damit, dass es dort erneut hakt: Jeder Ordner namens `.claude` ist geschützt, auch der im Arbeitsordner, und braucht denselben Dialog. Ohne Bestätigung kommt nur die `CLAUDE.md` im Wurzelordner durch, die Befehle nicht. **Liegt dort schon eine `CLAUDE.md`, hängst du auch dort nur mit dem Edit-Werkzeug an** und überschreibst sie nicht. Sag dazu deutlich: „Das gilt jetzt nur in diesem Ordner. Damit es überall gilt, müssen die Dateien später nach `~/.claude/` umziehen."

**Fasse dabei nie mehrere Schreibvorgänge in einen Befehl.** Wird der Befehl geblockt, fällt alles weg, auch ein vorangestelltes Backup.

---

## Etappe 3: Das Interview und die Ablagen

Jetzt lernst du Max kennen. Aus seinen Antworten entstehen zweierlei: die Ablagen im Second Brain und das Briefing in Etappe 4.

### Was Viktor schon weiß

Das hat Viktor vorab mit Max geklärt. Du setzt es voraus, fragst nicht noch einmal danach und nimmst es in Etappe 4 ins Briefing:

- **Beruf und Betrieb:** Max Beispiel ist Malermeister und Inhaber der Farbwerk Beispiel GmbH in Musterstadt.
- **Woran er gerade baut:** einen Ratgeber zur Wohnungsübergabe. Ein Reel führt zu einer kostenlosen Checkliste, von dort geht es auf eine Landingpage und zum Ratgeber für rund 29 €. Verkauft wird über Digistore24, die Nachrichten laufen über ManyChat.
- **Bisherige KI-Nutzung:** bisher ChatGPT, Claude ist neu für ihn. Alte Claude-Chats gibt es nicht.
- **Damit sind die Interviewfragen 1 und 2 beantwortet.** Du stellst nur die Fragen 3, 4 und 5, neu nummeriert als 1 bis 3. Den Arbeitstag leitest du in Etappe 4 aus seinen wiederkehrenden Aufgaben ab.
- **Regeln für „Wie ich arbeiten soll“, wörtlich übernehmen:**
  - Kurz und konkret. Ein Schritt nach dem anderen, keine langen Erklärungen.
  - Was du selbst erledigen kannst, erledigst du. Ich klicke nur, wo es nicht anders geht, und dann sagst du mir genau, wo.
  - Schreib so, wie ein Handwerksmeister mit Kunden redet: klar, ehrlich, ohne Fachchinesisch.
  - In Videos zeige ich mein Gesicht nicht. Schlag nie Formate vor, bei denen ich vor die Kamera muss.
  - Fakten zu Mietrecht, Schönheitsreparaturen und Schäden nie erfinden. Stehen sie nicht im Second Brain oder in meinem Material, frag nach.
- Er will Tempo. Halte deine Meldungen zwischen den Etappen besonders kurz.

### Das Interview

Sag einen Satz vorweg: Jetzt kommen ein paar offene Fragen, damit Claude ihn und seine Arbeit kennt. Danach schreibst du die offenen Fragen.

**Regeln für das Interview:**

- **Alle offenen Fragen in einer einzigen Nachricht**, nummeriert, als normale Nachricht und nicht mit AskUserQuestion. Er beantwortet sie in einem Rutsch, das spart im Termin die meiste Zeit.
- Fragen, die oben unter „Was Viktor schon weiß“ als beantwortet stehen, lässt du weg und nummerierst die übrigen neu. Was Etappe 0 gefunden hat, fragst du ebenfalls nicht.
- Sag einen Satz dazu, dass er diktieren darf statt zu tippen, gern ausführlich, und die Nummern dabei einfach mitsprechen kann.
- **Nimm jede Antwort so, wie sie kommt.** Höchstens EINE Nachfrage im ganzen Interview, und nur, wenn ohne sie eine Ablage unbelegt bliebe.
- Kommentiere die Antworten nicht, sammle sie.

**So gehst du vor (der Interviewprompt):** Du wartest nicht darauf, dass er dir etwas eingibt, du arbeitest ihn selbst ab. Er lautet:

> Lies zuerst meine CLAUDE.md, mein Second Brain (Landkarte und Startseite) und dein Gedächtnis. Stell mir danach höchstens fünf Fragen zu dem, was dort noch fehlt, in einer einzigen nummerierten Nachricht. Frag nichts, was schon drinsteht. Wenn ich geantwortet habe, ergänze meine CLAUDE.md mit dem Edit-Werkzeug, ohne etwas zu überschreiben, und zeig mir kurz, was neu dazugekommen ist.

Die Datei, die du zuerst liest, ist die CLAUDE.md aus Etappe 0b, dazu `wissen/index.md`, `wissen/start.md` und das Gedächtnis (liegt dort noch nichts, ist das normal). Aus der Liste „Die Fragen“ unten stellst du nur die, die dort noch nicht beantwortet sind. Der Befehl `/interview` (Etappe 5) enthält denselben Ablauf, damit er das Briefing später jederzeit nachschärfen kann. Sag ihm das in einem Satz.

**Die Fragen:**

1. Wer bist du beruflich, und was machst du an einem normalen Arbeitstag? Wenn du das System auch für private oder familiäre Dinge nutzt, nenn das gleich mit.
2. Wofür hast du Claude bisher benutzt? Gibt es Chats oder Projekte, auch aus einem alten Konto, die du weiterführen willst?
3. Welche Aufgaben kommen bei dir immer wieder, mindestens einmal im Monat?
4. Wo verlierst du die meiste Zeit mit Suchen oder Wiederholen? Denk dabei an die Dinge, die du dir immer wieder heraussuchen musst: Menschen, Zahlen, Abläufe, Vorlagen, Regeln, Termine.
5. Was soll auf keinen Fall in dieses System? Denk an fremde Daten, an heikle Themen, an alles, was ein Arbeitgeber oder Kunden betrifft.

### Danach: Die Ablagen vorschlagen

Aus den Antworten und dem, was Viktor schon weiß, schlägst du die Ablagen für `wissen/` vor. Das sind die Schubladen, in die später jedes Wissen einsortiert wird. Viktors Vorschlag aus dem Vorgespräch:

| Ablage | Was hineingehört |
|---|---|
| `ratgeber/` | alles zum Ratgeber Wohnungsübergabe: Kapitel, Fakten, Checkliste, Fragen von Kunden |
| `marketing/` | Reels, Texte, Landingpage, Funnel, Digistore24 und ManyChat |
| `betrieb/` | die Farbwerk Beispiel GmbH: Leistungen, Preise, Angebotsvorlagen, Baustellenalltag |
| `ablaeufe/` | wiederkehrende Abläufe, die Claude für ihn erledigt, Schritt für Schritt |

Die ersten drei sind durch „Was Viktor schon weiß“ belegt. `ablaeufe/` legst du nur an, wenn seine Antwort auf die Frage nach wiederkehrenden Aufgaben dafür einen Beleg liefert.

**Regeln für den Vorschlag:**

- Viktors Vorschlag ist der Ausgangspunkt. Du übernimmst ihn, wenn die Antworten ihn tragen, und änderst nur, was die Antworten ausdrücklich anders sagen.
- **Die Antwort, was nie ins System darf, geht vor.** Nennt eine Ablage in ihrer Beschreibung etwas, das er dort ausgeschlossen hat (etwa Kundendaten), streichst du es aus der Beschreibung und sagst es beim Vorschlag dazu.
- **Höchstens fünf Ablagen, mindestens drei.** Weniger ist besser. Wer zehn Schubladen hat, findet nichts wieder.
- **Jede Ablage braucht einen Beleg**: einen Satz aus seinen Antworten oder aus „Was Viktor schon weiß“. Findest du keinen, schlägst du die Ablage nicht vor.
- **Namen in seiner Sprache**, ohne Fachbegriffe. Spricht er von Exposés, heißt die Ablage `exposes` und nicht `dokumentation`.
- **Ordnernamen klein, ohne Umlaute und ohne ß.** macOS speichert Umlaute in Dateinamen anders als Windows, daran scheitern Suche und Verweise. Aus „Gespräche“ wird der Ordner `gespraeche`, der ausgeschriebene Name steht in der ersten Zeile seiner `index.md`.
- **Nur eine Ebene.** Keine Unterordner. Die einzelnen Wissensseiten entstehen später aus echtem Material.

**Zeig den Vorschlag als Liste:** Ordnername, ein Satz was hineingehört, der Beleg. Frag dann mit AskUserQuestion: „So anlegen (Empfohlen)“ oder „Namen ändern“. Im selben Aufruf stellst du die übrigen Fragen dieser Etappe, solange es zusammen höchstens vier sind, sonst in einem zweiten Aufruf direkt danach:

**Anrede in Texten für Kunden:** „Du, locker wie auf der Baustelle (Empfohlen)“ · „Sie, eher förmlich“. Die Antwort ändert die Anrede-Zeile unter „Wie ich arbeiten soll“ im Briefing (Etappe 4).

**Gab es in Etappe 0 oder 1 etwas zu klären** (ein Eingangskorb oder Wissensbereich soll umziehen, eine vorhandene `CLAUDE.md`, deren Regeln vielleicht übernommen werden sollen, ein vorhandener Befehl mit gleichem Namen oder ein eigener Abschlussbefehl wie `/log`, der bleiben soll), gehören diese Fragen ebenfalls dazu.

**Warte auf das Okay zu den Ablagen.** Wählt er „Namen ändern“, übernimmst du seine Namen nach den Regeln oben und legst ohne weitere Rückfrage an.

### Erst danach anlegen

- die freigegebenen Ablagen als Ordner unter `wissen/`
- `wissen/index.md` als **Landkarte**: zeigt nur auf die Ablagen, nie auf einzelne Seiten, ein Satz pro Ablage, jede Ablage als Verweis `[[<RESSOURCEN>/wissen/ablage/index|Ablage]]` mit dem echten Ordner. Verweise schreibst du immer als Pfad ab `<PFAD>/` ohne `.md`, so findet Obsidian sie eindeutig, und `ls "<PFAD>/<Verweis>.md"` prüft sie. Als `<Verweis>` gilt nur der Teil vor einem `|`, der Anzeigename dahinter gehört nicht zum Pfad
- in jeder Ablage eine `index.md` als **Verzeichnis**: in der ersten Zeile der ausgeschriebene Name und was dort hineingehört, ein Verweis zurück zur Landkarte `[[<RESSOURCEN>/wissen/index|Landkarte]]`, darunter eine zunächst leere Liste

Ab hier heißt `<ABLAGEN>` die Liste der echten Ordnernamen in Backticks, etwa `kunden`, `angebote` und `ablaeufe`.

**Die übrigen Antworten setzt du um, ohne weitere Rückfrage.** Antworten zur Arbeitsweise kommen als Spiegelstrich unter „Wie ich arbeiten soll“ ins Briefing, doppelte Regeln lässt du weg. Ist eine Antwort unentschieden, nimmst du die Empfehlung.

---

## Etappe 4: Das Briefing vervollständigen und das Gedächtnis

Das Briefing ist die Datei `~/.claude/CLAUDE.md`, die Claude bei jedem Start automatisch mitliest. Du hast sie in Etappe 0b als Grundstock angelegt. Sie liegt nicht im Arbeitsordner, damit sie in jedem Ordner gilt, in dem gearbeitet wird. Hier vervollständigst du sie mit den Antworten aus dem Interview und dem Second Brain.

**Deshalb stehen dort alle Pfade absolut**, also mit vollem PFAD. Ein Pfad wie `03.ressources/wissen/` würde in jedem anderen Ordner ins Leere zeigen und still scheitern. Für Schreibzugriffe gilt, was in Etappe 2 unter „Bevor du in den persönlichen Ordner schreibst“ steht.

### Erst klären, was mit dem Vorhandenen passiert

**Prüf vor dem Schreiben mit `ls ~/.claude/CLAUDE.md`, ob die Datei existiert.** `ls` fragt nie nach und klappt auch dann, wenn in Etappe 0 ein Dialog weggeklickt wurde. Existiert sie, gilt nur das Edit-Werkzeug.

Je nachdem, was Etappe 0 und Etappe 3 ergeben haben:

- **`~/.claude/CLAUDE.md` existiert schon:** Du lässt jede vorhandene Zeile unverändert stehen und hängst deinen neuen Block **mit dem Edit-Werkzeug** unten an. Niemals mit einem kompletten Neuschrieb der Datei, denn das Write-Werkzeug hängt nicht an, es ersetzt. Dabei geht alles verloren, was du nicht mitgeschrieben hast. Gestrichen wird nur in deinem Entwurf: Was schon in der Datei steht, nimmst du aus dem Entwurf heraus und sagst, welche Zeile das war. Die Titelzeile `# CLAUDE.md` lässt du beim Anhängen ebenfalls weg.
- **Eine `CLAUDE.md` liegt im Arbeitsordner:** Was Max in Etappe 3 davon bestätigt hat, übernimmst du unter „Wie ich arbeiten soll“. Übernimm das Bestätigte und **lass das Original liegen**, statt es zu verschieben oder zu löschen. Sag dazu, dass die Datei im Arbeitsordner weiterhin gilt, wenn er in diesem Ordner arbeitet, und dass doppelte Regeln an zwei Orten auseinanderlaufen. Empfiehl, sie später aufzuräumen, aber mach es nicht selbst.
- **Der Text kam aus einer alten Projekt-Anweisung:** Übernimm die Inhalte, ohne die Quelldatei anzufassen.

### Das Briefing vervollständigen

Du arbeitest nur mit dem **Edit-Werkzeug**, nie mit einem Neuschrieb der Datei, und das **ohne weitere Rückfrage**:

1. **„Wer ich bin“:** Ergänze bis zu drei Sätze in der Ich-Form, in seinen Worten: was ein normaler Arbeitstag enthält (fehlt dazu eine Antwort, leitest du es aus seinen wiederkehrenden Aufgaben ab) und wofür er Claude nutzen will. Nur, was er gesagt hat oder was in Etappe 0b steht. Nichts ausschmücken.
2. **„Wie ich arbeiten soll“:** Ergänze Spiegelstriche. Je wiederkehrender Aufgabe eine Zeile, in welcher Ablage du dafür zuerst nachsiehst. Je Zeitfresser (wo er mit Suchen oder Wiederholen Zeit verliert) eine Zeile, was du ihm dort abnimmst. Die Antwort auf die Frage, was nie ins System darf, kommt als eigene Regel hinein: „Was nie in dieses System darf: …“, mit seinen Worten. Hat er dazu nichts gesagt, schreibst du: „Fremde personenbezogene Daten, Zugangsdaten und Zahlungsdaten kommen nie in dieses System.“ Die Zeile zur Anrede aus Etappe 0b änderst du, wenn er in Etappe 3 „Sie“ gewählt hat. Doppelte Regeln lässt du weg.
3. **Hänge die beiden folgenden Abschnitte unten an.** `<PFAD>`, `<RESSOURCEN>` und `<ABLAGEN>` setzt du ein. Hat Etappe 3 etwas geändert (Eingangskorb oder Wissensbereich unter anderem Namen, eine bestätigte Regel aus einer alten Datei), setzt du die echten Pfade und die bestätigte Regel ein.

```markdown
## Wo mein Wissen liegt

Mein Second Brain liegt unter `<PFAD>/<RESSOURCEN>/wissen/`, aufgeteilt in die Ablagen <ABLAGEN>. Diese Pfade gelten immer, egal welchen Ordner ich gerade geöffnet habe.

- Bei Arbeitsbeginn liest du die Landkarte `<PFAD>/<RESSOURCEN>/wissen/index.md` und die Startseite `<PFAD>/<RESSOURCEN>/wissen/start.md` mit.
- Vor jeder inhaltlichen Aufgabe (einen Text schreiben, etwas bauen, eine Frage beantworten) suchst du in der Landkarte und den Verzeichnissen der Ablagen nach passenden Seiten und liest sie, bevor du loslegst. Nutzt du eine Seite, nennst du sie.
- Neues Material kommt zuerst nach `<PFAD>/<RESSOURCEN>/raw/inbox/`. Sortiert wird später mit `/verarbeiten`, nie sofort.
- Wenn ich sage „Nimm das in mein Second Brain auf" oder eindeutig dasselbe meine, behandelst du meine ausdrücklich genannten Fakten und Entscheidungen als neue Quelle. Zeig mir zuerst den Entwurf und warte auf mein Okay. Erst dann legst du ihn datiert im Eingangskorb ab und verarbeitest ihn.
- Nach jeder Änderung im Second Brain ziehst du das Verzeichnis der betroffenen Ablage nach und verlinkst die Seite mit verwandten Seiten, in beide Richtungen. Eine Seite, die in keinem Verzeichnis steht, wird nicht gefunden. Verweise setzt du nur auf Seiten, die es gibt.
- Entsteht in einer Arbeitssitzung dauerhaftes Wissen (ein Ablauf, eine Entscheidung, eine Vorlage), fragst du am Ende der Aufgabe einmal, ob es ins Second Brain soll. Bei Ja legst du es als Notiz mit der Quelle „aus der Sitzung vom JJJJ-MM-TT“ im Eingangskorb ab.
- Jede Sachaussage im Second Brain braucht einen Verweis auf die Datei, aus der sie stammt. Widersprüche markierst du mit `WIDERSPRUCH:`, Unsicheres mit `OFFENE FRAGE:`. Nichts still auflösen, nichts erfinden.
- Zeitkritische Angaben (Preise, Tool-Versionen, Marktzahlen) bekommen inline einen Stand-Marker `(Stand: JJJJ-MM, Quelle)`. Ohne ihn ist nicht erkennbar, wann eine Aussage veraltet.
- Wenn ich eine Frage stelle, prüfst du zuerst Landkarte und Startseite und öffnest dann nur die passenden Wissensseiten. Antworte mit Quellen. Gibt das Second Brain die Antwort nicht her, sag das offen statt zu raten.
- Dein Gedächtnis (Auto-Memory) liegt in `<PFAD>/<RESSOURCEN>/memory/`. Das Gedächtnis sammelt, das Second Brain behält: Auf Dauer bleibt im Gedächtnis nur, wie wir zusammenarbeiten (Vorlieben, Korrekturen). Sachwissen (Abläufe, Fachwissen, Vorlagen, Stil, Entscheidungen) überträgst du beim nächsten `/verarbeiten` als Wissensseite ins Second Brain, im Gedächtnis bleibt nur ein Verweis darauf. Zeigt ein Eintrag im Gedächtnis auf eine Wissensseite, liest du diese Seite.
- Am Ende des Arbeitstags starte ich `/feierabend`. Er legt fertige Stücke ab, fragt, was ins Second Brain gehört, und macht ein Backup.
- Etwa einmal im Monat läuft `/pruefung`, der Second Brain und Gedächtnis zusammen prüft. Hat `<PFAD>/<RESSOURCEN>/memory/MEMORY.md` bei Arbeitsbeginn mehr als 140 Zeilen oder mehr als 17.900 Bytes (70 Prozent der Ladegrenze), sagst du es mir von selbst und schlägst `/pruefung` vor.

## Ausgaben und Ablage

- Alles, was du für mich baust (ein Text als Datei, eine Grafik, eine Präsentation, eine Checkliste), bekommt eine eigene Mappe `<PFAD>/<RESSOURCEN>/claude-output/JJJJ-MM-TT_art_thema/`. Darin liegen die fertigen Dateien.
- Steckt im Stück ein Bild oder Logo von woanders, kopierst du es in den Unterordner `verwendet/` dieser Mappe und verweist in der fertigen Datei auf diese Kopie. So bleibt die Mappe vollständig, auch wenn sich das Original später ändert. Originale veränderst, verschiebst und löschst du nie, außer ich sage es ausdrücklich.
- Am Ende nennst du mir den vollen Pfad der Mappe.
```

**Nach dem Ergänzen** zeigst du ihm den Pfad der Datei sowie die Abschnitte „Wer ich bin“ und „Wie ich arbeiten soll“ und sagst in zwei Sätzen: Das Briefing ist aus seinen Antworten entstanden. Was nicht stimmt, ändert er jederzeit selbst, mit einem Satz wie „Ändere in meinem Briefing …“, oder er ruft `/interview` auf.


### Danach: Das Gedächtnis ins Second Brain legen

Claude Code merkt sich nebenbei selbst Dinge über die Zusammenarbeit: Vorlieben, Korrekturen, wie er arbeitet. Das ist das Auto-Memory. Ab Werk liegt es versteckt unter `~/.claude/projects/`. Du legst es jetzt in sein Second Brain, damit er es sieht, es mit dem Ordner umzieht und `/verarbeiten` das Sachwissen daraus ins Second Brain übertragen kann. **Dafür gibt es keine Rückfrage**, das ist fester Teil des Setups. Sag nur in einem Satz an, was du tust.

1. Leg `<PFAD>/<RESSOURCEN>/memory/` an. Der Ordner liegt neben `wissen/` und nicht darin: Das Second Brain hält Sachwissen mit Quelle, das Gedächtnis hält Notizen zur Zusammenarbeit. `/verarbeiten` überträgt Sachwissen aus dem Gedächtnis ins Second Brain und lässt dort einen Verweis stehen, `/pruefung` meldet, was noch nicht übertragen ist.
2. Lies `~/.claude/settings.json` (voller Pfad aus Etappe 0). Existiert sie nicht, leg sie mit diesem Inhalt an:

   ```json
   {
     "autoMemoryDirectory": "<PFAD>/<RESSOURCEN>/memory"
   }
   ```

   Existiert sie, liest du sie vorher einmal ganz, damit du den alten Stand zum Wiederherstellen hast. Dann fügst du mit dem Edit-Werkzeug den Schlüssel als erste Zeile direkt nach der öffnenden Klammer ein, mit Komma am Ende, wenn weitere Schlüssel folgen. Steht in der Datei nur `{}`, ohne Komma. Steht alles in einer Zeile, etwa `{"permissions":…}`, setzt du den Schlüssel direkt hinter die öffnende Klammer: `{"autoMemoryDirectory": "…", "permissions":…}`. Sonst fasst du nichts an. Steht dort schon ein `autoMemoryDirectory`, änderst du es nicht, sondern fragst mit AskUserQuestion, ob es umziehen soll. Windows-Pfade schreibst du mit Schrägstrichen. Validiere die Datei danach, wie unter „JSON prüfen“ in Etappe 0 beschrieben. Bei einem echten JSON-Fehler stellst du den vorherigen Stand wieder her. Wird der Schreibzugriff geblockt, gilt derselbe Weg wie in Etappe 2: zuerst der Moduswechsel. **Scheitert auch der zweite Versuch**, bleibt das Gedächtnis vorerst am alten Ort. Du sagst das, lässt den Ordner `memory/` stehen, schreibst in die Übergabe „Das Gedächtnis liegt noch unter `~/.claude/projects/`, Umzug offen“, und die Gedächtnis-Kontrolle in Etappe 6 entfällt. Die Gedächtnis-Zeile im gerade gespeicherten Briefing passt du mit dem Edit-Werkzeug an: „Dein Gedächtnis liegt noch unter `~/.claude/projects/`, Umzug offen.“
3. **Vorhandene Erinnerungen mitnehmen.** Schau mit `ls -d ~/.claude/projects/*/memory/` nach (voller Pfad des Benutzerordners). Meldet die Shell „no matches found“ oder „No such file or directory“, gibt es noch keinen solchen Ordner. Der passende Ordner heißt wie PFAD, nur ist jedes Zeichen, das kein Buchstabe und keine Ziffer ist (Schrägstrich, Doppelpunkt, Punkt, Leerzeichen), ein Bindestrich: aus `/Users/anna/KI-System` wird `-Users-anna-KI-System`, aus `C:/Users/anna/KI-System` wird `C--Users-anna-KI-System`. Umlaute und ß zählen dabei nicht als Buchstaben, auch sie werden zum Bindestrich. Liegt der Arbeitsordner in einem Git-Repository, heißt der Ordner nach dessen Wurzel. Im Zweifel nimmst du den Ordner mit dem jüngsten Änderungsdatum. Ist der Pfad sehr lang, kürzt Claude Code den Ordnernamen und hängt eine kurze Kennung an, etwa `-KI-Arbeitsplat-ksi9x4`. Dann nimmst du den Ordner, der so beginnt. Gibt es Dateien, kopierst du sie in den neuen Ordner, ohne die Originale anzufassen, und sagst, wie viele es waren. Diese laufende Sitzung hat den Ordner vermutlich schon angelegt und sich vielleicht etwas gemerkt, auch das nimmst du mit. Gibt es keine Dateien, ist das auf einem frischen Rechner der Normalfall.
4. Sag dazu: Die Einstellung greift erst in der nächsten Unterhaltung, also nach dem Neustart in Etappe 6. Ab dann gilt dasselbe Gedächtnis in jedem Ordner, genau wie das Briefing.

---

## Etappe 5: Die Befehle für den Alltag anlegen

Jetzt kommen vier Befehle: `/interview`, `/verarbeiten`, `/pruefung` und `/feierabend`, dazu ein kleines Backup-Skript.

Die Befehle kommen in den persönlichen Ordner, nach `~/.claude/commands/`. Damit stehen sie in jedem Projekt zur Verfügung. Gilt der Ausweichweg aus Etappe 2, kommen sie nach `.claude/commands/` im Arbeitsordner.

**Existiert `~/.claude/commands/` noch nicht, entsteht der Ordner mit der ersten Datei.** Schreib dabei den vollen Pfad aus Etappe 0 aus, nie `~`. Wenn alle vier Dateien geschrieben sind, prüf mit `ls` am vollen Pfad, dass sie wirklich dort liegen, und schau mit `ls` im Arbeitsordner nach, ob dort versehentlich ein Ordner namens `~` entstanden ist. Gibt es ihn, sag das, verschieb die Dateien an den richtigen Ort und lösch den leeren Ordner erst nach seinem Okay.

**Setze in allen Dateien `<PFAD>`, `<RESSOURCEN>`, `<ARCHIV>` und `<HOME>` (aus Etappe 0) durch die echten Werte ein.** Wenn eine der Dateien schon existiert: nicht überschreiben, den Unterschied zeigen und fragen. Zur Wahl stehen zwei Wege. Erstens ersetzen: Dann legst du den alten Text vorher als `interview-alt.txt`, `verarbeiten-alt.txt`, `pruefung-alt.txt` oder `feierabend-alt.txt` in den Archiv-Ordner aus Etappe 0, nie nach `commands/`, sonst entsteht daraus ein zweiter Befehl. Zweitens behalten: Dann bekommt der neue Befehl einen anderen Namen, und genau diesen Namen setzt du im Briefing, in Etappe 6 und in den Kontrollen ein.

`interview.md`:

```markdown
---
description: Interviewt dich zu dem, was Claude über dich noch nicht weiß, und ergänzt die CLAUDE.md. Jederzeit zum Nachschärfen
---

# /interview: Die CLAUDE.md nachschärfen

Lies zuerst `<HOME>/.claude/CLAUDE.md`, die Landkarte `<PFAD>/<RESSOURCEN>/wissen/index.md`, die Startseite `<PFAD>/<RESSOURCEN>/wissen/start.md` und das Gedächtnis `<PFAD>/<RESSOURCEN>/memory/MEMORY.md`. Stell mir danach höchstens fünf Fragen zu dem, was dort noch fehlt, in einer einzigen nummerierten Nachricht. Es ist eine normale Nachricht, ich darf die Antworten diktieren. Frag nichts, was schon drinsteht. Hat das Briefing nichts Offenes mehr, sag das und stopp.

Wenn ich geantwortet habe: Ergänze `<HOME>/.claude/CLAUDE.md` mit dem Edit-Werkzeug, ohne etwas zu überschreiben oder zu löschen, und zeig mir kurz, was neu dazugekommen ist. Doppelte Regeln lässt du weg. Sachwissen aus meinen Antworten (Abläufe, Fakten, Vorlagen) gehört nicht ins Briefing: Das legst du nach meinem Okay als Notiz in `<PFAD>/<RESSOURCEN>/raw/inbox/` ab.
```

`verarbeiten.md`:

```markdown
---
description: Überträgt Sachwissen aus dem Gedächtnis und räumt den Eingangskorb ins Second Brain. Etwa einmal pro Woche
---

# /verarbeiten: Gedächtnis und Eingangskorb ins Second Brain räumen

Überträgt Sachwissen aus dem Gedächtnis `<PFAD>/<RESSOURCEN>/memory/` und nimmt neues Material aus `<PFAD>/<RESSOURCEN>/raw/inbox/` ins Wissen auf. Etwa einmal pro Woche aufrufen.

Aufruf: `/verarbeiten` allein, oder `/verarbeiten` mit einer Internetadresse oder einem eingefügten Text dahinter.

## Ablauf

0. **Wenn beim Aufruf etwas mitgeschickt wurde**, also eine Internetadresse oder ein Textabschnitt: Leg daraus zuerst eine Datei im Eingangskorb an, bevor du weitermachst.
   - **Bei einer Internetadresse:** Ruf die Seite ab und speichere den lesbaren Text (ohne Navigation und Werbung) als `<PFAD>/<RESSOURCEN>/raw/inbox/JJJJ-MM-TT-kurzer-titel.md`. Ganz oben in die Datei kommen die Adresse und das Abrufdatum, das ist später der Quellverweis. Kannst du die Seite nicht abrufen, sag das offen und bitte darum, den Text einzufügen. Erfinde nie einen Inhalt, den du nicht gelesen hast.
   - **Bei eingefügtem Text:** dasselbe, nur ohne Abruf. Frag nach, woher der Text stammt, wenn es nicht dabeisteht. Ohne Herkunft gibt es später keinen Quellverweis.
   - Sag, welche Datei du angelegt hast, und mach dann bei Schritt 1 weiter.
   **Wenn der Auftrag stattdessen lautet „Nimm das in mein Second Brain auf" oder eindeutig dasselbe meint:** Fasse nur die ausdrücklich genannten Fakten und Entscheidungen aus der aktuellen Unterhaltung als Entwurf zusammen. Zeig ihn und warte auf ein Okay. Erst danach speicherst du ihn als `<PFAD>/<RESSOURCEN>/raw/inbox/JJJJ-MM-TT-notiz.md` und machst bei Schritt 1 weiter.
1. **Gedächtnis durchsehen, vor dem Eingangskorb.** Gibt es `<PFAD>/<RESSOURCEN>/memory/MEMORY.md` noch nicht oder ist `memory/` leer, gibt es nichts zu übertragen, und du machst mit Schritt 2 weiter. Sonst liest du `MEMORY.md` und jede Datei in `memory/`, die noch kein Verweis ist. Sortier jeden Eintrag:
   - **Zusammenarbeit** (Vorlieben, Korrekturen, wie du mit mir arbeiten sollst): bleibt im Gedächtnis.
   - **Sachwissen** (Abläufe, Fachwissen, Vorlagen, Stil, Entscheidungen): Merk es dir für den Übertrag. Geschrieben wird erst, wenn Schritt 2 die Liste genannt hat. Dann legst du je Eintrag eine Quelldatei `<PFAD>/<RESSOURCEN>/raw/inbox/JJJJ-MM-TT-gedaechtnis-thema.md` an, erste Zeile `Quelle: aus dem Gedächtnis, Eintrag memory/DATEINAME, übertragen am JJJJ-MM-TT`, darunter der Inhalt. Gibt es im Eingangskorb oder in `raw/` schon eine Datei mit derselben Quellzeile (`Eintrag memory/DATEINAME`), egal mit welchem Datum, nimmst du diese wieder und fragst nicht.
2. Lies jede Datei im Eingangskorb und nenn mir zuerst, welche du gefunden hast, getrennt nach „aus dem Gedächtnis“ und „neu“. Ist der Eingangskorb leer, hast du in Schritt 1 nichts zum Übertragen vorgemerkt und wurde nichts mitgeschickt, sag „Nichts zu verarbeiten“ und stopp.
3. Entscheide je Datei, ob eine bestehende Wissensseite erweitert wird oder eine neue entsteht. Prüf vorher im Verzeichnis der Ablage, ob es die Seite schon gibt. Passt eine Datei in keine Ablage, sag das und frag, statt eine neue Ablage zu erfinden.
4. Jede Aussage bekommt einen Verweis auf die Quelldatei. Preise, Zahlen und Tool-Versionen bekommen inline `(Stand: JJJJ-MM, Quelle)`. Widersprüche mit `WIDERSPRUCH:` markieren, Unsicheres mit `OFFENE FRAGE:`. Nichts erfinden, nichts still auflösen.
5. **Vernetzen.** Verweise in doppelten eckigen Klammern, immer als Pfad ab `<PFAD>/` ohne `.md`, etwa `[[<RESSOURCEN>/wissen/ablage/Seitenname]]`. Ein Verweis stimmt, wenn `ls "<PFAD>/<Verweis>.md"` die Datei findet, gemessen am Teil vor einem `|`. Jede neue oder ergänzte Seite verweist auf das Verzeichnis ihrer Ablage, auf ihre Quelldatei an ihrem endgültigen Ort, etwa `[[<RESSOURCEN>/raw/JJJJ-MM-TT-notiz]]`, und unter „Verwandt:“ auf verwandte Seiten, auch in anderen Ablagen. Auf jeder verwandten Seite ergänzt du den Rückverweis. Verweise nur auf Dateien, die es gibt, prüf jede mit `ls` (Quellverweise erst nach dem Verschieben in Schritt 7): Ein Verweis ins Leere legt in Obsidian beim Anklicken eine leere Datei an. Endet eine Quelldatei nicht auf `.md`, etwa `.txt` oder `.pdf`, schreibst du den Verweis mit Endung, etwa `[[<RESSOURCEN>/raw/Fragebogen.pdf]]`, und prüfst ihn mit `ls "<PFAD>/<Verweis>"`.
6. Zieh die Verzeichnisse der betroffenen Ablagen und die `start.md` nach.
7. Zeig mir die Änderungen und warte auf mein Okay. Erst danach verschiebst du die verarbeiteten Dateien von `inbox/` eine Ebene höher nach `raw/`. Bei jedem übertragenen Gedächtnis-Eintrag ersetzt du den Inhalt der Datei in `memory/` durch einen Satz wie `Steht jetzt im Second Brain: [[<RESSOURCEN>/wissen/ablage/Seitenname]] (übertragen am JJJJ-MM-TT).` (Kopfzeilen bleiben) und änderst seine Zeile in `memory/MEMORY.md` so, dass sie die Gedächtnis-Datei behält und auf die Wissensseite zeigt, mit vollem Pfad ab der Festplatte, etwa `- [Angebotsablauf](DATEINAME): steht im Second Brain, <PFAD>/<RESSOURCEN>/wissen/ablage/Angebotsablauf.md`. So steht das Wissen genau einmal, und das Gedächtnis, das bei jedem Start geladen wird, zeigt den Weg dorthin. Zum Schluss prüfst du jeden neuen Verweis, auch die Quellverweise, mit `ls "<PFAD>/<Verweis>.md"`.
8. Fasse zum Schluss zusammen: was aus dem Gedächtnis übertragen wurde, was neu ist, was erweitert wurde.
```

`pruefung.md`:

```markdown
---
description: Monatscheck für Second Brain und Gedächtnis. Misst, findet Lücken, Dubletten und Verwaistes, überträgt Sachwissen und räumt auf, aber nur nach Okay
---

# /pruefung: Second Brain und Gedächtnis prüfen

Ein Befehl für beides, etwa einmal im Monat. Teil A prüft das Second Brain, Teil B das Gedächtnis in `<PFAD>/<RESSOURCEN>/memory/`. Claude lädt bei jedem Start die Datei `MEMORY.md`, aber nur bis 200 Zeilen oder 25.600 Bytes. Was darüber liegt, fehlt still.

Grundregeln: Erst messen, dann urteilen. Nichts löschen: Was wegsoll, wandert nach `<PFAD>/<ARCHIV>/gedaechtnis-archiv/`. Vor jeder Änderung eine Sicherung. Nichts ändern ohne mein Okay. Läuft der Befehl als geplante Aufgabe, gilt dasselbe: Du berichtest, stellst die eine Frage und wartest, bis ich antworte.

## Teil A: Second Brain

1. Hat jede Ablage ihre `index.md`? Stimmen Landkarte und Verzeichnisse mit den tatsächlichen Seiten überein? Fehlt etwas, ist etwas verwaist?
2. Lösen sich alle Quellverweise auf? Gibt es Wissensseiten ohne Quelle (Landkarte, Verzeichnisse und `start.md` zählen nicht)? Zeigt jeder Verweis in doppelten eckigen Klammern auf eine vorhandene Datei? Welche Seiten sind verwaist, also ohne Verzeichniseintrag und ohne Verweis von einer anderen Seite? Fehlen Rückverweise?
3. Welche `WIDERSPRUCH:`- und `OFFENE FRAGE:`-Markierungen sind noch offen?
4. Liegt im Eingangskorb etwas Unverarbeitetes?
5. Welche Seiten tragen zeitkritische Angaben ohne Stand-Marker? Welche Stand-Marker sind älter als ein halbes Jahr?
6. Sind Ablagen dabei, die seit dem Anlegen leer geblieben sind, oder solche, die überquellen? Schlag in dem Fall vor, sie zusammenzulegen oder zu teilen.
7. Liegen in `<PFAD>/<RESSOURCEN>/claude-output/` lose Dateien außerhalb einer Mappe (versteckte Dateien wie `.gitkeep` zählen nicht)?

## Teil B: Gedächtnis

1. **Messen:** Gibt es `MEMORY.md` noch nicht, zählt sie als leer. Zeig als kleine Tabelle: Zeilen und Bytes von `MEMORY.md` mit Auslastung in Prozent gegen 200 Zeilen und 25.600 Bytes (der höhere Wert zählt), die Zahl der Einträge (`.md`-Dateien ohne `MEMORY.md`) und wie viele davon in den letzten 30 Tagen geändert wurden. Ab 70 Prozent ist Aufräumen nötig.
2. **Befunde sammeln:**
   - **Sachwissen, noch nicht übertragen:** Einträge mit Abläufen, Fachwissen, Vorlagen, Stil oder Entscheidungen.
   - **Dubletten:** zwei Einträge zum selben Thema. Vorschlag: zusammenführen, den anderen ins Archiv.
   - **Verwaistes:** eine Zeile in `MEMORY.md` ohne Datei, eine Datei ohne Zeile in `MEMORY.md`, ein `[[Verweis]]`, bei dem `ls "<PFAD>/<Verweis>.md"` nichts findet.
   - **Veraltet:** Einträge zu Erledigtem. Nur als Kandidat nennen, entscheiden tue ich.
   - **Datenschutz:** Einträge mit Passwörtern, Zugangsdaten, Gesundheitsdaten oder Klarnamen von Kunden. Nur melden, nie wörtlich zitieren.
   Eine Gedächtnis-Datei, die nur noch einen Verweis „Steht jetzt im Second Brain“ enthält, ist in Ordnung, solange ihre Zeile in `MEMORY.md` steht.

## Bericht und eine Frage

Zeig alle Befunde aus A und B als eine nummerierte Liste mit je einem Vorschlag. Dann genau ein AskUserQuestion-Aufruf mit höchstens drei Fragen:
1. Second Brain: „Vorschläge umsetzen (Empfohlen)“ · „Nur berichten“
2. Übertrag ins Second Brain: „Alle übertragen (Empfohlen)“ · „Keinen“
3. Gedächtnis aufräumen: „Alle Vorschläge umsetzen (Empfohlen)“ · „Nur Verwaistes“ · „Nichts ändern“
Ist eine Liste leer, fällt ihre Frage weg. Gibt es gar nichts, sag „Second Brain und Gedächtnis sind in Ordnung“ und hör auf.

## Umsetzen, was freigegeben ist

1. **Sicherung:** Kopier den ganzen Ordner `memory/` nach `<PFAD>/<ARCHIV>/gedaechtnis-sicherung-JJJJ-MM-TT/` und nenn den Pfad. Bei Änderungen am Second Brain sicherst du die betroffenen Seiten genauso nach `<PFAD>/<ARCHIV>/wissen-sicherung-JJJJ-MM-TT/`.
2. **Second Brain:** Setz die freigegebenen Vorschläge aus Teil A um. Seiten löschst du nie, verwaiste Seiten verlinkst du oder trägst sie ins Verzeichnis ein. Lose Dateien in `claude-output/` legst du nach dem Abschnitt „Ausgaben und Ablage“ im Briefing ab.
3. **Übertrag:** Lies die Datei `<HOME>/.claude/commands/verarbeiten.md` (der Ort der Befehle, den das Setup angelegt hat), und arbeite dort den Gedächtnis-Schritt und alle folgenden Schritte für die freigegebenen Einträge ab. Mein Okay aus Frage 2 gilt als Okay vor dem Aufräumen. So entsteht jede Wissensseite mit Quelle, Vernetzung und Verzeichniseintrag, und im Gedächtnis bleibt der Verweis.
4. **Gedächtnis aufräumen:** Dubletten zusammenführen und den überzähligen Eintrag ins Archiv verschieben, Zeilen ohne Datei aus `MEMORY.md` streichen, Dateien ohne Zeile eintragen, tote Verweise korrigieren.
5. **Nachmessen und Gegenprobe:** neue Auslastung, jede Zeile in `MEMORY.md` zeigt auf eine vorhandene Datei, jede Datei steht in `MEMORY.md`. Fehlt etwas, spielst du die Sicherung zurück und sagst es.
6. **Bericht** in höchstens sechs Zeilen: Second Brain behoben, Gedächtnis vorher und nachher in Prozent, übertragen, zusammengeführt, archiviert, gemeldet.
```

`feierabend.md`:

```markdown
---
description: Tagesabschluss. Legt fertige Stücke ab, fragt, was ins Second Brain gehört, misst das Gedächtnis und macht ein Backup
---

# /feierabend: Den Arbeitstag abschließen

Am Ende des Arbeitstags aufrufen, dauert rund fünf Minuten. Grundregeln: Du sendest nichts, du veröffentlichst nichts, du löschst nichts. Was du nicht sicher weißt, fragst du. Gesammelt wird in genau einem AskUserQuestion-Aufruf.

## 1. Was ist heute entstanden?

1. Geh diese Unterhaltung durch: Welche Stücke sind heute entstanden (Text als Datei, Grafik, Präsentation, Checkliste), und liegt jedes davon schon in einer Mappe unter `<PFAD>/<RESSOURCEN>/claude-output/`?
2. Schau mit `ls` in `<PFAD>/<RESSOURCEN>/claude-output/` nach losen Dateien außerhalb einer Mappe. Versteckte Dateien wie `.gitkeep` zählen nicht.
3. Zähl die Dateien in `<PFAD>/<RESSOURCEN>/raw/inbox/` (ohne `index.md`).

## 2. Eine Frage, alles auf einmal

Stell genau einen AskUserQuestion-Aufruf mit höchstens zwei Fragen. Eine Frage fällt weg, wenn ihre Liste leer ist.
1. **Ablegen?** (Mehrfachauswahl) je Stück ohne Mappe eine Option mit dem vorgeschlagenen Mappennamen `JJJJ-MM-TT_art_thema`. Was ich anhake, legst du ab.
2. **Ins Second Brain?** Prüf diese Sitzung auf dauerhaftes Wissen: ein Ablauf, eine Entscheidung, eine Vorlage, eine Regel zur Sache. Arbeitsstand und Termine zählen nicht. Frage: „Davon gehört ins Second Brain: [ein Satz je Punkt]. Übertragen?“, Optionen „Ja, in den Eingangskorb (Empfohlen)“ und „Nein“.

Gibt es in beiden nichts, sag „Heute ist nichts offen geblieben“ und mach mit Schritt 4 weiter.

## 3. Umsetzen

- Ablegen: genau nach dem Abschnitt „Ausgaben und Ablage“ im Briefing.
- Second Brain: je Punkt eine Notiz `<PFAD>/<RESSOURCEN>/raw/inbox/JJJJ-MM-TT-sitzung-thema.md`, erste Zeile `Quelle: aus der Sitzung vom JJJJ-MM-TT`, darunter nur, was ausdrücklich gesagt oder gebaut wurde. Sag dazu, dass es mit dem nächsten `/verarbeiten` ins Second Brain kommt.

## 4. Gedächtnis kurz messen

Zähl Zeilen und Bytes von `<PFAD>/<RESSOURCEN>/memory/MEMORY.md`. Gibt es die Datei noch nicht, zählt sie als leer. Liegt einer der Werte über 140 Zeilen oder 17.900 Bytes, empfiehl `/pruefung`. Sonst kein Wort dazu.

## 5. Backup

BACKUP-AUFRUF

Das Skript legt ein datiertes Zip von Arbeitsordner und Claude-Einstellungen im Ordner `Claude-Backup` im Benutzerordner ab und eine Kopie in der Cloud (BACKUP-WOLKE). Es behält jeweils die letzten 7. Videodateien und die Anmeldedaten von Claude bleiben draußen. Gibt es heute schon ein Backup, wird es ersetzt. Meldet das Skript einen Fehler, nenn ihn wörtlich und mach mit Schritt 6 weiter. Fehlt das Skript, sag das in einem Satz.

## 6. Schlussmeldung

Höchstens fünf Zeilen:
- heute entstanden und abgelegt (mit vollem Pfad der Mappen)
- im Eingangskorb abgelegt, und wie viele Dateien dort jetzt auf `/verarbeiten` warten
- Gedächtnis, nur wenn es über der Grenze liegt
- Backup: die Zeile, die das Skript ausgibt
```

**In `feierabend.md` ersetzt du zwei Stellen, je nach SYSTEM aus Etappe 0:**

| | Mac | Windows |
|---|---|---|
| `BACKUP-AUFRUF` | `bash "<HOME>/.claude/scripts/ki-system-backup.sh" "<PFAD>"` | `powershell.exe -NoProfile -ExecutionPolicy Bypass -File "<HOME>/.claude/scripts/ki-system-backup.ps1" "<PFAD>"` |
| `BACKUP-WOLKE` | `iCloud Drive, Ordner Claude-Backup` | `OneDrive, Ordner Claude-Backup` |

Der Aufruf steht in der fertigen Datei in einfachen Backticks, mit eingesetztem HOME und PFAD.

**Das Backup-Skript** (kein Befehl, ein Skript): Schreib nur die Fassung für SYSTEM, nach `<HOME>/.claude/scripts/`. Existiert sie schon, gilt dasselbe wie bei den Befehlen. Das Skript übernimmst du Zeichen für Zeichen, seine Klammern, `$`-Variablen und Umleitungen sind Programmcode und keine Platzhalter.

**Mac:** `ki-system-backup.sh`

```bash
#!/bin/bash
# Backup: Arbeitsordner und Claude-Einstellungen als datiertes Zip.
# Eine Kopie bleibt auf dem Mac (~/Claude-Backup), eine liegt in iCloud Drive (Claude-Backup).
# Von beiden bleiben die letzten 7 Stände.
#   bash ki-system-backup.sh "/Users/name/Desktop/KI-System"
set -e
ARBEIT="$1"
if [ -z "$ARBEIT" ] || [ ! -d "$ARBEIT" ]; then echo "Aufruf: bash ki-system-backup.sh /pfad/zum/arbeitsordner"; exit 1; fi
LOKAL="${BACKUP_LOKAL:-$HOME/Claude-Backup}"
ICLOUD_BASIS="${BACKUP_ICLOUD:-$HOME/Library/Mobile Documents/com~apple~CloudDocs}"
BEHALTEN=7
NAME="claude-backup_$(date +%Y-%m-%d).zip"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$LOKAL"
cd "$(dirname "$ARBEIT")"
zip -rqy "$TMP/$NAME" "$(basename "$ARBEIT")" \
  -x "*.DS_Store" "*.mp4" "*.MP4" "*.mov" "*.MOV" "*.mkv" "*/.obsidian/workspace*"
cd "$HOME"
[ -d .claude ] && zip -rqy "$TMP/$NAME" .claude -x ".claude/projects/*" ".claude/shell-snapshots/*" ".claude/statsig/*" ".claude/todos/*" ".claude/cache/*" ".claude/plugins/*" ".claude/debug/*" ".claude/.credentials.json"
cp "$TMP/$NAME" "$LOKAL/$NAME"

aufraeumen() { ls -1 "$1"/claude-backup_*.zip 2>/dev/null | sort -r | tail -n +$((BEHALTEN+1)) | while read -r alt; do mv "$alt" "$HOME/.Trash/" 2>/dev/null || true; done; }
aufraeumen "$LOKAL"

if [ -d "$ICLOUD_BASIS" ]; then
  mkdir -p "$ICLOUD_BASIS/Claude-Backup"
  cp "$TMP/$NAME" "$ICLOUD_BASIS/Claude-Backup/$NAME"
  aufraeumen "$ICLOUD_BASIS/Claude-Backup"
  ICLOUD="iCloud Drive/Claude-Backup"
else
  ICLOUD="iCloud Drive nicht gefunden, nur lokal gesichert"
fi
GROESSE=$(du -h "$LOKAL/$NAME" | cut -f1)
echo "Backup $NAME ($GROESSE): ~/Claude-Backup und $ICLOUD"
```

**Windows:** `ki-system-backup.ps1`. Es nutzt das `tar`, das in Windows 10 und 11 eingebaut ist, und braucht keine Installation. Der Text ist absichtlich ohne Umlaute, weil die Windows-PowerShell Skripte ohne Kennung als ANSI liest.

```powershell
# Backup: Arbeitsordner und Claude-Einstellungen als datiertes Zip (Windows).
# Eine Kopie bleibt unter Benutzerordner\Claude-Backup, eine liegt in OneDrive\Claude-Backup, falls OneDrive eingerichtet ist.
# Von beiden bleiben die letzten 7 Staende.
#   powershell.exe -NoProfile -ExecutionPolicy Bypass -File ki-system-backup.ps1 "C:/Users/name/KI-System"
param([string]$Arbeit)
$ErrorActionPreference = 'Stop'
if (-not $Arbeit -or -not (Test-Path -LiteralPath $Arbeit -PathType Container)) { 'Aufruf: powershell.exe -NoProfile -ExecutionPolicy Bypass -File ki-system-backup.ps1 C:/pfad/zum/arbeitsordner'; exit 1 }
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

$Wolke = 'OneDrive nicht gefunden, nur lokal gesichert'
$OneDrive = $env:OneDriveConsumer
if (-not $OneDrive) { $OneDrive = $env:OneDrive }
if ($OneDrive -and (Test-Path -LiteralPath $OneDrive)) {
  $Ziel = Join-Path $OneDrive 'Claude-Backup'
  New-Item -ItemType Directory -Force -Path $Ziel | Out-Null
  Copy-Item -LiteralPath $Zip -Destination (Join-Path $Ziel $Name) -Force
  Alte-Weg $Ziel
  $Wolke = 'OneDrive/Claude-Backup'
}
Remove-Item -Recurse -Force $Tmp
$Groesse = '{0:N1} MB' -f ((Get-Item -LiteralPath (Join-Path $Lokal $Name)).Length / 1MB)
$Hinweis = ''
if ($Code -ne 0) { $Hinweis = ', einzelne Dateien nicht gesichert' }
"Backup $Name ($Groesse$Hinweis): ~/Claude-Backup und $Wolke"
```

**Danach einmal von Hand ausführen**, mit dem Aufruf aus der Tabelle oben. Kommt die Zeile „Backup claude-backup_…“, stimmt es. Auf dem Mac heißt „iCloud Drive nicht gefunden“: In den Systemeinstellungen unter seinem Namen, dann iCloud, iCloud Drive einschalten. Auf Windows heißt „OneDrive nicht gefunden“: OneDrive ist nicht angemeldet. Dann sichert das Skript bis dahin nur in den Benutzerordner, und er meldet sich bei Gelegenheit in OneDrive an. Kommt „einzelne Dateien nicht gesichert“, war eine Datei gerade geöffnet. Das Zip ist trotzdem da.

**Lag in `~/.claude/commands/` schon ein eigener Abschlussbefehl** (etwa `/log`) und soll er laut Etappe 3 bleiben, häng seiner Datei mit dem Edit-Werkzeug ganz unten diesen Absatz an und lass alles andere stehen:

```markdown

## Zum Schluss: Gehört etwas ins Second Brain?

Prüf diese Sitzung auf dauerhaftes Wissen: ein Ablauf, eine Entscheidung, eine Vorlage, eine Regel zur Sache. Arbeitsstand, Termine und Aufgaben zählen nicht. Gibt es so etwas, stell genau eine Frage mit AskUserQuestion: „Davon gehört ins Second Brain: [ein Satz je Punkt]. Übertragen?“, Optionen „Ja, in den Eingangskorb (Empfohlen)“ und „Nein“. Bei Ja legst du je Punkt eine Notiz `<PFAD>/<RESSOURCEN>/raw/inbox/JJJJ-MM-TT-sitzung-thema.md` an, erste Zeile `Quelle: aus der Sitzung vom JJJJ-MM-TT`, darunter nur, was ausdrücklich gesagt oder gebaut wurde. Sag dazu, dass es mit dem nächsten `/verarbeiten` ins Second Brain kommt.
```

**Wenn die vier Befehlsdateien geschrieben sind, prüfe sie noch einmal, zusammen mit dem Briefing aus Etappe 4 und einem ergänzten Abschlussbefehl,** auf `<PFAD>`, `<RESSOURCEN>`, `<ARCHIV>`, `<PROJEKTE>`, `<BEREICHE>`, `<HOME>`, `BACKUP-AUFRUF`, `BACKUP-WOLKE`, auf jede andere spitze Klammer, auf `/.../` innerhalb von Pfaden und auf eckige Klammern. Jeder Treffer ist ein Platzhalter, den du sofort durch den echten Wert ersetzt. Gewollt und kein Platzhalter sind: Verweise in doppelten eckigen Klammern wie `[[…/wissen/ablage/Seitenname]]`, `<Verweis>` in den `ls`-Prüfbefehlen, `JJJJ-MM-TT`, `DATEINAME` (auch im Beispiel `[Angebotsablauf](DATEINAME)`), `JJJJ-MM-TT_art_thema` und `[ein Satz je Punkt]` in `feierabend.md` und im Zusatz für den Abschlussbefehl. Schreib dabei jeden Pfad voll aus, keine Abkürzungen oder Variablen, auch wenn er lang ist. **Prüfe dabei nur Zeilen, die du selbst geschrieben hast.** In wörtlich übernommenen Regeln stehen Auslassungspunkte manchmal absichtlich.

**Danach die Probe aufs Exempel:** Nimm jeden Ordnerpfad, der in diesen vier Dateien vorkommt, und prüf mit `ls`, ob er wirklich existiert. Ein Pfad, der ins Leere zeigt, ist ein Fehler, den du sofort korrigierst und meldest. Das ist die einzige Kontrolle, die einen falsch geschriebenen Ordnernamen noch vor dem Neustart findet. Ausgenommen sind Ordner, die ein Befehl erst bei seinem eigenen Lauf anlegt (etwa Sicherung und Archiv in `/pruefung`, `Claude-Backup` im Benutzerordner und in der Cloud aus dem Backup-Skript), und Beispielpfade wie `wissen/ablage/`. Die prüfst du nicht und legst sie auch nicht vorab an. Prüf dabei auch jede Ablage aus Etappe 3 einzeln mit `ls`, denn im Briefing stehen die Ablagen nur als Namen, und genau dort entstehen Tippfehler.

---

## Etappe 6: Abschluss

Wenn alles steht:

1. Zeig eine kurze Übersicht: welche Ordner und Dateien jetzt existieren, was davon neu ist, und welche Dateien außerhalb des Arbeitsordners liegen (im Normalfall `~/.claude/CLAUDE.md`, die vier Befehle in `~/.claude/commands/`, das Backup-Skript in `~/.claude/scripts/` und `~/.claude/settings.json` mit dem Ort des Gedächtnisses). Der Gedächtnis-Ordner `memory/` und der Ausgabe-Ordner `claude-output/` gehören mit in die Liste. Den Modus lässt er noch so, wie er ist, bis Schritt 7. **Prüf vorher mit `ls`**, dass `<PFAD>/<RESSOURCEN>/wissen/index.md`, `<PFAD>/<RESSOURCEN>/wissen/start.md` und in jeder Ablage eine `index.md` liegen, und nenn sie in der Übersicht. Fehlt eine, legst du sie nach den Regeln aus Etappe 3 an und meldest es. Sag dazu in einem Satz, dass es Verzeichnisse nur im Second Brain gibt und Eingangskorb, Projekte, Bereiche und Archiv bewusst keins haben.
2. Wenn eine alte Briefing-Datei im Spiel war: sag ausdrücklich, wo sie weiterhin liegt und was daraus übernommen wurde. Sonst entfällt dieser Punkt.
3. Erklär in drei Sätzen, wofür der Eingangskorb da ist: alles Neue landet erst dort, sortiert wird später, das hält das Second Brain sauber.
4. Erklär den einfachen Alltag: Fragen stellt er in normaler Sprache. Sachwissen kommt nur auf seinen ausdrücklichen Wunsch mit „Nimm das in mein Second Brain auf" hinein. `/verarbeiten` räumt den Eingangskorb auf. `/feierabend` schließt jeden Arbeitstag ab: Er legt fertige Stücke ab, fragt einmal nach dem Second Brain und macht ein Backup. `/pruefung` kontrolliert einmal im Monat Second Brain und Gedächtnis zusammen und räumt nach seinem Okay auf. Das eingebaute Auto-Memory sammelt im Hintergrund und schreibt in den Ordner `memory/` neben dem Second Brain. Das Gedächtnis sammelt, das Second Brain behält: `/verarbeiten` überträgt das Sachwissen daraus ins Second Brain, im Gedächtnis bleibt nur die Zusammenarbeit. Dort kann er jederzeit nachlesen, was Claude sich gemerkt hat, und Falsches einfach löschen. Ist der Umzug in Etappe 4 gescheitert, sagst du stattdessen, dass es noch unter `~/.claude/projects/` liegt und der Umzug offen ist.
5. Sag den Satz, auf den es ankommt: Dieses Wissen liegt jetzt auf seiner eigenen Festplatte. Es hängt an keinem Konto und an keinem Anbieter. Wenn er das Konto wechselt, wandert der Ordner einfach mit.
6. **Kopier vorher noch einmal das Gedächtnis.** Was du dir seit Etappe 4 gemerkt hast, liegt noch am alten Ort. Such dafür jetzt noch einmal mit `ls -d ~/.claude/projects/*/memory/` nach dem passenden Ordner (Regel aus Etappe 4), denn diese Sitzung kann ihn erst nach Etappe 4 angelegt haben. Kopier alles daraus in `<PFAD>/<RESSOURCEN>/memory/`. Gleichnamige Dateien überschreibst du dabei, vor allem den Index `MEMORY.md`: Der neue Ordner enthält bis zum Neustart nur deine Kopien aus Etappe 4, die Fassung am alten Ort ist immer die aktuellere. Einzige Ausnahme: Hat in Etappe 4 ein schon vorhandenes `autoMemoryDirectory` umziehen dürfen, überschreibst du nichts und meldest gleichnamige Dateien. Ist der Umzug in Etappe 4 gescheitert, entfällt dieser Schritt.

   **Schreib die Übergabe, bevor du um den Neustart bittest.** Nach dem Neustart liest ein frisches Claude, das diese Datei nie gesehen hat und nicht weiß, was heute gelaufen ist. Ohne Übergabe bleibt alles liegen, was nach dem Neustart noch kommt, oder das neue Claude beginnt die Datei von vorn und legt alles doppelt an. Gib ihm deshalb jetzt diesen Text zum Kopieren, mit den echten Werten eingesetzt und jedem Pfad voll ausgeschrieben, nie mit „…“ gekürzt, und sag dazu, dass er ihn in der neuen Unterhaltung als erste Nachricht einfügt:

   > Der Neustart ist schon passiert, das Setup ist heute gelaufen. Wiederhol nichts davon und leg nichts neu an. Lies die Datei `<voller Pfad zu dieser Setup-Datei>` und mach in Etappe 6 bei den Kontrollen weiter. SYSTEM ist `<Mac oder Windows>`, PFAD ist `<PFAD>`, RESSOURCEN ist `<RESSOURCEN>`, ARCHIV ist `<ARCHIV>`, HOME ist `<HOME>`, die Ablagen heißen <ABLAGEN>. Gelaufen sind die Etappen 0 bis 5 samt 0b. Das Briefing liegt unter `<Ort des Briefings>`, die Befehle unter `<Ort der Befehle>`, das Backup-Skript unter `<Ort des Skripts>`. Der Eingangskorb ist `<Pfad des Eingangskorbs>`, Verarbeitetes wandert nach `<Ordner für Verarbeitetes>`. Das Gedächtnis liegt unter [`<PFAD>/<RESSOURCEN>/memory/`, oder bei gescheitertem Umzug: `~/.claude/projects/`, Umzug offen].

   **Kennst du den Pfad zu dieser Datei selbst nicht**, weil er dir den Text nur eingefügt hat, frag ihn danach. Rate nicht.

7. **Jetzt der Neustart, und teste die Befehle dann wirklich.** Die vier Befehle sind gerade erst entstanden und werden erst danach geladen. Ohne diesen Schritt merkt niemand, dass sie nicht greifen.

   **Erst jetzt darf er zurück auf Auto**, falls er in Etappe 4 oder 5 auf Manual gestellt hat.

   **Neustart heißt hier:** im Claude-Fenster eine neue Unterhaltung starten, im selben Arbeitsordner. Dann fügt er die Übergabe ein. Bitte ihn danach, diese Kontrollen nacheinander selbst einzutippen, und warte jeweils auf die Eingabe:
   - „Was weißt du über mich und meine Arbeit, und wo liegt mein Second Brain?" Kommt eine Antwort aus dem Briefing samt Pfad zum Second Brain, ist das Briefing geladen.
   - „Was steht in meinem Second Brain über Wohnungsübergabe, und aus welcher Quelle stammt das?" Kommt eine belegte Antwort aus dem Wissensordner, funktioniert der natürliche Abruf. Liegt zu dem Thema noch nichts vor, muss Claude genau das sagen, statt zu raten. Auch das gilt als bestanden.
   - `/verarbeiten` eintippen. Claude sieht zuerst ins Gedächtnis, dann in den Eingangskorb. Ist beides ohne Neues, muss Claude „Nichts zu verarbeiten“ melden und stoppen. Liegt etwas vor, nennt Claude zuerst die Dateien. Damit ist der Befehl geladen. An dieser Stelle genügt ein Klick auf das Stopp-Symbol, verarbeitet wird erst in Schritt 8. Erscheint „unknown command", schließt er das Programm (VS Code oder die Claude-App) einmal ganz, öffnet es wieder, startet eine neue Unterhaltung und fügt die Übergabe noch einmal ein. Erscheint die Meldung dann immer noch, liegen die Befehle am falschen Ort. Prüf mit `ls`, ob sie am Ort aus der Übergabe liegen, und schau im Arbeitsordner nach einem Ordner namens `~` oder nach `.claude/commands/`. Findest du sie dort, verschiebst du sie an den Ort aus der Übergabe.
   - „In welchem Ordner liegt dein Auto-Memory? Nenn den vollen Pfad.“ Antwortet Claude mit `<PFAD>/<RESSOURCEN>/memory`, ist die Einstellung geladen. Backslashes statt Schrägstrichen oder ein Schrägstrich am Ende zählen als gleich. Zur Gegenprobe kann er `/memory` eintippen und dort den Ordner des Auto-Memory öffnen lassen, Finder oder Explorer zeigt dann, welcher es ist. Nennt Claude einen Pfad unter `~/.claude/projects/`, ist die Einstellung nicht geladen: Prüf `~/.claude/settings.json`, wie unter „JSON prüfen“ in Etappe 0 beschrieben, dann schließt er das Programm (VS Code oder die Claude-App) einmal ganz, öffnet es wieder und fügt die Übergabe noch einmal ein. Ist der Umzug in Etappe 4 gescheitert, entfällt diese Kontrolle.
   - `/feierabend` eintippen. Claude fragt höchstens einmal nach Ablage und Second Brain oder meldet „Heute ist nichts offen geblieben“. Am Ende steht die Zeile „Backup claude-backup_…“. Steht dort „Blocked by classifier“, stellt er den Modus kurz auf Manual und du wiederholst den Aufruf. Kommt stattdessen eine Fehlermeldung des Skripts, prüf mit `ls`, ob das Backup-Skript aus der Übergabe am vollen Pfad liegt.
   - `/interview` eintippen. Claude liest das Briefing und stellt nur Fragen, die noch offen sind, oder meldet, dass nichts Offenes mehr da ist. Danach genügt ein Klick auf das Stopp-Symbol. Erscheint „unknown command“, gilt derselbe Weg wie oben bei `/verarbeiten`.
   - `/pruefung` wird hier nicht ganz durchgespielt, weil es auf einem frischen Second Brain nichts zu prüfen gibt. Es genügt, `/pruefung` einzutippen und zu sehen, dass Claude mit dem Messen beginnt. Dann reicht ein Klick auf das Stopp-Symbol. Erscheint „unknown command“, gilt derselbe Weg wie oben bei `/verarbeiten`.
8. Schlag als ersten Auftrag in der neuen Unterhaltung vor: eine echte Sache aus dieser Woche in den Eingangskorb schreiben und danach `/verarbeiten` laufen lassen. Liegt dort schon etwas, reicht `/verarbeiten`.
9. **Die monatliche Prüfung einplanen.** Viktor will die Prüfung als Automation (29.10.2026): Du fragst nicht, sondern richtest sie direkt ein. Du richtest eine lokale geplante Aufgabe der Desktop-App ein, nie eine Cloud-Aufgabe (die läuft nicht auf seinem Rechner und sieht weder Befehle noch Dateien): Name `monatspruefung`, Anweisung `/pruefung`, nur auf diesem Rechner, Ordner `<PFAD>`. Beim Anlegen gibt es nur Hourly, Daily, Weekdays und Weekly. Leg sie mit Weekly an und stell danach über Bearbeiten auf Custom mit `0 10 1 * *`. Hast du dafür kein Werkzeug, führ ihn selbst hindurch: In der Claude-App links auf **Scheduled** (in älteren Fassungen **Routines**), dann **New task**, **Local** wählen, Name, Anweisung und Ordner wie oben, Weekly, speichern, danach die Aufgabe öffnen, **Edit** und bei der Wiederholung **Custom** mit `0 10 1 * *`. Arbeitet er nur in VS Code ohne Claude-App, entfällt die Einplanung, und du sagst ihm, dass er `/pruefung` am Monatsanfang selbst eintippt. Sag dazu: Die Aufgabe läuft nur, wenn die Claude-App offen und der Rechner wach ist. Hat er den Termin verpasst, holt die App ihn beim nächsten Start nach. Die Prüfung stellt dann ihre eine Frage und wartet, bis er antwortet: auf der Seite „Scheduled“ unter der Aufgabe im Verlauf.
10. Zum Schluss sagst du ihm in einem Satz: Diese Setup-Datei kann jetzt ins Archiv `<PFAD>/<ARCHIV>/`. Verschieb sie erst nach seinem Okay.
