---
name: GDAP Relationship Review
description: Audit MSP GDAP delegated-admin relationships across client tenants for least-privilege roles, security-group mapping, expiries, and unused access.
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
Audit the MSP's GDAP relationships across client tenants. The tech exports from Partner Center
and executes changes; you compile and prepare remediation. Access data is point-in-time: date
every export and re-pull before executing a plan older than two weeks (Sweep Honesty base skill
— say "at least N" when a list may be capped).

1. Inventory. The tech exports the GDAP list from Partner Center: client tenant, roles granted,
   duration and expiry, auto-extend status, and the security groups mapped to each role.
   Compile the dated master table into the MSP's documentation; note it if IT Glue or Hudu
   isn't connected (Connector Degradation base skill). Cross-check the client list both ways:
   active clients with no relationship, and relationships to tenants that are no longer
   clients.

2. Grade roles against least privilege — granted roles versus what the MSP actually does there.
   Flag roles unused since the last review and "every role in the list" relationships left by
   early-days defaults; verify current Microsoft least-privilege guidance. Draft the trimmed
   role set per client. Global Administrator in a relationship needs a written, client-approved
   justification or it is a finding — no grandfathering.

3. Audit the people side: roles are only as scoped as the groups holding them. Verify each
   role-to-group mapping and that membership is current MSP staff with a need. If the MSP's
   staff-offboarding checklist doesn't remove these memberships, file the process fix. Propose
   tiered groups (helpdesk, escalation, project) where one group grants all roles to all techs.

4. Handle expiries. Relationships are time-boxed, two years maximum. For each: renew,
   auto-extend, or lapse (correct for departed clients). Renewal runs through the client's
   approval flow, so schedule it well before expiry. Anything expiring within 90 days is this
   review's action list; an unplanned expiry found here is handled first.

5. Change with client consent. Trimming roles changes the client's tenant access: send an
   approval request to the client authority for reductions and removals, and to MSP leadership
   for group restructures. Check the trimmed set against the last 90 days of work types so
   support isn't cut mid-ticket. Rollback means re-requesting the roles, which needs client
   approval again.

6. Leave a plain-text summary note, no markdown or emojis (PSA Note Discipline base skill):
   relationship count, findings by class, one remediation ticket per client needing change, and
   the next review date. The per-client table goes in the MSP's documentation, not a PSA-synced
   note.

Access retained to a former client's tenant is removed and the client notified — escalate that
finding, don't batch it. This review covers cross-tenant access only; per-tenant admin hygiene
is a separate job. When in doubt, do nothing and escalate.
```
