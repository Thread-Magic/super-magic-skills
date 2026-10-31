---
name: Triage Ticket Type
description: Recommend the right ticket type for a new ticket still on the PSA default, telling broken from requested, so a technician can change it.
category: Triage & Routing
tools: [search_tickets]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Triage Ticket Type

**When to use:** Every ticket arrives as the PSA's default type (usually Incident), so service requests get reported as incidents. Super Magic has no tool that changes the ticket type, so this skill recommends the type in the triage note for a technician to set. Run by the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`), after Triage Learnings and Triage Similar Tickets.

**Run it:** on one ticket · or inside a triage Flow. Match the type names to the exact ones on your board.

## Prompt

```
Purpose: recommend the ticket type for a new ticket. You cannot change the ticket type; only recommend it. Only run when the type in the orchestrator's snapshot was still the PSA default (<e.g. Incident>). Skip a type a person chose.

TYPES (use the exact names on your PSA's ticket type list)
- Incident: something that worked is now broken, failing, slow or erroring. Includes failed backups, outages, login failures, error messages, "stopped working".
- Service Request: a request for something new or a change. New user, offboarding, new laptop or Mac setup, install software, add to a group or mailbox, permission or access change, license assignment, documentation or inventory updates, a quote.
- Problem: ONLY when the ticket says the issue recurs across several incidents, or asks for root-cause investigation. Never infer Problem from a single report.
- Change: ONLY for a planned infrastructure change the client asked to schedule (firewall rule change, migration window), and only if the board has this type.

HOW TO DECIDE
1. Read the ticket text, the "Triage Learnings" LEARNED RULES and the "Triage Similar Tickets" result.
2. If a learned rule matches, use it.
3. Else if the type agreement is Strong, follow it.
4. Otherwise ask: is something broken (Incident) or is someone asking for something (Service Request)?
5. If the default is right, report "default is right".
6. If you can't tell, report "default is right". A wrong recommendation costs more than none.
Never recommend a type that isn't on that list.

OUTPUT
Change nothing on the ticket. Report back to the orchestrator (no note of your own):
Type: <value> | recommended or default is right | Reason: <one line> | Confidence: High/Medium/Low
```
