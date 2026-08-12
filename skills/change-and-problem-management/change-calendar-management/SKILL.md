---
name: Change Calendar Management
description: Check a proposed change window against freeze windows, client business calendars, and other scheduled changes on the same systems — catch the collision before the maintenance email goes out, not during the outage.
category: Change & Problem Management
tools: [search_tickets, search_knowledge_base, search_clients, schedule_ticket, update_schedule_entry, add_ticket_note]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Change Calendar Management

**When to use:** "Can we do this Saturday night? / find a window for this change" / a change was approved and needs its window placed / a weekly sweep of upcoming scheduled changes for newly-introduced conflicts / two teams independently scheduled work on the same system.

**Run it:** on one change · or as a sweep across upcoming scheduled changes.

## Prompt

```
The change calendar is three overlapping calendars — the MSP's scheduled changes, each
client's freeze windows, and each client's business rhythm. A proposed window has to clear
all three. Run that clearance and schedule (or bounce) the change.

1. Load the change ticket: affected systems, affected clients, proposed window, expected
   duration INCLUDING rollback time. A window that fits the change but not
   change-plus-rollback is not a fitting window.

2. FREEZE CHECK: look up each affected client's freeze calendar (see
   maintenance-freeze-windows). A window inside a freeze is an automatic bounce to the
   requester with the freeze cited — the exception path lives in maintenance-freeze-windows,
   not here.

3. BUSINESS-CALENDAR CHECK: compare the window against the client's documented operating
   hours and known busy periods (month-end close, seasonal peaks, published events).
   "Saturday night" is not universally safe — some clients run weekends. If operating hours
   aren't documented, say so and ask rather than assuming 9-to-5.

4. COLLISION CHECK: search for other approved or scheduled changes overlapping the
   window on the same systems, the same client, or shared infrastructure in the dependency
   path. Flag both hard collisions (same system, overlapping window) and soft ones (same
   client hit by two unrelated maintenances in one week — reads as instability to the
   client even when each change is fine).

5. Render a verdict: CLEAR (all three checks pass), CONFLICT (cite each conflict
   specifically), or INSUFFICIENT (missing duration, undocumented client hours — list
   what's needed).

6. On CLEAR and with the requester's confirmation, place the window on the calendar (or move the existing entry when relocating one), and post a plain-text note recording
   the checks performed and their outcomes — the clearance is audit trail, not just a green
   light.

7. On CONFLICT, propose up to two alternative windows that clear all three calendars, but
   only propose — moving another team's scheduled change is a human conversation, never a
   silent reschedule.

8. Remind the requester of the client-notice obligation for user-visible windows.

Guardrails: never silently reschedule anything — conflicts are surfaced to humans with
options, and the requester confirms before any schedule write. A freeze window always wins
over convenience; only the documented exception path overrides it. Check shared-
infrastructure dependencies, not just the named system — two changes to "different servers"
on the same host or uplink are a collision. Scheduling is not approval: a change on the
calendar without its approval recorded gets flagged, not executed. Result-cap honesty: if
the collision search may have hit a cap, say the sweep is partial rather than declaring the
calendar clear.
```
