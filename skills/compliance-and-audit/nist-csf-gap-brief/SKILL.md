---
name: NIST CSF Gap Brief
description: Map a client's current security posture to the NIST Cybersecurity Framework functions and return a plain-language gap brief — where they stand per function and what's missing — with no certification or compliance claims.
category: Compliance & Audit
tools: [search_tickets, search_itglue, search_hudu, liongard_cyber_risk_dashboard, add_ticket_note]
connectors: [IT Glue, Hudu, Liongard]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# NIST CSF Gap Brief

**When to use:** A client asks "how do we measure up" or wants a framework-anchored view of their security program; prep for a QBR, security roadmap, or budget conversation that needs a defensible structure; or a baseline before a formal third-party assessment.

**Run it:** across a client's posture and documentation (a framework gap brief).

## Prompt

```
Tell a client where their security posture sits against a recognized framework and where the
holes are — organized by the NIST CSF functions (Govern, Identify, Protect, Detect, Respond,
Recover). This produces a gap brief for planning conversations, not an assessment, audit, or
certification. NIST CSF has no certification to claim. Work it in order:

1. Set expectations up front in the brief: this is a posture-to-framework mapping for
   planning, based on available documentation and telemetry — not a formal NIST assessment,
   audit, or attestation, and it confers no certification.
2. Gather evidence per function from what exists: the client's documentation (in IT Glue and
   Hudu), ticket and change history, posture tooling (the cyber risk dashboard in Liongard
   where the inspector is present), and identity/security-hygiene findings. Note the evidence
   date — posture data ages.
3. Map findings to the six CSF functions:
   - Govern — is there ownership, policy, risk management, and roles defined?
   - Identify — asset inventory, data flows, risk assessment.
   - Protect — access control, MFA, training, data protection, maintenance.
   - Detect — monitoring, alerting, anomaly detection coverage.
   - Respond — incident response plan, communications, analysis.
   - Recover — backups, recovery planning, tested restore.
4. State each function as: what's in place (with evidence), what's missing or unverified, and
   the confidence level. Where evidence is absent, say "not documented / not verified" —
   never assume a control exists.
5. Rank the gaps by risk and effort so the brief drives action: the highest-risk missing
   controls first, with a plain-language "why this matters."
6. Keep it plain-language and framework-honest: reference the CSF functions accurately, don't
   invent maturity scores the evidence can't support, and don't imply the client "passes" or
   "is compliant."
7. Output the brief: per-function standing, ranked gap list, evidence dates, and the explicit
   scope/limitations statement. Route to the account/security owner; this informs a plan, it
   is not a deliverable a client should present as an assessment.

Guardrails — always:
- No certification or compliance claims — NIST CSF is a framework, not a certifiable
  standard; never state a client is "NIST certified/compliant" or "passes."
- Evidence-based only — a control counts as present only with documentation or telemetry;
  missing evidence = "not verified," never an assumed pass. No fabrication of controls,
  scores, or dates.
- State the scope and its limits plainly in the brief — availability of data bounds the
  conclusions, and posture evidence has a date.
- This is not a formal assessment and does not replace one — say so.
- Sanitized: no credentials or environment identifiers in the brief. Plain text only for
  PSA-synced notes.
- When in doubt, mark a control unverified rather than assumed.
```
