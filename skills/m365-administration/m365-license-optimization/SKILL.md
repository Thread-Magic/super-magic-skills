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
You right-size a client's Microsoft 365 licensing from evidence. This is a proposal, never an executed action — a technician or account manager makes changes only after client approval. Apply the Write Guardrails base skill: never present an estimate as exact, and when in doubt do nothing and escalate.

1. Pull the assignment evidence: assigned vs. purchased per SKU, unassigned licenses, and disabled or departed users still holding a paid license. If Liongard's M365 inspector is connected, read assignments from it and state the dataprint age; otherwise use a point-in-time admin-center export and say so. Add context from the client's documentation, knowledge base and prior tickets; if an integration isn't connected, say so (Connector Degradation base skill). Apply the Sweep Honesty base skill — if a query capped, say "at least N" and name what you couldn't check. Count, don't estimate.

2. Categorize the opportunities, cheapest risk first:
   - Unassigned but purchased licenses — reclaim at the next true-up; pure saving, no user impact.
   - Disabled or departed users still licensed — remove only after confirming the account is genuinely a leaver and its mailbox and OneDrive are handled (retention or handover). Pulling a license can strand data; check onedrive-storage-governance first.
   - Over-provisioned users, e.g. E5 for someone using only mail and Office — candidate downgrade. Verify the specific features they actually use (Defender, Power BI, audit, phone) first; a downgrade that removes something they rely on is a false saving.
   - Redundant add-ons — standalone SKUs already included in a suite the user holds.

3. Model each downgrade's impact explicitly. Dropping from E5 or E3 silently removes features — advanced Defender, DLP, retention, archiving, Teams Phone. List what each change takes away so the client decides with eyes open.

4. Present the plan with per-line saving and risk, and get explicit client approval before any license is removed or changed.

5. Prepare execution, verified against the current admin center: Billing > Licenses, or group-based licensing changes. Sequence removals after data handling is confirmed, and time them with the client's renewal or true-up.

6. Verify: reclaimed licenses show unassigned or removed at true-up, downgraded users still have the features they need (spot-check), no mailbox or OneDrive lost. Leave a plain-text note — current vs. proposed counts, each line with its saving and impact, data handling confirmed for leavers, approver, date, and rollback. Capture current per-SKU counts before any change: that is the rollback and the before/after evidence. Log time.

Removing a license strands mailbox and OneDrive data, and after the grace period that data is deleted — confirm data handling before any removal, and treat reassigning a license as a time-limited rollback, not a safety net.
```
