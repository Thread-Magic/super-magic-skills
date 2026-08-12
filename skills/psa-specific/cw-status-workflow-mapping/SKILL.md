---
name: CW Status Workflow Mapping
description: For desks synced to ConnectWise Manage — map Thread statuses to CW board statuses, make only safe status transitions, and reconcile closed-in-CW-but-open-in-Thread drift.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# CW Status Workflow Mapping

**When to use:** "Move this ticket to <status>" on a CW-synced desk and you need the safe equivalent, a ticket showing different statuses in Thread and ConnectWise, or before any bulk status change on a CW-synced board.

**Run it:** on one ticket · across all tickets before a bulk status change · or as a Flow (triggered on status change, to map it onto a valid board status).

## Prompt

```
You are keeping status changes inside the ConnectWise Manage workflow and reconciling drift.
Thread statuses mirror the CW board's status list, and each CW board has its own workflow (which
statuses exist, which are closed-family, which fire notifications or stop SLA clocks).

1. Re-read the ticket and its full detail — never act on a status seen earlier in the
   conversation or in a list view. CW→Thread sync can lag by minutes.

2. Pull the live status list for the ticket's board (and the board list if the board is
   ambiguous). CW statuses are per-board: a status on the service board may not exist on the
   projects board.

3. Map the requested transition onto a status that actually exists on that board. Prefer the
   desk's documented map; if none exists, propose the closest match and say it is a proposal.

4. Classify the target status before moving: is it closed-family (closes the ticket in CW),
   does it stop the SLA clock (waiting-type statuses), does it fire client notifications (CW
   workflow rules trigger on status)? Call out each side effect in your proposal.

5. If Thread and CW disagree — most commonly closed in CW, still open in Thread — treat the PSA
   as master. Do not reopen in CW to match Thread. Instead: re-read once more to rule out lag;
   if the divergence is real, align Thread to the CW state and record what you did with a
   plain-text note.

6. Output: current status in each system, the proposed transition, its side effects, and the
   exact change — then apply only after confirmation.

Always: re-read full ticket detail immediately before trusting or changing status; a stale list
result is not evidence of divergence. The PSA is always master — when the systems disagree,
Thread moves to match CW, never the reverse, unless the desk has explicitly documented Thread as
master for that board. Never set a status name the board's live status list did not return; do
not invent statuses. Never move a ticket into a closed-family status as a side effect of "just
updating status" — closing is a deliberate act with its own QA gate. Notes that sync to CW must
be plain text. If the desk uses CW workflow rules keyed on status, warn that a status change may
auto-email the client; when unsure, propose and stop.
```
