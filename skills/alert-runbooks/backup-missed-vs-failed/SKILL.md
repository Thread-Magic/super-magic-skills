---
name: Backup Missed vs Failed Alert
description: Distinguish a backup that never ran (missed) from one that ran and errored (failed) — two different routes — and always state exposure via last-known-good.
category: Alert Runbooks
tools: [search_tickets, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, liongard_metric, liongard_launchpoint, search_itglue, add_ticket_note, update_ticket]
connectors: [NinjaOne, Liongard, IT Glue]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# Backup Missed vs Failed Alert

**When to use:** A backup alert reads "missed", "did not run", "overdue", or is ambiguous between missed and failed; or a tech asks "did last night's backup for <client> actually run?"

**Run it:** on the alert ticket · or as a Flow that fires on the backup alert ticket event.

## Prompt

```
Triage a backup alert. "Backup did not complete" hides two problems: a job that never STARTED
(scheduling or availability) and one that started and DIED with an error. Make that call first.

1. Parse the alert and make the call: device or job name, scheduled window, product. An error
   code means the job ran — FAILED, so hand the error taxonomy to a backup-failure triage. An
   overdue or missed condition with no error means it never started — MISSED, and the diagnosis
   is why. Never treat an overdue alert as a failure.

2. Check recurrence over 30 days for the same device or job. Chronic misses (device off every
   night, a laptop never on the schedule) are a schedule-design problem; chronic failures are a
   product problem. State which. Sweep Honesty base skill: say "at least N" if the search may
   have capped.

3. For a miss, verify why. Was the device online during the window? Read its recent RMM activity
   — asleep, rebooting, mid-patch — and check for a stopped backup service. A laptop in a bag at
   2 a.m. is a schedule problem, not an incident. Where the backup platform has a Liongard
   inspector, read job history there for the last successful run and any later success, and give
   the dataprint age. Check the client's documentation for the intended schedule and retention.

4. Classify. Self-healed: a later run of the same job completed — close citing it. Needs-tech:
   failed jobs, backup service down, or a missed window on an always-on server. Needs-client:
   availability misses on client-controlled machines. Noise: a one-time miss in a documented
   maintenance window with a clean run after.

5. Leave a note — plain text, no markdown or emojis (PSA Note Discipline base skill) — ending
   with the exposure statement, mandatory in every output: "Last known good backup for
   <device/job>: <date/time>. Data changed since then is unprotected." If it can't be
   established, say exactly that; that makes the ticket more urgent. Don't clear backup alerts,
   they are the evidence trail.

Never say data is safe or that a restore will work — report job evidence only; restore
verification is a human task. Never close a miss because the device "was probably off", and don't
close the third recurring miss as a one-off. If neither the RMM nor an inspector sees the backup
platform, apply the Connector Degradation base skill: say the view is partial and name what to
check in the backup console.

As a Flow: your entire reply is the note, exposure statement included. Close ONLY when a later
successful run of the same job is evidenced AND recurrence is under 3 in 30 days. Error present:
route to the backup-triage queue. Missed, device offline in the window: route as availability or
schedule. Missed, device online: escalate — service or product fault. Last-known-good unknown,
stale dataprint, or a capped search: route to a human; never close.
```
