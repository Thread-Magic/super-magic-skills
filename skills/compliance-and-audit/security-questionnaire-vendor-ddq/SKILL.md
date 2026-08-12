---
name: Security Questionnaire Vendor DDQ
description: An inbound vendor security questionnaire or due-diligence questionnaire (DDQ) needs answering — draft responses from documented facts only, cite the evidence for each, and flag every unknown for human review rather than guessing.
category: Compliance & Audit
tools: [search_tickets, search_itglue, search_hudu, search_knowledge_base, add_ticket_note, update_ticket]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Security Questionnaire Vendor DDQ

**When to use:** An inbound security questionnaire, DDQ, or vendor-assessment form arrives to be completed (SIG, CAIQ, a customer's custom spreadsheet); a prospect's procurement/security team requests control attestations before signing; or a client asks the MSP to help answer a DDQ their own customer sent them.

**Run it:** on one questionnaire (a drafting pass for human sign-off).

## Prompt

```
A prospect, customer, or partner sends a security DDQ and expects the MSP (or a client) to
attest to controls. The failure mode is confident wrong answers — every DDQ answer is an
attestation that can be held against you contractually. Draft from documented evidence, cite
sources, and mark anything unproven for human sign-off. Use this specifically for inbound
vendor/DDQ attestations answered from your own documented posture. Work it in order:

1. Establish whose posture is being attested — the MSP's own, or a specific client's. Answers
   must draw only from that entity's documented controls; do not blend the MSP's posture into
   a client's answer or vice versa.
2. Inventory the source evidence: existing policy docs, prior completed questionnaires, SOC 2
   report, the documentation platforms (IT Glue and Hudu), KB articles, and ticket/change
   history. This documented evidence is the ONLY basis for an answer.
3. Answer each question from evidence, and cite it: for every answer, record the source that
   backs it (policy name, SOC 2 control reference, documentation record). An answer with no
   citable source is not an answer yet.
4. Flag unknowns honestly — do not guess: where evidence is missing, ambiguous, or
   contradicts the question, mark the item "needs human review" with a note on what's
   missing, rather than asserting a control that may not exist.
5. Separate "yes," "no," "partial/compensating control," and "not applicable" precisely —
   DDQs punish vague affirmatives. A partial control is described as partial with its
   compensating measure, not rounded up to "yes."
6. Route the draft for human sign-off: the completed draft, with citations and flagged gaps
   clearly marked, goes to the accountable owner (MSP security lead or the client) for review
   and final attestation. You draft; a human attests.
7. Document what was produced: which questionnaire, whose posture, the evidence used, and the
   list of flagged items awaiting human input. Do not submit the questionnaire — submission
   is the owner's act.

Guardrails — always:
- Documented facts only — never invent a control, certification, or capability. No
  fabrication of policy names, dates, or SOC/audit references.
- Every answer carries a citation; every unknown is flagged for human review. "We don't
  currently document this" is an honest answer; a guessed "yes" is a misrepresentation.
- A DDQ answer is a binding attestation — you draft, a human owner reviews and submits. Never
  submit or send the questionnaire on the owner's behalf.
- Keep the MSP's posture and each client's posture strictly separate.
- Don't overstate partial controls — "partial with compensating control" is not "yes."
- Sanitized and confidential: don't expose one client's specifics inside another's
  questionnaire; no credentials or environment identifiers in answers. Plain text only for
  PSA-synced notes.
- When in doubt, flag for human review.
```
