---
name: Maintenance Window Notice
description: Draft a planned-work client notice — what's happening, when, expected impact, duration, and rollback promise — for patching, upgrades, or migrations.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Maintenance Window Notice

**When to use:** "Draft the maintenance notice for Saturday's server patching" / "let the client know we're migrating their email this weekend" — any planned change with client-visible impact needs its heads-up.

**Run it:** on one ticket.

## Prompt

```
Draft the advance notice for planned work so clients are informed, not surprised — and nobody
schedules a board meeting inside your maintenance window.

1. Pull the specifics from the ticket or change record: what work, which systems, date, start
   time WITH timezone, expected duration, and expected impact during the window.

2. Draft:
   - What and when: the work in plain terms, date, start-end time with timezone, stated twice
     if the window crosses midnight or a weekend.
   - Impact: exactly what will be unavailable, degraded, or unaffected during the window. "No
     impact expected" only when the record supports it.
   - Duration honesty: the window is the outer bound; note service often returns sooner.
   - Rollback promise: if anything doesn't go to plan, work will be rolled back to the current
     state and rescheduled — clients are never left worse than they started.
   - What to do: anything the client should do before/after (save work, reboot, log out), and
     how to reach the desk if something looks wrong after the window.

3. State when they'll hear from us again: confirmation after completion, or an update if the
   window extends.

4. Show me the draft for review, labeled "MAINTENANCE NOTICE DRAFT." Sending and choosing the
   audience is the technician's action.

Times come from the scheduled record, never assumed — always carry the timezone; multi-region
clients get an explicit zone label. Never promise "no downtime" unless the change record says
so; "brief interruptions possible" is the honest default. The rollback promise must reflect an
actual rollback plan — if the record shows none, flag that instead of promising one. Fill every
placeholder before presenting, or flag unfilled ones at the top ("NEEDS: exact window").
```
