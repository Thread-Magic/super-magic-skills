---
name: Tenant Onboarding Checklist
description: Onboard a new Microsoft 365 tenant: GDAP scoping, break-glass accounts, security-defaults-vs-CA decision, admin and licensing inventory.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, update_ticket, create_ticket, schedule_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu, Liongard]
scope: global
flow: no
role: [Service & Ops Manager, Security & Compliance Owner]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# Tenant Onboarding Checklist

**When to use:** "We just signed <client> — get their M365 tenant under management," standing up a brand-new tenant, inheriting a tenant from another MSP ("takeover" onboarding — the checklist doubles as the trust-nothing audit), or retro-fitting the standard onto a tenant onboarded informally. The first weeks with a new tenant decide whether it becomes a documented, recoverable environment or a mystery box — this skill turns onboarding into a fixed checklist (access, safety rails, baseline decisions, inventory, documentation) with each item a tracked ticket, not a memory.

**Run it:** as a whole-tenant onboarding pass — you prepare the checklist and compile inventories, technicians execute all tenant changes (not a Flow: no schedule trigger, and changes need a human at the console).

## Prompt

```
You prepare the checklist, compile inventories, and draft decisions; technicians execute all tenant changes. Never invent data — every inventory is point-in-time and dated; a takeover tenant changes under you while you onboard it.

1. Access — GDAP first, correctly scoped. Establish the delegated-admin relationship via GDAP with least-privilege roles mapped to MSP security groups (not Global Admin for everyone; see gdap-relationship-review for the role standard and expiry handling). No shared "admin@" credentials, no standing GA accounts created for convenience. Record the relationship, roles, and expiry in the client's documentation.

2. Safety rails before changes — break-glass accounts. Create two emergency-access accounts per the break-glass-account-audit standard (cloud-only, phishing-resistant or sealed credentials, excluded from CA, sign-in alerting, quarterly test). These exist BEFORE any policy work — no exceptions, including "we'll do it right after" — so nothing done later can lock everyone out.

3. The baseline decision — security defaults vs Conditional Access. Run the security-defaults-vs-ca decision: licensing, exception needs, and complexity determine which posture this tenant gets. Record the decision and rationale — this is the single most consequential onboarding choice and it must be a written one with a named approver. If CA: build the baseline with report-only soak per conditional-access-review; if security defaults: verify they are actually on.

4. Inventory — trust nothing, count everything. Tech pulls, agent compiles (all dated, labeled point-in-time):
   - Admin-role holders (run the global-admin-audit skill — takeover tenants routinely contain the previous MSP's accounts, which are offboarding line items with a deadline).
   - Users, licenses assigned vs purchased, and obvious waste.
   - Guests (guest-access-audit if the count warrants).
   - Devices and management state (enrolled vs unmanaged), plus MFA method quality (mfa-methods-audit) as a fast-follow.
   - Existing CA policies, mail rules, and third-party app consents worth flagging.
   If the partner runs a Liongard inspector for M365/Entra, confirm via Liongard that the inspector exists and last ran successfully, then use its identity/query pulls — state dataprint age in the output. No inspector, or Liongard not connected → console exports by the tech, degrading gracefully. Liongard reads require the inspector to exist and have run recently; verify and state dataprint age.

5. Legacy authentication check. Establish whether legacy auth is blocked and whether anything still uses it (sign-in log evidence, window stated). If traffic exists, that is a remediation ticket with named dependencies, not a same-day block.

6. Documentation. Everything lands in the client's documentation (if connected — otherwise flag the doc gap): tenant details, GDAP scope, break-glass procedure (credential location reference — never the credentials), baseline decision, inventories, and deviations from the MSP standard with reasons. The PSA note carries the summary and references (leave a note); the doc system carries the detail.

7. Ticketize and schedule. Each checklist item is a ticket (raise one per item) with an owner; remediations found in steps 4-5 become their own tickets. Takeover tenants: previous-MSP access removal is approval-gated with the client (send an approval request) and scheduled — never silently skipped; standing third-party admin access is the top takeover risk. Schedule the recurring hygiene the standard requires: quarterly break-glass test, CA review, guest audit, GDAP expiry check. Post the onboarding summary note: items completed, open remediations, decisions made with approvers.

When in doubt about authorization or standing third-party access, do nothing and escalate.
```
