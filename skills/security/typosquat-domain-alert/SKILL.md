---
name: Typosquat Domain Alert
description: Work a typosquat or lookalike domain alert impersonating a client: gather registrar and DNS facts without visiting, gauge capability, draft a warning.
category: Security
tools: [liongard_domain, search_clients, search_tickets, web_search, add_ticket_note, update_ticket, view_openDraft]
connectors: [Liongard]
scope: single
flow: yes
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Always-On Coverage]
---

# Typosquat Domain Alert

**When to use:** A user or monitoring tool reports a domain that looks like the client's; a phishing investigation surfaces a cousin domain that needs its own workup; or a client asks "should we worry about this domain?"

**Run it:** on one ticket · or as a Flow (triggered on a reported lookalike-domain ticket).

## Prompt

```
Work a lookalike-domain report from "someone registered our-cl1ent.com" to a fact-based
severity call and a client warning email — using passive sources only, never the domain
itself. Work it in order:

1. Capture the suspect domain exactly as written in the report. Do NOT visit it, resolve
   links on it, or fetch content from it — the workup is passive.
2. Gather facts: with Liongard enabled, read the client's legitimate domain records and any
   visibility on the suspect (registrar, creation date, name servers, MX/SPF presence).
   Supplement with a passive web search for registration facts. Record the as-of date on
   everything.
3. Read the capability signals: MX records on the lookalike mean it can send and receive
   mail — that is email-attack capability and raises severity. A very recent creation date
   raises it further. Parked with no MX and no content history is watch-and-warn territory.
4. Check for active use: search for the suspect domain appearing in recent mail, phishing
   reports, or vendor-fraud tickets. Active use converts this from a warning into a live
   phishing/BEC response — branch to phishing-triage or vendor-fraud-bec-alert.
5. Recommend actions: block the domain at the client's mail gateway and web filter; add it
   to monitoring/watchlists; prepare the evidence pack (registration facts, capability
   signals, any observed use) for a registrar abuse report or takedown — filing a takedown
   is a management and client decision, so package it, don't file it.
6. Draft the client warning email (present as a draft for a human to send): what the domain
   is, that it closely resembles theirs and could be used to impersonate them, to verify
   full sender addresses character by character, and to verify any payment or banking change
   by phone using a number on file. Use defensive-writing-standard wording — a registered
   lookalike does not mean the client "was targeted" or compromised.
7. Document the decision, not just the action: facts gathered, capability read,
   recommendation, and what was sent to whom.

Unattended (Flows) variant:
- The entire reply is the plain-text internal workup note posted verbatim — suspect domain
  (exactly as reported), registration facts with as-of dates, capability read (MX presence,
  creation date), severity call, and recommended next steps. No narration, no markdown.
- Deterministic input from the flow: the triggering ticket id containing the reported
  domain. No domain extractable verbatim → output nothing; never reconstruct or guess a
  domain.
- Active use found in recent tickets → the note leads with LIVE USE DETECTED - ESCALATE NOW
  plus the evidence; the phishing/BEC response itself stays attended.
- Permitted writes: the internal note only. The client warning email, status changes, and
  takedown packaging stay attended.

Guardrails — always:
- Never browse, screenshot, or interact with the suspect domain, and never click links
  containing it. Passive sources only; no probing or scanning.
- Don't overstate: registration alone is not an attack. Reserve stronger language for
  observed use, per the defensive-writing-standard.
- Takedown/abuse filings are prepared, not performed — management decides.
- Degradation: Liongard absent → registrar and DNS facts may be limited to passive search;
  state the visibility gap in the note instead of guessing record contents. Never invent
  data.
```
