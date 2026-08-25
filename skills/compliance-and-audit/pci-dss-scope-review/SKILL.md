---
name: PCI DSS Scope Review
description: Help a client understand PCI DSS scope — what counts as the cardholder data environment (CDE), what's in versus out — not a QSA assessment or AOC.
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
cardholder data, or claiming "we don't touch cards" when a process does. Help a client reason
about their cardholder data environment (CDE) and scope boundary. This is NOT a QSA assessment
and certifies nothing.

1. Frame it in the output: a scope-awareness review to inform the client's PCI effort, not an
   assessment, an SAQ, an AoC or certification. The client — with a QSA or their acquirer where
   required — owns the compliance determination.

2. Map how card data flows; this is the heart of scoping. Where and how is cardholder data
   captured, transmitted, processed or stored: e-commerce, POS, phone-taken payments,
   card-on-file, email or paper. A process nobody remembers — cards read over the phone, emailed
   authorization forms — is exactly what breaks a scope claim.

3. Identify the CDE: systems that store, process or transmit cardholder data, plus connected-to
   and security-impacting systems. Then identify what is genuinely out of scope, strictly — a
   system that can reach the CDE is in scope even if it never touches a card number.

4. Pressure-test any "we don't touch the CDE" boundary. A fully outsourced redirect or
   hosted-payment-page model, where card data never hits the client's systems, narrows scope
   dramatically — but only if it is true end to end. Verify there is no hidden path — phone
   payments, refunds, saved cards, terminals on the flat network — before endorsing it.

5. Segmentation is the scope lever: isolating the CDE reduces scope, a flat network pulls
   everything in. Flag segmentation state as a finding, not a given.

6. Point to the likely direction — which SAQ type tends to fit the model — as orientation only,
   never a determination, and route to the client and, where required, a QSA or acquirer.

7. Output the card-data-flow summary, the CDE and in/out-of-scope inventory, the boundary
   verification, the segmentation note, evidence dates, and the scope and limitations statement.

Never state or imply the client "is PCI compliant" or "certified", or that scope is "confirmed".
Follow the data, not the assumption: don't accept "we don't touch cards" without tracing the
phone, email, refund, saved-card and terminal paths. Scope conclusions rest on the documented
data flow, and unknowns are "not verified", never assumed out of scope. Never put actual
cardholder data, a PAN or environment identifiers in the review or notes, which are plain text
for PSA sync (PSA Note Discipline base skill). If the documentation platforms aren't connected,
apply the Connector Degradation base skill and say which evidence you couldn't reach. When in
doubt, treat it as in scope and route to a QSA: over-scoping costs money, a wrongly excluded
card-handling path is an attestation failure and a breach exposure.
```
