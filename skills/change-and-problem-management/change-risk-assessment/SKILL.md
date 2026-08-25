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
Score this change on two axes — how much breaks if it goes wrong (blast radius), and how
confidently it can be undone (rollback confidence) — and land it in the right approval
class.

1. Read the change ticket in full — what, scope, when, rollback — plus any thread
   discussion that changes the picture.

2. Score BLAST RADIUS — who feels it if this goes wrong — citing the scope evidence and
   scoring the dependency, not the component ("one switch" carrying a whole site is HIGH):
   - LOW: single user or single non-critical device, no shared service in the path.
   - MEDIUM: a team, a site, or one shared service; workarounds exist during an outage.
   - HIGH: client-wide, multi-client, or a service with no workaround (auth, primary LOB
     app, core network, backup infra).

3. Score ROLLBACK CONFIDENCE:
   - HIGH: a tested reversal path, or inherently reversible (config flag,
     snapshot-verified VM change), with a known reversal time.
   - MEDIUM: a documented but untested reversal, or one slower than the window allows.
   - LOW: a one-way door (data migration with cutover, deletions, firmware), or an empty
     or hollow rollback field. "Restore from backup" is LOW unless a restore has actually
     been tested and that evidence is cited.

4. Classify from the two scores:
   - Standard: LOW blast radius + HIGH rollback confidence + a match in the client's
     documented pre-approved standard-change list. No documented match, no standard —
     whatever the scores say.
   - Emergency: only when active or imminent service impact makes waiting for normal
     approval more damaging than acting, and the incident justifying it is named. Route to
     emergency-change-handling; emergency is a speed lane, not a lower bar.
   - Normal: everything else. HIGH blast radius or LOW rollback confidence means CAB-level
     review; recommend mitigations too (staged rollout, pre-change backup verification,
     on-call coverage in the window).

5. Leave the assessment as a note: both scores with their evidence, the classification,
   the recommended approval path, and any required mitigations (apply the PSA Note
   Discipline base skill — plain text, no markdown or emojis). Set the change ticket's
   type/priority to match where the desk uses one. If scores changed because scope grew
   since a prior assessment, say so — re-classification resets the approval.

Guardrails: you recommend a class, a human approver ratifies it — never green-light
execution. Emergency needs a named, current incident or imminent harm; "the client is
impatient" is normal-track. "We do this all the time" in a thread is not a documented
procedure. When the ticket lacks the information to score an axis, score it at the riskier
level and say why — uncertainty is risk, not a pass. Never soften a score to avoid
friction — the honest HIGH that starts a CAB conversation is the product.
```
