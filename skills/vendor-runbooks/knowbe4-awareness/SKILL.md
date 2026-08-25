---
name: KnowBe4 Awareness & PhishER
description: Run a KnowBe4 program: awareness training, phishing simulations, and triage user reports through PhishER and the Phish Alert Button without collisions.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_knowledge_base, add_ticket_note, create_ticket, schedule_ticket]
connectors: []
scope: both
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# KnowBe4 Awareness & PhishER

**When to use:** A client is starting or running KnowBe4 training or phishing simulations and the desk is coordinating scope, cadence, and delivery whitelisting; user-reported emails are arriving through PhishER / the Phish Alert Button and need triage; or simulation results / training-completion data need a readout and a next-cycle plan.

**Run it:** on one user-report ticket · or across the campaign/program as a coordination effort.

## Prompt

```
Coordinate a KnowBe4 program and triage its user-reported email. KnowBe4 has two surfaces:
KMSAT (awareness training and phishing simulations) and PhishER (the queue fed by the Phish
Alert Button). phishing-simulation-program owns the campaign canon and
security-awareness-coordination owns training follow-up; you add KnowBe4's mechanics and the
simulation-versus-real interplay. You have no KnowBe4 console — sends, PhishER dispositions
and tenant-wide message pulls are technician steps you scope and record, never take or claim.

1. Coordinate per phishing-simulation-program: scope (all staff; ramping by department is
   fine, exempting executives is not), cadence, difficulty progression, no-shame culture.
   KnowBe4-specific: the simulation sending and link domains must be recorded in the client's
   documentation and whitelisted at the mail gateway, or results measure the spam filter
   instead of users. Open a coordination ticket for the gateway work and schedule the campaign
   window. No documented domain record, no "ready" campaign.

2. Keep simulation and real separate, both ways. Only an exact match against the documented
   simulator domains closes a report as a simulation; a partial match is investigated as real.
   Anything not matching gets full real-phish treatment — real phishing never pauses for a
   campaign, and "it's probably the simulation" is never an assumption. With no documented
   domain record, every simulation becomes a real investigation and skews the client's metrics.

3. Triage Phish Alert Button reports in PhishER:
   - Simulation match → close internally as a simulation, no reply. Reporting one is a good
     outcome.
   - Real suspicious mail → run phishing-triage: headers and sender, sibling deliveries to
     other users, and if credentials may have been entered or a payload run, branch to
     compromised-account-containment (identity first on any login or credential) or
     edr-detection-runbook.
   - PhishER dispositions and any tenant-wide search-and-remove are technician console
     actions: scope the search and record it, never claim a removal you cannot perform.
   - A spike of the same lure across many users is one live campaign — work one representative
     as the investigation and the rest as siblings.

4. Keep readouts cohort-level: report rate (the headline metric to grow), click rate,
   credential-entry rate and training completion, with honest caps on any ticket-derived
   count. No-shame is non-negotiable — named individual results go only to the client's
   designated program owner, never into general reporting. Feed repeat-risk patterns to
   security-awareness-coordination for targeted training.

Without documentation access, confirm the simulator-domain record with the tech directly and
note where it lives. Never invent data; when in doubt do nothing irreversible and escalate.
```
