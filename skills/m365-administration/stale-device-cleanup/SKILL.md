---
name: Stale Device Cleanup
description: Clean up stale Entra device objects on a last-activity threshold with BitLocker-key-loss warnings, Autopilot exclusions, and disable-before-delete.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Risk & Compliance]
---

# Stale Device Cleanup

**When to use:** "Entra has <hundreds of> devices that haven't checked in for a year," a periodic device-hygiene pass for a managed tenant, device-count-based licensing or reporting skewed by dead records, or pre-cleanup before a tenant migration or management-tool change. Deleting a device object is the rare hygiene task that can destroy data recovery — BitLocker keys stored on the Entra device object die with it — so this skill sequences the cleanup so keys are preserved first, Autopilot devices are excluded, and nothing is deleted that was merely asleep.

**Run it:** as an on-demand sweep across every device object in the tenant — you prepare and sequence the cleanup, a technician exports, disables, and deletes (not a Flow: no schedule trigger, and changes need a human at the console).

## Prompt

```
You prepare and sequence; the tech exports, disables and deletes. Apply the Write Guardrails
base skill — never invent data; when in doubt about BitLocker preservation or a device's live
state, do nothing and escalate.

1. Inventory on activity. The tech exports Entra devices with approximate last sign-in, join
   type, management state and registration date, dated. Threshold from the client's standard
   (knowledge base or their documentation — Connector Degradation base skill if off), else 90
   days minimum, Microsoft's floor; 180 days is conservative for deletes (verify guidance). Intune and Entra device state differ — join both
   views first: cleaning the Entra object of an actively managed device breaks it. Apply
   Sweep Honesty — "at least N", and what you couldn't check.

2. Build the EXCLUSION list before the candidate list:
   - Autopilot-registered devices. Deleting the Entra object breaks redeployment; deregister
     from Autopilot first if the hardware is retired (autopilot-deployment).
   - Seasonal, spare and loaner devices — carts, field spares, seasonal staff — are offline
     by design. Ask which exist.
   - Recently imaged or in-transit: a young registration with no activity is a device in a
     box, not a stale one.
   - Hybrid-joined devices. The on-prem AD object is the source: deleting only the Entra
     object gets it re-created by sync. Clean these in AD through the client's change process
     and let them age out — a separate workstream.

3. Preserve BitLocker keys FIRST. Before disabling or deleting anything, the tech exports
   every candidate's recovery keys to the client's secure store: deleting the device object
   deletes its stored keys, and that disk is then unrecoverable. No deletion,
   ever, without preservation confirmed for the batch. Record where they went — a location
   reference, never the keys.

4. Disable first, delete later. Disable the candidates (blocking authentication) and wait an
   agreed window, 30 days by default: a live device fails loudly and reversibly, a deleted
   one does not. Straight to delete only for never-activated duplicate
   records, and the note must say why. Delete after the window with no breakage reports, and
   schedule the pass so the window is real.

5. Approval gate before the disable pass: sign-off from the client's documented authority on
   threshold, candidate count, exclusions, BitLocker preservation confirmed, the
   disable-wait-delete schedule, and rollback — re-enable during the window; post-delete
   recovery is re-enrollment, and hybrid devices may need on-prem cleanup and re-sync.

6. Note it (PSA Note Discipline base skill: plain text, no markdown): threshold, dated
   counts (candidates, excluded, disabled, deleted), key-preservation reference, approver,
   schedule, cadence. Re-pull the export if over two weeks pass between approval and
   execution.
```
