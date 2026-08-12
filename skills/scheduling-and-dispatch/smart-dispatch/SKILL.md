---
name: Smart Dispatch
description: The composite dispatcher partners keep asking for — classify a new ticket, consult a routing matrix (tech specialties plus client familiarity from resolved-ticket history), then assign and schedule it in one pass.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, search_clients, list_boards, list_ticket_priorities, list_ticket_statuses, update_ticket, schedule_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Smart Dispatch

**When to use:** "Automate our dispatching" — a Flow fires on ticket creation and the desk wants classify → route → assign → schedule in one pass; or a dispatcher wants one command that does the whole first-pass dispatch instead of running triage, routing, and assignment separately.

**Run it:** on one ticket · or as a Flow that classifies, routes, assigns, and schedules each new ticket.

## Prompt

```
You are doing end-to-end dispatch in a single pass: classify the ticket, score candidate
technicians against a routing matrix (who knows the stack/client AND who has capacity),
assign the winner, and put the work on their schedule — with the reasoning written down.

1. Classify. Apply intake-classification logic to the ticket's summary and description:
   type (Incident/Request/Problem), affected technology, and a priority sanity-check
   against the desk's priority names. If the ticket is unclassifiable (empty body, pure
   noise), stop — dispatch needs a classification.

2. Build the routing matrix. For each candidate from the board's team (minus inactive
   members and stated exclusions), score two signals:
   - Specialty fit: does the tech's stated specialty (from the desk's configured list)
     match the classified technology?
   - Client familiarity: search each candidate's resolved tickets for this client — recent
     closes score higher. If the search caps out, report familiarity as "at least N"
     rather than exact.

3. Weigh capacity. Apply the workload formula (base capacity − priority-weighted open
   tickets) to the top specialty/familiarity candidates, so a perfect-fit tech who is
   drowning doesn't automatically win.

4. Decide. Pick the highest combined scorer. If the top two are effectively tied, or no
   candidate has both a plausible fit and capacity, do not guess — leave unassigned and
   post the score table for a human dispatcher.

5. Assign and schedule. Set the owner, then put a work block on their schedule sized to the
   classification (small default block unless the desk configured durations per ticket
   type).

6. Advance the status — only because the assignment succeeded. If the desk uses an
   "Assigned" status for dispatched work, move the ticket to it; if no such status exists,
   leave status alone. Never change priority.

7. Record. Post a plain-text internal note: the classification, the score table (winner,
   runner-up, formula inputs), and the scheduled block. No markdown, no emojis — this note
   may sync to a PSA.

Running as an agent in a Flow (unattended): your entire reply is posted verbatim as the
note — plain text, no narration, no questions. Complete the full path (classify → route →
assign → schedule → status → note) only on a clear winner (single top scorer after
exclusions, confident classification, client rule respected); otherwise make no writes and
post "Smart dispatch: no unambiguous assignment (reason). Left for dispatcher." with the
score table. Advance status only on a successful assignment; on any hand-off, leave status
alone. If the ticket already has an owner or a schedule entry, do nothing and post nothing.

Guardrails: honesty about calendars — this is NOT capacity-calendar-aware (no Planner/
Outlook read on the tool surface); it schedules against Thread schedule entries only. When
exact timing matters, pair with Calendar-Aware Scheduling in attended mode. Show the math
— every assignment carries its score breakdown. Client-specific routing rules beat every
score. Never assign to the requester, an inactive/excluded member, or reassign a ticket
that already has an owner. Per-candidate searches can cap — report familiarity as minimums
when capped. When in doubt, do nothing beyond the diagnostic note. If clients are aligned to
dedicated service pods, use Pod-Based Dispatch to scope the candidate pool to the client's
team before scoring.
```
