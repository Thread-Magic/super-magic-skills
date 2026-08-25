---
name: RAID Degradation Alert
description: Triage a RAID degraded or failed-member alert with zero-margin urgency — one failure from data loss — and enforce the verify-backups-BEFORE-rebuild rule.
category: Alert Runbooks
tools: [search_tickets, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, liongard_metric, liongard_launchpoint, search_itglue, add_ticket_note, update_ticket]
connectors: [NinjaOne, Liongard, IT Glue]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# RAID Degradation Alert

**When to use:** An "array degraded / disk failed in array / RAID rebuild started" alert fires from a server, NAS, or storage controller; or a tech asks "how urgent is this degraded-array ticket really?"

**Run it:** on the alert ticket · or as a Flow that fires on the RAID/array alert ticket event.

## Prompt

```
Triage a RAID degradation alert with zero-margin urgency. A degraded array still serves data, so
these get parked — but redundancy is spent, and the next failure, including one the rebuild
triggers, is data loss.

1. Parse the alert: device, array id, RAID level, which member failed, whether a rebuild is
   running. RAID level sets the margin — RAID 5 degraded has zero redundancy left, RAID 6 or a
   mirrored pair with one loss may retain one. State which, or "level unknown".

2. Check recurrence and current state. Search this device's array alerts over 90 days: a second
   member failure or repeated degradation on the same chassis is an aging-batch signal, so treat
   the remaining members as suspect. Read device health and related RMM alerts for SMART or
   predictive-failure warnings on other members — one on a second member during degradation is an
   emergency. Where a Liongard inspector covers the storage platform, read array state and
   rebuild progress there and give the dataprint age. Sweep Honesty base skill: say "at least N"
   if a search may have capped.

3. THE RULE — backups before rebuild. Establish the last known good backup of the data on this
   array, from the client's documentation and job evidence, before recommending replacement or
   rebuild; rebuild stress is a classic second-failure trigger. Backups current, go to
   replacement urgency. Stale or unknown, the FIRST action is a fresh copy of critical data, and
   the note says so in that order.

4. Classify. Self-healed means the rebuild completed AND the array reports optimal in fresh data
   — close on that evidence. Degraded, rebuilding, or ambiguous is needs-tech, act-now: a running
   rebuild is not resolution, rebuilds fail. Replacement is physical work with a procurement step
   (drive model and size from the documentation); a hot spare changes the timeline.

5. Leave a note — plain text, no markdown or emojis (PSA Note Discipline base skill): array
   state, RAID level and remaining margin, batch signal, ordered actions, and the mandatory
   exposure statement — last known good backup for this array, or an explicit "unknown, treat as
   unprotected". Don't clear the RAID alert; it is the evidence trail.

A degraded array is never noise, never client-only, never closed on assumption. RMM visibility
into RAID controllers is shallow — per the Connector Degradation base skill, say the view is
partial and name the controller or NAS console to check.

As a Flow: your entire reply is the note, exposure statement included. The only close is verified
array-optimal in fresh data after a completed rebuild with no other member alerts. Everything
else escalates to the urgent hardware queue, priority raised when backups are stale or unknown, a
second member shows SMART warnings, or the RAID level leaves zero redundancy. Any ambiguity
escalates — never close, never downgrade.
```
