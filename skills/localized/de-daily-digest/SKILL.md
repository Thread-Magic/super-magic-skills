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
Erstelle die Tagesübersicht der offenen Tickets des anfragenden Mitglieds.

1. Rufe alle offenen Tickets des anfragenden Mitglieds ab (ermittle das Mitglied bei Bedarf zuvor). Falls eine Ergebnisobergrenze die Liste gekappt haben könnte, das vorab sagen („50 angezeigt — es können mehr sein"), statt die Übersicht als vollständig auszugeben.
2. Sortiere jedes Ticket in genau eine Rubrik, in dieser Prioritätsreihenfolge (ein Ticket landet in der ersten Rubrik, für die es sich qualifiziert):
   - Wartet auf Ihre Antwort — der Kunde hat zuletzt geantwortet und wartet. Nach Wartedauer sortieren.
   - Dringend / gefährdet — hohe Priorität, SLA am oder nahe am Bruch, oder Threads mit negativer Stimmung. Nach Schwere sortieren.
   - Heute geplant — Tickets mit Termineintrag oder zugesagter Nachverfolgung heute, in zeitlicher Reihenfolge.
   - Wartet auf Dritte — Kunde, Hersteller oder Eskalation ist am Zug. Alles markieren, was 3+ Tage still ist, ohne dass diese Rubrik den Seitenkopf verdrängt.
   - Alles Übrige — nur Anzahl und eine Charakterisierung in einer Zeile; keine Einzelzeilen pro Ticket.
3. Jede Ticketzeile ist eine einzige Zeile: Nummer, Kunde (kurz), Zustand in 5–8 Wörtern und die nächste Aktion („#1234 <Kunde> — Drucker seit 2 T offline, Kunde hat gestern geantwortet → prüfen, ob der Fix greift").
4. Eröffne mit „Hier anfangen:" dem wichtigsten Ticket und einem Satz, warum (die am längsten wartende Kundenantwort schlägt vage Dringlichkeit; ein harter SLA-Bruch schlägt alles).
5. Schließe mit der Tagesform: Summen je Rubrik und ein Satz.
6. Wird die Kurzfassung verlangt („3 Zeilen"), genau drei Zeilen ausgeben: (1) Hier anfangen + warum, (2) die Zähler — X warten auf Antwort / Y dringend / Z geplant, (3) das eine Thema, das heute wehtut, wenn es ignoriert wird. Keine Überschriften, keine Vorrede.
7. Biete die natürliche Fortsetzung an: „Sollen Antwortentwürfe für die Tickets erstellt werden, die auf Sie warten?"

Deutsche Konvention: Datum als TT.MM.JJJJ („15.07.2026"); Uhrzeit im 24-Stunden-Format mit „Uhr" („10:00 Uhr"). Die Übersicht ist ein internes Dokument: Unter Kollegen ist das Du auf vielen deutschen Desks üblich — dem Hausbrauch folgen; interne Abkürzungen („ggf.", „z. B.", „i. O.") sind in internen Zeilen zulässig, nie in Kundentext.

Leitplanken: Strikt auf die eigenen Tickets des anfragenden Mitglieds beschränken; niemals die Warteschlangen anderer Techniker einbeziehen, außer es wird ausdrücklich verlangt. Nur lesend — die Übersicht ändert nichts (keine Statusänderungen, Notizen, Erinnerungen), außer das Mitglied bittet anschließend darum. Niemals Ticketnummern, SLA-Zeiten oder Kundenantworten erfinden; ist die letzte Aktivität mehrdeutig, das Ticket in die vorsichtigere Rubrik einsortieren (Wartet auf Ihre Antwort). Jede Rubrikzeile muss handlungsfähig sein. Im Zweifel nichts tun.

Unbeaufsichtigte Variante (Flows — über Run Skill bei einem Ticket-Ereignis, niemals geplant): Deine gesamte Antwort wird wortwörtlich als Morgenbriefing ausgeliefert, keine Erzählstimme oder Fragen; immer die Zeile Hier anfangen und die Zähler, ohne Anschlussangebot. Leere Warteschlange → exakt: „Keine offenen Tickets für Sie. Genießen Sie den freien Schreibtisch." Fehlgeschlagene Suche → eine einzige Zeile, dass die Übersicht nicht erstellt werden konnte, niemals eine erfundene Übersicht.
```
