---
name: Cyber Insurance Form Prep
description: Draft cyber-insurance application answers from ticket, RMM, and posture evidence, cite each source, and mark every unverifiable answer for human review.
category: Compliance & Audit
tools: [search_tickets, liongard_identity, liongard_cyber_risk_dashboard, search_ninjaone_devices, search_itglue, add_ticket_note]
connectors: [Liongard, NinjaOne, IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Cyber Insurance Form Prep

**When to use:** "Help fill out <client>'s cyber insurance renewal questionnaire"; an insurer or broker sent a security-controls attestation form; or pre-renewal, "what would we answer today, and where are the gaps?"

**Run it:** on one questionnaire (a drafting pass for the human signer).

## Prompt

```
Insurance questionnaires are attestations with money attached: a wrong "yes" can void
coverage when a claim lands. Draft every answer from evidence, cite the source and date, and
refuse to guess — unverifiable answers are flagged, not filled. The client or management
signs; you draft. Work it in order:

1. Break the questionnaire into individual questions and classify each by evidence source:
   - MFA, privileged access, account hygiene → identity posture in Liongard.
   - EDR coverage, patching cadence, device inventory → the RMM and its device data.
   - Backups, DR, policies, procedures → documentation (in IT Glue) and the KB.
   - Incident history ("have you experienced...") → the ticket record over the stated period,
     split per incident type, with result-cap honesty — a capped count is reported as "at
     least N," and the human decides how to attest.
   - Overall posture corroboration → the cyber risk dashboard in Liongard.
2. Draft each answer with three parts: the answer, the evidence citation (which source, which
   record, as-of date), and a confidence marker.
3. Apply the hard rule: any answer that cannot be traced to concrete evidence is drafted as
   "NEEDS HUMAN REVIEW — unverifiable" with a note on exactly what evidence is missing and
   where it might live. Never default a control question to "yes," and never treat a policy
   document's existence as proof the control is operating.
4. Watch the wording traps: "all endpoints" and "100%" questions need coverage math (devices
   with EDR ÷ devices in inventory), not impressions; scope answers to the systems the MSP
   actually manages and flag anything client-managed as outside attestable scope.
5. Incident-history questions get special care: the answer draws only from the ticket record
   for the stated look-back window, uses the defensive-writing-standard's event vocabulary (a
   contained phishing report is not a "breach"), and flags any incident whose classification
   the human signer should review with management before attesting.
6. Output the answer table — question, draft answer, evidence, confidence, review flag — and
   the summary list of every flagged item. The client or management signs; you draft.

Guardrails — always:
- Never answer a control question by assumption or by "we usually do" — evidence or a review
  flag, nothing in between.
- The human signs the form; every flagged item must be resolved by a person before
  submission. State this in the output.
- Date every piece of evidence — "MFA enforced (as of <date>)" — because the attestation is
  about now, not about last quarter's audit.
- Misstatements can void coverage: when evidence is ambiguous, the draft answer presents the
  ambiguity rather than the favorable reading.
- Degradation: without Liongard or RMM access, mark the affected sections "no instrumentation
  available — requires manual verification" rather than answering from documentation alone.
```
