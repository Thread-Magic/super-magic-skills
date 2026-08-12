---
name: CW Time Entry Conventions
description: For desks synced to ConnectWise Manage — log time entries that survive the CW sync: correct work role/work type, deliberate billable flag, agreement application, and plain-text notes.
category: PSA-Specific
tools: [search_tickets, log_time_entry, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# CW Time Entry Conventions

**When to use:** Logging time on a CW-synced ticket ("log 30 minutes on this", call wrap-ups), a tech asking which work role/work type or billable flag to use, or cleaning up time entries that failed to apply to an agreement.

**Run it:** on one ticket.

## Prompt

```
You are logging time that lands correctly on the ConnectWise Manage side. In CW, a time entry
is a billing event: work role and work type set the rate; the billable flag and agreement
application decide whether the client is invoiced.

1. Re-read the ticket before logging — confirm it is still open and on the expected board. Time
   logged against a closed or moved ticket may not apply to the agreement.

2. Determine the client's coverage before setting the billable flag: what agreement covers this
   work, and is this ticket's work inside it? If coverage was not established at intake,
   establish it now. If coverage is unknown, ask — do not default silently to billable or non-
   billable.

3. Choose work role and work type from the desk's documented conventions (or values observed on
   comparable tickets). These set the invoice rate in CW; never invent them.

4. Write the time-entry note in plain text only — no markdown, no bullets-as-asterisks that
   render as noise, no emojis. Structure: what was done, outcome, next step. Never record a
   recommendation as a completed action.

5. Estimate duration honestly from evidence (call length, timestamps). Do not round up "to be
   safe" and do not fabricate start/end times.

6. Log the time. State in your output exactly what was logged: duration, billable flag, and the
   note text. If the desk needs an internal-only remark, put it in a separate internal note,
   not inside the billable time note.

Always: the time note may appear on the client's invoice — write every time-entry note as if
the client's finance team will read it. No internal commentary, no speculation, no other
clients named. Re-read full ticket detail before logging; the ticket's status, board, or
agreement linkage may have changed in CW. Billable flag is a deliberate decision, never a
default — when coverage is ambiguous, log with the desk's documented fallback and flag it for
billing review. Plain text only in anything that syncs to CW. Do not delete or rewrite an
existing time entry to fix a billing problem — propose the correction and route it to a human;
invoiced time may already be locked in CW.
```
