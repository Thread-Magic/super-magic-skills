---
name: Printer Issues Intent Design
description: Design the printer-problems intent: three top self-help fixes first, then an escalated ticket that already carries the diagnostics collected from the user.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Printer Issues Intent Design

**When to use:** "Build an intent for printer problems" / "printer tickets are constant and always the same three fixes" / Intent Mining ranked printing as a high-volume, high-automatability candidate.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a printer intent that walks the user through the three fixes that resolve most printer
tickets, and — when they fail — creates a ticket with the diagnostics already captured so the
tech skips the twenty questions. Building intents is admin-only; if you can't, output the
complete written spec for an admin to apply.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "printer not working", "can't print",
  "cant print", "printer offline", "print job stuck", "nothing comes out of the printer",
  "printer says offline", "printing problem", "printer error", "documents stuck in queue",
  "printer won't print". Near-miss watch: "need a new printer" is a hardware request; "add a
  printer for a new user" is onboarding/setup; "scan to email broken" may be a separate flow.
- Arguments (before/during self-help): which printer (name/location, <device>); one user or
  everyone nearby (scopes device vs server/queue problem); what happens (nothing / error
  message — capture exact text / prints garbage / stuck in queue); what they already tried.
- Reply flow (self-help ladder, top 3 fixes): (1) restart the printer — power off, wait 30s,
  power on, retry; (2) clear the local queue — cancel stuck job(s) and reprint (plain steps
  for the client's OS mix); (3) reconnect/restart from the computer side — restart the
  computer, or remove/re-add / set-default if the environment supports user-level fixes. After
  each rung: "did that fix it?" — stop the moment it works and close as deflected. (4) if all
  three fail, or multiple users affected -> create a ticket carrying printer identity/location,
  scope, exact error text, rungs attempted and results. Multiple-users-affected skips straight
  to the ticket (likely a queue/server issue).
- Handoff rule: no credential steps, no admin-rights driver installs in self-help — those go
  to the ticket. Anything smelling of print-server outage (everyone affected) short-circuits
  self-help.
- Variation hooks (per client): printer fleet names/locations, whether users can add printers
  themselves, managed-print vendor to mention, OS mix for step phrasing.
- Success metric: deflection rate on printer conversations plus diagnostics completeness on
  the tickets still created.

Steps:
1. List the existing intents — check for an existing printer intent; prefer updating.
2. Search recent printer tickets; confirm the top three fixes for THIS desk from
   resolution notes — replace any rung the data says rarely works.
3. Search the knowledge base for existing printer self-help articles; link rather than restate.
4. Draft the full spec (triggers, arguments, the 3-rung ladder with stop conditions, the
   diagnostics block for the ticket, variations) plus a test plan (5 should-match, 3–5 should-
   not: hardware-request and new-user-setup near-misses). Show before any write.
5. On explicit confirmation: create the intent, then set its variations.
6. Report what was created, restate the test plan, recommend activation after tests pass. Do
   NOT activate.

Guardrails: self-help steps must be safe for a non-technical user — no admin credentials, no
registry/driver surgery, no steps that could take other users' printing down. Ground the three
fixes in this desk's resolution data where possible; don't present generic fixes as "what
usually works here" without evidence. Multiple-users-affected always escalates — never keep a
probable outage in a self-help loop. Confirm before any write; diagnostics block in plain text.
```
