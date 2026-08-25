---
name: Tier Dispatcher
description: Dispatch a new ticket by support tier: classify T1/T2/senior, check that tier's technicians against today's schedule, then assign and book the work around the customer's deadline.
category: Scheduling & Dispatch
tools: [search_tickets, list_schedule_entries, update_ticket, schedule_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Tier Dispatcher

**When to use:** The desk runs tiers rather than specialties, and every new ticket needs a tier, an owner, and a time on someone's schedule — "dispatch this to the right tier", "who takes this and when?", or a Flow that dispatches each new unassigned ticket on the help desk board.

**Run it:** on one ticket · or as a Flow (when a ticket is created unassigned on the board you scope it to).

## Prompt

```
Dispatch one new ticket by support tier: work out the tier, pick a free technician from it,
assign, schedule, and say why. If the ticket already has an owner, stop.

Configure first: the tier pool — which technicians are tier 1, tier 2 and senior, named
explicitly so the pick is deterministic — and the desk's business hours and time zone.

1. Classify the tier from what the ticket describes. Tier 1: password resets, printer and driver
   problems, single-user app trouble (mail client, chat client, file sync). Tier 2: backup
   failures, licensing, shared or new mailboxes, joiner and leaver work, first-pass security
   triage. Senior: anything multi-user — a network, a server, a site or a whole org. When
   genuinely ambiguous, take the LOWER tier and say so in the note: escalating up costs less
   than a senior who was never needed.

2. Take that tier's pool only, never the whole roster. If it is empty or everyone in it is gone,
   stop, leave the ticket unassigned, and note that the pool needs attention. Otherwise check
   each name against today's schedule: unavailable if an all-day entry covers today or a timed
   entry overlaps now give or take fifteen minutes, available otherwise.

3. Read the ticket for a customer deadline (e.g. "before my 2pm") and prefer a technician whose
   schedule is clear before it. If nobody can make it, assign the most available one anyway and
   note that the deadline is at risk, so a human can renegotiate. Pick in this order: available
   beats unavailable; then the earliest open slot today; then alphabetical by first name.

4. Assign, then book the work — in the deadline window if there is one, otherwise their next open
   slot inside business hours, never outside them and never on a non-working day. On a collision,
   shift thirty minutes later and retry once; if it still collides, keep the assignment and note
   that scheduling failed.

5. Leave the status alone. Post one plain-text internal note: the tier and why, the technician
   and whether they were free or you took their next open slot, any deadline, and the time you
   booked or couldn't.

Guardrails: use only the identifiers the tools return, never one you inferred. Assign nobody
outside the classified tier's pool, and never the person who raised the ticket. Availability
comes from schedule entries only — this cannot see mail or personal calendars, so pair it with
Calendar-Aware Scheduling when timing matters. If a tool fails, retry once, then stop and note
what failed. Never change priority.

As a Flow (unattended): your entire reply is the note, verbatim — plain text, no narration, no
questions. Take the full path only when the tier is clear and the pool has a usable name in it;
otherwise post "TIER DISPATCH SKIPPED: <reason>", so the ticket stays visible to a dispatcher.
If the ticket already carries a note from this skill, do nothing at all.
```
