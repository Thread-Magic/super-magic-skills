---
name: Intake Classification Tree
description: Walk a new ticket through the Incident / Request / Problem decision tree and recommend the matching type, subtype, and item so intake classification stays consistent.
category: Triage & Routing
tools: [search_tickets, list_boards, update_ticket]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Intake Classification Tree

**When to use:** A new ticket needs its type/subtype/item set and the tech wants a consistent call, "is this an incident or a request?", or intake review found inconsistently classified tickets to re-run through the tree.

**Run it:** on one ticket · across a set of tickets to re-classify · or as a Flow (when a ticket is created).

## Prompt

```
Walk the desk's decision tree — Incident, Request, or Problem first, then type/subtype/item —
and recommend one classification with the reasoning shown. Consistent classification makes
every downstream report trustworthy.

1. Read the ticket body and thread — classify from what's described, not the title.

2. Top of the tree — pick exactly one:
   - Incident: something that worked is now broken or degraded ("can't", "down", "error",
     "stopped working").
   - Request: the user wants something new or changed that isn't broken (access, equipment,
     how-do-I, moves/adds/changes).
   - Problem: the underlying cause behind recurring incidents, or a proactively identified
     defect — typically opened by the desk, not the client.

3. Descend to type/subtype/item using the desk's category tree (as configured for this
   tenant): affected system first (email, endpoint, network, identity, application, printing,
   telephony), then the specific service or action. Choose only from the tenant's actual
   category values; if no fitting item exists, recommend the closest parent and flag the gap
   rather than inventing a value.

4. Edge rules: a request blocked by an error is an Incident on the blocking error; "it broke
   because we changed it" is an Incident referencing the change; multiple recurrences of the
   same incident → recommend also opening/linking a Problem, don't reclassify the incident
   itself. One classification per ticket: if it genuinely contains both an Incident and a
   Request, that's a splitter case — say so instead of blending.

5. Output the recommendation: Incident/Request/Problem, type > subtype > item path, and one
   line of reasoning per level. Apply the classification only if the tech confirms —
   classification drives SLAs and billing, so a silent wrong write is expensive. Never let the
   requester's urgency influence type; priority is a separate decision.

Running as a Flow: reply with exactly one line (logged, not posted): "CLASSIFIED #<n>:
<Incident|Request|Problem> > <type> > <subtype> > <item>." or "NO ACTION." — no reasoning
trace. Permitted write: set the classification, only when the top-of-tree call is unambiguous
AND exactly one existing type/subtype/item path fits. Deterministic stops, each → NO ACTION:
ticket contains both an Incident and a Request; no fitting item exists in the tenant tree
(never invent values, never write the "closest parent" unattended — that flag is attended
work); classification already set by a human; body too thin to classify from content.
Priority is never touched in this variant.
```
