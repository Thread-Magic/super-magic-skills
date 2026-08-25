---
name: CMMC Readiness Brief
description: Produce a CMMC level-readiness snapshot for a defense-adjacent client with likely standing and obvious gaps — never a certification or formal assessment.
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
Defense-adjacent clients handling federal contract information (FCI) or controlled unclassified
information (CUI) face CMMC. Give them an early, honest readiness snapshot against a target
level's practices, and hand the real work to the compliance owner. Certification comes only from
an authorized C3PAO after a formal assessment: this brief is NEITHER.

1. Set the frame explicitly in the brief — an informal readiness snapshot from available
   evidence, not an assessment, not a gap analysis of record, not certification. Only an
   authorized C3PAO can assess and certify at Level 2 and above.

2. Establish the target and scope: which level the client is aiming at (Level 1 for FCI, Level 2
   for CUI) and what data and systems are in scope. Level 2 maps to NIST SP 800-171, so anchor to
   that. If the client hasn't identified CUI and FCI boundaries, that scoping gap is itself the
   first finding.

3. Gather evidence from what exists: the client's documentation in IT Glue and Hudu, ticket and
   change history, and any existing NIST CSF or 800-171 work (nist-csf-gap-brief gives the
   broader posture picture). Note evidence dates.

4. Map current state to the target level's practice families at summary level — access control,
   identification and authentication, audit and accountability, configuration management,
   incident response, media protection. Mark each likely-in-place, likely-gap or unverified, with
   its evidence.

5. Call out the CMMC-specific traps plainly: CUI scoping and boundary definition, whether a
   System Security Plan and POA&M exist, and that at Level 2 self-attestation isn't enough where
   a C3PAO assessment is required.

6. Route the brief to the client's compliance or contract owner and the MSP's security lead, with
   the clear message that formal readiness and certification need a qualified assessor. You
   produce the snapshot, you do not attest readiness.

7. Output the target level, the scope note, the per-family readiness snapshot, the top gaps
   ranked, evidence dates, and the scope and limitations statement.

Never state or imply that a client "is CMMC ready", "compliant" or "certified" — this is a
snapshot to inform next steps, and it does not substitute for a qualified assessor. Practices
count as in-place only with documentation; missing evidence is "unverified", and SSP or POA&M
contents, control mappings and dates are never invented. Scoping is a finding, not an assumption:
if CUI and FCI boundaries aren't defined, say so. State limitations plainly and date the
evidence. Keep the brief sanitized — no credentials, contract numbers or environment identifiers
— in plain text for PSA sync (PSA Note Discipline base skill). If the documentation platforms
aren't connected, apply the Connector Degradation base skill and say which evidence you couldn't
reach. When in doubt, mark unverified and escalate to the compliance owner.
```
