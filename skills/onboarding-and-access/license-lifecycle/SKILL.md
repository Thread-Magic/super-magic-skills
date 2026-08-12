---
name: License Lifecycle
description: Assign or reclaim software licenses — check for unused licenses before buying, and leave a billing note on every change. Use when a ticket asks to add a license, free one up, or asks why the client is paying for seats.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, update_ticket, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# License Lifecycle

**When to use:** "Assign an M365 license to <user>" / "new hire needs <application> — do we have a spare seat?" / "we're over our license count / why are we paying for <n> seats?" — or a license removal inside an offboarding, or a periodic license-hygiene sweep.

**Run it:** on one ticket — a spend decision, so purchases are approval-gated by a human.

## Prompt

```
Treat every license request as a spend decision: reuse an idle seat before buying,
reclaim on departure, and leave a billing-ready note so the client's invoice never
surprises anyone.

1. Identify the user (look up the contact), the exact license/SKU requested, and the
   client's licensing setup (knowledge base / IT Glue documentation): how are seats
   purchased (CSP, direct, annual commitment) and who approves spend?

2. Before buying anything, check for reclaimable seats: unassigned licenses in the
   tenant, seats held by disabled accounts, and recent offboarding tickets (search the
   tickets) where the license removal may not have happened. Reuse beats purchase every
   time.

3. If a purchase is genuinely needed, get spend approval first (send an approval
   request, or use the client's documented channel) with cost, term, and commitment
   spelled out. Note whether the SKU is monthly-flexible or annual-committed — an annual
   seat "just for a temp" is the classic mistake.

4. Assign the license. If the requested SKU exceeds the role's documented profile (a
   premium SKU where the profile says standard), flag it rather than silently
   upgrading.

5. Reclaim path: on departure or downgrade, remove the license only after any
   mailbox/data preservation step is complete (mailbox conversion before license
   removal — see Employee Offboarding), then return the seat to the pool or reduce the
   count at the next billing boundary per the client's agreement.

6. Post a plain-text billing note on every change: license/SKU, user, action (assigned
   from pool / purchased / reclaimed), cost impact, approver, effective billing date.
   Log time.

Guardrails: never purchase before checking for reclaimable seats — say in the note the
check was done and what it found. Never remove a license before confirming dependent
data (mailbox, OneDrive) is preserved per policy. Spend requires the client's
documented approver — a technical requester is not a spend approver. The billing note
is mandatory. Quote counts honestly: if a tenant query may be capped or stale, say so
rather than presenting the number as exact.
```
