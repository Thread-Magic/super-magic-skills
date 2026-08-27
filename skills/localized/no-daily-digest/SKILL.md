---
name: Daglig oversikt (Norwegian)
description: Daglig oversikt over en teknikers åpne saker: hva som trenger svar, hva som haster, hva som er planlagt i dag, med ultrakort 3-linjers variant.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Daglig oversikt (Norwegian)

**Når skal den brukes:** en tekniker vil ha morgenlesningen — alt som ligger på bordet, sortert etter hva som trenger ham eller henne nå, lesbar på under ett minutt. «Gi meg en oppsummering av mine åpne saker», «morgenoversikt», «kortversjonen».

**Kjør den:** på alle åpne saker tildelt medlemmet som spør.

## Prompt

```
Lag den daglige oversikten over de åpne sakene til medlemmet som spør. Avgrens strengt til vedkommendes egne saker — aldri andre teknikeres køer, med mindre det bes om eksplisitt.

1. Hent alle åpne saker tildelt medlemmet (finn medlemmet ved behov). Hvis et resultattak kan ha kuttet listen, si det med en gang («viser 50 — det kan finnes flere») i stedet for å presentere oversikten som komplett.
2. Sorter hver sak i nøyaktig én bøtte, i denne rekkefølgen (første bøtte som passer, vinner):
   - Venter på svar fra deg — kunden svarte sist og venter. Sorter etter hvor lenge de har ventet.
   - Haster / i faresonen — høy prioritet, SLA på eller nær brudd, eller negativ tone. Sorter etter alvorlighet.
   - Planlagt i dag — kalenderoppføring eller lovet oppfølging i dag, i tidsrekkefølge.
   - Venter på andre — kunden, en leverandør eller en eskalering har ballen. Flagg saker som har vært stille i 3+ dager, men la ikke denne bøtta ta over toppen.
   - Alt annet — kun antall og en énlinjes karakteristikk.
3. Hver sak får én handlingsrettet linje: nummer, kunde (kort), tilstand på 5–8 ord og neste handling («#1234 <kunde> — skriver frakoblet 2 d, kunden svarte i går → bekreft at løsningen fungerer»).
4. Innled med «Start her:» den viktigste enkeltsaken og én setning om hvorfor (kundesvaret som har ventet lengst slår vag hastefølelse; et hardt SLA-brudd slår alt).
5. Avslutt med dagens fasong: totaler per bøtte og én setning.
6. Blir kortversjonen bedt om («3 linjer»), lever nøyaktig tre linjer, uten overskrifter og innledning: (1) Start her + hvorfor, (2) antall — X trenger svar / Y haster / Z planlagt, (3) den ene tingen som biter deg i dag hvis den ignoreres.
7. Tilby oppfølgingen: «Vil du ha svarutkast for sakene som venter på deg?»

Kun lesing: ingenting endres — ingen statusendringer, notater eller påminnelser — med mindre medlemmet ber om det etterpå. Finn aldri på saksnumre, SLA-frister eller kundesvar; er siste aktivitet tvetydig, velg den tryggeste bøtta (Venter på svar fra deg).

Norsk konvensjon: datoer i DD.MM.ÅÅÅÅ («15.07.2026»), i løpende tekst gjerne «tirsdag 15. juli». Klokkeslett i 24-timersformat med «kl.» («kl. 10.00»). Du-form hele veien — standard i norsk arbeidsliv, både internt og mot kunder; «De»-formen er utdatert. Bokmål, ikke nynorsk, med mindre desken ber om noe annet; behold etablerte fagtermer (SLA, VIP) og produktnavn på engelsk.

Uovervåket variant (Flows — via Run Skill på en sakshendelse, aldri planlagt): hele svaret ditt er briefingen, ingen fortellerstemme eller spørsmål, alltid med Start her-linjen og antallene, uten oppfølgingstilbud. Tom kø → nøyaktig: «Ingen åpne saker tildelt deg. Nyt den rene lista.» Mislykket søk → én linje om at oversikten ikke kunne lages, aldri en fabrikkert oversikt.
```
