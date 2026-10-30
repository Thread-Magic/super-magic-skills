---
name: Triage Similar Tickets
description: Find closed tickets about the same product and problem and report how your techs finally filed them, as evidence for setting category, type and priority on a new ticket.
category: Triage & Routing
tools: [search_tickets]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Triage Similar Tickets

**When to use:** Before classifying a new ticket, you want to know how your own techs filed the last tickets like it, so the pick follows your desk's habits and not a generic guess. Run by the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`).

**Run it:** on one ticket · or inside a triage Flow, before the category, type and priority skills.

## Prompt

```
Purpose: find how this desk's technicians filed past tickets like this one. Their final choices are the evidence for the category, ticket type and priority skills.

STEPS
1. From the current ticket, pull out: the product or app name, any error code, server or device names, the client, the action asked for (setup, access, outage, patch, restore) and how many people are affected.
2. Search this desk's CLOSED tickets from the last 180 days. Run at least 3 searches:
   a. product + problem
   b. the error code or exact phrase
   c. the same client + the product
   If you have fewer than 5 good matches, search again with synonyms.
3. Keep 5-10 tickets about the SAME thing (same product AND same kind of problem). Drop tickets that only share a generic word ("email", "slow", "help").
4. For each kept ticket, read its "Closure Review" note if it has one. Tickets marked "corrected" are the strongest evidence: they show what a tech fixed.
5. Record for each: ticket number, title, final category, final ticket type, final priority, closure result.

WEIGHTING
- Tickets with a "corrected" Closure Review count double.
- The same client counts more than other clients.
- Newer tickets count more than older ones.

OUTPUT
Similar tickets:
- #<id> | <title> | <category> | <type> | <priority> | <corrected / match / none>
Category pattern: <e.g. "6 of 7 Server > Patch Management">
Type pattern: <...>
Priority pattern: <...>
Agreement per field: Strong (75%+ of weighted matches agree) | Mixed | None found

RULES
- Read only. Change nothing on any ticket.
- Use the values each ticket CLOSED with, not the ones it opened with.
- Ignore test, merged and deleted tickets.
- If a search may have hit a result cap, say so.
- If nothing relevant turns up, say "None found". Never stretch to fill the list and never invent a ticket number.
```
