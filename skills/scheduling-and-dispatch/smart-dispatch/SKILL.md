---
name: Smart Dispatch
description: Composite dispatcher skill: classify a new ticket, consult a routing matrix of tech specialties and client familiarity, then assign and schedule.
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
Do end-to-end dispatch in one pass: classify the ticket, score candidates against a routing
matrix, assign the winner, schedule the work, and write the reasoning down.

1. Classify from the summary and description: type (Incident/Request/Problem), affected
   technology, and a priority sanity-check against the desk's priority names. If it is
   unclassifiable (empty body, noise), stop — dispatch needs a classification.

2. Build the routing matrix. For each candidate on the board's team, minus inactive and excluded
   members, score specialty fit (does their stated specialty match the classified technology?)
   and client familiarity (their resolved tickets for this client, recent closes scoring higher).
   If that search caps out, report familiarity as "at least N" rather than exact.

3. Weigh capacity across the top candidates with the workload formula: base capacity minus
   priority-weighted open tickets, so a perfect-fit tech who is drowning doesn't win.

4. Pick the highest combined scorer. If the top two are effectively tied, or no candidate has
   both a plausible fit and capacity, leave the ticket unassigned and post the score table for a
   dispatcher.

5. Set the owner, then put a work block on their schedule sized to the classification — a small
   default unless the desk configured per-type durations.

6. Advance the status only because the assignment succeeded: if the desk uses an "Assigned"
   status, move it there; otherwise leave status alone. Never change priority.

7. Post a plain-text internal note — no markdown or emojis, it may sync to a PSA — with the
   classification, the score table (winner, runner-up, formula inputs), and the scheduled block.

Guardrails: show the math — every assignment carries its score breakdown. Client-specific routing
rules beat every score. Never assign to the requester, an inactive or excluded member, or
reassign a ticket that already has an owner. When in doubt, do nothing beyond the diagnostic
note. This reads Thread schedule entries only — not Planner or Outlook — so pair it with
Calendar-Aware Scheduling in attended mode when exact timing matters. If clients are aligned to
service pods, use Pod-Based Dispatch to scope candidates to the client's team first. If the desk
runs tiers rather than specialty scoring, use Tier Dispatcher — a fixed per-tier pool, checked
against today's schedule before booking.

As a Flow (unattended): your entire reply is posted verbatim as the note — plain text, no
narration, no questions. Complete the full path only on a clear winner: one top scorer after
exclusions, a confident classification, client rules respected. Otherwise make no writes and post
"Smart dispatch: no unambiguous assignment (reason). Left for dispatcher." with the score table.
On any hand-off, leave status alone. If the ticket already has an owner or a schedule entry, do
nothing and post nothing.
```
