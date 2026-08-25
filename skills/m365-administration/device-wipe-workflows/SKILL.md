---
name: Device Wipe Workflows
description: Choose the right Intune remote action - retire, wipe, fresh start, Autopilot reset, or delete - with data-loss warnings and approval gate.
category: M365 Administration
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Device Wipe Workflows

**When to use:** "Wipe it" arrives as one phrase but names five different actions with five different blast radii — from removing only company data to destroying everything on the disk. Use for "wipe <user>'s laptop — they're leaving" / offboarding cleanup, "this machine is a mess, reset it" / handing a device to a new user, "remove company data from <user>'s personal device" (BYOD), or a failed deployment/corrupted profile where reset is proposed (cross-check autopilot-deployment before defaulting to a wipe). For lost or stolen devices the time-critical path lives in mobile-device-mdm — use this skill for the action-selection detail once that runbook engages.

**Run it:** on one device — you map the request to the least-destructive action and gate on approval, a technician triggers the action in the console (not a Flow: it needs a human at the console).

## Prompt

```
Map a "wipe it" request to the least destructive Intune action that meets the intent. You
prepare and verify; a technician triggers the action.

1. Intent, ownership, data. What outcome does the requester want, on a corporate or BYOD
   device? Does it hold data that exists nowhere else — local files, un-synced folders? Verify
   it; don't take "it's all in OneDrive". For offboarding the authorized requester is the
   client authority, never the departing user. Check the client's documentation for the device
   standard and ownership, noting if IT Glue or Hudu isn't connected (Connector Degradation
   base skill).

2. Choose from the tree, least destructive first:
   - Retire — removes company data, apps and management; personal data untouched. Default for
     BYOD offboarding and devices leaving management with their owner.
   - Autopilot Reset / reprovision wipe — rebuilds the OS and re-enrolls in the same tenant;
     on-device user data is destroyed. For reassigning a corporate device or a broken
     deployment.
   - Fresh Start — reinstalls Windows and strips OEM bloat; keep-user-data still removes apps.
   - Wipe (factory reset) — everything on the device is destroyed. Disposal, lease return,
     confirmed loss.
   - Delete (record only) — removes the Intune/Entra record, touches the device not at all.
     Never the answer to "wipe it", and BitLocker keys die with the object — preserve first.
   Semantics differ by platform and change — verify against Microsoft's docs.

3. Salvage, then gate. Before any OS-destroying action: confirm sync state, recover local-only
   data, preserve the BitLocker recovery key, and do license or app deactivations while the OS
   still boots. Then send an approval request to the authorized client contact naming the
   device, the exact action, what is destroyed ("all data on the device, unrecoverable" vs
   "company data only; personal files untouched"), and the point of no return. Tell a BYOD
   owner before their device is retired. Nothing destructive runs without the recorded
   approval; urgency does not waive it (Write Guardrails base skill — no irreversible action
   without a confirmed go).

4. Execute, verify, document. An offline device executes the wipe whenever it next checks in,
   so record a pending wipe prominently and cancel it explicitly if the request is dropped.
   Verify completion in the console and that reprovisioning succeeded. Leave a plain-text note,
   no markdown or emojis (PSA Note Discipline base skill): device, action and why gentler
   options failed, salvage steps, approver, verification, and follow-ups (record deletion,
   asset disposal, license reclaim). Log the time.

Record why anything stronger than the minimum was chosen. Never substitute record deletion for
a device action, never wipe to troubleshoot enrollment, and escalate rather than guess at
authorization.
```
