---
name: Disk Space Alert
description: Triage a low-disk-space alert from any monitor — separate threshold noise from real pressure, read growth rate from history, rank consumer hypotheses.
category: Alert Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, list_ninjaone_alerts, get_ninjaone_device_activities, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# Disk Space Alert

**When to use:** A "disk space below X%" alert lands on the intake or alerts board; or the same volume keeps alerting and someone asks "is this real or just the threshold?"

**Run it:** on the alert ticket · or as a Flow that fires on the disk-space alert ticket event.

## Prompt

```
Alert-layer triage for a disk-space alert: threshold artifact, slow creep, or act-now emergency?
Route it with a growth estimate and consumer hypotheses.

1. Parse the alert: device, volume, threshold fired (percent versus absolute GB), current
   reading, timestamp. Percent thresholds on large volumes mislead: 5% of a 4 TB volume is 200 GB
   of headroom, so convert to absolute free space before judging severity.

2. Check recent tickets for this device and volume, 30 days. An open ticket on the same volume
   makes this a duplicate: note it and route there.

3. Read the live volume numbers: the alert is a snapshot, and the disk may have recovered (temp
   files flushed, backup staging cleared) or worsened since. Then read growth from repeated RMM
   alerts on this volume: crossing 85%, then 90%, then 95% across days is a filling trend, so
   compute a rough days-to-full from the alert intervals. A single crossing with recovery is
   churn around the threshold. Correlate with recent RMM activity too: a patch run, backup job or
   app install just before the alert explains a spike; nothing preceding it suggests organic
   growth (logs, profiles, data).

4. Classify, then note it — plain text, no markdown or emojis (PSA Note Discipline base skill):
   verdict, absolute free space now, growth estimate (or "single event, no trend"), hypotheses,
   route. Self-healed (free space back above threshold with margin, no repeat): close as
   recovered. Needs-tech (under threshold now, or a short days-to-full): route with severity — a
   system volume under 5% or 5 GB is act-now — and ranked consumer hypotheses, labelled as
   inferred since the RMM has no per-folder view (workstation: profiles, caches, updates; server:
   logs, backup staging, databases, shadow copies). Needs-client (client-managed share filling
   with business data): capacity conversation, account owner. Noise (threshold misconfigured for
   the volume): recommend a threshold change, don't just close and let it re-fire.

Never close a repeat offender as recovered: three alerts on one volume in 30 days is a capacity
problem whatever the current reading. Don't do the cleanup or recommend deletions here; that is
the remediation skill's job with its safety ordering. If the RMM isn't connected, apply the
Connector Degradation base skill: fall back to alert text and ticket history, and saying the live
view is unavailable.

As a Flow: your entire reply is the note. Close as recovered ONLY when the reading is above
threshold with margin (5 percentage points or 10 GB), there are fewer than 3 alerts on this
volume in 30 days, and no sibling ticket is open. Act-now: escalate to the on-call queue with the
days-to-full estimate. Everything else: tech queue with the classification. If the device is
unreachable or the reading won't pull, route to a human marked "current state unverifiable" —
never close.
```
