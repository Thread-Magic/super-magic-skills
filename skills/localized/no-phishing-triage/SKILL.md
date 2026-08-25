---
name: Phishing-triage (Norwegian)
description: Phishing-triage av en mistenkelig e-post: vurder uten å røre nyttelasten, sjekk spredningsradius, inneslutt hvis skadelig, svar melderen med konklusjon.
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Phishing-triage (Norwegian)

**Når skal den brukes:** en bruker har videresendt noe mistenkelig («er dette phishing?»), et phishing-meldingssak lander på sikkerhetstavla, eller en tekniker vil ha en ny vurdering før en melding slippes ut eller slettes.

**Kjør den:** på én meldt melding.

## Prompt

```
Før en meldt mistenkelig e-post fram til en dokumentert konklusjon.

1. Fang indikatorene fra saken kun som tekst: avsenderadresse og visningsnavn, reply-to, emne, sendetidspunkt, hvert lenkemål nøyaktig slik det står, og navn og typer på vedlegg. Åpne, klikk, hent eller gjengi aldri en lenke eller et vedlegg fra meldingen — heller ikke «bare for å se hva det er».
2. Simuleringsgren: sammenlign avsender- og lenkedomener mot kundens dokumenterte simuleringsdomener i kunnskapsbasen. Kun ved eksakt treff på et dokumentert simulatordomene → klassifiser som simulering, lukk internt med et rentekstnotat som navngir domenet, og svar IKKE kunden (det forvrenger måltallene i simuleringsprogrammet deres). Stopp her. Delvis domenetreff er ikke treff: lukk aldri ekte phishing som simulering, og utløs aldri en ekte hendelse for en simulering.
3. Vurder indikatorene: etterligner- eller søskendomene, hastverks- og betalingsagn, legitimasjonshøstingslenke (vist tekst avviker fra faktisk mål), uventede vedleggstyper, kapring av en ekte tidligere tråd. Er fulle headere limt inn, overlat dybdeanalysen til email-header-analysis.
4. Spredningsradius: søk etter samme avsender eller emne på tvers av kundens boards og nylige saker. Fastslå hvem andre som mottok meldingen og — kritisk — om noen klikket, svarte, oppga legitimasjon eller åpnet et vedlegg. Slå aldri fast «ingen andre mottok denne» ut fra et avkuttet søk; skriv «ingen andre meldinger i de siste N gjennomsøkte sakene» (basisskillen Sweep Honesty).
5. Har noen samhandlet med en melding du vurderer som skadelig, eskaler umiddelbart og start compromised-account-containment for de berørte brukerne. Inneslutning går foran rapporten: inneslutt raskt, undersøk etterpå.
6. Lever konklusjonen. Skadelig → karantene eller fjerning fra alle mottakerpostbokser, blokkering av avsender og domene på gatewayen, og nullstilling av legitimasjon for alle som klikket. Mistenkelig, men ubekreftet → si nøyaktig det, sammen med hva som ville bekreftet det. Legitim → forklar signalene som frikjenner den.
7. Svar melderen som et åpent utkast og takk for meldingen; loggfør konklusjon, bevis og resonnement som et internt notat i ren tekst, uten markdown og emoji (basisskillen PSA Note Discipline), og klassifiser saken og sett status. Dokumenter beslutningen, ikke bare handlingen.

Norsk konvensjon: defensivt vokabular — «meldt melding», «mistenkt phishing-forsøk»; aldri «hacking» eller «datalekkasje» før formell bekreftelse. Svaret til melderen holder du-formen og avsluttes med en eksplisitt takk. Tidsstempler i DD.MM.ÅÅÅÅ og 24-timersformat med tidssone («15.07.2026 kl. 09:12 CET»). Tekniske indikatorer (headere, URL-er, filnavn, feilstrenger) gjengis verbatim på engelsk — de er bevis og søkenøkler. Er du i tvil, inneslutt.
```
