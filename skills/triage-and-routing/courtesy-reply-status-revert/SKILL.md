---
name: Courtesy Reply Status Revert
description: When a thanks-only client reply flips a resolved ticket back to open, revert it to the correct status per a fixed per-board map — the only permitted write.
category: Triage & Routing
tools: [search_tickets, update_ticket, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise]
---

# Courtesy Reply Status Revert

**When to use:** Resolved tickets keep reappearing in the active queue because clients say "thanks so much!" — a flow fires on customer-responded status changes to catch courtesy flips, or "revert the status if that last reply was just a thank-you."

**Run it:** on one ticket · or as a Flow (when a resolved ticket flips to a customer-responded status).

## Prompt

```
When a courtesy-only reply moved a resolved ticket's status, put the status back according
to a fixed per-board mapping — and do nothing else.

1. Read the ticket: current status, prior status, board, and the message that triggered the
   status change.

2. Confirm the triggering message is courtesy-only: gratitude, acknowledgment, or sign-off
   with zero questions, zero requests, zero new symptoms, and no attachment for action.
   Evaluate the entire message, in its language (courtesy phrases vary by locale).

3. Look up this board in the fixed per-board revert map configured for this skill (e.g.
   "help desk board: customer-responded reverts to resolved-pending-close"). Verify the
   target status actually exists on this desk. Boards not present in the map are out of
   scope — no improvised mappings.

4. If the message is courtesy-only AND the board has a mapping AND the ticket was flipped
   from a resolved-family status: revert to the mapped status. Only revert flips out of
   resolved-family statuses; never touch tickets genuinely in progress.

5. Otherwise, do nothing.

WHEN IN DOUBT, DO NOTHING. Any hint of a question, complaint, new symptom, or "but…" means
the reply is real — leave the status alone. The status revert is the ONLY permitted write:
no notes, no replies, no priority/owner/board changes, no closing. Revert at most once per
triggering message; if the client replies again after the revert, re-evaluate as
courtesy-only before reverting again.

Running as a Flow: reply with exactly one line (logged, not posted to the ticket):
"REVERTED #<n> to <status> per board map." or "NO ACTION." — nothing else, no narration.
Deterministic stops: message not courtesy-only → NO ACTION; board unmapped → NO ACTION;
prior status not resolved-family → NO ACTION; mapped status missing on tenant → NO ACTION.
Never add a note or send anything to the client in this variant.
```
