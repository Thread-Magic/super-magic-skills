---
name: Phishing-Triage (German)
description: Phishing-Triage einer verdächtigen E-Mail: Bewertung ohne Nutzlast, Streuradius prüfen, bei Böserkennung eindämmen, Melder mit Urteil antworten.
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Phishing-Triage (German)

**Wann einsetzen:** Ein Nutzer hat etwas Verdächtiges weitergeleitet („ist das Phishing?"), ein Phishing-Meldeticket landet auf dem Sicherheits-Board, oder ein Techniker will eine Zweitmeinung, bevor er eine Nachricht freigibt oder löscht.

**Ausführen:** für eine einzelne gemeldete Nachricht.

## Prompt

```
Führe eine gemeldete verdächtige E-Mail zu einem dokumentierten Urteil.

1. Erfasse die Indikatoren aus dem Ticket nur als Text: Absenderadresse und Anzeigename, Reply-To, Betreff, Sendezeit, jedes Linkziel exakt wie es dasteht, sowie Namen und Typen der Anhänge. Öffne, klicke, lade oder rendere niemals einen Link oder Anhang aus der Nachricht — auch nicht „zum Nachsehen".
2. Simulationszweig: Vergleiche Absender- und Link-Domänen mit den dokumentierten Simulationsdomänen des Kunden in der Wissensdatenbank. Nur bei exakter Übereinstimmung mit einer dokumentierten Simulator-Domäne → als Simulation klassifizieren, intern mit einer Klartextnotiz schließen, die die Domäne nennt, und dem Kunden NICHT antworten (das verzerrt dessen Kennzahlen). Hier stoppen. Teilweise Übereinstimmung zählt nicht: nie echtes Phishing als Simulation schließen, nie wegen einer Simulation einen echten Vorfall auslösen.
3. Bewerte die Indikatoren: Doppelgänger- oder Cousin-Domäne, Dringlichkeits- und Zahlungsköder, Zugangsdaten-Abgreif-Link (Anzeigetext weicht vom echten Ziel ab), unerwartete Anhangstypen, Kaperung eines früheren Gesprächs. Bei vollständigen Headern übergib die Feinanalyse an email-header-analysis.
4. Streuradius: Suche denselben Absender oder Betreff in den Boards und Tickets des Kunden. Stelle fest, wer die Nachricht sonst erhalten hat und — entscheidend — ob jemand geklickt, geantwortet, Zugangsdaten eingegeben oder einen Anhang geöffnet hat. Behaupte nie „niemand sonst hat sie erhalten" aus einer gekappten Suche; schreibe „keine weiteren Meldungen in den letzten N durchsuchten Tickets" (Basis-Skill Sweep Honesty).
5. Hat jemand mit einer als bösartig eingestuften Nachricht interagiert, eskaliere sofort und starte compromised-account-containment für die betroffenen Nutzer. Eindämmung geht dem Bericht vor.
6. Liefere das Urteil. Bösartig → Quarantäne/Entfernung aus allen Empfängerpostfächern, Sperrung von Absender und Domäne am Gateway, Zugangsdaten-Reset für alle, die geklickt haben. Verdächtig, aber unbestätigt → genau das sagen, mit dem, was es bestätigen würde. Legitim → die entlastenden Signale erklären.
7. Antworte dem Melder als offenen Entwurf und danke ihm; halte Urteil, Belege und Begründung als interne Notiz fest — reiner Text, kein Markdown, keine Emojis (Basis-Skill PSA Note Discipline) —, klassifiziere und setze den Status. Dokumentiere die Entscheidung, nicht nur die Handlung.

Deutsche Konvention: defensives Vokabular — „gemeldete Nachricht", „mutmaßlicher Phishing-Versuch"; nie „Hack" oder „Datenleck" vor formaler Bestätigung. Die Antwort an den Melder bleibt beim Sie und dankt ausdrücklich. Zeitstempel als TT.MM.JJJJ, 24-Stunden-Format mit Zeitzone („15.07.2026 09:12 Uhr CET"). Technische Indikatoren (Header, URLs, Dateinamen, Fehlermeldungen) verbatim auf Englisch übernehmen: Belege und Suchschlüssel. Im Zweifel eindämmen.
```
