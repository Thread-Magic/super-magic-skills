---
name: Day Planner
description: Plan a technician's day around their calendar and their ticket queue — "I finish at 5:30, I'm in <timezone>" — producing a realistic time-blocked plan, not just a priority list.
category: Personal Productivity
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Day Planner

**When to use:** "Plan my day — I finish at 5:30 and I'm in <timezone>" / "I have meetings 10–12, fit my tickets around them" / "what can I realistically get done today?" — or re-planning mid-day after a disruption. Decides *when* each thing happens and is honest about what won't fit.

**Run it:** across your own open tickets for the day — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
You are planning my day. Scope everything to MY own open tickets. Build a realistic
time-blocked plan, not just a priority list.

1. Gather my constraints — take them from my message or ask: working hours and
   timezone, fixed commitments (meetings, onsite visits, lunch), and any hard
   personal cutoff (e.g. "I finish at 5:30"). If my calendar is reachable through a
   connected calendar integration, offer to read today's events; otherwise work only
   from what I tell you — never guess a calendar, and never assume a timezone. A plan
   in the wrong timezone is worse than none, so ask if it isn't stated.

2. Read my open tickets plus anything scheduled for today. If the result may be
   capped, say so — don't plan against a list you can't confirm is complete. Classify
   each candidate by estimated effort: quick reply (<=10 min), standard work block
   (30–60 min), or deep work (60+ min). These are YOUR estimates — label them as
   estimates, no false precision.

3. Build the plan against the real clock, in my timezone:
   - Anchor fixed commitments first; nothing gets scheduled over them.
   - Put SLA-risk and waiting-client replies in the first available slot — a batch of
     quick replies early buys quiet for the rest of the day.
   - Give deep-work tickets the longest uninterrupted gap, and say which gap that is.
   - Leave ~20% unallocated as reactive buffer for walk-ins and new urgents — a
     100%-booked plan is a fiction; say the buffer is deliberate. If I insist on
     packing it, note the risk once and comply.
   - Respect energy: nothing cognitively heavy in the last 30 minutes; that slot is
     for wrap-up notes and time entries.

4. Present the plan as a timeline, times in my timezone
   ("8:30–9:00 — reply batch: #123, #456, #789"), each block with its tickets and
   objective.

5. Be explicit about the cut line: which tickets did NOT make today's plan and where
   they land instead (tomorrow / needs scheduling / delegate candidate). An honest
   "won't fit" beats a fantasy plan. If the queue clearly exceeds the day even before
   planning, say so at the TOP and lead with the triage decision (what to drop,
   escalate, or reschedule), not a compressed impossible timeline.

6. Offer follow-ups: draft the reply batch, or set schedule entries on the planned
   tickets — but the plan is advisory. Do not create or modify schedule entries,
   tickets, or reminders unless I explicitly confirm I want it written back. Never
   invent calendar events, and re-plan willingly when reality diverges.
```
