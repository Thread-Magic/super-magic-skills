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

1. Capture the suspect domain exactly as written in the report. Never visit, browse,
   screenshot, scan or resolve links on it, and never click a link containing it — the
   workup stays passive throughout.
2. Gather facts: with Liongard enabled, read the client's legitimate domain records and any
   visibility on the suspect — registrar, creation date, name servers, MX/SPF presence.
   Supplement with passive web search for registration facts. Record the as-of date on
   everything. Without Liongard the registrar and DNS picture may be thin: state the
   visibility gap in the note rather than guessing record contents (apply the Connector
   Degradation base skill).
3. Read the capability signals: MX records on the lookalike mean it can send and receive
   mail — that is email-attack capability and raises severity. A very recent creation date
   raises it further. Parked with no MX and no content history is watch-and-warn territory.
4. Check for active use: search recent mail, phishing reports and vendor-fraud tickets for
   the suspect domain. Active use converts this from a warning into a live phishing/BEC
   response — branch to phishing-triage or vendor-fraud-bec-alert.
5. Recommend actions: block the domain at the client's mail gateway and web filter, add it
   to monitoring and watchlists, and assemble the evidence pack — registration facts,
   capability signals, any observed use — for a registrar abuse report. Package the takedown;
   never file it. That is a management and client decision.
6. Draft the client warning email for a human to send: what the domain is, that it closely
   resembles theirs and could be used to impersonate them, to verify full sender addresses
   character by character, and to verify any payment or banking change by phone using a
   number on file. Registration alone is not an attack — per defensive-writing-standard,
   never write that the client "was targeted" or compromised; stronger language waits for
   observed use.
7. Document the decision, not just the action: facts gathered, capability read,
   recommendation, and what was sent to whom.

As a Flow: your entire reply is the internal workup note, plain text, no narration — suspect
domain exactly as reported, registration facts with as-of dates, capability read (MX
presence, creation date), severity call, recommended next steps. Input is the triggering
ticket id. No domain extractable verbatim → output nothing; never reconstruct or guess one.
Active use found in recent tickets → lead the note with LIVE USE DETECTED - ESCALATE NOW plus
the evidence. The note is the only permitted write; the client email, status changes and
takedown packaging stay attended.
```
