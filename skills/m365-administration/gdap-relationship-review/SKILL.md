---
name: GDAP Relationship Review
description: Audit the MSP's delegated-admin (GDAP) relationships across client tenants — least-privilege roles, security-group mapping, expiring relationships, and unused access — before an expiry locks the MSP out mid-support. Use for periodic GDAP reviews, "what access do we have to <client>'s tenant", or a GDAP expiry warning.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, update_ticket, create_ticket, schedule_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner, MSP Owner / Leadership]
outcome: [Risk & Compliance]
---

# GDAP Relationship Review

**When to use:** GDAP is the MSP's own privileged access, so this review points the least-privilege lens inward — which client tenants the MSP can touch, with which roles, granted to which people, expiring when. Use for periodic (quarterly/semiannual) review of the MSP's delegated access across all managed tenants, a GDAP expiry warning or access to a client tenant that suddenly stopped working, "what can we actually do in <client>'s tenant?" (audit/insurance/client-security-review), or after MSP staff changes to confirm role-group membership still matches who should hold client access. The two failure modes are opposite and both real — over-broad roles nobody remembers granting, and an expiry nobody tracked that cuts access during an incident.

**Run it:** as an on-demand review across every client tenant the MSP touches — you compile the dated artifact and prepare remediation, a technician exports from Partner Center and executes changes (not a Flow: no schedule trigger, and changes need a human at the console).

## Prompt

```
You are auditing the MSP's GDAP relationships across client tenants for least privilege, correct group mapping, and expiry tracking. The technician exports from Partner Center and executes changes; the agent compiles the dated artifact and prepares remediation. Never report a change as done on intention — never invent data. All access data is point-in-time: date the export, and re-pull before executing changes planned more than two weeks earlier.

1. Inventory every relationship. The tech exports the GDAP relationship list from Partner Center: client tenant, roles granted, duration and expiry date, auto-extend status, and the MSP security groups mapped to each role. The agent compiles the dated master table — this is the review artifact, and it lives in the MSP's own documentation (check the knowledge base and the client's documentation for where the standard says it goes; skip gracefully if not connected). Cross-check against the client list: active clients with no relationship (access debt about to surprise someone) and relationships to tenants that are no longer clients (remove — offboarded clients retaining MSP access is a serious finding in both directions).

2. Grade roles against least privilege. For each relationship, compare granted roles to what the MSP actually does for that client. Flag: Global Administrator in a GDAP relationship (should be rare-to-absent; day-to-day work maps to scoped roles — verify current Microsoft least-privilege guidance, as recommended role sets evolve); roles granted but unused since the last review; and "every role in the list" relationships created by early-days defaults. Draft the trimmed role set per client. Global Administrator in a GDAP relationship requires a written, client-approved justification or it is a finding — no grandfathering.

3. Audit the people side — group mapping. Roles are only as scoped as the security groups holding them: verify each role-to-group mapping, and that group membership is current MSP staff with a need (tie-in: staff offboarding must remove these memberships — if the MSP's own offboarding checklist lacks that step, file the process fix). Everyone-in-one-group granting all roles to all techs defeats GDAP's point; propose tiered groups (helpdesk vs escalation vs project) where absent.

4. Handle expiries deliberately. GDAP relationships are time-boxed by design (max two years). For each: decide renew vs auto-extend vs lapse (lapse is correct for departed clients). Schedule renewals comfortably before expiry — renewing requires client approval flow, so "week of expiry" is too late; an expired relationship during a client incident is the nightmare this review exists to prevent. Flag anything expiring within 90 days as this review's action list. Never let a needed relationship lapse for process reasons; an unplanned expiry discovered during this review is handled before the review continues.

5. Change with client consent. Trimming roles or re-scoping a relationship is a change to the client's tenant access: send an approval request to the client authority for role reductions and removals (clients approve GDAP changes on their side regardless — align the paperwork), and to MSP leadership for internal group restructures. Sequence trims so active support work isn't cut mid-ticket: verify the trimmed role set against the last 90 days of work types for that client before removing. Rollback = re-request the roles, which needs client approval again; say so in the plan.

6. Document and recur. Leave a plain-text summary note documenting what/why/when/rollback: relationship count, findings by class (over-broad roles, unused relationships, expiring soon, group-mapping issues, offboarded-client access), remediation tickets raised (one per client needing change), and the next review scheduled. The full per-client table goes in the MSP's documentation system, not a PSA-synced note.

Relationships to offboarded clients are removed with the client notified — retained access to a former client's tenant is indefensible in any audit; the finding is escalated, not batched. This review covers the MSP's cross-tenant access; per-tenant admin hygiene inside a client tenant is global-admin-audit's job — run both, confuse neither. When in doubt, do nothing and escalate.
```
