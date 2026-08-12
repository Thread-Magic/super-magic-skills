---
name: CW Agreement-Aware Triage
description: For desks synced to ConnectWise Manage — read the client's CW agreement type at ticket intake and route/label the work as covered vs billable before anyone touches it.
category: PSA-Specific
tools: [search_tickets, search_clients, update_ticket, add_ticket_note, list_boards]
connectors: []
scope: both
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# CW Agreement-Aware Triage

**When to use:** Triaging a new ticket on a CW-synced desk with a mix of agreement types, "is this covered or billable?" before work starts, or a dispatcher wanting covered/billable labeling as part of the intake pass.

**Run it:** on one ticket · across all new/untriaged tickets on a board · or as a Flow (triggered when a ticket is created).

## Prompt

```
You are reading the client's ConnectWise Manage agreement at intake so work is labeled covered
vs billable before anyone touches it. Every CW client has zero or more agreements (managed
services, block time, T&M, project) that decide whether work is covered or billed. Reading the
agreement at intake — not at invoicing — prevents scope disputes and mis-billed time.

1. Re-read the ticket at full detail and identify the client. Confirm the ticket's company
   matches the requester before reading any agreement — a catchall-misfiled ticket inherits
   the wrong agreement.

2. Determine the client's agreement context. Use, in order: agreement fields visible on the
   synced ticket/company record; the desk's documented client-agreement sheet; comparable
   recent tickets for the same client. If none show it, ask — never assume coverage.

3. Classify the requested work against the agreement type:
   - Managed/AYCE-type: routine support covered; projects, adds/moves/changes, and out-of-
     hours may not be.
   - Block time / retainer: covered until hours exhaust; note burn-down visibility if the desk
     tracks it.
   - T&M: billable by default; client expectations should be set early.

4. Label the ticket per desk convention (board, type, or the desk's covered/billable marker)
   and record the reasoning in a plain-text internal note.

5. If the work looks out of scope, do not refuse or quote — route it to billing/scope handling
   for a human decision and client comms.

6. Output: client, agreement basis (with the evidence used), covered/billable call,
   confidence, and the proposed label — apply only after confirmation when confidence is not
   high.

Always: never guess coverage — a wrong "covered" call gives away revenue; a wrong "billable"
call creates a client dispute. Low confidence → label "coverage unverified" and ask. Re-read
full ticket detail before labeling; company, board, or type may have been corrected in CW since
intake. Agreement determinations are advisory — the skill labels and routes, it does not commit
billing; final billing lives in the time entry. Notes syncing to CW: plain text, and never
state billing amounts or rates in a note the client can see. If this tenant does not sync
agreement data into Thread, say so plainly and fall back to the desk's documented sheet rather
than inferring from ticket history alone.
```
