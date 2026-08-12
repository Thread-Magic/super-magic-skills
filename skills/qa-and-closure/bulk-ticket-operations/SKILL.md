---
name: Bulk Ticket Operations
description: The safe procedure for "close/reassign/update all tickets where <filter>" — enumerate and itemize first, per-ticket eligibility check, explicit sign-off on the full list, chunked writes with progress, per-ticket audit note, abort on anomaly. The only skill authorized to execute bulk ticket writes.
category: QA & Closure
tools: [search_tickets, update_ticket, add_ticket_note, list_ticket_statuses, list_boards, search_members]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Bulk Ticket Operations

**When to use:** "Close all tickets where <filter>" / "reassign everything on <board> from <tech A> to <tech B>" / "set all <status> tickets to <new status>", a cleanup another skill identified that needs its writes executed, or any operation touching more than a handful of tickets with the same change.

**Run it:** across a defined set of tickets (attended only — always requires explicit sign-off).

## Prompt

```
"Close everything older than 90 days" is one sentence that can destroy a hundred open client
commitments. This skill OWNS the bulk write — and earns that ownership by never executing one
blind: every ticket is enumerated, individually checked, shown to a human, written in chunks, and
audit-noted. Other skills (aging-and-sla-cleanup, no-response-closure-sequence,
psa-migration-hygiene, halo-recurring-tickets, noise-auto-close) decide WHAT deserves a bulk
change; this skill is HOW it executes safely. There is no unattended variant, by design.

1. Pin down the operation precisely before searching: the exact filter, the exact change (target
   status, target assignee, target board), and the reason that will go in every audit note.
   Ambiguity in any of these → ask, don't interpret.

2. Enumerate the matching tickets — split searches per board/status as needed. If any search hits
   a result cap, the population is incomplete: say so, and either narrow the filter or iterate
   until the enumeration is provably complete. Never bulk-operate on a capped list presented as
   complete.

3. Per-ticket eligibility check — every ticket, individually (never collapsed into "the filter
   already checked that"), against exclusion criteria:
   - Recent human activity (client reply, tech work, time entry) inconsistent with the premise.
   - Open commitments in the thread (promised callbacks, scheduled work, pending parts/vendor).
   - SLA-active, escalated, or VIP-flagged tickets.
   - Tickets another skill owns mid-sequence (e.g. a no-response ticket still inside its cadence).
   - Anything whose thread contradicts the filter's assumption.
   Ineligible tickets are pulled from the batch and listed separately with the reason.

4. Present the full itemized plan for explicit sign-off: the operation, the eligible list (ticket
   number + one-line subject + key evidence per ticket), the excluded list with reasons, and total
   counts. The human must approve the list as shown — "yes to these N tickets", not "yes in
   general". Any edit → re-present. NO WRITES BEFORE SIGN-OFF, however obvious the batch looks.

5. Execute in chunks (e.g. 10-20 tickets), reporting progress after each. For each ticket: apply
   the change and leave a plain-text audit note — what changed, why (the reason), on whose
   authorization, and the batch identifier/date so the operation is reconstructible per ticket.

6. Abort on anomaly: an update failing unexpectedly, a ticket's state having changed since
   enumeration (new reply, new status), or results not matching expectations → STOP the batch
   immediately, report exactly which tickets were completed and which were not, and re-confirm
   before resuming. Never push through anomalies to finish the list.

7. Final report: tickets changed (with numbers), excluded, aborted/skipped, and where the batch
   stopped if it did. The report must let someone undo the operation ticket-by-ticket.

Prefer reversible forms of the operation (a "pending-close" status over hard close) when the
desk's workflow offers one, and say so when proposing the plan. Deletion is out of scope entirely
— this skill closes, reassigns, and updates; it never deletes. Audit notes are plain text and go
on every ticket touched — a bulk operation without per-ticket audit notes is invisible to the next
person working the ticket.
```
