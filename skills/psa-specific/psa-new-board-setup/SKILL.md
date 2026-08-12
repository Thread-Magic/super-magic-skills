---
name: PSA New Board Setup
description: New PSA board or queue setup checklist: statuses, ticket types, SLA mapping, and Thread View plus Flow implications so it syncs cleanly from day one.
category: PSA-Specific
tools: [list_boards, list_ticket_statuses, list_ticket_priorities, list_flows, create_flow]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# PSA New Board Setup

**When to use:** "We're adding a new board/queue — help me design it", planning a VIP / project / after-hours / new-client-tier board before creating it in the PSA, or reviewing a proposed board layout for gaps before it goes live.

**Run it:** across the whole desk as a design task (run manually before the board is created in the PSA).

## Prompt

```
You are running the design checklist for a new board/queue on a PSA-synced desk (ConnectWise
Manage, Autotask, HaloPSA). Standing up a new board is a DESIGN task, not a data task — and it's
usually done in the PSA, then mirrored into Thread. Get the status list, types, SLA mapping, and
downstream Thread implications right up front, or the board ships with statuses that don't map,
Views that don't filter, and Flows that fire on the wrong board. Work the checklist, capturing
decisions as you go; this produces a design spec a human enacts in the PSA (and, where noted, in
Thread).

1. Purpose & population. State what the board is for in one line and what tickets belong on it
   (which clients, work types, or trigger). A board without a crisp population rule becomes a
   dumping ground. Decide whether tickets are routed here manually or by a Flow condition.

2. Statuses. Design the status list as a workflow, not a pile: an entry status, the in-progress
   states, the waiting/hold states (which stop the SLA clock), and the closed-family states. Note
   per-status side effects the PSA will attach (notifications, SLA pause, closed-family). Statuses
   are per-board in CW/Halo — this list is specific to this board. Cross-check the closed-family
   design against the closed-status taxonomy.

3. Types / subtypes / items. Decide the type taxonomy for the board and keep it minimal and non-
   overlapping — reuse the desk's existing taxonomy where it fits rather than inventing parallel
   values. Every added value is future cleanup debt.

4. SLA mapping. Map each priority (from the tenant's priority list) to the board's
   response/resolution targets, and confirm which statuses pause the clock (from step 2). State
   the business hours/calendar the SLA runs against. An SLA with no defined pause states or
   calendar will misfire.

5. Agreement & billing implications. Note how tickets on this board bill — default agreement,
   whether work is billable, and how it feeds month-end. A board whose billing attributes are
   undefined creates invoice anomalies later.

6. Thread View implications. Specify the Views the desk needs for this board (queue view, waiting-
   on-customer, breaching-SLA) so the board is workable in Thread the day it appears. Views are
   built in-app; this step defines which Views, not how to create them.

7. Flow implications. Determine what should fire on this board and whether Flows can express it.
   Flows are ticket-event triggered against conditions (board, status, priority, type, etc.) —
   they are NOT scheduled and CANNOT trigger on ticket age / time-in-status / elapsed time. So
   "route incoming to this board", "set priority on entry", or "run a skill when status enters X"
   are valid Flow designs; "escalate after N hours idle" is not (that's a manual sweep). Check
   existing Flows for overlap before proposing new ones; only create a Flow after the design is
   confirmed.

8. Output a plain-text board design spec organized by the sections above, with a clear split
   between PSA-side actions (create the board, statuses, types, SLAs — human work in the PSA, the
   master system) and Thread-side actions (Views to build, Flows to create). End with an ordered
   enactment sequence and what to verify after the board syncs into Thread.

Always: design output, not silent creation — default to producing the spec; do not create Flows or
other Thread objects until the design is confirmed, and never create anything on the PSA side. The
PSA is master — the board is authored in the PSA and syncs to Thread. Don't over-promise Flows —
only propose Flow behavior that fits real conditions and actions (no scheduled/age-based triggers;
a flow's native actions are limited, so email/ticket-create/time-log only happen when a flow calls
Run Skill / New Super Magic Agent); state the limit rather than designing a Flow that can't exist.
Validate every referenced status/priority against the board's live status/priority lists once it
exists. Keep the type taxonomy minimal — flag when a proposed value duplicates an existing one.
Plain-text spec; no markdown/emojis in anything destined for a PSA note.
```
