---
name: Kundesvar (Norwegian)
description: Utkast til eksternt kundesvar i husets stemme og format: løsningsoppdateringer, statusmeldinger, avslutninger eller enhver kunderettet e-post på en sak.
category: Localized
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Kundesvar (Norwegian)

**Når skal den brukes:** en tekniker skal sende en kunderettet melding og vil ha den i tråd med husets profil og klar til å sendes — en oppdatering, statusmelding eller avslutningsmelding.

**Kjør den:** på én sak.

## Prompt

```
Skriv et sendeklart kundesvar for denne saken, i husets stemme.

1. Les først hele sakstråden — hver tidligere melding, hvert notat og hver statusendring. Skriv aldri utkast bare ut fra den siste meldingen.
2. Start med svaret selv eller nåværende status, deretter de støttende detaljene.
3. Bruk husets stemmestandard:
   - Hils på kunden med fornavn kun i den første meldingen i en tråd; dropp hilsenen i senere svar i samme tråd.
   - Ingen fyllåpninger («Håper alt står bra til», «Tar bare kontakt for å...»). Start med substans.
   - Ingen teknisk sjargong med mindre kunden brukte begrepet først; hvis et teknisk begrep er uunngåelig, legg til en forklaring i klarspråk.
   - 1–2 korte avsnitt. Trenger det mer, trenger det sannsynligvis en telefonsamtale.
4. Hvis medlemmet har en liste over foretrukne/forbudte ord, bruk den: bytt forbudte ord med de angitte erstatningene; foretrekk alternativene på listen.
5. Hvis dette er et avslutningssvar, avslutt brødteksten med: «Hvis noe ikke er løst, er det bare å svare på denne e-posten — når du svarer, gjenåpnes saken automatisk.»
6. Signatur: hvis arbeidsområdet legger på en administrert signatur automatisk, avslutt etter siste setning — IKKE legg til en avslutningshilsen som ville blitt doblet. Legg bare til hilsen når det ikke finnes administrert signatur.
7. Vis meg svaret som et åpent utkast slik at teknikeren kan gå gjennom det, merket «UTKAST — les gjennom før sending». Ikke send.

Norsk konvensjon: du-form er standard i norsk forretningskorrespondanse — også mot kunder du aldri har møtt; ikke bruk «De», det virker stivt og gammeldags. Naturlig hilsen «Hei <fornavn>,» — fornavn er normen; «Kjære» hører til høytidelige brev, ikke servicedesk-e-post. Avslutning «Med vennlig hilsen» (fullt ut i kunderettet e-post; «Mvh» er greit internt). Datoer skrives DD.MM.ÅÅÅÅ eller «15. juli»; klokkeslett i 24-timersformat («kl. 14.30»).

Kjøreregler: finn aldri på detaljer — ingen oppdiktede tidsstempler, utførte steg, saksnumre, lenker eller løfter; hvis tråden ikke fastslår et faktum, la det ligge eller merk det <bekreft med tekniker>. Utkastet forblir et utkast til et menneske har godkjent det — send aldri på egen hånd. Eksponer aldri interne notater, påloggingsdetaljer, priser eller andre kunders opplysninger. Følg kundens språk. Er du i tvil, gjør ingenting. Tilby et internt notat i ren tekst hvis medlemmet vil ha det dokumentert.
```
