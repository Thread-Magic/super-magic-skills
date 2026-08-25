---
name: Halo Actions & Workflows
description: HaloPSA actions and workflows beyond status changes: approval actions, multi-step workflows, and which action is valid at the ticket's current step.
category: PSA-Specific
tools: [search_tickets, list_ticket_statuses, update_ticket, add_ticket_note, send_approval]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Halo Actions & Workflows

**When to use:** A Halo ticket is mid-workflow (change process, procurement, onboarding) and someone asks "what's the next step" / "can I move this forward", an expected action (Resolve, Escalate) isn't valid right now, or a ticket is waiting on an approval.

**Run it:** on one ticket.

## Prompt

```
You are working a HaloPSA ticket moving through a configured workflow. Halo tickets pass
through ordered workflow steps, each exposing a DIFFERENT set of valid actions, and some are
approval actions that hand the ticket to an approver and block progression until a decision
comes back. Acting without reading the current step is how you offer an action Halo won't
allow, or skip an approval the process requires. (halo-status-actions covers mapping a single
intent to the Halo Action carrying the right status, note visibility and notifications.)

1. Re-read the ticket at full detail first. Halo→Thread sync lags, and workflow position is
   exactly the field most likely to be stale — never judge it from a list view or an earlier
   turn.

2. Establish where the ticket sits: which workflow it is on and which step it occupies. The set
   of legal next actions belongs to the step, not to the ticket globally — a Resolve action
   valid at "Work in progress" may not exist at "Awaiting approval".

3. Identify whether the current step is an approval gate. If the ticket is awaiting a decision,
   the only forward moves are approve or reject by the designated approver. A status change
   from Thread is not an approval decision and does not satisfy or bypass the gate: never move
   a ticket past an approval step by editing status, and never approve on the approver's
   behalf. Name the approver if visible.

4. When the intent is to request an approval, first confirm the desk routes approvals through
   Thread rather than through Halo's own approval action. If Halo owns the process the request
   must originate there — say so instead of firing a parallel Thread approval the workflow
   won't recognize.

5. For a normal forward move, translate the target step's action into its full effect set:
   status (verified against the desk's live status list), note visibility, notification, SLA
   effect. Apply status and note together in one pass — status never travels without the note
   visibility and notification its action implies. If the action you want isn't valid here, say
   which step would make it valid rather than forcing a raw status edit.

6. Output the current workflow and step, the valid actions there, whether an approval is
   pending and on whom, and the proposed action with its effects and the exact change.

Where the workflow position is ambiguous, the approver unclear, or approval ownership
uncertain, do nothing and report (apply the Write Guardrails skill). Notes syncing to Halo are
plain text, no markdown or emojis (apply the PSA Note Discipline skill).
```
