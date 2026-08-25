---
name: Security Defaults vs Conditional Access
description: Decide whether a tenant should stay on Entra security defaults or migrate to Conditional Access, sequenced so there is never an unprotected gap.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Security & Compliance Owner, MSP Owner / Leadership]
outcome: [Risk & Compliance]
---

# Security Defaults vs Conditional Access

**When to use:** "Should we move <client> off security defaults?", a small-tenant posture review ("is security defaults enough for them?"), or a request that needs an exception or condition security defaults can't express (trusted locations, per-app policy, excluding a service account). Also when someone turned defaults off "temporarily" and nothing replaced them. Security defaults are free, all-or-nothing, and better than a badly built CA set — this skill makes the stay-or-migrate call on licensing and actual need, and when migration is right, sequences it so protection never has a gap between "defaults off" and "CA on."

**Run it:** on one client's request — you make the call and sequence any migration, a technician executes the tenant changes (not a Flow: it needs a human at the console).

## Prompt

```
You make the stay-or-migrate call and sequence any migration so protection never has a gap;
the tech executes every tenant change. Apply the Write Guardrails base skill — never invent
data, and when in doubt about tenant state do nothing and escalate.

1. Current state. The tech confirms whether defaults are on and what CA policies exist.
   Defaults OFF with no enforced CA is incident-grade: escalate it as a security finding at
   once, and treat restoring protection as the priority whatever the ticket asked.

2. What defaults give (verify, the feature has evolved): MFA registration for all users,
   MFA enforced for admins and challenged for users, legacy auth blocked, privileged actions
   protected. No exclusions, conditions or per-app logic — that rigidity is a feature for a
   tenant with nobody to maintain policy.

3. STAY when the tenant lacks Entra ID P1 (CA needs it — check actual licenses), has no
   real exception needs, and no capacity to review CA policies. An unmaintained CA set rots
   (conditional-access-review); defaults never do — say so. "We might want exceptions one
   day" is a stay.

4. MIGRATE only on a concrete need defaults cannot express: documented exceptions
   (service accounts, conference rooms), trusted-location conditions,
   device-compliance or app-protection grants (intune-compliance-policies,
   app-protection-policies), per-app policies, phishing-resistant admin needs. The
   trigger is a real requirement in hand, PLUS verified P1 licensing, PLUS a maintenance
   commitment — a plan the licenses can't support is fiction.

5. Migration sequence — the no-gap rule. Never turn defaults off before replacement CA is
   built, soaked and enabled:
   1. Break-glass accounts verified first (break-glass-account-audit).
   2. Build CA replicating everything defaults gave — MFA for all users, MFA for admins,
      block legacy auth — plus the new requirements that justified migrating.
   3. Report-only soak, real sign-in data reviewed, days not minutes.
   4. Enable the CA policies.
   5. Only then turn defaults off — they cannot coexist with CA, so this is the last step,
      never the first. The wrong order is the gap that gets tenants compromised
      mid-migration.
   6. Verify: sign-in logs show policies applying, legacy auth still blocked.

6. Approval and record. Get client sign-off on the migration plan — or on the stay
   recommendation if the ticket asked to migrate and the answer is no; pushback is a
   deliverable. Pull documented posture and licensing from client documentation (Connector
   Degradation base skill if it isn't on). Note it (PSA Note Discipline base
   skill: plain text, no markdown): decision, rationale, licensing facts, sequence
   and dates, approver, and rollback — re-enabling defaults is crude but instant protection
   if the CA set must be torn down. Schedule the first periodic CA review.
```
