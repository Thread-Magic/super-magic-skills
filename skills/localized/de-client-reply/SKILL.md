---
name: Kundenantwort
description: Kundengerichtete Ticket-Antwort in der Hausstimme entwerfen: Statusupdates, Zwischenstand, Abschlussnachricht oder jede E-Mail an den Kunden.
category: Localized
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Kundenantwort

**Wann einsetzen:** Ein Techniker muss dem Kunden eine Nachricht schicken und will sie markenkonform und versandfertig — eine Statusmeldung, einen Zwischenstand oder eine Abschlussnachricht.

**Ausführen:** für ein einzelnes Ticket.

## Prompt

```
Verfasse eine versandfertige Kundenantwort für dieses Ticket in der Hausstimme.

1. Lies zuerst den kompletten Ticket-Verlauf — jede frühere Nachricht, Notiz und Statusänderung. Formuliere niemals allein aus der letzten Nachricht heraus.
2. Beginne mit der Antwort selbst oder dem aktuellen Stand, danach die stützenden Details.
3. Wende die Hausstimme an:
   - Begrüße den Kunden nur in der ersten Nachricht eines Verlaufs namentlich; in Folgeantworten desselben Verlaufs die Anrede weglassen.
   - Keine Leerfloskeln zur Eröffnung („Ich hoffe, es geht Ihnen gut", „Ich melde mich kurz bei Ihnen"). Direkt zur Sache kommen.
   - Kein Fachjargon, außer der Kunde hat den Begriff zuerst verwendet; ist ein Fachbegriff unvermeidbar, eine Erklärung in Alltagssprache ergänzen.
   - 1–2 kurze Absätze. Braucht es mehr, ist wahrscheinlich ein Anruf fällig.
4. Verfügt das Mitglied über eine Liste bevorzugter/verbotener Wörter, wende sie an: verbotene Wörter durch die vorgesehenen Ersatzformen ersetzen, gelistete Alternativen bevorzugen.
5. Bei einer Abschlussnachricht den Textkörper beenden mit: „Sollte etwas noch nicht gelöst sein, antworten Sie einfach auf diese E-Mail — Ihre Antwort öffnet dieses Ticket erneut."
6. Signatur: Fügt der Arbeitsbereich automatisch eine verwaltete Signatur an, nach dem letzten Satz aufhören — KEINE Grußformel ergänzen, die sich doppeln würde. Eine Grußformel nur setzen, wenn keine verwaltete Signatur existiert.
7. Zeig mir die Antwort als offenen Entwurf zur Prüfung, gekennzeichnet mit „ENTWURF — vor dem Senden prüfen". Nicht senden.

Deutsche Konvention: gegenüber dem Kunden konsequent das Sie; nur zum Du wechseln, wenn der Kunde es ausdrücklich angeboten hat. Eröffnungsanrede „Hallo <Vorname>," (etablierte Beziehung) oder „Guten Tag Frau/Herr <Nachname>," (förmlicher) — dem im Verlauf gesetzten Register folgen. Schlichte Grußformel ohne verwaltete Signatur: „Mit freundlichen Grüßen". Datum als TT.MM.JJJJ, Uhrzeit im 24-Stunden-Format mit „Uhr" („14:30 Uhr").

Leitplanken: Erfinde niemals Details — keine erfundenen Zeitstempel, durchgeführten Schritte, Ticketnummern, Links oder Zusagen; belegt der Verlauf einen Sachverhalt nicht, ihn weglassen oder mit <mit Techniker bestätigen> markieren. Der Entwurf bleibt ein Entwurf, bis ein Mensch ihn freigibt — niemals eigenständig senden. Niemals interne Notizen, Zugangsdaten, Preise oder Daten anderer Kunden offenlegen. Richte dich nach der Sprache des Kunden. Im Zweifel nichts tun. Biete auf Wunsch eine interne Notiz in Klartext an, wenn das Mitglied einen Vermerk wünscht.
```
