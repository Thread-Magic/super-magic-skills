---
name: Zapier QuickBooks Time & Billing
description: Push ticket time entries into QuickBooks as Time Activities and draft (never send) an invoice for out-of-contract work, gated by approval.
category: Connectors
tools: [search_tickets, send_approval, add_ticket_note]
connectors: [Zapier: QuickBooks Online]
scope: both
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Zapier QuickBooks Time & Billing

**When to use:** "Push the time from ticket <number> into QuickBooks," "this project work is out of contract — draft the invoice," or "which billable ticket time never made it into QuickBooks?"

**Run it:** on one ticket · or across all billable ticket time in a reconciliation window.

## Prompt

```
Stop revenue leaking between the ticket and the ledger: mirror ticket time entries into QuickBooks
Online as Time Activities, and when work falls outside the client's agreement, assemble a draft
invoice — created only after explicit approval, sent only by a human.

This runs only if the member has connected Zapier with the tenant's QuickBooks Online. If it's
absent, degrade to producing the formatted time/invoice data for manual entry — do not stop. Each
Zapier call = 2 Zapier tasks; batch reconciliation reads and mirror time per-entry only after one
batched confirmation.

1. Pull the ticket's time entries: tech, duration, date, work notes, and the billable flag /
   agreement coverage as the desk records it.
2. Resolve the QuickBooks customer matched from the client record — ambiguous or missing → stop and
   ask; never bill a best-guess customer.
3. Dedupe before writing: check for an existing Time Activity for the same tech/date/ticket (search
   by the ticket reference carried in the activity description). Already mirrored → skip and report
   it. Double-billed time is the failure this skill must never produce.
4. For each unmirrored billable entry, show me the batch (tech, duration, date, description incl.
   ticket reference), wait for confirmation, then create the Time Activity per entry. Leave a note
   (plain text) recording what was mirrored.
5. Out-of-contract invoice path (approval-gated): assemble line items from actual time entries and
   materials on the ticket, at rates the member confirms — rates are never assumed. Send the
   approval request (or use the Teams/Slack approval gate) to whoever owns billing, with full
   line-item detail. Approved → create the invoice as a DRAFT; note the draft's number on the ticket.
   Not approved/timeout → nothing created; note why. Sending the invoice stays a human action in
   QuickBooks — never send an invoice from this skill.
6. Reconciliation mode: for a stated window, list billable ticket time with no matching Time
   Activity, and Time Activities referencing tickets with no billable time; output both mismatch
   lists with amounts, no writes without steps 3–4. Financial figures in chat come only from tool
   results — no estimated totals presented as ledger fact. When coverage is ambiguous, ask.
```
