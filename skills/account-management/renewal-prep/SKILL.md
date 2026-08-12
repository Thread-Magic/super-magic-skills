---
name: Renewal Prep
description: Build a pre-renewal readout for a client — service record over the term, open risks, the value story, and prep for the pricing conversation.
category: Account Management
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager, Sales & Business Development]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Renewal Prep

**When to use:** "<client>'s renewal is coming up — prep me"; "build a renewal readout for <client>"; or "what's our case for the price increase with <client>?"

**Run it:** across a client's contract term of history — a manual internal readout, not a Flow.

## Prompt

```
You are assembling everything the account manager needs before opening a renewal
conversation: what the record shows, what the client might weaponize, and what justifies
the number. Internal ammunition, honestly assembled.

1. Confirm the client (look it up) and the term to review — default to the full current
   contract period; fall back to the last 12 months if term dates are unknown, and say
   which you used.

2. Pull the term's tickets (excluding auto-resolved and merged noise) and build four
   sections:

3. Service record. Volume handled, responsiveness on urgent work, SLA performance in one
   or two lines, and the two or three hardest problems we solved — one representative
   example per theme, plain language, no ticket IDs.

4. Open risks. The honest list of what could sour the conversation: unresolved issues,
   recent misses or breaches, declining sentiment, promises made in threads and not kept.
   One line each. This section exists so the AM is never surprised in the room.

5. Value story. The business-outcome framing of the term — what kept running, what was
   prevented, roughly what disruption was avoided (estimates labeled as such). If a fuller
   version is needed, run Business Value Summary and fold it in.

6. Pricing-conversation prep. Grounded in the record: where scope grew beyond the contract
   (seats, sites, systems, out-of-scope work absorbed), which recurring costs justify
   adjustment, the two or three objections the client is most likely to raise, and a
   suggested response to each.

Deliver as a section-headed internal readout in that order. Note any result caps hit and
which counts are therefore order-of-magnitude.

Guardrails: strictly internal — nothing here goes to the client verbatim; client-facing
renewal materials are a separate deliverable with IDs and candor stripped. The open-risks
section must be honest, not flattering — hiding the misses sets the AM up to lose the room.
No invented metrics, contract terms, or pricing figures; if contract details (seats, rate,
term dates) aren't in reach, mark them "confirm before the meeting". Quantified value
claims are labeled estimates with a stated basis. If the record points at an individual's
performance, frame it as a process gap; employee evaluation goes to the manager. One
representative example per pattern throughout.
```
