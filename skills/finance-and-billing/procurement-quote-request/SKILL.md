---
name: Procurement Quote Request
description: When a ticket needs hardware or software purchased and you want a structured quote-request note (specs, quantity, budget, needed-by) plus a vendor email draft.
category: Finance & Billing
tools: [search_tickets, search_clients, search_contacts, add_ticket_note, web_search]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Procurement Quote Request

**When to use:** "Client needs three new laptops — put together the quote request" / "draft the vendor email for the switch replacement on this ticket" / "structure this purchase request so procurement can action it."

**Run it:** on one procurement ticket, or across a set of purchase tickets you point me at — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Turn a "we need to buy something" ticket into a structured, complete quote request — exact
specs, quantity, budget signal, needed-by date — as an internal note and a ready-to-review
vendor email draft.

1. Read the ticket thread and extract every requirement stated: item type, model or spec
   hints, quantity, who it's for, budget mentions, deadline drivers (start date, failed
   hardware, project milestone).

2. Fill the gaps deliberately. Required fields: item + minimum specs, quantity, needed-by
   date, ship-to (client site vs MSP), budget or approval owner on the client side. Anything
   the thread doesn't answer becomes an explicit "TO CONFIRM" line — never silently pick a
   spec the client didn't ask for.

3. If model selection is needed, search the web to check current-generation equivalents and
   note availability/EOL concerns; present at most two candidate models with the trade-off in
   one line each. Public prices found this way are labeled indicative only.

4. Leave the structured quote-request as a plain-text internal note:
   ITEM / SPECS / QTY / NEEDED BY / SHIP TO / BUDGET SIGNAL / CLIENT APPROVER / TO CONFIRM.
   No markdown, no emojis (PSA-sync safe).

5. Draft the vendor email: item and full specs, quantity, requested delivery date and
   location, ask for price + availability + quote validity, and the desk's PO reference
   placeholder. Neutral tone, no client end-user names beyond what shipping requires.

6. Return both artifacts. The requester sends the vendor email themselves and confirms the TO
   CONFIRM lines with the client.

Guardrails: draft + approval-gated, like every money-moving action — this skill never sends the
vendor email, never places an order, and never commits the client to a spend. Never state that
the client has approved a budget or purchase without the approval evidence in the ticket —
quote requests before client approval must say "pending client approval". No fabricated part
numbers, SKUs, or prices; a spec you inferred (e.g. RAM size from the user's role) is marked as
inferred. Do not include credentials, license keys, or unnecessary end-user personal details in
the vendor draft. If the desk has a preferred-vendor or standard-model policy in the knowledge
base, follow it; deviations are flagged, not silently chosen.
```
