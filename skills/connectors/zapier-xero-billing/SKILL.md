---
name: Zapier Xero Billing
description: For Xero-shop MSPs — draft (never send) invoices from ticket time entries and check a client's overdue-invoice standing before billable work.
category: Connectors
tools: [search_tickets, send_approval, add_ticket_note]
connectors: [Zapier: Xero]
scope: both
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Zapier Xero Billing

**When to use:** "This project work is out of contract — draft the Xero invoice," "check <client>'s invoice standing in Xero before we dispatch," or "which billable ticket time never became a Xero invoice line?"

**Run it:** on one ticket · or across all billable ticket time in a reconciliation window.

## Prompt

```
The Xero twin of Zapier QuickBooks Time & Billing: keep ticket work and the ledger in agreement —
assemble draft invoices from actual ticket time only after explicit approval, and give dispatch
overdue-awareness so the desk doesn't sink hours into an account that hasn't paid the last three
invoices.

This runs only if the member has connected Zapier with the tenant's Xero org. If it's absent,
degrade to producing the formatted line items and standing summary for manual entry — do not stop.
Each Zapier call = 2 Zapier tasks; batch reconciliation reads.

Overdue-awareness check (before billable dispatch):
1. Resolve the Xero contact matched from the client record — ambiguous or missing → stop and ask; a
   standing check against the wrong contact is misinformation.
2. Find the contact's overdue/unpaid invoices; report count, total, and oldest-overdue age with "per
   Xero as of now" provenance. This is decision input for the member — the skill never blocks work
   itself, and never mentions arrears to the client; that conversation belongs to the business owner.

Draft invoice from ticket time (approval-gated):
3. Pull the ticket's time entries: tech, duration, date, work notes, billable flag / coverage as the
   desk records it. Coverage ambiguous → ask; misbilling a covered client costs more than the invoice.
4. Dedupe: check Xero for an existing invoice/line referencing this ticket. Already invoiced → stop
   and report; double-billing is the failure this skill must never produce.
5. Assemble line items from actual time entries and materials, at rates the member confirms — never
   assumed; each line carries the ticket reference. Send the approval request (or use the Teams/Slack
   gate) to whoever owns billing, with full detail and total. Approved → create the invoice as a
   DRAFT; note the draft's number on the ticket. Not approved/timeout → nothing created; note why.
   Sending or authorizing the invoice stays a human action in Xero.
6. Reconciliation mode: for a stated window, list billable ticket time with no matching Xero line, and
   lines referencing tickets with no billable time; output both with amounts, no writes without steps
   4–5. Financial figures in chat come only from tool results.
```
