---
name: Liongard Active Directory Read
description: Answer on-prem Active Directory questions from the Liongard AD inspector — privileged group membership, stale accounts, password-policy posture, GPO changes, FSMO roles, and DC health — without a domain login.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_identity, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Active Directory Read

**When to use:** "Who's in Domain Admins at <client> / any new privileged-group members?", "which accounts haven't logged in for 90 days?", domain password-policy and password-never-expires questions, "did a GPO change / which DC holds FSMO?" — on-prem AD facts without an RDP session.

**Run it:** on one client — name the client and the AD question.

## Prompt

```
Answer an on-prem Active Directory question for CLIENT_NAME from the Liongard Active Directory inspector. Read-only — membership changes, GPO edits, and account disables go to a technician through the client's change process.

1. Find the Active Directory inspector for this client and confirm it ran recently; date the data — every answer carries "as of <timestamp>." AD inspectors run through an on-prem agent, so a failing inspector often means the agent host itself is down, which is its own finding.
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint before trusting a zero:
   - Privileged groups → membership of Domain Admins, Enterprise Admins, Schema Admins, Administrators, and client-specific admin groups. Compare against the last authorized state; every member must be explainable. For unexplained recent additions, cross-check ticket history for the authorizing change and escalate the unclaimed ones.
   - Stale accounts → enabled users by last-logon timestamp. Last-logon replicates lazily — treat 90 days as the honest floor, never as exact last activity. A stale enabled account WITH an offboarding ticket is an incomplete offboarding.
   - Password posture → domain policy (min length, complexity, max age, lockout) plus per-account flags: password-never-expires, password-not-required, reversible encryption. Service accounts legitimately carry never-expires — mark "verify purpose," don't auto-flag.
   - GPO / structural changes → check what changed for GPO modifications, new OUs, trust changes, DC additions, with before/after where captured.
   - Domain plumbing → FSMO role holders, DC list and OS versions, functional levels. A DC on an EOL OS is a lead for the Windows Server EOL sweep.
   - Open-ended → ask in plain language, then verify with targeted reads.
3. When the client is hybrid, reconcile against the cross-system identity view — the same human may show different MFA/staleness posture on-prem vs. Entra (disabled in AD but active in Entra is a classic offboarding gap). Never recommend disabling an account on data staleness alone.
4. Privileged-group findings lead the output regardless of what was asked. Output: direct answer, evidence rows, data as-of date, replication caveat where last-logon is involved. Leave a plain-text note on request. Degradation: no AD inspector → ticket history and documentation only, labeled "not instrumented"; never guess group membership from memory.
```
