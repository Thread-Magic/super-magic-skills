---
name: RFO Letter
description: Draft the reason-for-outage letter a client receives after a major incident (facts, impact, remediation, prevention) written defensively for legal review.
category: Change & Problem Management
tools: [search_tickets, search_knowledge_base, add_ticket_note, search_contacts]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# RFO Letter

**When to use:** "Write the RFO for last week's outage" / a client contractually requires an RFO within N days of a major / a major incident stood down and the closure notice promised a written account / reworking an internal post-mortem into the client-safe formal letter.

**Run it:** on one incident.

## Prompt

```
Draft the client-facing formal account of what happened. It outlives the incident — it
gets forwarded to the client's board, their insurer, sometimes their lawyers. Draft from
ticket evidence under defensive-writing rules: complete enough to rebuild trust, careful
enough to never claim more than the record supports.

1. Gather the record: master incident ticket and workstream tickets ,
   the comms trail (what the client was told and when — the RFO must not contradict it),
   and the internal post-mortem if one exists.

2. Draft in the fixed structure:
   - Summary: one paragraph, plain language — what service was affected, when, how long,
     and that it is resolved.
   - Facts / timeline: dated, timestamped events from the ticket record only — detection,
     response milestones, restoration. Client-relevant granularity. Reconstructed times
     marked "approximately."
   - Impact: what the client experienced, concretely and only as evidenced. No
     speculative business-loss quantification — that's the client's number, not the MSP's.
   - Cause: the confirmed causal account. If root cause is not fully confirmed, say "the
     investigation identified <X> as the most probable cause" — never dress a hypothesis
     as a finding. Distinguish trigger from root cause where the post-mortem does.
   - Remediation: what was done to restore service and what has been done since.
   - Prevention: specific measures being taken, each real and tracked (map to
     post-incident-action-tracking items). Only commit in writing to actions that have
     owners; vague "we will review our processes" reads as evasion and specific false
     promises read worse later.

3. Apply the defensive-writing rules: facts you can cite, in plain past tense — no
   admissions of negligence, no "we should have." No blame of named individuals; vendors
   named only where the fact is established and necessary. For security-related incidents,
   never "breach," "hack," or "compromise" unless confirmed and the desk has decided to
   state it; regulatory notification language is a legal decision. Every sentence passes:
   "are we prepared to stand behind this in a dispute?"

4. Reconcile against the comms trail: if an in-incident update said something the
   investigation later disproved, the RFO addresses the correction gracefully rather than
   silently contradicting it.

5. Deliver the draft in chat for human review — flag explicitly: this letter requires
   management sign-off before sending, and for incidents with legal/insurance exposure,
   review by counsel. The agent never sends it.

6. Once approved and sent by a human, record the sent version and date in a plain-text
   note on the master ticket.

Guardrails: draft only — a human with authority signs and sends it, always. Nothing in the
letter that isn't in the record: no invented timestamps, no smoothed-over gaps, no
prevention promises without tracked actions behind them. Where the record is embarrassing
(slow detection, failed first fix), be honest at the level of fact without self-
incriminating editorializing — state the timeline, skip the adjectives. Do not include
internal tooling detail, other clients' names, staff names (roles only), or anything from
another tenant's incidents. If the requester wants the RFO before root cause is confirmed,
offer the "most probable cause" framing or a preliminary RFO labeled as such — never a
confident cause the evidence doesn't support.
```
