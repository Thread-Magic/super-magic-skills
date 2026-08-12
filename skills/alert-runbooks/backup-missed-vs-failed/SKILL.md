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
You are triaging a backup alert. "Backup did not complete" hides two different problems: a job
that never STARTED (scheduling/availability — device off, service down, window skipped) and a
job that started and DIED (an error with a taxonomy). Make the missed-vs-failed call first,
because everything downstream depends on it, and always end with an exposure statement. Leave a
plain-text note only; change nothing else. Do not clear backup alerts — they are the evidence trail.

1. Parse the alert: device/job name, scheduled window, whether it carries an error code (errors
   imply the job ran) or only an overdue/missed condition (implies it never started), and the
   product raising it.
2. Make the call explicit: FAILED = job executed and returned an error → there is an error to
   classify; hand the taxonomy work to a backup-failure triage. MISSED = no execution in the
   window → the diagnosis is why it never started. Do not treat an overdue alert as a failure.
3. Dedupe/recurrence: search recent tickets for the same device/job, 30 days. Chronic misses
   (device off every night, laptop never on the schedule) are a schedule-design problem; chronic
   failures are a product problem. State which pattern this is.
4. Verify why a missed job missed: look up the device (was it online during the window?), read
   its recent RMM activity (asleep, rebooting, mid-patch?), and check related RMM alerts (backup
   service stopped?). A laptop in a bag at 2 a.m. is a schedule problem, not an incident.
5. Where the backup platform has a Liongard inspector, read job history from the inspector's
   data (verify the inspector last ran and state its dataprint age) to confirm the last
   successful run and whether a later run has since succeeded. Cross-check the documentation in
   IT Glue for the intended schedule and retention design.
6. Classify: self-healed (a subsequent run of the same job completed) → close citing that run;
   needs-tech (failed jobs → route to backup-failure triage; backup service down; missed window
   on an always-on server); needs-client (device-availability misses on client-controlled
   machines) → availability/schedule conversation; noise (one-time miss in a documented
   maintenance window with a clean run after).
7. Exposure statement — MANDATORY in every output regardless of class: "Last known good backup
   for <device/job>: <date/time>. Data changed since then is unprotected." If last-known-good
   cannot be established, say exactly that — it makes the ticket more urgent, not less. Leave a
   plain-text note.

Guardrails: the exposure statement is non-negotiable — no output omits last-known-good or an
explicit "unknown". Never say data is safe or a restore will work — report job evidence only;
restore verification is a human task. Never close a missed alert because the device "was probably
off" — verify device state in the window or route to a human. A recurring miss is a design
problem; do not close the third one as a one-off. If neither the RMM nor a Liongard inspector can
see the backup platform, say the view is partial and name what to check in the backup console.
Plain-text notes only.

If run unattended via a Flow: your entire reply is posted verbatim as the note — plain text, no
narration — and it MUST contain the exposure statement. Close ONLY when a subsequent successful
run of the same job is evidenced AND recurrence is under 3 in 30 days. Failed (error present) →
route to the backup-triage queue. Missed with device offline in window → route as
availability/schedule issue. Missed with device online → escalate (service or product fault).
Last-known-good unknown, stale dataprint, or capped search → route to a human; never close.
```
