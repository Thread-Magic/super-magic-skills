---
name: Identity MFA Health Check
description: Review a client's identity hygiene — MFA coverage, privileged accounts, and stale accounts — and return ranked findings with remediation recommendations.
category: Security
tools: [liongard_identity, search_tickets, add_ticket_note]
connectors: [Liongard]
scope: global
flow: no
role: [Security & Compliance Owner, CSM / Account Manager]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# Identity MFA Health Check

**When to use:** "Check <client>'s MFA coverage" / "audit their identity hygiene"; prep for a posture review, QBR, or insurance questionnaire; or after an identity incident, to find the next weakest account.

**Run it:** across a client's identity accounts (an identity-hygiene review).

## Prompt

```
Identity is where most incidents start, so this is the highest-yield health check: who
lacks MFA, which privileged accounts are exposed, and which accounts should no longer exist —
ranked by how badly each finding can hurt. Report and recommend only; never disable,
remove, or modify an account from this skill. Work it in order:

1. Pull the client's identity data from Liongard: per-account MFA enrollment, privileged
   role assignments, last sign-in activity, and account enabled/disabled state. Date the
   pull.
2. Build the finding classes, ranked worst-first: privileged accounts without MFA
   (critical, always first); enabled privileged accounts that are stale (no sign-in in
   60–90 days — dormant power is attacker fuel); enabled user accounts without MFA; stale
   enabled user accounts; service or shared accounts with interactive sign-in ability.
3. Cross-check every stale account against offboarding history: search for an offboarding or
   departure ticket matching the account. A stale account WITH an offboarding ticket is an
   incomplete offboarding (process gap); a stale account with NO ticket is an unknown —
   flag it for the client to identify before anyone touches it.
4. Verify "stale" isn't seasonal before recommending removal: contractors, seasonal staff,
   and break-glass accounts legitimately sit idle. Mark those "verify with client" rather
   than "disable."
5. Output the ranked findings table (finding class, account count, named accounts,
   evidence, recommended action) plus the two or three highest-impact recommendations up
   top. Leave it as a plain-text note on request.

Guardrails — always:
- Report and recommend only — never disable, remove, or modify an account; changes go
  through the client's change process.
- Never recommend disabling an account whose staleness isn't corroborated (offboarding
  ticket, client confirmation, or known purpose).
- Privileged findings are never buried: they lead the output regardless of counts
  elsewhere.
- Date the data; identity posture drifts weekly.
- Result-cap honesty when cross-checking tickets — "no offboarding ticket found" means none
  found within the search, and the note says so.
- Degradation: Liongard absent → offer the offboarding-ticket-based staleness check only,
  clearly labeled partial; do not estimate MFA coverage without instrumentation. Never
  invent coverage numbers.
```
