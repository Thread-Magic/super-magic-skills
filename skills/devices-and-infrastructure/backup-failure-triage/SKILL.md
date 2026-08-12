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
Turn a raw backup-failure alert into a classified failure mode with a recurrence verdict and a clear handle-here vs escalate-to-vendor call.

1. Read the alert text carefully — backup products embed the failure reason. Resolve the source device in the RMM without stopping to ask mid-lookup, then pull its current state and recent device activity. Don't trust a class filter — confirm the class in the device details.
2. Classify the failure mode from alert text + device state:
   - Device offline/unreachable at job time -> scheduling/availability, not a backup problem.
   - Destination full or quota exceeded -> capacity; check disk/storage on the device.
   - VSS/snapshot/writer errors -> OS-level; often follows a pending reboot or recent patch (check the activity history).
   - Credential/auth failures -> recently rotated passwords or service-account changes.
   - Network/timeout to target -> path/bandwidth; check whether other devices at the site also failed.
   - Agent/version errors -> recent agent update in the activity history.
3. Recurrence: check ticket history for the same device, same class, over the past 30-90 days. One failure with a later success is noise; three of the same class is a problem ticket. State the verdict explicitly; if the history search may have capped, say "at least N".
4. Check the documentation for the client's backup product, retention design, and documented known issues / vendor support contacts (degrade gracefully if the documentation platform is absent).
5. Decide the path: handle here (offline-at-job-time, pending-reboot VSS, obvious destination-full — local remediations exist); escalate to vendor (repeated same-class failures after local remediation, corruption/integrity errors, failures across many clients at once, or anything the vendor's docs mark support-required). Name the vendor generically from docs — do not guess the product.
6. Output: classification, evidence, recurrence verdict, recommended action, and — critically — the last known good backup date (the client's real exposure). Offer to leave a plain-text note (no markdown/emojis).

Guardrails: never state data is safe or that a restore will work — report only the last successful job on record; restore verification is a human task. Do not clear/reset backup alerts — the alert is the evidence trail. A recurring failure is never closed as a one-off. If the backup product is not visible through the RMM (many run their own consoles), say the view is partial and name what to check in the console. Degrade gracefully if the RMM is absent.

Unattended (Flow) mode: entire reply is the plain-text triage note posted verbatim (classification, evidence, recurrence verdict, last known good date, handle-here vs escalate). Input is the alert/ticket id. If the device cannot be resolved, classify from alert text alone and mark "DEVICE UNRESOLVED - alert-text classification only"; if the text yields no classification, output nothing. Permitted write: the note only — never reset alerts, close tickets, or touch the device.
```
