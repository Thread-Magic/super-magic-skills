---
name: Change Risk Assessment
description: Classify a change request as standard, normal, or emergency by scoring blast radius and rollback confidence so approval effort matches actual risk.
category: Change & Problem Management
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Change Risk Assessment

**When to use:** "How risky is this change? / does this need CAB or can we just do it?" / a normalized change request needs classification before approval routing / re-assessing a change whose scope grew / building the risk-ranking column of the CAB brief.

**Run it:** on one change request.

## Prompt

```
Score this change on two axes — how much breaks if it goes wrong (blast radius) and how
confidently it can be undone (rollback confidence) — and land it in the right approval
class. The point is proportionality: a DNS TTL tweak and a hypervisor migration should
not travel the same approval path.

1. Load the change ticket in full: what/scope/when/rollback fields,
   plus any thread discussion that changes the picture.

2. Score BLAST RADIUS (who/what feels it if this goes wrong), citing scope evidence:
   - LOW: single user or single non-critical device; no shared service in the path.
   - MEDIUM: a team, site, or one shared service; workarounds exist during an outage.
   - HIGH: client-wide, multi-client, or a service with no workaround (auth, primary LOB
     app, core network, backup infra).
   When shared infrastructure is touched, score the dependency, not the component — "one
   switch" that carries a whole site is HIGH.

3. Score ROLLBACK CONFIDENCE:
   - HIGH: tested reversal path or inherently reversible (config flag, snapshot-verified
     VM change); reversal time is known.
   - MEDIUM: plausible documented reversal, untested, or reversal takes longer than the
     window allows.
   - LOW: one-way door (data migration with cutover, deletions, firmware) or the
     rollback field is empty/hollow. "Restore from backup" counts as LOW unless a
     restore has actually been tested and that evidence is cited.

4. Classify from the two scores:
   - Standard: LOW blast radius + HIGH rollback confidence + matches a documented,
     pre-approved, repeatable procedure (check the client's documentation for the standard-change
     list; no match → cannot be standard, regardless of scores).
   - Emergency: only when active or imminent service impact makes waiting for normal
     approval more damaging than acting. The incident justifying it must be named. Route
     to emergency-change-handling; emergency is a speed lane, not a lower bar.
   - Normal: everything else. HIGH blast radius or LOW rollback confidence means
     CAB-level review, and recommend extra mitigations (staged rollout, pre-change
     backup verification, on-call coverage during the window).

5. Post the assessment as a plain-text note: the two scores with the
   evidence behind each, the classification, and the recommended approval path plus any
   required mitigations. Update the change ticket's type/priority to match if the desk
   uses one.

6. If scores changed because scope grew after a prior assessment, say so explicitly —
   re-classification resets the approval, and the note must make that visible.

Guardrails: the assessment recommends a class; a human approver ratifies it — the agent
never green-lights execution. No standard-change classification without a documented
pre-approved procedure to point at ("we do this all the time" in a thread is not
documentation). Emergency classification requires a named, current incident or
imminent-harm justification — "the client is impatient" is normal-track. When the ticket
lacks the information to score an axis, score it at the riskier level and say why —
uncertainty is risk, not a pass. Do not soften scores to avoid friction; the honest HIGH
that triggers a CAB conversation is the product.
```
