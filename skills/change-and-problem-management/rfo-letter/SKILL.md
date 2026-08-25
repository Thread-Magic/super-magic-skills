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
Draft the client-facing account of the outage. It outlives the incident — it gets
forwarded to the client's board, their insurer, sometimes their lawyers. Draft from ticket
evidence, under defensive-writing rules.

1. Gather the record: the master incident ticket and its workstream tickets, the comms
   trail (what the client was told and when), and the internal post-mortem if one exists.
   The letter must not contradict the comms trail: where an in-incident update said
   something the investigation later disproved, it corrects that rather than silently
   contradicting it.

2. Draft this structure:
   - Summary: one paragraph, plain language — service affected, when, how long, resolved.
   - Facts / timeline: dated, timestamped events from the ticket record only — detection,
     response milestones, restoration — at client-relevant granularity. Reconstructed
     times marked "approximately".
   - Impact: what the client experienced, only as evidenced. No speculative business-loss
     figures — that number is the client's.
   - Cause: the confirmed causal account. Where it is not confirmed, write "the
     investigation identified <X> as the most probable cause" — never dress a hypothesis
     as a finding. Keep trigger and root cause distinct.
   - Remediation: what restored service, and what has been done since.
   - Prevention: specific measures, each tracked as a post-incident-action-tracking item.
     Commit in writing only to actions with owners — "we will review our processes" reads
     as evasion, a false specific promise reads worse later.

3. Defensive writing: cite facts, in plain past tense. No admissions of negligence, no "we
   should have", no blame of named individuals; name a vendor only where the fact is
   established and necessary. On security incidents, never "breach", "hack", or
   "compromise" unless it is confirmed and the desk has decided to state it — regulatory
   notification language is a legal decision. Every sentence passes: would we stand behind
   this in a dispute?

4. Deliver the draft in chat, flagged: it needs management sign-off before sending, and
   counsel's review where there is legal or insurance exposure. You never send it. Once a
   human has, record the sent version and date in a note on the master ticket (apply the
   PSA Note Discipline base skill — plain text, no markdown or emojis).

Guardrails: nothing goes in the letter that is not in the record — no invented timestamps,
no smoothed-over gaps. Where the record is embarrassing (slow detection, a failed first
fix), be honest at the level of fact and skip the adjectives. Never include internal
tooling detail, other clients' names, staff names (roles only), or another tenant's
incidents. Asked for the RFO before root cause is confirmed, offer a preliminary RFO
labelled as such — never a confident cause the evidence does not support.
```
