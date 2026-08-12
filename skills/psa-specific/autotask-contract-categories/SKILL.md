---
name: Autotask Contract Categories
description: Read Autotask contract type at triage (recurring, block, retainer, T&M, fixed) to label covered vs billable and add burn-down notes on hourly deals.
category: PSA-Specific
tools: [search_tickets, search_clients, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Autotask Contract Categories

**When to use:** Triage on an Autotask desk with mixed contract types ("is this covered?"), work on a block-hour or retainer client where burn-down matters, or before a tech sinks hours into a T&M client without expectations set.

**Run it:** on one ticket · across all new/untriaged tickets · or as a Flow (triggered when a ticket is created).

## Prompt

```
You are reading the client's Autotask contract at triage so work is labeled covered vs
billable before it costs anyone a surprise invoice. Autotask bills through contracts, and the
type changes what a ticket costs the client: Recurring Service (covered), Block Hours /
Retainer (covered until the balance exhausts), Time & Materials (billable), Fixed Price, Per
Ticket.

1. Re-read the ticket and confirm the client — a coverage read against the wrong company is
   worse than no read.

2. Determine the contract in effect. Evidence order: contract fields visible on the synced
   ticket/company; the desk's documented client-contract sheet; comparable recent tickets for
   this client. If none show it, ask. Never infer contract type from client size or tone.

3. Classify the work against the contract type:
   - Recurring Service: routine support covered; projects and out-of-scope items typically
     excluded — check the desk's exclusion list.
   - Block Hours / Retainer: covered while balance remains. If the desk tracks balance, state
     hours remaining if visible; if not visible from Thread, say so and recommend a check in
     Autotask before large efforts.
   - T&M: billable — expectations should be set with the client before significant work.
   - Fixed Price / Per Ticket: flag scope carefully; extra work erodes the fixed fee.

4. Label the ticket per desk convention and record the coverage reasoning in a plain-text
   internal note.

5. For hour-based contracts, add the burn-down note convention: each significant work
   session's note states hours consumed this ticket so the client-facing balance story stays
   reconstructible ("2.0h this session; ticket total 5.5h"). Do not state contract balances
   you cannot see.

6. This skill labels; it does not quote or bill. Out-of-scope work routes to a human/billing
   owner.

Always: never guess coverage — low confidence → label "coverage unverified" and ask; a wrong
covered/billable call is a revenue or trust incident. Re-read full ticket detail before
labeling; contract association and company can be corrected Autotask-side at any time. Burn-
down figures must come from evidence (logged time on tickets you can see) — never state or
estimate the contract's remaining balance unless it is actually visible; report "balance not
visible from Thread" instead. Plain-text notes only; never put rates or amounts in notes the
client can see. If this tenant does not sync contract data into Thread, run in advisory mode
from the desk's documented sheet only and state that limitation in every output.
```
