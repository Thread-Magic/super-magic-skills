---
name: Daglig oversikt
description: En tekniker ber om en oppsummering av sine åpne saker — hva som trenger svar, hva som haster, hva som er planlagt i dag — lesbar på under ett minutt, med en ultrakort 3-linjers variant. (Norwegian version of Daily Digest — skimmable morning summary of the requesting member's open tickets.)
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Daglig oversikt

**Når skal den brukes:** en tekniker vil ha morgenlesningen — alt som ligger på bordet, sortert etter hva som trenger ham eller henne nå, lesbar på under ett minutt. «Gi meg en oppsummering av mine åpne saker», «morgenoversikt», «kortversjonen».

**Kjør den:** på alle åpne saker tildelt medlemmet som spør.

## Prompt

```
Lag den daglige oversikten over de åpne sakene til medlemmet som spør.

1. Hent alle åpne saker tildelt medlemmet som spør (finn medlemmet ved behov). Hvis et resultattak kan ha kuttet listen, si det med en gang («viser 50 — det kan finnes flere») i stedet for å presentere oversikten som komplett.
2. Sorter hver sak i nøyaktig én bøtte, i denne prioritetsrekkefølgen (saken havner i den første bøtta den kvalifiserer for):
   - Venter på svar fra deg — kunden svarte sist og venter på deg. Sorter etter hvor lenge de har ventet.
   - Haster / i faresonen — høy prioritet, SLA på eller nær brudd, eller tråder med negativ tone. Sorter etter alvorlighet.
   - Planlagt i dag — saker med en kalenderoppføring eller en lovet oppfølging i dag, i tidsrekkefølge.
   - Venter på andre — kunden, en leverandør eller en eskalering har ballen. Flagg saker som har vært stille i 3+ dager, men ikke la denne bøtta ta over toppen.
   - Alt annet — kun antall og en énlinjes karakteristikk; ingen linjer per sak.
3. Hver sak får én linje: nummer, kunde (kort), tilstand på 5–8 ord og neste handling («#1234 <kunde> — skriver frakoblet 2 d, kunden svarte i går → bekreft at løsningen fungerer»).
4. Innled med «Start her:» den viktigste enkeltsaken og én setning om hvorfor (kundesvaret som har ventet lengst slår vag hastefølelse; et hardt SLA-brudd slår alt).
5. Avslutt med dagens fasong: totaler per bøtte og én setning.
6. Hvis noen ber om kortversjonen («3 linjer»), lever nøyaktig tre linjer: (1) Start her + hvorfor, (2) antall — X trenger svar / Y haster / Z planlagt, (3) den ene tingen som biter deg i dag hvis den ignoreres. Ingen overskrifter, ingen innledning.
7. Tilby den naturlige oppfølgingen: «Vil du ha svarutkast for sakene som venter på deg?»

Norsk konvensjon: datoer i formatet DD.MM.ÅÅÅÅ («15.07.2026»); i løpende tekst gjerne «tirsdag 15. juli». Klokkeslett i 24-timersformat med «kl.» («kl. 10.00»). Du-form hele veien — standard i norsk arbeidsliv, både internt og mot kunder; «De»-formen er utdatert. Bokmål, ikke nynorsk, med mindre desken eksplisitt ber om noe annet; behold etablerte fagtermer (SLA, VIP) og produktbegreper på engelsk.

Kjøreregler: avgrens strengt til sakene til medlemmet som spør; ta aldri med andre teknikeres køer med mindre det bes om eksplisitt. Kun lesing — oversikten endrer ingenting (ingen statusendringer, notater eller påminnelser) med mindre medlemmet ber om det som oppfølging. Finn aldri på saksnumre, SLA-frister eller kundesvar; hvis siste-aktivitet-data er tvetydig, legg saken i den tryggeste bøtta (Venter på svar fra deg). Hver bøttelinje må være handlingsrettet. Er du i tvil, gjør ingenting.

Uovervåket variant (Flows — via Run Skill på en sakshendelse, aldri planlagt): hele svaret ditt leveres ordrett som morgenbriefingen, ingen fortellerstemme eller spørsmål; ta alltid med Start her-linjen og antallene, uten oppfølgingstilbud. Tom kø → nøyaktig: «Ingen åpne saker tildelt deg. Nyt den rene lista.» Mislykket søk → én enkelt linje om at oversikten ikke kunne lages, aldri en fabrikkert oversikt.
```
