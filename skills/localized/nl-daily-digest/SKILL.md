---
name: Dagelijkse samenvatting
description: Dagelijkse samenvatting van openstaande tickets van een technicus: wat wacht op antwoord, wat is urgent, wat staat vandaag gepland, met 3-regelvariant.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Dagelijkse samenvatting

**Wanneer gebruiken:** een technicus wil de ochtendleesbeurt — alles wat op zijn of haar bord ligt, gesorteerd op wat nú aandacht nodig heeft, in minder dan een minuut te scannen. "Geef me een overzicht van mijn open tickets", "ochtendoverzicht", "korte versie".

**Uitvoeren:** over alle open tickets van het aanvragende teamlid.

## Prompt

```
Maak de dagelijkse samenvatting van de open tickets van het teamlid dat erom vraagt.

1. Haal alle open tickets van het aanvragende teamlid op (zoek het teamlid indien nodig op). Kan een resultaatlimiet de lijst hebben afgekapt, meld dat meteen ("50 getoond — er kunnen er meer zijn") in plaats van de samenvatting als volledig te presenteren.
2. Sorteer elk ticket in precies één categorie, in deze prioriteitsvolgorde (een ticket valt in de eerste categorie waarvoor het kwalificeert):
   - Wacht op jouw antwoord — de klant reageerde als laatste en wacht op jou. Sorteer op wachttijd.
   - Urgent / risico — hoge prioriteit, SLA op of nabij overschrijding, of threads met negatief sentiment. Sorteer op ernst.
   - Vandaag gepland — tickets met een agenda-item of toegezegde opvolging vandaag, in tijdsvolgorde.
   - Wachten op anderen — de klant, een leverancier of een escalatie is aan zet. Markeer alles dat 3+ dagen stil is, maar laat deze categorie de top niet verdringen.
   - De rest — alleen een aantal en een typering in één regel; geen regels per ticket.
3. Elke ticketregel is één regel: nummer, klant (kort), status in 5–8 woorden, volgende actie ("#1234 <klant> — printer 2 d offline, klant reageerde gisteren → bevestigen dat de fix werkt").
4. Open met "Begin hier:" het belangrijkste ticket en één zin waarom (het langst wachtende klantantwoord wint van vage urgentie; een harde SLA-overschrijding wint van alles).
5. Sluit af met de vorm van de dag: totalen per categorie en één zin.
6. Wordt om de korte versie gevraagd ("3 regels"), lever exact drie regels: (1) Begin hier + waarom, (2) de tellingen — X wachten op antwoord / Y urgent / Z gepland, (3) het ene ding dat vandaag pijn gaat doen als het genegeerd wordt. Geen koppen, geen inleiding.
7. Bied de natuurlijke opvolging aan: "Wil je conceptantwoorden voor de tickets die op jou wachten?"

Nederlandse conventie: datums in DD-MM-JJJJ ("15-07-2026"); tijden in 24-uursnotatie ("10:00"). De samenvatting is intern: tussen collega's is "je" gangbaar op Nederlandse en Vlaamse desks; interne afkortingen ("z.s.m.", "n.a.v.", "t.b.v.") mogen in interne regels, nooit in klanttekst.

Vangrails: beperk je strikt tot de eigen tickets van het aanvragende teamlid; neem nooit de wachtrijen van andere technici mee tenzij expliciet gevraagd. Alleen-lezen — de samenvatting verandert niets (geen statusupdates, notities of herinneringen) tenzij het teamlid daar als vervolg om vraagt. Verzin nooit ticketnummers, SLA-tijden of klantreacties; is de laatste activiteit onduidelijk, zet het ticket dan in de veiligere categorie (Wacht op jouw antwoord). Elke categorieregel moet actiegericht zijn. Bij twijfel: doe niets.

Onbeheerde variant (Flows — via Run Skill op een ticketgebeurtenis, nooit gepland): je volledige antwoord wordt letterlijk als ochtendbriefing afgeleverd, geen vertelstem of vragen; altijd de Begin hier-regel en de tellingen, zonder vervolgaanbod. Lege wachtrij → exact: "Geen open tickets aan jou toegewezen. Geniet van de schone lei." Mislukte zoekopdracht → één regel dat de samenvatting niet gegenereerd kon worden, nooit een verzonnen samenvatting.
```
