---
name: Device Wipe Workflows
description: Choose the right Intune remote action — retire, wipe, fresh start, Autopilot reset, or delete — with explicit data-loss warnings and an approval gate before anything destructive runs. Use whenever a ticket asks to "wipe", "reset", "clean up", or "remove company data from" a device.
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
You are mapping a "wipe it" request to the least destructive Intune remote action that achieves the intent, stating the data loss in plain language and gating execution behind recorded approval. You prepare and verify; the technician triggers the action in the console. Never report a wipe as done on intention — never invent data.

1. Establish intent, ownership, and data reality before naming an action (read the ticket for context). What outcome does the requester actually want? Corporate or personal (BYOD) device? Does the device hold data that exists nowhere else (local files, un-synced folders — ask explicitly; "everything's in OneDrive" is a claim to verify, not an assumption)? Who is the authorized requester — for offboarding wipes, that is the client authority, never the departing user's word alone. Check the client's documentation for the device standard and ownership records (skip gracefully if neither is connected).

2. Map to the decision tree, least destructive first:
   - Retire — removes company data, apps, and management; personal data untouched. The default for BYOD offboarding (the selective wipe app-protection-policies promises) and for devices leaving management but staying with their owner.
   - Autopilot Reset / Wipe with reprovision intent — rebuilds the OS and re-enrolls for the same tenant; user data on the device is destroyed. For handing a corporate device to a new user or recovering from a broken deployment.
   - Fresh Start — reinstalls Windows removing manufacturer bloat; the keep-user-data option exists but removes apps. Narrow use: cleaning up OEM images.
   - Wipe (factory reset) — everything on the device is destroyed. For device disposal, return-to-lessor, or confirmed-loss scenarios.
   - Delete (record only) — removes the Intune/Entra record and touches the device not at all. Never the answer to "wipe it"; pairs with stale-device-cleanup rules (BitLocker keys die with the object — preserve first).
   Verify current action behavior per platform against Microsoft's current docs — remote-action semantics differ by platform and change.

3. Pre-wipe salvage. For any OS-destroying action: confirm data backup state (sync health, local-only data recovered), retrieve and preserve the BitLocker recovery key BEFORE the action (see bitlocker-key-retrieval — post-wipe recovery needs it if anything goes sideways), and note license or app deactivations that need doing while the OS still boots.

4. Approval gate — always, with consequences stated plainly. Send an approval request to the authorized client contact naming: the device, the exact action, what is destroyed ("all data on the device, unrecoverable" vs "company data only; personal files untouched"), what survives, and the point of no return. For BYOD retires, the device owner is informed before execution — company data vanishing from a personal phone without warning reads as an attack. No destructive action executes without the recorded approval; when in doubt about authorization, do nothing and escalate. Urgency does not waive the gate.

5. Execute and verify. The tech triggers the action; note that an offline device executes the wipe whenever it next checks in — a pending wipe is a live grenade, so record it prominently and reconcile if the request is later cancelled (cancel the pending action explicitly; do not assume it expired). Verify completion in the console (action status; update the ticket) and, where relevant, that re-enrollment/reprovisioning succeeded. "The user said it's all backed up" is verified (sync status, spot check), not trusted — the wipe is unrecoverable and the claim is free.

6. Document what/why/when/rollback: leave a plain-text note with device, action chosen and why the less destructive options were insufficient, data-salvage steps done, approver and approval reference, execution time, verification, and follow-ups (record deletion, asset disposal, license reclaim). Log time.

Always propose the least destructive action that meets the intent and record why anything stronger was chosen. BitLocker key preservation precedes every OS-destroying action on an encrypted device. Track pending wipes on offline devices to completion or explicit cancellation — an orphaned pending wipe firing weeks later is a self-inflicted incident. Never use record deletion as a substitute for a device action, and never wipe to troubleshoot enrollment (see intune-enrollment-troubleshooting).
```
