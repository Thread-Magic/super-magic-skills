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
You are working a HaloPSA ticket that is moving through a configured workflow. Halo tickets pass
through ordered workflow steps, each exposing a DIFFERENT set of valid actions, and some actions
are approval actions that hand the ticket to an approver and block progression until a decision
comes back. Acting without reading the current step is how you offer an action Halo won't allow,
or skip an approval the process requires. (This extends halo-status-actions, which maps a single
intent to the Halo Action carrying the right status, note visibility, and notifications.)

1. Re-read the ticket at full detail before anything — Halo→Thread sync lags, and workflow
   position is exactly the field most likely to be stale.

2. Establish where the ticket sits in its workflow: which workflow it's on and which step/stage
   it currently occupies. The set of legal next actions is a property of the step, not of the
   ticket globally — a Resolve action valid at "Work in progress" may not exist at "Awaiting
   approval".

3. Identify whether the current step is an approval gate. If the ticket is awaiting a decision,
   the only forward moves are approve / reject by the designated approver — a status nudge from
   Thread does not satisfy or bypass the gate. Report who the approver is if visible; do not
   self-approve on their behalf.

4. When the intent is to request an approval, send an approval request — and first confirm the
   desk actually routes approvals through Thread rather than through Halo's own approval action.
   If Halo owns the approval process, the request must originate in Halo; say so instead of
   firing a parallel Thread approval the workflow won't recognize.

5. For a normal (non-approval) forward move, translate the target step's action into its full
   effect set: status (verify it against the desk's live status list), note visibility,
   notification, SLA effect — and apply status + note together in one pass.

6. Output: current workflow + step, the valid actions at this step, whether an approval is
   pending (and on whom), the proposed action with its effects, and the exact change. When the
   workflow position is ambiguous or the approval owner is unclear, propose and stop.

Always: sync lag first — never judge workflow position or approval state from a list view or
earlier turn; re-read full detail immediately before acting. Never skip or fake an approval
gate — a status change from Thread does not equal an approval decision; do not move a ticket
past an approval step by editing status, and never approve on the approver's behalf. Don't offer
an action the current step doesn't expose; if the desired action isn't valid here, say what step
would make it valid rather than forcing a raw status edit. Status never travels without the note
visibility and notification the action implies. Confirm where approvals live (a Thread approval
request vs Halo's native action) before sending. Notes that sync to Halo are plain text. When in
doubt — ambiguous step, unclear approver, uncertain approval ownership — do nothing and report.
```
