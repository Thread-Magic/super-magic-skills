---
name: Phishingtriage (Dutch)
description: Phishingtriage van een verdachte e-mail: beoordelen zonder payload aan te raken, verspreiding controleren, isoleren bij kwaadaardigheid, oordeel geven.
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Phishingtriage (Dutch)

**Wanneer gebruiken:** een gebruiker stuurde iets verdachts door ("is dit phishing?"), een phishingmeldingsticket landt op het securityboard, of een technicus wil een second opinion voordat een bericht wordt vrijgegeven of verwijderd.

**Uitvoeren:** op één gemeld bericht.

## Prompt

```
Breng een gemeld verdacht bericht naar een gedocumenteerd oordeel.

1. Leg de indicatoren uit het ticket alleen als tekst vast: afzenderadres en weergavenaam, reply-to, onderwerp, verzendtijd, elk linkdoel exact zoals het er staat, en bijlagenamen en -types. Open, klik, download of render nooit een link of bijlage uit het bericht — ook niet "even kijken wat het is".
2. Simulatietak: vergelijk afzender- en linkdomeinen met de in de kennisbank gedocumenteerde simulatiedomeinen van de klant. Alleen bij een exacte match met een gedocumenteerd simulatordomein → classificeer als simulatie, sluit intern af met een platte-tekstnotitie die het domein noemt, en antwoord NIET aan de klant (dat vertekent hun simulatieprogramma). Stop hier. Een gedeeltelijke match is geen match: sluit echte phishing nooit als simulatie af, en start nooit een echt incident voor een simulatie.
3. Beoordeel de indicatoren: lookalike- of neefdomein, urgentie- en betalingslokkers, credential-harvestlink (weergavetekst wijkt af van het echte doel), onverwachte bijlagetypes, kaping van een eerdere conversatie. Bij volledige headers: geef de diepe analyse aan email-header-analysis.
4. Verspreidingscontrole: zoek dezelfde afzender of hetzelfde onderwerp in de boards en recente tickets van de klant. Stel vast wie het nog meer ontving en — cruciaal — of iemand klikte, antwoordde, inloggegevens invulde of een bijlage opende. Beweer nooit "niemand anders heeft dit ontvangen" op basis van een afgekapte zoekopdracht; schrijf "geen andere meldingen in de laatste N doorzochte tickets" (basisskill Sweep Honesty).
5. Heeft iemand geïnteracteerd met een bericht dat jij kwaadaardig acht, escaleer dan onmiddellijk en start compromised-account-containment voor de getroffen gebruikers. Indammen gaat vóór het verslag.
6. Lever het oordeel. Kwaadaardig → quarantaine of verwijdering uit alle ontvangende mailboxen, blokkade van afzender en domein op de gateway, en een credentialreset voor wie klikte. Verdacht maar onbevestigd → zeg dat precies zo, met wat het zou bevestigen. Legitiem → leg uit welke signalen het vrijpleiten.
7. Antwoord de melder als open concept, met dank voor de melding; leg oordeel, bewijs en redenering vast als interne notitie in platte tekst, zonder markdown of emoji's (basisskill PSA Note Discipline), classificeer het ticket en zet de status. Documenteer de beslissing, niet alleen de actie.

Nederlandse conventie: defensief vocabulaire — "gemeld bericht", "vermoedelijke phishingpoging"; nooit "hack" of "datalek" vóór formele bevestiging. "Datalek" heeft onder de AVG een juridische lading en meldplicht: gebruik het pas als dat is vastgesteld. Antwoord aan de melder in de u-vorm, met expliciete dank. Tijdstempels in DD-MM-JJJJ, 24-uursnotatie met tijdzone ("15-07-2026 09:12 CEST"). Technische indicatoren (headers, URL's, bestandsnamen) letterlijk in het Engels. Bij twijfel: indammen.
```
