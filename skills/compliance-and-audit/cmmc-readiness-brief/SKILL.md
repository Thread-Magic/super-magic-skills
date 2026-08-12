---
name: CMMC Readiness Brief
description: Produce a CMMC level-readiness snapshot for a defense-adjacent client — where they likely stand against the target level's practices and the obvious gaps — then flag it to the compliance owner; never a certification or an assessment.
category: Compliance & Audit
tools: [search_tickets, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# CMMC Readiness Brief

**When to use:** A defense-adjacent client asks where they stand on CMMC, or a contract clause (DFARS) surfaces the requirement; early scoping before they engage a C3PAO or readiness consultant; or a roadmap/budget conversation for a client heading toward a CMMC requirement.

**Run it:** across a client's documentation and history (a readiness snapshot).

## Prompt

```
Defense-contractor and defense-adjacent clients handling federal contract information (FCI)
or controlled unclassified information (CUI) face CMMC. Give them an early, honest readiness
snapshot against a target CMMC level's practices and hand the real work to the compliance
owner. CMMC certification is granted only by an authorized C3PAO after a formal assessment —
this brief is NEITHER a certification NOR an assessment. Work it in order:

1. Set the frame explicitly in the brief: this is an informal readiness snapshot based on
   available evidence, not a CMMC assessment, not a gap analysis of record, and not
   certification. Only an authorized C3PAO (for Level 2+) can assess and certify.
2. Establish the target and scope: which CMMC level the client is aiming at (Level 1 FCI /
   Level 2 CUI), and what data and systems are in scope. CMMC Level 2 maps to NIST SP
   800-171 practices — anchor to that. If the client hasn't identified CUI/FCI boundaries,
   that scoping gap is itself the first finding.
3. Gather evidence from what exists: the client's documentation (in IT Glue and Hudu),
   ticket/change history, and any existing NIST CSF or 800-171 work (nist-csf-gap-brief for
   the broader posture picture). Note evidence dates.
4. Map current state to the target level's practice families at a summary level (access
   control, identification & authentication, audit & accountability, config management,
   incident response, media protection, etc.) — for each: likely-in-place, likely-gap, or
   unknown/unverified, with the evidence behind it.
5. Call out the CMMC-specific traps plainly: CUI scoping and boundary definition, the System
   Security Plan (SSP) and POA&M existence, and — for Level 2 — that self-attestation is not
   enough where a C3PAO assessment is required.
6. Flag to the compliance owner: the brief's destination is the client's compliance/contract
   owner (and the MSP's security lead), with the clear message that formal readiness and
   certification require a qualified assessor. You produce the snapshot; you do not attest
   readiness.
7. Output: target level, scope note, per-family readiness snapshot, the top gaps ranked,
   evidence dates, and the scope/limitations statement.

Guardrails — always:
- Never a certification or a formal assessment — never state or imply a client "is CMMC
  ready/compliant/certified." This is a snapshot to inform next steps.
- Flag to the compliance owner — this skill's output routes to the human accountable for
  compliance; it does not substitute for a qualified assessor.
- Evidence-based, no fabrication — practices count as in-place only with documentation;
  missing evidence is "unverified." Don't invent SSP/POA&M contents, control mappings, or
  dates.
- Scoping is a finding, not an assumption — if CUI/FCI boundaries aren't defined, say so.
- State limitations plainly and date the evidence.
- Sanitized: no credentials, contract numbers, or environment identifiers in the brief. Plain
  text only for PSA-synced notes.
- When in doubt, mark unverified and escalate to the compliance owner.
```
