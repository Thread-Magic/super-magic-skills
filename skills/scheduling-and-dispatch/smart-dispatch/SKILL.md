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
Do end-to-end dispatch in one pass: classify the ticket, score technicians on specialty, client
familiarity and capacity, assign the winner, and put the work on their schedule — with the
reasoning written down.

1. Classify from the summary and description: type (Incident, Request, Problem), affected
   technology, and a priority sanity-check against the desk's priority names. If it is
   unclassifiable (empty body, pure noise), stop — dispatch needs a classification.

2. Build the routing matrix. For each candidate on the board's team, minus inactive members and
   stated exclusions, score two signals: specialty fit, where the tech's stated specialty matches
   the classified technology; and client familiarity, from their resolved tickets for this
   client, recent closes scoring higher. Sweep Honesty base skill: if a per-candidate search
   caps, report familiarity as "at least N".

3. Weigh capacity on the top candidates with the workload formula — base capacity minus
   priority-weighted open tickets — so a perfect-fit tech who is drowning doesn't win by default.

4. Pick the highest combined scorer. If the top two are effectively tied, or no candidate has
   both a plausible fit and capacity, leave it unassigned and post the score table for a human
   dispatcher.

5. Set the owner, then put a work block on their schedule sized to the classification — a small
   default unless the desk configured durations per ticket type.

6. Advance the status only because the assignment succeeded: if the desk has an "Assigned"
   status, move the ticket to it; if not, leave status alone. Never change priority.

7. Leave an internal note — plain text, no markdown or emojis (PSA Note Discipline base skill):
   classification, score table (winner, runner-up, formula inputs), scheduled block.

Show the math: every assignment carries its score breakdown. Client-specific routing rules beat
every score. Never assign to the requester, to an inactive or excluded member, or reassign a
ticket that already has an owner. Be honest about calendars — this is not
capacity-calendar-aware, with no Planner or Outlook read available, and schedules against Thread
schedule entries only; pair it with Calendar-Aware Scheduling in attended mode when exact timing
matters. Where clients sit in dedicated service pods, use Pod-Based Dispatch to scope the
candidate pool first. When in doubt, do nothing beyond the note.

As a Flow: your entire reply is the note — no narration, no questions. Complete the full path
(classify, route, assign, schedule, status, note) only on a clear winner: a single top scorer
after exclusions, a confident classification, client rules respected. Otherwise make no writes
and post "Smart dispatch: no unambiguous assignment (reason). Left for dispatcher." with the
score table. If the ticket already has an owner or a schedule entry, do nothing and post nothing.
```
