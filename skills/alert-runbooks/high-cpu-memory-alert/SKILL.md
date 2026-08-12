---
name: High CPU/Memory Alert
description: Triage a CPU or memory threshold alert — separate a transient spike from sustained pressure via history, and route servers versus workstations differently.
category: Alert Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, list_ninjaone_alerts, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# High CPU/Memory Alert

**When to use:** A "CPU above X%" or "memory above X%" alert opens a ticket; or a tech asks "<device> keeps alerting on performance — real or noise?"

**Run it:** on the alert ticket · or as a Flow that fires on the performance-threshold alert ticket event.

## Prompt

```
You are triaging a CPU/memory alert. A CPU pegged for 90 seconds during an AV scan and a server
at 95% for six hours produce the same alert — separate spike from sustained, name likely consumers
as hypotheses, and route servers and workstations down their different paths. Leave a plain-text
note only; change nothing else. Never reboot or kill anything — this is a triage layer.

1. Parse the alert: device, metric (CPU vs memory — different playbooks), threshold, observed
   value, sample duration if stated. A 5-second sample means almost nothing; a 15-minute average
   means a lot.
2. Dedupe/recurrence: search recent tickets and the device's RMM alert history for the same
   device + same metric, 30 days. The alert history IS the spike-vs-sustained instrument — one
   alert with recovery = spike; alerts recurring daily at the same hour = scheduled-workload
   pattern (backup, scan, report job); continuous or escalating = sustained pressure.
3. Verify current state by looking up the device in the RMM: current utilization, uptime, device
   class. Long uptime plus creeping memory alerts suggests a leak pattern.
4. Correlate the device's recent RMM activity with the alert timestamps: patch installs, AV scans,
   backup jobs, update downloads are classic benign spikes; a new app install just before pressure
   began is a prime suspect.
5. Offer top-consumer hypotheses by role, LABELLED as hypotheses (the RMM does not show live
   per-process data): workstations — browser tab sprawl, AV scan, sync clients, video calls,
   runaway update; servers — database growth, IIS/app-pool leak, backup/dedup jobs, terminal-server
   user load, runaway logging.
6. Split by device class: workstation — sustained pressure usually means a reboot cures it or the
   hardware is undersized; route needs-tech with hypotheses, and if the user reports slowness merge
   that ticket with this alert. Server — never suggest a casual reboot; sustained pressure is a
   capacity or workload-fault investigation and any restart goes through a maintenance window;
   multiple users affected, weight urgency accordingly.
7. Classify: self-healed (spike recovered, no recurrence) → close with the recovery evidence;
   needs-tech (sustained, or recurring outside a benign scheduled-job correlation) → route with
   hypotheses and the RMM deep link to the device; needs-client (client-owned workload) → account
   owner; noise (threshold too tight for the device's normal duty cycle) → recommend
   threshold/schedule tuning, do not just close. Leave a plain-text note: metric, spike-vs-sustained
   verdict with the alert-history evidence, hypotheses, path, route.

Guardrails: consumer lists are hypotheses, not observations — say so. A daily-recurring alert
correlated to a scheduled job is tuning noise, but confirm the job exists in activities before
calling it that. Recurring sustained pressure is a capacity problem — do not present the third "it
recovered" as resolution. If NinjaOne is not enabled, degrade to alert text + ticket history and
say the live view is unavailable. Plain-text notes only.

If run unattended via a Flow: your entire reply is posted verbatim as the note — plain text, no
narration. Close ONLY when current utilization is back under threshold AND this is the first such
alert on the device in 30 days. Recurrence 2+ correlated to the same scheduled window → route as
threshold-tuning with the pattern stated. Sustained now (still above threshold) on a server →
escalate; on a workstation → tech queue. Never close a server alert on recovery alone if recurrence
≥2. Unverifiable current state → route to a human; never close.
```
