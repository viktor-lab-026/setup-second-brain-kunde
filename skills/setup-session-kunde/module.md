# Modul-Katalog: welcher Kundenwunsch wohin gehört

Jeder Wunsch und jede Frage aus dem Kundenprofil bekommt **genau ein Ziel**. Die Setup-Datei bekommt nur die Bausteine A bis D. Alles andere landet im Handout, im Use-Case-Plan oder im Folgetermin.

## Zuordnung

| Signal im Profil | Ziel | Umsetzung | Zeit im Termin |
|---|---|---|---|
| Eigene Marke mit CI, Firmenkunde mit Stilvorgaben | Setup: **Baustein A** | Stilguide in der Vorlage vorbefüllen (Farben, Ton, Zielgruppen). Nicht bei fremder Dachmarke (Franchise), weil die Marke dem Kunden nicht gehört | +20 Min, ohne Vorbefüllung +30 |
| Claude soll seinen Stil kennen, ohne Firmen-CI | Kern + Use-Case-Plan + Spickzettel | Etappe 2 übernimmt vorhandene Stilregeln. Im Use-Case-Plan ein Prompt, der aus zwei bis drei eigenen Texten einen Stilguide ableitet und im Second Brain ablegt. Spickzettel 05 (Vorlage aus alten Texten) darauf zuschneiden. Baustein A nur bei Firmen-CI | 10 Min im Use Case |
| „Will sehen, was im Wissen steckt“, Obsidian genannt | Handout: Abschnitt **B** (Standard) | Obsidian-Abschnitt im Handout behalten. Baustein B in der Setup-Datei nur auf ausdrücklichen Wunsch und bei freier Zeit | 0 Min, im Setup +20 bis 25 |
| Will das Gedächtnis kontrollieren, automatische Verknüpfung, geht sicher mit dem Rechner um | Setup: **Baustein C** | C1 und C2. `{{HANDOUT-URL}}` setzen, `vault-autolink.txt` hochladen. Handout-Blöcke `OPTIONAL:C` behalten | +25 bis 30 Min, Windows ohne Python nur C1: 8 bis 10 |
| Mehrere Personen einer Firma arbeiten mit demselben Wissen | Setup: **Baustein D** | Bei Firmenkunden mit A oder C meist zweiter Termin | +18 Min |
| Will Werkzeuge verbinden oder fragt danach (Notion, Canva, Google, Microsoft 365, Outlook). Die reine Nutzung eines Werkzeugs zählt nicht, sie steht nur im Wofür-Abschnitt | Handout-Zusatz „Deine Werkzeuge verbinden“ + Use-Case-Plan | Klickpfad über claude.ai Connectors, die dann auch in Claude Code erscheinen (`/mcp`). Einschränkungen nach Konto und Plan recherchieren (Microsoft 365: Geschäftskonto, Admin-Zustimmung). Live verbinden nur, wenn der Use Case es braucht. In der Vorbereitung fragen, welche Connectoren schon stehen | 5 Min je Werkzeug im Use Case |
| Programm auf dem Rechner ohne claude.ai-Connector (Apple Notizen, lokale Dateien anderer Apps) | Folgetermin | Läuft über `claude mcp add` im Terminal, braucht Handout-Schritt 5. Apple Notizen braucht zusätzlich Homebrew (Rechnerpasswort im Terminal) und Node.js. Nie im Kerntermin | +15 Min |
| Plugin im Termin (etwa `frontend-design` für Visuals) | Use-Case-Plan | Erst nach Handout-Schritt 5, also nach einem vollständigen `claude`-Start im Terminal. Scheitert es am Marktplatz: `claude plugin marketplace add anthropics/claude-plugins-official`, dann erneut. Reibungspunkt 13 in `LIESMICH.md` | +5 Min |
| Memory in claude.ai löschen oder aufräumen, Projekte in claude.ai | Use-Case-Plan, bei Bedarf Handout-Zusatz | Oberflächen trennen. Klickpfad mit Quelle. Vor einem Reset sichern lassen, was brauchbar ist | 3 bis 5 Min |
| Anderes KI-Werkzeug (ChatGPT) verbinden oder umziehen | Use-Case-Plan, Folgetermin | Ehrlich sagen, was es offiziell gibt (Stand prüfen). Export-Weg nennen, gute alte Texte später in den Eingangskorb | 0 Min |
| Skills | Handout Abschnitt 6 (steht immer drin), Folgetermin | Eigener Skill erst, wenn der Ablauf zweimal von Hand lief. Im Termin höchstens ein Ausblick auf einen von Viktors Skills | 2 Min Ausblick |
| Konkrete Aufgabe (Posts, Mails, Unterlagen, Angebote) | Use-Case-Plan + Spickzettel im Handout | Zwei bis drei Prompts für den Teil nach dem Setup. Zwei Spickzettel-Aufträge darauf zuschneiden. Bei Visuals zwei, drei Beispiele anfordern, die dem Kunden gefallen | 25 bis 30 Min |
| Bestandsnutzer mit altem Konto oder alten Anweisungen | Kern (Etappe 2) + Handout | Kontowechsel als eigenen Schritt ins Handout (Reibungspunkt 8 in `LIESMICH.md`) | +10 Min |
| Heikle Daten der Branche (Gesundheit, Mandanten, Personal, Kinder) | Setup Frage 5 + Handout Datenschutz + Use-Case-Prompts | In allen drei Stellen ausdrücklich nennen. Use Cases arbeiten nur mit eigenem Material. Bei Gesundheitsberufen zusätzlich die Regel „keine Heilaussagen“ im Interview abfragen | 0 Min |
| Der Wunsch-Use-Case selbst braucht heikle Daten (Mandantenmails, Patientenkorrespondenz, Bewerbungen) | Use-Case-Plan | Im Termin mit Vorlagen, Antwortbausteinen und erfundenen Beispielen üben. Die Rechtsfrage (Berufsgeheimnis, Auftragsverarbeitung, Kammer oder Datenschutzbeauftragter) steht im Plan als offen, ohne Rechtsauskunft. Echte Daten erst, wenn der Kunde das selbst geklärt hat | 0 Min |

## Zeitrechnung

| Teil | Minuten |
|---|---|
| Kern, Etappen 0 bis 6 | 65 bis 75 |
| Terminal-Einrichtung (Handout Schritt 5) | 5 bis 10 |
| Baustein A | +20, ohne Vorbefüllung +30 |
| Baustein B im Setup | +20 bis 25 |
| Baustein C | +25 bis 30 |
| Baustein D | +18 |
| Use Case nach dem Setup | 25 bis 30 |
| Fragenblock (Memory, Oberflächen) | 5 bis 10 |
| Alte widersprüchliche `CLAUDE.md` | +10 |

Zwei Stunden sind die Obergrenze, ab Minute 90 lässt die Aufnahme nach. Passt die Summe nicht, schlag diese Kürzungsreihenfolge vor: Obsidian ins Handout, C2, C1, D in einen zweiten Termin, zuletzt Zusatzschritte im Use Case. Reicht selbst das nicht, läuft der Kern schneller: Kundenmail in Etappe 2 einfügen lassen, weniger Ablagen, `/fragen` und `/pruefung` nur benennen. Datenschutz-Satz, Etappe 6 und den Use Case kürzt du nie. Die Terminal-Einrichtung fällt nur weg, wenn im Termin weder ein Plugin noch `claude mcp add` vorkommt.
