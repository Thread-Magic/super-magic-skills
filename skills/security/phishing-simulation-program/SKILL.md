---
name: Phishing Simulation Program
description: Plan a client phishing-awareness simulation: scope, cadence, lure difficulty, a no-shame reporting culture, and desk triage that doesn't collide.
category: Security
tools: [search_tickets, search_clients, search_contacts, search_knowledge_base, add_ticket_note, create_ticket, schedule_ticket]
connectors: []
scope: global
flow: no
role: [Security & Compliance Owner, CSM / Account Manager]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# Phishing Simulation Program

**When to use:** A client asks to start (or restart) phishing simulations, often driven by insurance or compliance; a campaign is being planned and the desk needs scope, schedule, and coordination tickets; or simulation results are in and the client wants the readout and next-cycle plan.

**Run it:** across a client's user population (a simulation program, planned and coordinated).

## Prompt

```
Turn "we should run phishing tests" into a coordinated program. You plan and coordinate; the
technician or the client's program owner operates the simulation platform.

1. Scope the program with the client's stakeholder: which user groups — ramping by department
   is fine, exempting executives is not, since leadership is the most-targeted group in real
   attacks; cadence, typically monthly or quarterly, because more frequent breeds alarm
   fatigue; and difficulty, starting obvious and ramping toward role-relevant. Record the
   agreed scope in a plain-text note.
2. Set the culture rule before the first send: the program measures the organization's
   resilience, not individuals' failures. Reported-rate is the headline metric; named click
   lists go ONLY to the client's designated program owner, never into general reporting. A
   click earns a short training moment, not a reprimand.
3. Document the simulation platform's sending domains and link domains in the client's
   knowledge record — check what is already recorded and flag gaps for the tech to fill. The
   phishing-triage skill's simulation branch matches against exactly this record; undocumented,
   every simulation email becomes a real investigation and every reply skews the metrics.
4. Get the simulation domains allowed through the mail gateway and filters, so results measure
   users, not the spam filter. Open a coordination ticket for the gateway work and schedule the
   campaign window, so the desk knows when simulation report volume is due.
5. During the campaign, user reports of simulation emails are GOOD outcomes — phishing-triage
   closes them internally without replying, since a reply skews metrics. Real phishing does not
   pause for campaigns: anything not matching the documented simulator domains gets the full
   real-phish treatment. Never assume "it's probably the simulation."
6. Readout: cohort-level metrics — report rate, click rate, credential-entry rate, trend
   against prior cycles — with "at least N" honesty on any ticket-derived count (Sweep Honesty
   base skill). Recommend the next cycle's difficulty and any targeted training for high-risk
   patterns, not for named individuals. Deliver the plan or readout as chat or a note.

No-shame is non-negotiable: never publish a "wall of shame". Only an EXACT match against the
documented simulator domains closes a report as simulation — partial matches are investigated
as real. Do not send or schedule simulation emails yourself; the platform owner executes sends.
Lure content stays professional: no fake terminations, bonus revocations or health-scare lures
— realistic is the goal, cruel is a program-killer. Don't mark a campaign "ready" until the simulator domains and scope are
documented. Without knowledge-base access, confirm the simulator-domain record with the tech and
note where it lives. Never invent metrics.
```
