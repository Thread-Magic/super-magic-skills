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
You are auditing a tenant's B2B guest accounts and putting a self-maintaining mechanism in place, with cleanup gated behind approval. The technician exports from Entra and executes removals; the agent compiles the dated table and prepares approvals. Never report a removal as done on intention — never invent data. Counts and activity windows are point-in-time console exports — date them and label them as such; do not present the inventory as continuously true.

1. Inventory. The tech exports all users with userType Guest from Entra, with: display name, home domain, creation date, invite state (accepted vs pending), last sign-in date, and sponsor/inviter if recorded. The agent compiles the dated table. Note honestly where data is missing — last sign-in is blank for guests who authenticate only into SharePoint sharing links, so absence of sign-in is evidence, not proof, of staleness.

2. Classify:
   - Never redeemed — invited, never accepted (30+ days): near-free removals; the access was never used.
   - Stale — no sign-in activity past the client's threshold (default 90 days; use the client's documented standard if one exists in the client's documentation or the knowledge base, skipping gracefully if not connected).
   - Unknown-purpose — active but no one can say why: route to the client contact for a keep/remove verdict, listing what each guest can reach (group and Teams memberships).
   - Active and sponsored — keep; record the sponsor.
   Blank sign-in data is not a staleness verdict on its own — corroborate (creation date, group memberships, sponsor check) before listing a guest for removal.

3. Check what guests can reach. Flag guests holding privileged roles (critical finding — cross-reference global-admin-audit; a guest with a privileged role is an immediate escalation, not a cleanup line item), guests in broad-access groups, and tenant settings that over-permit (guest invite settings set to "anyone can invite", guest access to all groups). These are findings even if every individual guest is legitimate.

4. Cleanup with a soft-delete pattern. For approved removals: disable (block sign-in) first, wait an agreed window (e.g., 14–30 days) for breakage reports — a guest wired into a Teams workflow or shared library breaks visibly — then delete. Removing a guest removes their access to Teams, shared files, and apps at once; say so in the approval. No guest deletion without approval and the disable-first wait window; deletion severs sharing links and Teams membership irreversibly.

5. Approval gate. Send an approval request to the client's documented authority with the removal list (name + home domain + last activity + what they lose), the disable-then-delete schedule, and the rollback (re-enable during the wait window; re-invite after deletion loses prior permissions — that part is one-way).

6. Make it self-maintaining. Propose Entra access reviews for guests (requires Entra ID P2/Governance licensing — state the dependency; if unlicensed, schedule the manual re-audit instead) with auto-removal on non-response, and sensible invite-restriction settings.

7. Document what/why/when/rollback in a plain-text note: counts per class (dated, labeled as point-in-time), actions taken with approver, the recurring mechanism now in place, and follow-up tickets raised for tenant-setting findings. Full guest lists with names and domains go in the client's documentation system, not in PSA-synced notes — the note carries counts and the storage reference.

When in doubt about a guest's purpose or authorization to remove, do nothing and escalate.
```
