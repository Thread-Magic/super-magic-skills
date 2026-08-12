---
name: PCI DSS Scope Review
description: Help a client understand their PCI DSS scope — what counts as the cardholder data environment (CDE), what's in versus out, and hold the "we don't touch cardholder data" boundary honestly — not a QSA assessment or an Attestation of Compliance.
category: Compliance & Audit
tools: [search_tickets, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# PCI DSS Scope Review

**When to use:** A client that takes card payments asks what falls under PCI, or which SAQ might apply; prep before the client completes a Self-Assessment Questionnaire or engages a QSA; or validating a "we outsource all card handling / we don't store cardholder data" claim before it goes into an attestation.

**Run it:** across a client's card-data flows and systems (a scope-awareness review).

## Prompt

```
Most PCI mistakes are scope mistakes: assuming systems are out of scope when they can reach
cardholder data, or claiming "we don't touch cards" when a process actually does. Help a
client reason about their cardholder data environment (CDE) and scope boundary. This is NOT a
QSA assessment, does not produce an SAQ or Attestation of Compliance, and certifies nothing.
Work it in order:

1. Frame it in the output: this is a scope-awareness review to inform the client's PCI
   effort, not a QSA assessment, not an SAQ/AoC, and not certification. The client (with a
   QSA or their acquirer where required) owns the compliance determination.
2. Map how card data flows, honestly — the heart of scoping: where and how cardholder data is
   captured, transmitted, processed, or stored (e-commerce, POS, phone-taken payments, saved
   card-on-file, email/paper). Follow the data, not the assumption. A process nobody
   remembers (cards read over the phone, emailed authorization forms) is exactly what breaks
   a scope claim.
3. Identify the CDE: systems that store, process, or transmit cardholder data, plus
   connected-to and security-impacting systems. Then identify what's genuinely out of scope —
   and be strict about "connected-to," because a system that can reach the CDE is in scope
   even if it never touches a card number.
4. Pressure-test the "we don't touch the CDE" boundary: if the client uses a fully
   outsourced/redirect or hosted-payment-page model (card data never hits their systems),
   that dramatically narrows scope — but only if it's actually true end to end. Verify
   there's no hidden path (phone payments, refunds, saved cards, terminals on the flat
   network) before endorsing the boundary.
5. Note segmentation as the scope lever: network segmentation that isolates the CDE reduces
   scope; a flat network pulls everything in. Flag segmentation state as a finding, not a
   given.
6. Point to the likely direction (which SAQ type tends to fit the model) as orientation only
   — not a determination — and route to the client and, where required, a QSA/acquirer for
   the actual answer.
7. Output: card-data-flow summary, CDE and in/out-of-scope inventory, the boundary
   verification result, segmentation note, evidence dates, and the scope/limitations
   statement.

Guardrails — always:
- Not a QSA assessment, SAQ, or AoC — never state or imply the client "is PCI
  compliant/certified" or that scope is "confirmed."
- Follow the data, not the assumption — don't accept "we don't touch cards" without tracing
  phone, email, refund, saved-card, and terminal paths.
- "Connected-to" is in scope — a system that can reach the CDE counts even if it never sees a
  card number.
- Evidence-based, no fabrication — scope conclusions rest on the documented data flow;
  unknowns are "not verified," never assumed out-of-scope.
- Extra sanitization: never place actual cardholder data, PAN, or environment identifiers in
  the review or notes. Plain text only for PSA-synced notes.
- When in doubt, treat it as in scope and route to a QSA — over-scoping is a cost; a
  wrongly-excluded card-handling path is an attestation failure and a breach exposure.
```
