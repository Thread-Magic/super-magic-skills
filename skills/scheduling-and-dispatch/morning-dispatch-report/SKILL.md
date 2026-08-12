---
name: Morning Dispatch Report
description: The dispatcher's start-of-day briefing: overnight arrivals, P1/P2 status, unassigned aging, today's scheduled work, and a top-10 priority work list.
category: Scheduling & Dispatch
tools: [search_tickets, list_boards, list_ticket_priorities, search_members]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Morning Dispatch Report

**When to use:** "Morning dispatch report" / "what came in overnight?"; a lead standing in for the dispatcher needs the start-of-day picture.

**Run it:** across the desk's boards at start of day — a manual sweep (Flows can't time-trigger it; use an external scheduler if you want it automated).

## Prompt

```
You are producing the dispatcher's start-of-day briefing in one skimmable, read-only
report: what came in overnight, what's urgent, what's aging, what's already booked, and
the ten things to attack first.

1. Look up the boards and priority names. Define "overnight" as close of business
   yesterday to now, in the desk's timezone (use the desk's stated hours; default
   6pm–now).

2. Overnight arrivals. New tickets created in the window, per board (one search per board
   — result caps apply). Group by priority, then client; call out clusters (several
   tickets from one client or alert source usually mean one incident).

3. P1/P2 status. All open Critical and High tickets regardless of age: assignee, last
   activity, whether the last word is the client's. Unassigned P1/P2s at the very top.

4. Unassigned aging. Open unassigned tickets by age bucket (<4h / 4–24h / >24h), flagging
   anything past the desk's thresholds.

5. Today's schedule. Scheduled entries for today by technician — onsites, booked sessions,
   blocks — so the dispatcher knows what capacity is already spoken for.

6. Top-10 priority work list. Rank open work by priority, age, client-response-waiting,
   and SLA pressure where visible; list the top 10 with a one-line "why it's here" each.

7. Output in that order with a two-line headline on top ("9 overnight, 1 Critical
   unassigned, 3 onsites today"). Compact tables, skimmable in under a minute.

This is a cadence/sweep report. Thread Flows fire on ticket EVENTS only — no schedule,
cron, or ticket-age trigger — so this cannot run "every morning" from a Flow; run it
manually or from an external scheduler. If invoked unattended (e.g. an external scheduler
posting the report), your entire reply is the report: no narration, no questions, fixed
section order and format every run, the date and overnight window included, plain text if
the destination is a PSA-synced note. If a data pull fails or returns nothing, include the
section with "no data / lookup failed" rather than omitting it. Take no assignment actions
from this run.

Guardrails: read-only — report and recommend, never assign or modify tickets. Result-cap
honesty: label any possibly-capped section's counts as "at least N". Aggregate, don't
editorialize about people — this is a queue report, not a performance report. Cite real
ticket numbers only; never fabricate tickets, counts, or SLA states. If the overnight
window or business hours are unstated and it matters, use the defaults and say which.
```
