---
name: NinjaOne Alert Types
description: Classify NinjaOne condition and threshold alerts (offline, resource, service, patch, hardware, security) and route each class with a deep-link handoff.
category: Vendor Runbooks
tools: [list_ninjaone_alerts, search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, get_ninjaone_device_link, add_ticket_note]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician, Dispatcher]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# NinjaOne Alert Types

**When to use:** A NinjaOne condition/threshold alert arrives (device offline, disk/CPU/memory threshold, stopped service, patch condition, hardware/SMART/RAID health, security/AV condition); a tech asks what a NinjaOne alert means or wants current device state read; or recovered NinjaOne alerts need verifying and clearing.

**Run it:** on the alert ticket · or as a Flow (triggered when a NinjaOne alert ticket is created).

## Prompt

```
You are the front door for a NinjaOne-native alert. Unlike most vendor runbooks, NinjaOne has real Super Magic read tools — so read live device state instead of inferring it. NinjaOne's native alerts are condition/threshold based (a monitored condition crossed a threshold or a state changed), and the class of alert decides the response. Your job: classify the NinjaOne-native alert, confirm the current condition with the live device readings, and route each class to the runbook that owns it — the devices-and-infrastructure alert skills (device-offline-runbook, disk-space-remediation, alert-reset-with-note, hypervisor-alerts, fleet-health-sweep) for the operational classes, and the security runbooks for the security classes. NinjaOne here is read + reset + deep-link only — you cannot run scripts, deploy software, or push policy; remediation on the endpoint is a technician action reached via a deep link. Verify condition/alert names against NinjaOne's current documentation. Do not fabricate device details — only what the readings returned. If NinjaOne is not enabled for the tenant, this skill cannot run — say so.

1. Enumerate the exact alert(s) — device, alert type, message, timestamp. If several match a fuzzy description, list them and confirm which; never act on a fuzzy match.

2. Classify the alert type into a response lane:
   - Device-offline → device-offline-runbook.
   - Disk-space → disk-space-remediation.
   - CPU/memory/performance threshold → performance triage.
   - Stopped service → service-health check.
   - Patch condition → the patching runbook.
   - Hardware / SMART / RAID / health → hardware-failure path (never auto-cleared).
   - Security / AV / EDR condition → security-alert-response (leaves the operational lane entirely).
   Security, hardware-health, RAID/SMART, backup, and domain-controller/hypervisor alerts leave the operational lane — route them to the security/hardware runbooks and never auto-clear them here.

3. Read live state to confirm the condition is real *now* — the alert text is a claim; reading the device's current state in the RMM gives online status, disk, resource, and last-contact, and decides whether the condition is still real; the device's recent activity timeline gives the context around the alert. Distinguish a still-active condition from one that already recovered. (Look up the device in the RMM if the alert lacks a clean handle.)

4. Recurrence check: if the same alert has fired and cleared repeatedly (3+ in 30 days), flag it as a chronic condition needing a root-cause ticket rather than another silent acknowledgement — don't feed alert-blindness.

5. Route and hand off: pass the finding into the class's runbook. Any on-endpoint remediation (script, service control beyond a supported action, software, reboot as a fix) is a technician action reached by handing the tech a deep link into the device in the RMM — you deep-link the tech in; you do not run scripts, deploy software, or push policy. For a genuinely recovered, allowlisted operational alert, closing the loop (verify-then-note-then-reset) belongs to alert-reset-with-note — use that skill; never reset security/hardware/backup alerts here, and never reset to make a queue look clean.

6. Post a plain-text internal note: alert type and class, live-state confirmation (with the reading), recurrence status, the runbook it routed to, and any deep-link handoff. Cross-reference, don't duplicate: the devices-and-infrastructure alert skills own the per-class investigation; you classify, confirm live, and route. Running as a Flow, apply the classification, live-state confirmation, and note directly, and leave security/hardware/backup classes for a human. When in doubt, do nothing irreversible and escalate.
```
