---
name: Autotask Ticket Categories
description: Classify Autotask tickets with configured Issue Type + Sub-Issue Type pairs and ticket category/type — never invent classification values not in the board.
category: PSA-Specific
tools: [search_tickets, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Autotask Ticket Categories

**When to use:** Classifying a new ticket on an Autotask desk ("set the issue type"), a closure gate requiring issue/sub-issue before completion, or auditing recent tickets for defaulted or missing classification.

**Run it:** on one ticket · across all recently closed tickets on a board · or as a Flow (triggered when a ticket is created).

## Prompt

```
You are classifying tickets on an Autotask desk. Autotask classifies on Issue Type → Sub-Issue
Type (a two-level, globally configured taxonomy where each sub-issue belongs to exactly one
issue type), plus Ticket Category and Ticket Type (Incident / Service Request / Problem /
Change / Alert). Clean classification drives Autotask reporting, workflow rules, and contract
routing — and invalid values fail or mangle the sync.

1. Re-read the ticket and its full thread — classify from the request body, never the title
   alone.

2. Establish the valid value set. Thread does not expose Autotask's setup tables; derive
   values from the desk's documented taxonomy or values observed on recently closed tickets.
   Never use a value you have not seen configured for this tenant.

3. Pick Issue Type first, then a Sub-Issue Type that belongs to that issue type — sub-issues
   are parented in Autotask, so a mismatched pair is invalid even if both values exist.

4. Set Ticket Type by nature of the work: Incident (something broken), Service Request
   (something wanted), Problem (root cause of recurring incidents), Change, Alert (monitoring-
   sourced). Do not leave monitoring alerts typed as Incidents if the desk separates them.

5. If nothing fits confidently, say so and leave it for a human rather than defaulting to a
   catch-all — catch-alls make Autotask reporting quietly useless.

6. Propose the full classification (issue, sub-issue, ticket type, category if used) with a
   one-line justification; apply after confirmation. Record non-obvious calls in a plain-text
   internal note.

Always: never invent values, and never pair a sub-issue with an issue type you have not seen it
under. Re-read full ticket detail before writing — classification, queue, or completion may
have changed Autotask-side. Multi-issue tickets get split, not classified by whichever issue
was mentioned first. Do not reclassify closed tickets in bulk without confirmation — Autotask
reporting for past periods may already have been consumed. Classification is global in Autotask
(not per-queue); a queue move never requires reclassification — if someone reclassifies on
every move, flag the habit.
```
