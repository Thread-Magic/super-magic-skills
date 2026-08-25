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
You prepare and compile; technicians execute every tenant change. Apply the Write Guardrails base skill — never invent data, and when in doubt about
authorization or standing third-party access, do nothing and escalate.

1. Access — GDAP first, least-privilege roles mapped to MSP security groups, not Global
   Admin for everyone (gdap-relationship-review owns the role standard and expiry). No
   shared "admin@" credentials, no standing GA accounts for convenience.

2. Safety rails before any policy work — two break-glass accounts per
   break-glass-account-audit: cloud-only, phishing-resistant or sealed credentials, excluded
   from CA, sign-in alerting, quarterly test. They exist BEFORE step 3, no exceptions, so
   nothing done later can lock everyone out.

3. Baseline — security defaults vs Conditional Access. Run security-defaults-vs-ca: licensing, exception needs and maintenance capacity decide it.
   Record the decision, rationale and a named approver. If CA, build the baseline with a
   report-only soak per conditional-access-review; if defaults, verify they are on.

4. Inventory — trust nothing, count everything. All dated and labelled point-in-time:
   - Admin-role holders (global-admin-audit). Takeover tenants routinely still carry the
     previous MSP's accounts — offboarding line items with a deadline.
   - Users, licenses assigned versus purchased, obvious waste.
   - Guests (guest-access-audit), devices and management state, MFA method quality
     (mfa-methods-audit).
   - Existing CA policies, mail rules, third-party app consents worth flagging.
   - Legacy authentication: blocked or not, and does anything still use it? Sign-in-log
     evidence, window stated. Live traffic is a remediation ticket with named dependencies,
     never a same-day block.
   Where a Liongard M365/Entra inspector exists, confirm it last ran and state the dataprint
   age; otherwise the tech takes console exports (Connector Degradation base skill: name the
   missing integration and carry on). Apply Sweep Honesty — "at least
   N", plus what you could not check.

5. Documentation. Tenant details, GDAP scope and expiry, break-glass procedure (where the
   credentials live, never the credentials), the baseline decision, the inventories, and
   deviations from the standard with reasons. Flag the gap if nothing is connected.

6. Ticketize. Each checklist item is a ticket with an owner; remediations found above get
   their own. On a takeover, removing the previous MSP's access is approval-gated
   with the client and scheduled — never silently skipped: standing third-party admin access
   is the top takeover risk. Schedule the quarterly break-glass test, CA review, guest audit
   and GDAP expiry check. Close with a summary note — items done, open remediations,
   decisions and approvers (PSA Note Discipline base skill: plain text, no markdown or
   emojis).
```
