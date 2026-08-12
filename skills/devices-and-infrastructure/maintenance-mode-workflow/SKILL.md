---
name: Maintenance Mode Workflow
description: Put a device into (or take it out of) RMM maintenance mode with an explicit duration and reason, plus a follow-up task so monitoring is re-enabled on time. Use for "silence monitoring on <device> during the migration" or "set maintenance for tonight's window".
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, set_ninjaone_device_maintenance, add_ticket_note, create_ticket, schedule_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Fewer Escalations & Less Noise]
---

# Maintenance Mode Workflow

**When to use:** "Put <device> in maintenance for tonight's patching/migration", "cancel maintenance on <device>, the work is done", or planned work that will generate alert noise.

**Run it:** on one device, on demand (not a Flow — it changes monitoring state and needs requester confirmation).

## Prompt

```
Set or cancel device maintenance windows the disciplined way: bounded duration, recorded reason, and a scheduled follow-up so a "temporary" silence never becomes a permanently blind device. This needs the RMM connected; if absent, say maintenance mode is unavailable.

1. Resolve organization then device in the RMM; rank by organization match then last-contact and state your pick. Verify device class in the details — don't trust a class filter; silencing the wrong machine (or a server you thought was a workstation) defeats monitoring where it matters.
2. Collect the three required facts before acting; ask if any is missing:
   - Duration: explicit start and end. Never open-ended — if the requester says "until further notice", propose a concrete end (default: end of the stated work window plus 1 hour) and get agreement.
   - Reason: what work is happening, one line.
   - Ticket: which ticket the work belongs to, so the trail lands somewhere.
3. Check current state: read the device details, and if the device already has active alerts, note them in the reply — maintenance suppresses new noise but existing problems should be acknowledged, not buried.
4. Confirm the plan with the requester (device, window, reason), then put the device into maintenance mode in the RMM.
5. Leave a plain-text note (no markdown/emojis): device, maintenance start/end, reason, who requested it.
6. Create the re-enable follow-up: open a ticket (or a task on the existing ticket) scheduled for the window's end — "Verify <device> maintenance expired and monitoring is active; check for suppressed alerts." Not optional; this is the guard against silent devices.
7. For cancellation: verify with the requester that the work is complete, take the device out of maintenance mode, re-check the device details for any alert conditions that arose during the window, report them, and note the cancellation on the ticket.

Guardrails: no open-ended maintenance, ever — every window has an end time and a follow-up task. Confirm before setting maintenance on servers or shared infrastructure — suppressed monitoring on a DC or hypervisor is a business risk the requester should own explicitly. When maintenance ends, alerts that fire are real — never bulk-reset post-window alerts; triage them. If another tech's activity is visible on the device, coordinate before silencing — you may be muting the monitoring they rely on.
```
