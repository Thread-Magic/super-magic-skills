---
name: Backup Failure Triage
description: Classify a backup failure by alert text and device state, check for recurrence, and decide whether to fix locally or escalate to the backup vendor.
category: Devices & Infrastructure
tools: [list_ninjaone_alerts, get_ninjaone_device, get_ninjaone_device_activities, search_tickets, search_itglue, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Backup Failure Triage

**When to use:** "Backups failed again on <device> — what's going on?" or "have backups for <client> been failing repeatedly?"

**Run it:** on one backup-failure ticket/alert · or as a Flow triggered when a backup-failure alert lands on the ticket.

## Prompt

```
Turn a raw backup-failure alert into a classified failure mode, with a recurrence verdict
and a clear handle-here-or-escalate call.

1. Read the alert text closely — backup products embed the failure reason in it. Resolve the
   source device in the RMM without stopping to ask mid-lookup, then pull its state and
   recent activity. Confirm the class in the device details, not from a filter.

2. Classify the failure mode from the alert text plus device state:
   - Offline or unreachable at job time — scheduling and availability, not backup.
   - Destination full or quota exceeded — capacity; check storage on the device.
   - VSS, snapshot or writer errors — OS-level, usually downstream of a pending reboot or a
     recent patch. Check the activity history.
   - Credential or auth failures — rotated passwords or service-account changes.
   - Network or timeout to target — path and bandwidth; did other devices at the site fail?
   - Agent or version errors — look for a recent agent update in the activity history.

3. Recurrence. Check ticket history for the same device and failure class over the last 30
   to 90 days. One failure with a later success is noise; three of a class is a problem
   ticket. State the verdict, and apply the Sweep Honesty base skill if the search may have
   capped — "at least N", not a bare count.

4. Check the documentation for the client's backup product, retention design, known issues
   and vendor support contacts.

5. Decide the path. Handle here: offline-at-job-time, pending-reboot VSS, obvious
   destination-full — local remediations exist. Escalate to the vendor: repeated same-class
   failures after local remediation, corruption or integrity errors, failures across many
   clients, or anything the vendor's docs mark support-required. Name the vendor from the
   documentation — never guess the product.

6. Output the classification, evidence, recurrence verdict, recommended action, and — the
   number that actually matters — the last known good backup date, which is the client's
   real exposure. Offer to leave it as a note (PSA Note Discipline base skill).

Never state that data is safe or that a restore will work — report the last successful job
on record and nothing more; restore verification is a human task. Don't clear or reset
backup alerts, which are the evidence trail, and never close a recurring failure as a
one-off. Many backup products run their own console and aren't fully visible through the
RMM: say the view is partial and name what to check there.

As a Flow: your entire reply is the triage note — classification, evidence, recurrence
verdict, last known good date, handle-or-escalate. Input is the alert or ticket id. If the
device won't resolve, classify from alert text alone and mark "DEVICE UNRESOLVED - alert-text
classification only"; if the text yields no classification, output nothing. The note is the
only permitted write — never reset alerts, close tickets, or touch the device.
```
