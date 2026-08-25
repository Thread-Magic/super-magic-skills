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
Triage a CPU or memory alert. A 90-second CPU peg during an AV scan and a server at 95% for six
hours look identical here. Never reboot or kill anything — this is triage.

1. Parse the alert: device, metric (CPU and memory are different playbooks), threshold, observed
   value, sample duration. A 5-second sample means almost nothing; a 15-minute average means a
   lot.

2. The device's RMM alert history over 30 days is the spike-versus-sustained instrument; read it
   with recent tickets on the same metric. One alert with a recovery is a spike; alerts recurring
   daily at the same hour are a scheduled-workload pattern (backup, scan, report job); continuous
   or escalating is sustained pressure.

3. Read current utilization, uptime and device class (long uptime with creeping memory alerts
   suggests a leak), and correlate recent RMM activity with the alert timestamps: patch installs,
   AV scans, backup jobs and update downloads are benign spikes; a new app installed just before
   the pressure began is a prime suspect.

4. Offer top-consumer hypotheses, LABELLED as such (the RMM shows no live per-process data).
   Workstations: browser sprawl, AV scan, sync clients, video calls, a runaway update. Servers:
   database growth, an IIS or app-pool leak, backup and dedup jobs, terminal-server user load,
   runaway logging.

5. Classify, then note it — plain text, no markdown or emojis (PSA Note Discipline base skill):
   metric, the verdict and its evidence, hypotheses, route. Self-healed (spike recovered, no
   recurrence): close with that evidence. Needs-tech (sustained, or recurring outside a benign
   scheduled job): route with hypotheses and the RMM deep link — on a workstation a reboot
   usually cures it or the hardware is undersized, so merge in any user slowness ticket; on a
   server never suggest a casual reboot, treat it as a capacity or workload-fault investigation,
   and put any restart in a maintenance window. Needs-client (client-owned workload): account
   owner. Noise (threshold too tight for the duty cycle): recommend threshold or schedule tuning,
   don't just close.

Confirm the scheduled job exists in the activity before calling a recurring alert noise.
Recurring sustained pressure is a capacity problem: don't present the third "it recovered" as
resolution. If the RMM isn't connected, apply the Connector Degradation base skill: fall back to
alert text and ticket history, and say the live view is unavailable.

As a Flow: your entire reply is the note. Close ONLY when utilization is back under threshold AND
it is the device's first such alert in 30 days. Recurrence of 2+ on the same scheduled window:
threshold-tuning, state the pattern. Still above threshold: escalate on a server, tech queue on a
workstation. Never close a server alert on recovery alone once recurrence reaches 2. Unverifiable
state: route to a human, never close.
```
