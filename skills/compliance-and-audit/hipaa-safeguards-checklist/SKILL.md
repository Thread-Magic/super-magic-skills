---
name: HIPAA Safeguards Checklist
description: Walk a healthcare client's environment against the HIPAA Security Rule technical safeguards, returning a checklist of what's in place versus missing.
category: Compliance & Audit
tools: [search_tickets, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# HIPAA Safeguards Checklist

**When to use:** A healthcare client or business associate asks for a technical review of their ePHI protections; prep before the client's own HIPAA risk analysis or a payer/partner assessment; or a roadmap/remediation conversation for a client that handles ePHI.

**Run it:** across a client's environment (a technical-safeguards checklist).

## Prompt

```
Healthcare clients (and their business associates) must protect electronic protected health
information (ePHI) under the HIPAA Security Rule. Review the technical safeguards an MSP can
actually observe and document what's in place versus missing — a technical checklist to feed
the client's compliance program. This is NOT legal advice and does not cover administrative
or physical safeguards, or the required risk analysis. Work it in order:

1. Frame the scope in the checklist: this covers the HIPAA Security Rule TECHNICAL safeguards
   observable in the environment. It does not constitute the required formal risk analysis,
   does not address administrative or physical safeguards, and is not legal or compliance
   advice. HIPAA determinations are the client's (with their counsel/compliance officer).
2. Identify where ePHI actually lives before checking controls — which systems, mailboxes,
   applications, and storage hold ePHI. If the client can't say, that scoping gap is the
   first finding.
3. Walk the technical safeguards checklist against evidence (the client's documentation,
   ticket/change history, security tooling):
   - Access control — unique user IDs, role-based access, automatic logoff, and (addressable)
     encryption/decryption of ePHI at rest.
   - Audit controls — logging and review of activity on systems holding ePHI.
   - Integrity — protection of ePHI from improper alteration/destruction.
   - Authentication — verifying users are who they claim (MFA, strong auth).
   - Transmission security — encryption of ePHI in transit (email, file transfer, remote
     access).
4. Mark each item in-place / gap / not-verified with the evidence behind it, and note the
   "addressable vs. required" nature where it applies — "addressable" means
   documented-justification-if-not-implemented, not optional. Don't let "addressable" become
   "skipped."
5. Rank gaps by risk to ePHI so the checklist drives remediation, in plain language.
6. Route to the client's compliance/privacy owner (and the MSP's security lead): the
   checklist informs the client's HIPAA program; the client and their counsel own the
   compliance determination and the required risk analysis.
7. Output: ePHI scope note, per-safeguard status with evidence, ranked gaps, evidence dates,
   and the scope/limitations statement.

Guardrails — always:
- Not legal advice, not a HIPAA compliance determination — say so in the output.
- Technical safeguards only — this does not cover administrative or physical safeguards, the
  required risk analysis, BAAs, or breach-notification obligations. Don't imply it's a
  complete HIPAA review.
- Evidence-based, no fabrication — a safeguard counts as present only with evidence; missing
  evidence is "not verified." Don't invent control status, encryption states, or dates.
- "Addressable" ≠ optional — flag addressable items honestly.
- Scope to where ePHI lives — an unscoped checklist is meaningless.
- Extra sanitization: never place actual ePHI, patient data, credentials, or environment
  identifiers in the checklist or notes. Plain text only for PSA-synced notes.
- When in doubt, mark not-verified and route to the compliance owner.
```
