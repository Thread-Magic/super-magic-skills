---
name: Phishing-triage
description: Phishing-triage av en mistenkelig e-post: vurder uten å røre nyttelasten, sjekk spredningsradius, inneslutt hvis skadelig, svar melderen med konklusjon.
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Phishing-triage

**Når skal den brukes:** en bruker har videresendt noe mistenkelig («er dette phishing?»), et phishing-meldingssak lander på sikkerhetstavla, eller en tekniker vil ha en ny vurdering før en melding slippes ut eller slettes.

**Kjør den:** på én meldt melding.

## Prompt

```
Før denne meldte mistenkelige e-posten til en dokumentert konklusjon.

1. Fang indikatorene fra saken uten å samhandle med dem: avsenderadresse og visningsnavn, reply-to, emne, sendetidspunkt, hvert lenkemål nøyaktig slik det står skrevet, og navn og typer på vedlegg. Åpne aldri lenker eller vedlegg, og hent aldri en URL fra meldingen for å «se hva det er».
2. Simuleringsgren: sammenlign avsender- og lenkedomener mot kundens dokumenterte phishing-simuleringsplattform-domener (slå opp kundens simuleringsleverandør-oppføring i kunnskapsbasen). Matcher det en kjent simulator → klassifiser som simulering, lukk internt med et rentekst-notat som navngir det matchede domenet, og svar IKKE kunden (et svar skjevfordeler måltallene i simuleringsprogrammet deres). Stopp her.
3. Vurder indikatorene: etterligner- eller søskendomene, hastverks- og betalingsagn, legitimasjonshøstingslenke (avvik mellom vist tekst og faktisk mål), uventede vedleggstyper, kapring av en ekte tidligere samtaletråd. Er fulle headere limt inn, overlat dybdeanalysen til skillen email-header-analysis og innarbeid konklusjonen dens.
4. Spredningsradius-sjekk: søk etter samme avsender eller emne på tvers av kundens boards og nylige saker. Fastslå hvem andre som mottok meldingen og — kritisk — om noen klikket, svarte, oppga legitimasjon eller åpnet et vedlegg (identifiser mottakere via kontaktlisten).
5. Har noen samhandlet med en melding du vurderer som skadelig → eskaler umiddelbart og start skillen compromised-account-containment for den eller de berørte brukerne. Innesluttning går foran å fullføre rapporten: inneslutt raskt, undersøk etterpå.
6. Lever konklusjonen: Skadelig → anbefal karantene/fjerning fra alle mottakerpostbokser, blokkering av avsender/domene på gatewayen, og en legitimasjonsnullstilling for alle som klikket. Mistenkelig, men ubekreftet → si nøyaktig det, sammen med hva som ville bekreftet det. Legitim → forklar signalene som frikjenner den.
7. Svar melderen som et åpent utkast i vokabularet for defensiv skriving (en mistenkelig e-post er en «meldt melding», ikke et «brudd»). Loggfør konklusjonen, bevisene og beslutningsresonnementet som et internt notat; klassifiser og sett status på saken. Takk melderen.

Norsk konvensjon: defensivt vokabular — «meldt melding», «mistenkt phishing-forsøk», «uvanlig aktivitet»; aldri «hacking» eller «datalekkasje» før formell bekreftelse. Svaret til melderen holder du-formen og avsluttes med en eksplisitt takk: «Takk for at du meldte denne meldingen — det var akkurat riktig gjort.» Tidsstempler i tidslinjer i DD.MM.ÅÅÅÅ og 24-timersformat, med tidssone («15.07.2026 kl. 09:12 CET»). Tekniske indikatorer (headere, URL-er, filnavn, feilstrenger) gjengis verbatim på engelsk — oversett dem aldri, de tjener som bevis og søkenøkler.

Kjøreregler: åpne, klikk, hent eller gjengi aldri lenker eller vedlegg fra den meldte meldingen — fang indikatorer kun som tekst. Sjekk simuleringsstatus begge veier (utløs aldri en ekte hendelse for en simulering; lukk aldri en ekte phishing som simulering på en delvis domenematch — krev et nøyaktig, dokumentert simulatordomene). Svar aldri kunden på en bekreftet simulering. Klikket eller svart betyr eskaler umiddelbart. Slå aldri fast «ingen andre mottok denne» ut fra et avkuttet søk; skriv «ingen andre meldinger funnet i de siste N gjennomsøkte sakene». Dokumenter beslutningen, ikke bare handlingen. Er du i tvil, inneslutt.
```
