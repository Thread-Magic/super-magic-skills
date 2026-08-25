---
name: Veeam Job Failures
description: Diagnose Veeam backup job failures: classify by taxonomy (VSS, credentials, repository, network), apply retry discipline, and state the last restore point.
category: Vendor Runbooks
tools: [search_tickets, search_itglue, get_ninjaone_device, get_ninjaone_device_activities, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Always-On Coverage, Risk & Compliance]
---

# Veeam Job Failures

**When to use:** A Veeam job failure/warning alert lands as a ticket (email notification or RMM-forwarded); "backups failed again on <server>" for a Veeam-protected client; or someone asks what a specific Veeam error class means for the client's exposure.

**Run it:** on the alert ticket · or as a Flow (triggered when a matching Veeam job-failure ticket is created).

## Prompt

```
Triage a Veeam Backup & Replication or Veeam Agent job failure — the vendor specialization
of backup-failure-triage, which owns the classify-recur-decide loop. Console checks, retries
and log exports are technician actions you direct and record. Verify error text against
Veeam's docs; messages shift by version.

1. Read the job report, not the subject: Veeam gives per-object results, so a "Failed" job
   may have succeeded for most objects and a "Warning" may hide a failed one — still a
   failure for that object. Extract the job name, failed objects, error text, and last fully
   successful run.

2. Classify into the Veeam taxonomy:
   - VSS or application-aware errors (writer failures, snapshot timeouts) → guest-OS, not
     Veeam: pending reboots, recent patches, low disk, failing writers (RMM activity around
     job time). Classic after patch night.
   - Credential or authentication failures (guest processing, host connection) → rotated
     service accounts or expired passwords; check prior tickets for rotations.
   - Repository or storage failures (out of space, unavailable, I/O errors) → capacity or
     target health; repeated I/O errors on the repository disk are a data-integrity red
     flag, not a retry case.
   - Network or timeout to a proxy, host or repository → a path problem; did other jobs to
     that target fail?
   - Snapshot-chain or corruption errors ("failed to verify", chain-broken) → stop: they
     threaten restorability of prior points. Escalate, no manual chain surgery, never delete
     restore points to "fix" a job.

3. Retry discipline: one manual retry is legitimate AFTER the classified cause is addressed
   (reboot completed, space freed, credentials fixed) — Veeam's automatic retries have
   usually run, so a blind rerun only eats the backup window. Never loop retries; two
   informed failures of the same class is a problem ticket. Document each retry and result. Check recurrence
   per backup-failure-triage over 30-90 days for the same job and class, and the
   documentation for backup design, retention intent and known issues.

4. End every note with the exposure statement: "Last successful restore point for <object>:
   <date/time>. Recovery exposure is everything since then." If SureBackup or equivalent
   hasn't confirmed restorability recently, say the point is unverified. Never claim data is
   safe or that a restore will work, and never clear alerts as triage. Plain text, no
   markdown or emojis (apply the PSA Note Discipline base skill). As a Flow, apply that note
   and priority directly and flag chain, corruption or repeated failures for a human.

5. Handle here or escalate per backup-failure-triage; the Veeam support package is build
   number, job type, exact error text, per-object results, what was ruled out, and
   technician-exported log excerpts. When in doubt escalate rather than act.
```
