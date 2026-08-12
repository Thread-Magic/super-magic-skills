---
name: Autotask SLA Workflow
description: Autotask SLA event model — First Response, Resolution Plan, Resolved — with clock-pausing statuses and breach-risk assessment for synced desks.
category: PSA-Specific
tools: [search_tickets, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Autotask SLA Workflow

**When to use:** "Is this ticket going to breach?" on an Autotask desk, deciding whether moving a ticket to a waiting status actually stops the SLA clock, or explaining why a ticket breached despite "being responded to".

**Run it:** on one ticket · across all at-risk tickets on a board · or as a Flow (triggered on status change, to verify a waiting status actually paused the clock).

## Prompt

```
You are assessing SLA state on an Autotask desk. Autotask SLAs are event-based: each ticket
tracks separate targets for First Response, Resolution Plan, and Resolved, and only specific
configured "waiting" statuses pause the clock. Misreading which event is at risk — or assuming
a status pauses the clock when it doesn't — produces false confidence and real breaches.

1. Re-read the ticket at full detail. SLA state read from a stale listing is worthless — a
   first response may have landed in Autotask minutes ago.

2. Identify which SLA event is live: First Response not yet met → the response clock runs;
   response met but no plan → Resolution Plan clock; plan met → Resolved clock. Each has its
   own target; report the event, not just "the SLA".

3. Check what satisfies each event on this desk. In Autotask these are configured per SLA, but
   the common pattern: First Response = a status change or outbound reply by a resource;
   Resolution Plan = a documented plan; Resolved = ticket completed. A silent internal note
   usually satisfies nothing — say so if a tech believes otherwise.

4. Check pause state: only the desk's configured waiting statuses (typically Waiting Customer,
   Waiting Vendor, and similar) pause the clock, and only for the events configured to pause.
   "In Progress with a note saying waiting on client" pauses nothing — the status itself must
   be set. Verify status names against the desk's live status list; never assume a status
   pauses by its name alone.

5. Assess risk: time remaining on the live event vs the desk's working hours (Autotask SLAs
   usually count business hours — flag if you cannot confirm the coverage calendar). Tier the
   breach risk.

6. Output: live SLA event, met/unmet events with timestamps where visible, pause state, breach
   risk tier, and the single action that satisfies the live event. Change status only after
   confirmation, with a plain-text note when the change is clock-affecting.

Always: re-read before reporting breach risk or changing a clock-affecting status; an Autotask-
side reply or status change may not have synced yet. Never declare a breach from Thread data
alone — recommend confirming in Autotask for anything contractual. Never park a ticket in a
waiting status to stop the clock without a genuine wait reason and a note stating what is being
waited on — clock-gaming is an audit finding, not a technique. Do not assert pause behavior for
a status you have not verified for this desk. Business-hours math: if you cannot see the
coverage calendar, give the deadline as configured-hours-unknown and say so. Do not invent SLA
targets; if the ticket shows no SLA data, report "no SLA visible", not "no SLA".
```
