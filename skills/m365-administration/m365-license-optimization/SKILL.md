---
name: M365 License Optimization
description: Right-size Microsoft 365 licensing from usage evidence: reclaim unused licenses, downgrade over-provisioned users, and rationalize add-ons.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# M365 License Optimization

**When to use:** A client asks to cut Microsoft 365 spend or review whether they're over-licensed, wants to know how many licenses aren't assigned, asks whether a specific user could drop from E5 to Business Premium, or you're doing a recurring license true-up/renewal. Every removal is a proposal with evidence, never a silent downgrade that breaks someone's mailbox. For the billing-side reconciliation and margin view see finance-and-billing/license-cost-optimization — this skill is the M365 tenant-side assignment analysis that feeds it.

**Run it:** as an on-demand review across all of a tenant's users and SKUs — you prepare the proposal, a technician or account manager executes changes only after client approval (not a Flow: it needs a human at the console).

## Prompt

```
You are right-sizing a client's Microsoft 365 licensing from evidence. This is a recommendation, never an executed action — the agent prepares the proposal; a technician or account manager executes changes only after client approval. Never invent data — count from real assignment data, never present an estimate as exact.

1. Pull the assignment evidence: assigned vs. purchased counts per SKU, unassigned licenses, and users who are disabled/leavers still holding a paid license. If Liongard's M365 inspector is present, use it (via the connected integration) to read license assignment across the tenant and state the dataprint age; otherwise use a point-in-time admin-center export and say so. Pull documented context from the client's documentation (connector-gated — skip gracefully if neither is connected), the knowledge base, and prior tickets. Do not estimate — count.

2. Categorize the reclaim opportunities, cheapest-risk first:
   - Unassigned/purchased-but-idle licenses → reclaim at next true-up (pure saving, no user impact).
   - Disabled or departed users still licensed → remove after confirming the account is genuinely a leaver and its mailbox/OneDrive is handled (retention or handover) — pulling a license can strand data; check onedrive-storage-governance / retention before removing.
   - Over-provisioned users (e.g. E5 for someone using only mail + Office) → candidate downgrade. Verify the specific features they actually use (Defender, Power BI, audit, phone) before proposing a drop; a downgrade that removes a feature they rely on is a false saving.
   - Redundant add-ons (standalone SKUs already included in a suite the user holds) → rationalize.

3. Model the impact of each downgrade explicitly. Dropping from E5/E3 can remove features silently (advanced Defender, DLP, retention, archiving, Teams Phone). List what each proposed change would take away so the client decides with eyes open — not a spreadsheet of savings with hidden costs.

4. This is a recommendation, never an executed action. Present the plan with per-line saving and per-line risk; get explicit client approval (send an approval request) before any license is removed or changed. The zero-assumption rule applies hard here — do not convert "you could save X" into a completed downgrade.

5. Prepare execution for the tech / account manager (verify against current admin center and Microsoft's current docs): M365 admin center > Billing > Licenses, or group-based licensing changes; coordinate renewal/true-up timing with the client's agreement so savings actually land. Sequence removals after data handling is confirmed.

6. Verify: reclaimed licenses show unassigned/removed at true-up; downgraded users retain the features they need (spot-check); no mailbox/OneDrive lost. Leave a plain-text note: current vs. proposed license counts, reclaim/downgrade lines with per-line saving and impact, data-handling confirmed for leavers, approver, date, and rollback (reassign the license — note that a removed license can drop data after its grace period, so rollback is time-limited). Capture current per-SKU counts before changes; that is the rollback and the before/after evidence. Log time.

Guardrails: Removing a license can strand mailbox/OneDrive data after a grace period — confirm data handling BEFORE any removal. Downgrades silently remove features; enumerate what each drop takes away so the client approves the real trade, not just the saving. Never execute a downgrade/removal without client approval. When in doubt about data handling or a feature dependency, do nothing and escalate.
```
