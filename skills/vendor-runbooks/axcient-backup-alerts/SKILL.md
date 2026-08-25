---
name: Axcient Backup Alerts
description: Triage Axcient x360Recover alerts: distinguish appliance vs Direct-to-Cloud failure families, verify retention, and state the last recoverable point.
category: Vendor Runbooks
tools: [search_tickets, search_itglue, get_ninjaone_device, get_ninjaone_device_activities, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Always-On Coverage, Risk & Compliance]
---

# Axcient Backup Alerts

**When to use:** An x360Recover backup failure, health, or replication alert lands as a ticket; a D2C-protected laptop/server shows stale backups; or someone asks whether retention/rollup is actually keeping the points the client's design promises.

**Run it:** on the alert ticket · or as a Flow (triggered when a matching Axcient backup alert ticket is created).

## Prompt

```
Triage an Axcient x360Recover alert — the vendor specialization of backup-failure-triage,
which owns the classify-recur-decide loop. Portal checks, verifications and reinstalls are
technician actions you direct and record; verify product specifics against Axcient's docs.

1. Identify the protection model first: appliance-based (local appliance plus cloud
   replication, two failure surfaces) or Direct-to-Cloud (agent straight to Axcient's cloud,
   one surface, wholly dependent on the endpoint's connectivity and change rate). "The
   appliance is fine" is meaningless for D2C.

2. Appliance-based families. Local job failures classify per backup-failure-triage (VSS or
   snapshot errors, credentials, storage pressure, agent versions); read the machine's live
   state and recent activity in the RMM. Replication lag → quantify how far cloud is behind
   and classify the cause (bandwidth, change rate, appliance health); persistent growth is a
   design problem ticket. Appliance health alerts are urgent capacity work: it is the single
   point for local recovery, and never "fixed" by deleting recovery points.

3. Direct-to-Cloud families. Stale or missing backups are endpoint-side first: offline or
   off-network for the window (check last-seen in the RMM — a roaming laptop is the classic
   benign cause, but verify it), agent service stopped, bandwidth caps. A server on D2C that
   lags is an incident. Repeated agent errors point at agent version or health. Wholesale
   failures across many D2C endpoints suggest a service-side incident — check Axcient's
   status channels before burning hours endpoint by endpoint.

4. Verify retention against the client's documented design. Spot-check the oldest expected
   point: a design promising a year with an oldest recoverable point of 60 days is a silent
   failure, however green the daily jobs look. Retention shortfalls are contract findings —
   flag them to service leadership with dates. Never adjust retention or delete points from
   a triage seat.

5. End every note with the exposure statement: the last recoverable point (local and cloud
   for appliance sites) and whether it is verified — AutoVerify or boot-check where
   available; unverified is stated as unverified. Note recurrence per backup-failure-triage:
   same system and class over 30-90 days, the third a problem ticket, never a one-off close.
   Never claim data is safe or that a restore will work; alerts stay as the evidence trail.
   Plain text, no markdown or emojis (apply the PSA Note Discipline base skill). As a Flow,
   apply that classification, exposure statement and priority directly.

6. Handle here or escalate per backup-failure-triage; the Axcient support package is
   protection model, agent and appliance versions, exact error text, job history, what was
   ruled out. When in doubt do nothing irreversible and escalate.
```
