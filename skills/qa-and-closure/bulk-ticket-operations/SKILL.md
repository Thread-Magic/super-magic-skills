---
name: Bulk Ticket Operations
description: Safe procedure for bulk close, reassign, or update ticket operations: enumerate, eligibility check, chunked writes, audit notes, abort on anomaly.
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
commitments. This skill owns the bulk write and earns that by never executing one blind. Sibling
skills decide WHAT deserves a bulk change; this is HOW it runs safely. There is no unattended
variant, by design.

1. Pin the operation down before searching: the exact filter, the exact change (target status,
   assignee or board), and the reason that goes in every audit note. Ambiguity in any of them
   means ask, not interpret.

2. Enumerate the matching tickets, splitting searches per board or status as needed. Sweep
   Honesty base skill: a result cap means the population is incomplete — say so, and narrow the
   filter or iterate until enumeration is provably complete. Never bulk-operate on a capped list
   presented as complete.

3. Check eligibility per ticket, individually — never collapsed into "the filter already checked
   that": recent human activity (client reply, tech work, time entry) against the premise; open
   commitments in the thread (promised callbacks, scheduled work, pending parts); XLA-active,
   escalated or VIP-flagged tickets; tickets another skill owns mid-sequence, like a no-response
   ticket inside its cadence; anything whose thread contradicts the filter. Pull ineligible
   tickets out and list them separately with the reason.

4. Present the full itemized plan for explicit sign-off: the operation, the eligible list (ticket
   number, one-line subject, key evidence each), the excluded list with reasons, and total
   counts. The human approves the list as shown — "yes to these N tickets", never "yes in
   general". Any edit means re-present. NO WRITES BEFORE SIGN-OFF, however obvious the batch
   looks.

5. Execute in chunks of 10 to 20, reporting progress after each. For every ticket, apply the
   change and leave an audit note — plain text, no markdown or emojis (PSA Note Discipline base
   skill) — recording what changed, why, on whose authorization, and the batch id and date, so it
   is reconstructible per ticket.

6. Abort on anomaly — an update failing unexpectedly, a ticket's state changing since enumeration
   (new reply, new status), results not matching expectations. STOP the batch, report exactly
   which tickets were completed and which were not, and re-confirm before resuming. Never push
   through to finish the list.

7. Final report: tickets changed with numbers, excluded, aborted or skipped, and where the batch
   stopped — enough to undo the operation ticket by ticket.

Prefer a reversible form where the workflow offers one — a pending-close status over a hard close
— and say so when proposing the plan. Deletion is out of scope: this skill closes, reassigns and
updates, never deletes. Audit notes go on every ticket touched; without them a bulk operation is
invisible to the next person on the ticket.
```
