---
name: CW Sync Lag Audit
description: Sweep Thread ↔ ConnectWise Manage divergence — status, owner, board mismatches — separate real drift from sync lag, and reconcile with CW as the master.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# CW Sync Lag Audit

**When to use:** "Do a sync audit" / "why do Thread and ConnectWise disagree?", a periodic hygiene sweep (weekly or after a CW maintenance window / integration outage), or one mismatched ticket reported and you want to know how widespread it is.

**Run it:** across all recently-touched tickets on the boards in scope (run manually or on a cadence).

## Prompt

```
You are sweeping a ConnectWise Manage desk for Thread↔CW divergence, filtering out transient
lag, and reconciling what remains — always toward the PSA. CW→Thread sync can lag or drop
individual updates, leaving tickets closed in CW but open in Thread, owned by different people,
or on different boards.

1. Scope the sweep: which boards, what time window (default: tickets touched in the last 14
   days). Get the live board and status lists.

2. Sweep the tickets — one search per signal per board, not one giant query. Signals:
   open-in-Thread tickets with no activity since a CW-side close is suspected; tickets whose
   owner field is empty or changed unexpectedly; tickets on a board that does not match their
   type. If any search may have hit a result cap, state that the count is a floor, not a total.

3. For every candidate, re-read the full ticket detail individually before calling it
   divergent. Most "mismatches" are sync lag, and a fresh read resolves them. Only a ticket
   that still disagrees on a fresh, full-detail read counts.

4. Classify each confirmed divergence: status drift (most common: closed in CW, open in
   Thread), owner drift, board drift. Note age and whether the ticket has client-visible
   activity pending.

5. Propose reconciliation with CW as master: align Thread's status/owner/board to the CW state,
   with a plain-text note on each recording "reconciled to PSA state on <date>, was <X> in
   Thread". Never push Thread's state back into CW during an audit.

6. Output a report: per-board counts, the confirmed divergence list (ticket number, field,
   Thread value vs CW value, age), the proposed fixes, and any tickets you are not confident
   about. Apply fixes only after the reviewer confirms — never bulk-reconcile unconfirmed.

Always: sync lag is the null hypothesis — no ticket is "divergent" until re-read individually
at full detail; never reconcile from list-view or cached data. The PSA is always master —
reconciliation moves Thread toward CW; if someone believes CW is wrong, that is a manual CW-side
fix for a human, not this skill. Never close a ticket in reconciliation that has an unanswered
client message — flag it for a human instead. Result-cap honesty: a capped sweep is a sample,
not a census. Notes are plain text (they sync back to CW). When in doubt about any single
ticket, exclude it from the fix list and report it separately.
```
