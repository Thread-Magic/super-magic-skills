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
You are running the design checklist for a new board or queue on a PSA-synced desk
(ConnectWise, Autotask, HaloPSA). This is a design task: the board is built in the PSA and
mirrored into Thread, so your output is a spec a human enacts — never create anything
PSA-side, and create nothing Thread-side until the design is confirmed.

1. Purpose and population. One line on what the board is for, and the rule for what belongs
   on it — which clients, work types, or trigger. Without one it becomes a dumping ground.
   Decide whether tickets land here manually or by a Flow condition.

2. Statuses. Design the list as a workflow: an entry status, in-progress states, waiting and
   hold states that stop the SLA clock, and the closed-family states. Record the
   side effects the PSA attaches to each (notifications, SLA pause, closed-family). Statuses
   are per-board on ConnectWise and HaloPSA, so this list is specific to this board.
   Cross-check the closed family against the desk's closed-status taxonomy.

3. Types and subtypes. Keep the taxonomy minimal and non-overlapping, reusing the
   desk's existing values wherever they fit — every new value is future cleanup debt, so flag
   any proposal that duplicates an existing value.

4. SLA mapping. Map each priority on the tenant's priority list to the board's response and
   resolution targets, name the business-hours calendar the SLA runs against, and confirm
   which statuses from step 2 pause the clock. An SLA with no pause states or calendar
   misfires.

5. Agreement and billing. State the default agreement, whether work here is billable, and
   how it feeds month-end. Undefined billing attributes become invoice anomalies later.

6. Views. Name the Thread Views the desk needs on day one — queue, waiting-on-customer,
   breaching. Views are built in-app; this step decides which, not how.

7. Flows. Flows are triggered by ticket events against conditions (board, status, priority,
   type). They are NOT scheduled and CANNOT trigger on ticket age or time in status, so "route
   incoming here" and "run a skill when status enters X" are valid designs and "escalate after
   4 hours idle" is not — that stays a manual sweep. A Flow's own actions are limited; email,
   ticket creation and time logging only happen when it calls Run Skill or New Super Magic
   Agent. Check existing Flows for overlap, and state the limit rather than designing a Flow
   that cannot exist.

8. Output a plain-text spec in these sections, splitting PSA-side actions (board, statuses,
   types, SLAs — human work in the master system) from Thread-side actions (Views, Flows).
   End with the enactment order and what to verify once the board syncs into Thread.

Validate every status and priority you name against the board's live lists once it exists.
The spec is plain text — no markdown or emojis (apply the PSA Note Discipline skill).
```
