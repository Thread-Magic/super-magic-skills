---
name: Halo Status Actions
description: HaloPSA transitions run through configured Actions, not raw status edits — pick the action that fires the right status, note visibility, and notifications.
category: PSA-Specific
tools: [search_tickets, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager, Technician]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Halo Status Actions

**When to use:** Changing status or replying on a Halo-synced ticket ("resolve this", "put it on hold"), or a tech asking why their Thread-side status change didn't behave like it does in Halo.

**Run it:** on one ticket · across all tickets needing a status move on a board · or as a Flow (triggered on status change or reply).

## Prompt

```
You are transitioning a HaloPSA ticket through the action model, not a raw status edit. In Halo,
agents don't set a status field directly — they perform an Action (Respond, Update, Place On
Hold, Escalate, Resolve, Close...), and each action is configured to set a status, control note
visibility (customer-visible or private), fire notifications, and touch the SLA clock. A raw
status edit that bypasses the action model skips those side effects, which is how Thread-side
changes diverge from what a Halo agent would produce.

1. Re-read the ticket at full detail — Halo→Thread sync can lag, and Halo statuses are a known
   weak spot in carrying over.

2. Identify the intent, then the Halo action it corresponds to on this desk: respond to
   customer, internal update, hold (waiting on customer/vendor/parts), escalate, resolve, close.
   The desk's action list is configured per ticket type in Halo — use the desk's documented
   action map when one exists.

3. Translate the action into its full effect set before writing: target status (verify it exists
   on the desk's live status list), note visibility (customer-visible vs private), notification
   expectation, SLA effect (hold-type actions typically pause; respond-type actions typically
   satisfy response targets).

4. Execute the effect set together, not piecemeal: set the status plus leave a note with the
   correct visibility, in one pass. A status change with no note, or a note with the wrong
   visibility, is a half-performed action.

5. Distinguish Resolve from Close: Halo desks commonly resolve first (client can reopen during a
   confirmation window) and close later, often automatically. Do not jump straight to closed if
   the desk uses the two-stage pattern.

6. Output: the action performed (named as the desk names it), the status set, the note text and
   its visibility, and any notification the client will receive. When the mapping is uncertain,
   propose and stop.

Always: re-read full ticket detail immediately before acting; Halo-side actions since your last
read change which transitions are valid. Never perform a bare status edit when the desk's
convention is action-driven — always pair status with the note and visibility that action
implies. Never set a status the desk's live status list didn't return; Halo statuses are
configured per tenant and often per ticket type. Note visibility is part of the action: an
internal remark sent customer-visible is a leak. Respect the resolve→close two-stage pattern if
the desk uses it; closing early kills the client's reopen window. Hold actions require a stated
wait reason in the note; a hold with no reason is clock-gaming.
```
