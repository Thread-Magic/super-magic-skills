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
Führe diese gemeldete verdächtige E-Mail zu einem dokumentierten Urteil.

1. Erfasse die Indikatoren aus dem Ticket, ohne mit ihnen zu interagieren: Absenderadresse und Anzeigename, Reply-To, Betreff, Sendezeit, jedes Linkziel exakt so, wie geschrieben, sowie Namen und Typen der Anhänge. Niemals Links oder Anhänge öffnen und niemals eine URL aus der Nachricht abrufen, um „zu sehen, was es ist".
2. Simulationszweig: Absender- und Link-Domänen mit den dokumentierten Domänen der Phishing-Simulationsplattform des Kunden vergleichen (in der Wissensdatenbank nach dem Datensatz des Simulationsanbieters nachschlagen). Passt es zu einem bekannten Simulator → als Simulation klassifizieren, intern mit einer Klartextnotiz schließen, die die passende Domäne nennt, und dem Kunden NICHT antworten (eine Antwort verzerrt die Kennzahlen seines Simulationsprogramms). Hier stoppen.
3. Indikatoren bewerten: Doppelgänger- oder Cousin-Domäne, Dringlichkeits- und Zahlungsköder, Zugangsdaten-Abgreif-Link (Abweichung zwischen Anzeigetext und tatsächlichem Ziel), unerwartete Anhangstypen, Kaperung eines echten früheren Gesprächsverlaufs. Wurden vollständige Header eingefügt, die Feinanalyse an den Skill email-header-analysis übergeben und dessen Urteil einarbeiten.
4. Streuradius-Prüfung: nach demselben Absender oder Betreff über die Boards des Kunden und jüngere Tickets suchen. Feststellen, wer die Nachricht sonst noch erhalten hat und — entscheidend — ob jemand geklickt, geantwortet, Zugangsdaten eingegeben oder einen Anhang geöffnet hat (die Empfänger anhand der Kontakte identifizieren).
5. Hat jemand mit einer von dir als bösartig eingestuften Nachricht interagiert → sofort eskalieren und den Skill compromised-account-containment für die betroffenen Nutzer starten. Eindämmung geht dem Fertigstellen des Berichts vor: schnell eindämmen, danach untersuchen.
6. Das Urteil liefern: Bösartig → Quarantäne/Entfernung aus allen Empfängerpostfächern, Sperrung von Absender/Domäne am Gateway und Zugangsdaten-Reset für jeden, der geklickt hat, empfehlen. Verdächtig, aber unbestätigt → genau das sagen, mitsamt dem, was es bestätigen würde. Legitim → die Signale erklären, die es entlasten.
7. Dem Melder als offenen Entwurf antworten, im Vokabular des defensiven Schreibens (eine verdächtige E-Mail ist eine „gemeldete Nachricht", kein „Sicherheitsvorfall"). Urteil, Belege und Entscheidungsbegründung als interne Notiz festhalten; das Ticket klassifizieren und den Status setzen. Dem Melder danken.

Deutsche Konvention: defensives Vokabular — „gemeldete Nachricht", „mutmaßlicher Phishing-Versuch", „ungewöhnliche Aktivität"; nie „Hack" oder „Datenleck" vor formaler Bestätigung. Die Antwort an den Melder bleibt beim Sie und schließt mit ausdrücklichem Dank: „Vielen Dank, dass Sie diese Nachricht gemeldet haben — genau so ist es richtig." Zeitstempel in Zeitleisten als TT.MM.JJJJ und 24-Stunden-Format, mit Zeitzone („15.07.2026 09:12 Uhr CET"). Technische Indikatoren (Header, URLs, Dateinamen, Fehlerzeichenketten) verbatim auf Englisch übernehmen — niemals übersetzen, sie dienen als Belege und Suchschlüssel.

Leitplanken: Niemals Links oder Anhänge der gemeldeten Nachricht öffnen, anklicken, abrufen oder rendern — Indikatoren ausschließlich als Text erfassen. Den Simulationsstatus in beide Richtungen prüfen (niemals einen echten Vorfall für eine Simulation auslösen; niemals ein echtes Phishing bei teilweiser Domänenübereinstimmung als Simulation schließen — eine exakte, dokumentierte Simulator-Domäne verlangen). Niemals dem Kunden bei einer bestätigten Simulation antworten. Geklickt oder geantwortet heißt sofort eskalieren. Niemals „niemand sonst hat das erhalten" aus einer gekappten Suche behaupten; „keine weiteren Meldungen in den letzten N durchsuchten Tickets gefunden" schreiben. Die Entscheidung dokumentieren, nicht nur die Handlung. Im Zweifel eindämmen.
```
