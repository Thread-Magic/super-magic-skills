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
Under the HIPAA Security Rule, healthcare clients and their business associates must protect
electronic protected health information (ePHI). Review the technical safeguards an MSP can
actually observe and document what is in place versus missing, as a checklist feeding the
client's compliance program.

1. Frame the scope in the checklist itself: it covers the TECHNICAL safeguards observable in the
   environment, is not the required formal risk analysis, and does not address administrative or
   physical safeguards. HIPAA determinations belong to the client, with their counsel or
   compliance officer.

2. Identify where ePHI actually lives before checking controls: which systems, mailboxes,
   applications and storage hold it. If the client can't say, that scoping gap is the first
   finding.

3. Walk the safeguards against evidence from the client's documentation, ticket and change
   history and security tooling:
   - Access control: unique user IDs, role-based access, automatic logoff, and (addressable)
     encryption of ePHI at rest.
   - Audit controls: logging and review of activity on systems holding ePHI.
   - Integrity: protection of ePHI from improper alteration or destruction.
   - Authentication: verifying users are who they claim (MFA, strong auth).
   - Transmission security: encryption of ePHI in transit — email, file transfer, remote access.

4. Mark each item in-place, gap or not-verified with its evidence, and note where an item is
   addressable rather than required. "Addressable" means documented justification if not
   implemented — never "skipped".

5. Rank the gaps by risk to ePHI in plain language, so the checklist drives remediation.

6. Route to the client's compliance or privacy owner and the MSP's security lead: the checklist
   informs the client's HIPAA program, and the client and their counsel own the determination and
   the required risk analysis.

7. Output the ePHI scope note, per-safeguard status with evidence, ranked gaps, evidence dates,
   and the scope and limitations statement.

Say plainly in the output that this is not legal advice and not a HIPAA compliance determination.
Technical safeguards only: it does not cover administrative or physical safeguards, the required
risk analysis, business associate agreements, or breach-notification obligations, so never imply
a complete HIPAA review. A safeguard counts as present only with evidence; missing evidence is
"not verified", and control status, encryption states and dates are never invented. Never put
actual ePHI, patient data, credentials or environment identifiers in the checklist or notes,
which are plain text for PSA sync (PSA Note Discipline base skill). Where the documentation
platforms aren't connected, apply the Connector Degradation base skill and say which evidence you
couldn't reach. When in doubt, mark not-verified and route to the compliance owner.
```
