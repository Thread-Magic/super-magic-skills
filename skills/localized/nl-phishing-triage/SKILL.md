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
Breng deze gemelde verdachte e-mail naar een gedocumenteerd oordeel.

1. Leg de indicatoren vast vanuit het ticket zonder ermee te interacteren: afzenderadres en weergavenaam, reply-to, onderwerp, verzendtijd, elk linkdoel exact zoals geschreven, en bijlagenamen en -types. Open nooit links of bijlagen, en haal nooit een URL uit het bericht op om "even te kijken wat het is".
2. Simulatietak: vergelijk de afzender- en linkdomeinen met de gedocumenteerde domeinen van het phishingsimulatieplatform van de klant (zoek in de kennisbank naar het simulatieleveranciersrecord). Matcht het een bekende simulator → classificeer als simulatie, sluit intern af met een platte-tekstnotitie die het gematchte domein noemt, en antwoord NIET aan de klant (een antwoord vertekent de metrics van hun simulatieprogramma). Stop hier.
3. Beoordeel de indicatoren: lookalike- of neefdomein, urgentie- en betalingslokkers, credential-harvestlink (weergavetekst wijkt af van het echte doel), onverwachte bijlagetypes, kaping van een echte eerdere conversatie. Zijn de volledige headers geplakt, geef de diepe analyse dan aan de skill email-header-analysis en verwerk diens oordeel.
4. Verspreidingscontrole: zoek op dezelfde afzender of hetzelfde onderwerp over de boards en recente tickets van de klant. Stel vast wie het bericht nog meer ontving en — cruciaal — of iemand klikte, antwoordde, inloggegevens invulde of een bijlage opende (identificeer ontvangers via de contactenlijst).
5. Heeft iemand geïnteracteerd met een bericht dat jij als kwaadaardig beoordeelt → escaleer onmiddellijk en start de skill compromised-account-containment voor de getroffen gebruiker(s). Isolatie gaat vóór het afmaken van het verslag: eerst indammen, daarna onderzoeken.
6. Lever het oordeel: Kwaadaardig → adviseer quarantaine/verwijdering uit alle ontvangende mailboxen, blokkade van afzender/domein op de gateway, en een credentialreset voor iedereen die klikte. Verdacht maar onbevestigd → zeg dat precies zo, met wat het zou bevestigen. Legitiem → leg de signalen uit die het vrijpleiten.
7. Antwoord de melder als open concept in het vocabulaire van defensief schrijven (een verdachte e-mail is een "gemeld bericht", geen "datalek"). Leg het oordeel, het bewijs en de beslisredenering vast als interne notitie; classificeer en zet de status van het ticket. Bedank de melder.

Nederlandse conventie: defensief vocabulaire — "gemeld bericht", "vermoedelijke phishingpoging", "ongebruikelijke activiteit"; nooit "hack" of "datalek" vóór formele bevestiging. Let op: "datalek" heeft onder de AVG een specifieke juridische lading en meldplicht — gebruik dat woord pas als het incident daadwerkelijk als zodanig is vastgesteld. Antwoord aan de melder in de u-vorm, afgesloten met "Bedankt voor het melden van dit bericht — dit is precies de juiste reactie." Tijdstempels in DD-MM-JJJJ en 24-uursnotatie met tijdzone ("15-07-2026 09:12 CEST"). Technische indicatoren (headers, URL's, bestandsnamen) letterlijk in het Engels overnemen — nooit vertalen.

Vangrails: open, klik, download of render nooit links of bijlagen uit het gemelde bericht — leg indicatoren uitsluitend als tekst vast. Controleer de simulatiestatus in beide richtingen (nooit een echt incident voor een simulatie; nooit echte phishing als simulatie afsluiten op een gedeeltelijke domeinmatch — eis een exact gedocumenteerd simulatordomein). Antwoord de klant nooit op een bevestigde simulatie. Geklikt of geantwoord = onmiddellijk escaleren. Beweer nooit "niemand anders heeft dit ontvangen" op basis van een begrensde zoekopdracht; rapporteer "geen andere meldingen gevonden in de laatste N doorzochte tickets". Documenteer de beslissing, niet alleen de actie. Bij twijfel: indammen.
```
