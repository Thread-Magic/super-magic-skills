---
name: Sophos Endpoint Alerts
description: Triage Sophos Central endpoint alerts: read health status and cleanup result, handle tamper protection correctly, and verify cleanup before closing.
category: Vendor Runbooks
tools: [search_tickets, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Sophos Endpoint Alerts

**When to use:** A Sophos Central alert lands as a ticket (malware detected/cleaned, PUA, manual cleanup required, device health red/yellow); a tech is about to reinstall/repair a Sophos agent and hits tamper protection; or someone asks whether a Sophos "cleaned up" alert can just be closed.

**Run it:** on the alert ticket.

## Prompt

```
Triage a Sophos Central endpoint alert — the vendor specialization of edr-detection-runbook. You
add Sophos's health colors, cleanup outcomes and tamper-protection discipline. Console and
on-endpoint work are technician steps you direct and record.

1. Parse the anatomy: alert type and severity, hostname, threat name and path, and the cleanup
   outcome: "cleaned up" (automatic cleanup succeeded), "manual cleanup required" (it didn't),
   or running/pending. Note the health color — green/yellow/red aggregates protection state,
   pending reboots and active threats.

2. Get context per edr-detection-runbook: live device state in the RMM for role and assigned
   user, the activity timeline around the detection, and user corroboration on a verified
   channel.

3. Branch on the cleanup outcome:
   - Cleaned up automatically → a claim, not a verdict. Verify health returned to green and no
     repeat detections followed. A cleaned commodity hit with corroborated context can close
     with evidence; repeated cleanups of the same threat on one device mean an uncleaned source
     (persistence, network share, USB, browser sync) — keep it open and scope.
   - Manual cleanup required → automation failed; treat the threat as present. The technician
     remediates hands-on via a deep link into the device; credential exposure branches to
     compromised-account-containment for signed-in users.
   - PUA → judgment: corroborate with the user and business context (remote-access tools and
     crack-adjacent utilities); authorize-or-remove is a documented decision, never a silent
     allow.

4. Tamper protection: any repair, reinstall or removal of the agent needs it disabled for that
   device from Sophos Central first — never worked around on the endpoint. Re-enable it
   immediately after the maintenance window and record both timestamps; tamper protection is
   never left disabled after maintenance. A tamper alert with no matching maintenance record is
   hostile until explained.

5. For active or spreading threats the technician isolates the device from Sophos Central;
   release only after cleanup verification — rescan clean, health green, persistence rechecked.

6. Health alerts with no threat (outdated definitions, stopped service, reboot required) are
   hygiene work: fix the cause, don't suppress it; recurring fleet noise routes to
   security-noise-tuning or patch-compliance-review.

7. Note the cleanup outcome, verification evidence and tamper-protection windows; classify per
   soc-classification-tree. Exclusions and PUA authorizations are security decisions: narrowest
   scope, named approver, review date — convenience is not a justification. Client-facing
   wording per defensive-writing-standard.

With no RMM, work from the alert and ticket history and say so. When in doubt escalate — a false
escalation is cheap, a missed compromise isn't.
```
