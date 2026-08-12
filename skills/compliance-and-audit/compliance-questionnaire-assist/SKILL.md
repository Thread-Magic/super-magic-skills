---
name: Compliance Questionnaire Assist
description: A client received a security or compliance questionnaire (from their customer, prospect, or regulator) — draft answers from documented facts only, cite sources, and flag unknowns honestly instead of guessing.
category: Compliance & Audit
tools: [search_itglue, search_knowledge_base, search_tickets, add_ticket_note]
connectors: [IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Compliance Questionnaire Assist

**When to use:** "Help answer this security questionnaire <client> got from their customer"; a prospect's vendor-risk assessment landed on the client and the MSP is asked to help; or a recurring annual questionnaire needs this year's refresh.

**Run it:** on one questionnaire (a drafting pass for human review).

## Prompt

```
Vendor security questionnaires reward confident-sounding answers, which is exactly the trap.
Answer only from documented facts, cite where each answer came from, and make the unknowns
impossible to miss. A human reviews and submits; you draft. Work it in order:

1. Parse the questionnaire into individual questions and, before answering anything, sort
   each by whose control it asks about: controls the MSP operates and can attest to, versus
   the client's own controls (their HR policies, their physical office security, their
   internally managed apps). The MSP drafts only the former; the latter are routed to the
   client with a note — attesting to controls outside your management scope is how
   questionnaires go wrong.
2. Answer from documented facts only: the client's documentation (in IT Glue), KB articles
   and policies (the knowledge base), and the ticket record for operational evidence like
   patch cadence or incident handling. Each answer carries its source and the document's
   last-reviewed or as-of date.
3. Undocumented or unverifiable → the draft answer is "unknown — needs owner input," with a
   pointer to who likely knows. No optimistic defaults, and no "aspirational" answers: a
   planned control ("we intend to roll out MFA") is drafted as not-yet-implemented, never as
   implemented.
4. Watch scope words in the questions — "all," "always," "100%," "every employee" — and
   answer them with measured language and the actual coverage where known ("MFA is enforced
   for all accounts under our management as of <date>").
5. Incident-history questions use the ticket record for the stated window and the
   defensive-writing-standard's event vocabulary; anything that could read as a disclosure
   decision (naming past incidents to a third party) gets flagged for management rather than
   answered unilaterally.
6. Output the draft: question, answer, source citation, confidence, and the flag list
   (unknowns, client-scope items, management-review items) up top. A human reviews and
   submits; you draft.

Guardrails — always:
- Documented facts only — never answer from what is probably true, industry-standard, or
  remembered.
- "We plan to" is never drafted as "we do"; aspirational answers are misrepresentations with
  a delay.
- Never attest to controls outside the MSP's management scope — route those to the client,
  visibly.
- Unknowns are flagged honestly; a questionnaire full of honest gaps beats one confident
  wrong answer at contract-dispute time.
- Disclosure of incident history to third parties is management's call — flag, don't decide.
- Human review before submission, always.
```
