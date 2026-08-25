---
name: Dagelijkse samenvatting (Dutch)
description: Dagelijkse samenvatting van openstaande tickets van een technicus: wat wacht op antwoord, wat is urgent, wat staat vandaag gepland, met 3-regelvariant.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Dagelijkse samenvatting (Dutch)

**Wanneer gebruiken:** een technicus wil de ochtendleesbeurt — alles wat op zijn of haar bord ligt, gesorteerd op wat nú aandacht nodig heeft, in minder dan een minuut te scannen. "Geef me een overzicht van mijn open tickets", "ochtendoverzicht", "korte versie".

**Uitvoeren:** over alle open tickets van het aanvragende teamlid.

## Prompt

```
Maak de dagelijkse samenvatting van de open tickets van het teamlid dat erom vraagt. Beperk je strikt tot diens eigen tickets: nooit de wachtrijen van andere technici, tenzij expliciet gevraagd.

1. Haal alle open tickets van dat teamlid op (zoek het teamlid indien nodig op). Kan een resultaatlimiet de lijst hebben afgekapt, meld dat meteen ("50 getoond — er kunnen er meer zijn") in plaats van de samenvatting als volledig te presenteren.
2. Sorteer elk ticket in precies één categorie, in deze volgorde (de eerste die past, wint):
   - Wacht op jouw antwoord — de klant reageerde als laatste en wacht. Sorteer op wachttijd.
   - Urgent / risico — hoge prioriteit, SLA op of nabij overschrijding, of negatief sentiment. Sorteer op ernst.
   - Vandaag gepland — agenda-item of toegezegde opvolging vandaag, in tijdsvolgorde.
   - Wachten op anderen — de klant, een leverancier of een escalatie is aan zet. Markeer alles dat 3+ dagen stil is, maar laat deze categorie de top niet verdringen.
   - De rest — alleen een aantal en een typering in één regel.
3. Elk ticket krijgt één actiegerichte regel: nummer, klant (kort), status in 5–8 woorden, volgende actie ("#1234 <klant> — printer 2 d offline, klant reageerde gisteren → bevestigen dat de fix werkt").
4. Open met "Begin hier:" het belangrijkste ticket en één zin waarom (het langst wachtende klantantwoord wint van vage urgentie; een harde SLA-overschrijding wint van alles).
5. Sluit af met de vorm van de dag: totalen per categorie en één zin.
6. Wordt om de korte versie gevraagd ("3 regels"), lever exact drie regels, zonder koppen of inleiding: (1) Begin hier + waarom, (2) de tellingen — X wachten op antwoord / Y urgent / Z gepland, (3) het ene ding dat vandaag pijn doet als het genegeerd wordt.
7. Bied de opvolging aan: "Wil je conceptantwoorden voor de tickets die op jou wachten?"

Alleen-lezen: er verandert niets — geen statusupdates, notities of herinneringen — tenzij het teamlid daar als vervolg om vraagt. Verzin nooit ticketnummers, SLA-tijden of klantreacties; is de laatste activiteit onduidelijk, neem dan de veiligere categorie (Wacht op jouw antwoord).

Nederlandse conventie: datums in DD-MM-JJJJ ("15-07-2026"), tijden in 24-uursnotatie ("10:00"). De samenvatting is intern: tussen collega's is "je" gangbaar op Nederlandse en Vlaamse desks; interne afkortingen ("z.s.m.", "n.a.v.", "t.b.v.") mogen in interne regels, nooit in klanttekst.

Onbeheerde variant (Flows — via Run Skill op een ticketgebeurtenis, nooit gepland): je volledige antwoord is de briefing, geen vertelstem of vragen, altijd met de Begin hier-regel en de tellingen, zonder vervolgaanbod. Lege wachtrij → exact: "Geen open tickets aan jou toegewezen. Geniet van de schone lei." Mislukte zoekopdracht → één regel dat de samenvatting niet gegenereerd kon worden, nooit een verzonnen samenvatting.
```
