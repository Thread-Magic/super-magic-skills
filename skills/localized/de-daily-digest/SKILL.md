---
name: Tagesübersicht (German)
description: Tagesübersicht offener Tickets eines Technikers: was auf Antwort wartet, was dringend ist, was heute geplant ist — inklusive 3-Zeilen-Variante.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Tagesübersicht (German)

**Wann einsetzen:** Ein Techniker will die Morgenlektüre — alles, was auf dem Tisch liegt, sortiert danach, was jetzt Aufmerksamkeit braucht, in unter einer Minute überfliegbar. „Gib mir eine Übersicht über meine offenen Tickets", „Morgenübersicht", „Kurzfassung".

**Ausführen:** über alle offenen Tickets des anfragenden Mitglieds.

## Prompt

```
Erstelle die Tagesübersicht der offenen Tickets des anfragenden Mitglieds. Beschränke dich strikt auf dessen eigene Tickets — nie fremde Warteschlangen, außer es wird ausdrücklich verlangt.

1. Rufe alle offenen Tickets des Mitglieds ab (ermittle es bei Bedarf). Könnte eine Ergebnisobergrenze die Liste gekappt haben, sage das vorab („50 angezeigt — es können mehr sein"), statt sie als vollständig auszugeben.
2. Sortiere jedes Ticket in genau eine Rubrik, in dieser Reihenfolge (die erste passende gewinnt):
   - Wartet auf Ihre Antwort — der Kunde hat zuletzt geantwortet und wartet. Nach Wartedauer sortieren.
   - Dringend / gefährdet — hohe Priorität, SLA am oder nahe am Bruch, oder negative Stimmung. Nach Schwere sortieren.
   - Heute geplant — Termineintrag oder zugesagte Nachverfolgung heute, in Zeitfolge.
   - Wartet auf Dritte — Kunde, Hersteller oder Eskalation ist am Zug. Alles markieren, was 3+ Tage still ist, ohne dass diese Rubrik den Kopf verdrängt.
   - Alles Übrige — nur Anzahl und eine Charakterisierung in einer Zeile.
3. Jedes Ticket: eine einzige, handlungsfähige Zeile — Nummer, Kunde (kurz), Zustand in 5–8 Wörtern und die nächste Aktion („#1234 <Kunde> — Drucker seit 2 T offline, Kunde hat gestern geantwortet → prüfen, ob der Fix greift").
4. Eröffne mit „Hier anfangen:" dem wichtigsten Ticket und einem Satz, warum (die am längsten wartende Kundenantwort schlägt vage Dringlichkeit; ein harter SLA-Bruch schlägt alles).
5. Schließe mit der Tagesform: Summen je Rubrik und ein Satz.
6. Wird die Kurzfassung verlangt („3 Zeilen"), gib genau drei Zeilen aus, ohne Überschriften und Vorrede: (1) Hier anfangen + warum, (2) die Zähler — X warten auf Antwort / Y dringend / Z geplant, (3) das eine Thema, das heute wehtut, wenn es ignoriert wird.
7. Biete die Fortsetzung an: „Sollen Antwortentwürfe für die wartenden Tickets erstellt werden?"

Nur lesend: nichts ändern — keine Statusänderungen, Notizen, Erinnerungen —, außer das Mitglied bittet danach darum. Erfinde nie Ticketnummern, SLA-Zeiten oder Kundenantworten; ist die letzte Aktivität mehrdeutig, nimm die vorsichtigere Rubrik (Wartet auf Ihre Antwort).

Deutsche Konvention: Datum TT.MM.JJJJ („15.07.2026"), Uhrzeit im 24-Stunden-Format mit „Uhr" („10:00 Uhr"). Die Übersicht ist intern: Das Du unter Kollegen ist auf vielen deutschen Desks üblich — folge dem Hausbrauch; interne Abkürzungen („ggf.", „z. B.", „i. O.") sind hier zulässig, nie in Kundentext.

Unbeaufsichtigte Variante (Flows — über Run Skill bei einem Ticket-Ereignis, nie geplant): Deine gesamte Antwort ist das Briefing, ohne Erzählstimme oder Fragen, immer mit der Zeile Hier anfangen und den Zählern, ohne Anschlussangebot. Leere Warteschlange → exakt: „Keine offenen Tickets für Sie. Genießen Sie den freien Schreibtisch." Fehlgeschlagene Suche → eine Zeile, dass die Übersicht nicht erstellt werden konnte, nie eine erfundene.
```
