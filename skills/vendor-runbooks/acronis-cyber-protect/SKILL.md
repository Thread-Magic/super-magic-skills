---
name: Acronis Cyber Protect
description: Handle Acronis Cyber Protect alerts: separate a backup failure from an Active Protection anti-ransomware detection and run the matching triage discipline.
category: Vendor Runbooks
tools: [search_tickets, search_itglue, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Always-On Coverage]
---

# Acronis Cyber Protect

**When to use:** An Acronis alert lands and it isn't obvious whether it's backup or security; an Active Protection / ransomware-detection alert fires on a protected machine; or an Acronis backup job failure needs classification and an exposure statement.

**Run it:** on the alert ticket.

## Prompt

```
Acronis Cyber Protect combines backup and security in one alert stream that belongs to two
disciplines: backup-failure-triage (classify, check recurrence, fix here or escalate) and
edr-detection-runbook (verify, contain, scope). You have no Acronis console access — quarantine,
recovery, and exclusions are technician steps you direct and record, never take or invent — and
RMM device state is read-only, so hands-on work is a deep link.

1. Classify the stream first:
   - Backup: job failed or warning, storage or quota, agent offline at job time, validation
     failure.
   - Security: Active Protection (the suspicious file-modification ransomware heuristic),
     antimalware detections, or tamper events against the Acronis agent.
   - Ambiguous: treat as security until classified — a ransomware detection triaged as backup
     noise is the miss this skill exists to prevent.

2. Security path, on top of edr-detection-runbook:
   - Note what the product did: blocked the process, possibly reverted files from its cache.
     Reverting contains the symptoms only — the process, its origin, and its persistence still
     need working.
   - Read device state and recent activity in the RMM, corroborate with the user on a verified
     channel; backup software, sync clients, and bulk file operations trigger false positives.
   - Confirmed malicious gets full EDR handling — isolate, deep-link the tech into the device —
     and credential exposure branches to compromised-account-containment. Verify backups
     immediately: the last clean restore point before the detection is the recovery floor — record
     it.
   - Tamper alerts with no maintenance record are hostile until explained — ransomware kills
     backup agents first.

3. Backup path: run backup-failure-triage's taxonomy — VSS/snapshot, credentials, destination
   storage or quota, network, agent version — and its recurrence rule. A validation failure means
   restore in doubt, not a warning. Its guardrails carry over: no data-safety claims, alerts are
   the evidence trail, a recurring failure never closes as a one-off.

4. Cross-check both streams: a backup failure preceded by a security detection is sabotage until
   shown otherwise. After any security detection, restore points spanning the infection window are
   suspect — mark them, and never recommend restoring from one without a technician's
   clean-or-dirty assessment.

5. Backup-path notes end with the exposure statement: last successful backup, validation status.
   End a security-path note with the verdict, product-versus-technician actions, and the last
   clean restore point; classify per soc-classification-tree, client-facing wording factual
   (defensive-writing-standard). Exclusion requests need confirmed false-positive evidence,
   narrowest scope, a named approver, review date.

When in doubt, do nothing irreversible and escalate.
```
