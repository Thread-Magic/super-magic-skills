---
name: SOC2 Evidence Collection
description: An auditor sent an evidence request list (SOC 2 or similar) — map each request to ticket, change, and access evidence, and package it with citations and honestly flagged gaps.
category: Compliance & Audit
tools: [search_tickets, search_itglue, search_knowledge_base, add_ticket_note]
connectors: [IT Glue]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# SOC2 Evidence Collection

**When to use:** "The auditor sent the evidence request list — pull what we have"; SOC 2 / ISO / similar audit fieldwork prep; or a readiness dry-run against a control framework's evidence expectations.

**Run it:** across the desk's tickets and documentation (an evidence-collection pass).

## Prompt

```
Turn an auditor's request list into an evidence index: every item mapped to the tickets,
changes, and documents that satisfy it, cited precisely, with coverage gaps declared instead
of papered over. You collect and index; the compliance owner reviews and submits. Work it in
order:

1. Parse the request list into individual items, keeping the auditor's own numbering — the
   deliverable must map one-to-one back to their list.
2. Map each item to its evidence type in the desk's systems:
   - Change management → change tickets with approvals, prerequisites, and outcomes (the
     change-request-prerequisites discipline is what makes these auditable).
   - Access reviews and terminations → access-review tickets and offboarding tickets with
     completion timestamps.
   - Incident response → incident tickets, containment timelines, and postmortems
     (security-incident-postmortem outputs).
   - Policies and procedures → the client's documentation (in IT Glue) and KB articles, with
     last-reviewed dates.
3. Gather with citations: for each item, the specific ticket numbers, document titles, and
   dates that satisfy it, plus a one-line note on how the evidence maps to the request.
   Sample-based requests ("provide 3 examples of...") get the auditor's sample size, selected
   across the period, not the three prettiest.
4. Flag gaps honestly and precisely: "no access-review ticket found for Q2" is a finding to
   disclose and remediate, not a hole to fill creatively. If a search may have hit a result
   cap, re-scope it before declaring absence, and note the search boundaries either way.
5. Package the evidence index: request item → evidence citations → coverage status (complete /
   partial / gap) → notes. Leave it as a plain-text note or deliver as the working document
   for the compliance owner.

Guardrails — always:
- Never fabricate, backdate, reconstruct-after-the-fact, or "tidy up" evidence — a flagged
  gap is defensible; altered evidence ends audits and careers.
- Do not invent ticket numbers or document titles; every citation must be a real record you
  located.
- Absence claims carry their search scope: "none found in <boards> over <period>," never a
  bare "none exists."
- The compliance owner reviews the package before anything goes to the auditor; you collect
  and index, you do not submit.
- Evidence leaves the building on management's decision — check for other-client data or
  credentials inside any document before it enters the package.
```
