---
name: CW Project Tickets
description: Recognize ConnectWise Manage project tickets, understand the project → phase → ticket structure, and work within what Thread sees of the Projects module.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# CW Project Tickets

**When to use:** A ticket on a CW-synced desk smells like project work (install, migration, rollout, multi-visit onsite), a ticket number behaves oddly (statuses that don't match the service board), or a service-desk sweep is about to touch tickets on a project board.

**Run it:** on one ticket · or across all tickets a service-desk sweep is about to touch.

## Prompt

```
You are handling a possible project ticket on a ConnectWise desk. ConnectWise splits work
between the Service module and the Projects module (projects → phases → project tickets).
Project tickets look alike but behave differently: they carry project and phase membership,
roll time up to project budgets, and service-desk conventions — SLA clocks, triage, closure
QA — mostly don't apply.

1. Re-read the ticket at full detail and check its board against the board list. If the desk
   designates it a project board, say so first: service-desk rules stop applying. Where the
   list doesn't distinguish, use the desk's board map; with no map, ask rather than classify
   from the title.

2. Recognition signals, evidence not proof — confirm each: work quoted or sold rather than
   reported, a phase or project reference in the fields or notes, planned multi-visit
   scheduling, budget-hours language. Scope creep past the desk's project threshold is a
   recommendation to management, not a conversion you perform — converting either direction is
   ConnectWise-side human work.

3. Project boards carry their own status workflows: pull that board's status list
   specifically, never reusing service-board statuses. A closed-family status on a project
   ticket can mark a phase deliverable complete, so confirm before any closed-family move.

4. Thread's visibility varies by tenant: phase structure, project budget, remaining budget
   hours and overall project status are generally NOT visible even when project tickets sync.
   Never state budget burn or phase progress you cannot see; report "project-level data not
   visible from Thread — check the ConnectWise Projects module."

5. Time on project tickets burns project budget, and misrouted time distorts both service
   metrics and project profitability. Log per the desk's convention, usually where the work
   order lives.

6. Sweep protection: exclude project boards from bulk audits and closure sweeps unless asked
   otherwise, and say so. Project tickets legitimately idle between scheduled
   visits, so auto-closing one that "looks stale" is a classic false positive. Report capped
   counts as "at least N" (apply the Sweep Honesty skill).

7. Output the classification and its evidence, which conventions apply, any proposed action
   and its side effects, and what wasn't visible from Thread.

ConnectWise is master; on drift, Thread moves. Never reopen or restructure a project ticket
from Thread to match a Thread-side impression — these get updated ConnectWise-side during
onsite visits with no Thread activity. Never invent project or phase names, budget
figures or board designations. Record what you did in a note — plain text, no markdown or
emojis (apply the PSA Note Discipline skill). If this tenant doesn't sync project tickets at
all, run advisory-only: name the work as likely project-side and hand off.
```
