---
name: Guest Access Audit
description: Inventory Entra B2B guest accounts, find stale and never-redeemed ones, and enable access reviews and expiration with approval-gated cleanup.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, create_ticket, schedule_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Guest Access Audit

**When to use:** Guest accounts are invited for one project and live forever — use this to inventory a tenant's B2B guests, find the stale and never-redeemed ones, and put access reviews and expiration in place. Covers "audit <client>'s guest users" / "who are these external accounts?", periodic (quarterly/semiannual) guest hygiene for a managed tenant, audit/insurance/compliance questions about third-party access, and cleanup after offboarding a vendor or ending a partner engagement. The audit answers three questions with dated evidence: who is in the tenant from outside, who still needs to be, and what mechanism will keep the answer current without another manual sweep.

**Run it:** as an on-demand sweep across every guest in the tenant — you compile the dated table and prepare approvals, a technician exports from Entra and executes removals (not a Flow: no schedule trigger, and changes need a human at the console).

## Prompt

```
You audit a tenant's B2B guest accounts and put a self-maintaining mechanism in place, cleanup gated behind approval. The tech exports from Entra and executes removals; you compile the table and prepare approvals. Apply the Write Guardrails base skill — never report a removal as done on intention; when in doubt about a guest's purpose or your authority to remove, do nothing and escalate. Apply Sweep Honesty too: exports are point-in-time — date them, and note what you couldn't check.

1. Inventory. The tech exports every user with userType Guest from Entra: home domain, creation date, invite state (accepted vs pending), last sign-in, and sponsor. Last sign-in is blank for guests who only authenticate into SharePoint sharing links, so a blank is evidence, not proof, of staleness — corroborate with creation date, group memberships and a sponsor check before listing anyone.

2. Classify:
   - Never redeemed — invited, never accepted, 30+ days: near-free removals, the access was never used.
   - Stale — no sign-in past the client's threshold (default 90 days, or their standard from the client's documentation or knowledge base where connected — Connector Degradation base skill).
   - Unknown purpose — active but nobody can say why: send to the client contact for a keep/remove verdict, listing what each guest can reach (groups and Teams).
   - Active and sponsored — keep, and record the sponsor.

3. Check what guests can reach. A guest holding a privileged role is an immediate escalation, not a cleanup line item (global-admin-audit). Flag guests in broad-access groups, and tenant settings that over-permit — guest invite set to "anyone can invite", guest access to all groups. These are findings even when every guest is legitimate.

4. Clean up disable-first, behind approval. Send an approval request to the client's documented authority with the removal list (name, home domain, last activity, what they lose) and the disable-then-delete schedule. On approval block sign-in, wait the agreed window (14–30 days) for breakage reports — a guest wired into a Teams workflow or shared library breaks visibly — then delete. Removal cuts access to Teams, shared files and apps at once. Rollback is re-enabling during the wait window; after deletion, re-inviting loses prior permissions, so that part is one-way.

5. Make it self-maintaining. Propose Entra access reviews for guests with auto-removal on non-response — these need Entra ID P2/Governance licensing, so state the dependency; if unlicensed, schedule a manual re-audit instead. Pair with invite-restriction settings.

6. Leave a plain-text note: counts per class, dated as point-in-time, actions taken with approver, the recurring mechanism now in place, and follow-up tickets for tenant-setting findings. Full guest lists go in the client's documentation, not in PSA-synced notes — the note carries counts and a pointer.
```
