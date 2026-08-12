---
name: Liongard Duo Read
description: Answer Duo MFA posture questions via the Liongard Duo inspector: enrollment coverage, bypass users, admin list, and protected-integration inventory.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Duo Read

**When to use:** "What's Duo enrollment coverage at <client> / who still isn't enrolled?", "any users in bypass status?", "who are the Duo admins / which apps are behind Duo?", or feeding MFA-coverage numbers to a posture review, QBR, or insurance questionnaire.

**Run it:** on one client — name the client and the Duo question.

## Prompt

```
Answer a Duo posture question for CLIENT_NAME from the Liongard Duo inspector. Read-only — enrollment pushes, bypass revocation, and admin changes are technician actions.

1. Find the Duo inspector for this client and confirm it ran recently; date the data.
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint before trusting a zero:
   - Enrollment coverage → users by status: active-enrolled, pending/not-enrolled, disabled, bypass. Coverage percent = enrolled / active users, and the denominator matters: reconcile the Duo user count against the directory source (the AD or M365 read) — a 100% Duo enrollment over half the workforce is a 50% finding. Never report coverage percent without naming the denominator and its source.
   - Bypass users → every account in bypass is a standing MFA hole; for each, cross-check ticket history for the authorizing request and its intended expiry. Bypass with no ticket, or past its stated window, is a flagged finding. Bypass findings are never softened.
   - Admins → the Duo administrator list, each explainable; Duo admins can weaken MFA for everyone, so unexplained entries escalate.
   - Integrations → the protected-application inventory (VPN, RDP gateways, M365, LDAP) read against the client's documented stack — the gap list is usually the QBR's most actionable slide.
   - Changes → check what changed for new bypass grants, admin additions, integration changes.
   - Open-ended → ask in plain language, verified before reporting.
3. Output: coverage numbers with both numerator and denominator stated, bypass and admin findings flagged first, integration gap list, data as-of timestamp. Leave a plain-text note on request. Degradation: no Duo inspector → answer from directory-side MFA data and tickets, labeled "Duo not instrumented — coverage from directory view only."
```
