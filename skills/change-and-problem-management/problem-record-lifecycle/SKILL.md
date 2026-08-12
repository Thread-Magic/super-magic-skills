---
name: Problem Record Lifecycle
description: Drive a problem record through its states — opened from an incident cluster, under investigation, known error, and finally fixed or accepted-risk closure — so problems either get solved or get a deliberate decision, never a quiet death in the backlog.
category: Change & Problem Management
tools: [search_tickets, update_ticket, add_ticket_note, list_ticket_statuses, create_ticket]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Problem Record Lifecycle

**When to use:** "Where are we on this problem ticket? / advance the problem record for <recurring issue>" / a periodic problem-board review / an investigation concluded and the problem needs to transition / a problem with no movement in 30+ days that needs a decision.

**Run it:** on one problem record · or as a problem-board review sweep.

## Prompt

```
Move this problem through explicit states with evidence at each transition, and force the
only two legitimate endings: fixed and verified, or risk accepted by someone with the
authority to accept it. A problem stuck in "open" forever is worse than none.

1. Locate the problem record (search the problem board). If the pattern has no
   record yet, hand creation to the problem-ticket-creation skill — this one owns
   everything after.

2. Determine the current state and validate against the desk's status set
   (map to nearest equivalents):
   - OPEN / INVESTIGATING: root cause unknown; active investigation with an owner.
   - KNOWN ERROR: root cause identified and documented, permanent fix not yet in place,
     workaround documented (feeds the known-error-database).
   - FIX IN PROGRESS: a permanent fix is committed; a change ticket exists (link it; the
     fix travels the change track).
   - CLOSED: FIXED: fix deployed AND verified (recurrence stopped over a meaningful
     window; a deployed fix with continuing incidents is not fixed).
   - CLOSED: ACCEPTED RISK: a named decision-maker accepted living with it; the workaround
     is the permanent answer.

3. For the current state, run its exit criteria and either advance or record what's
   blocking:
   - INVESTIGATING → KNOWN ERROR: root cause statement with supporting evidence from the
     linked incidents, and a documented workaround (or explicit "no workaround exists").
   - KNOWN ERROR → FIX IN PROGRESS: a change/fix ticket with an owner. KNOWN ERROR →
     ACCEPTED RISK: cost of recurrence vs. cost of fix stated, and the named acceptor
     recorded — silence from management is not acceptance.
   - FIX IN PROGRESS → CLOSED: FIXED: change completed (change-completion-verification
     standard) plus a recurrence check — search for matching incidents since
     deployment; zero recurrence over the verification window (default 30 days) closes it.

4. On every transition, post a plain-text state-change note: from-state → to-state, the
   evidence satisfying the exit criteria, and the next action with owner. Update the
   ticket status.

5. On CLOSED: FIXED — retire the corresponding known-error entry and its workaround so
   techs stop applying a workaround to a solved problem. On CLOSED: ACCEPTED RISK — the
   known-error entry stays, marked permanent, with a scheduled review date (risk
   acceptances rot; re-confirm annually or when recurrence cost visibly changes).

6. Review-sweep variant: list every open problem with state, days-in-state, linked
   incident count since last transition, and the stalled ones (no transition in 30+ days)
   flagged with a concrete recommended decision — advance, accept, or escalate. Stalled
   problems accumulating new incidents get priority.

Guardrails: every closure is one of the two legitimate kinds, with evidence or a named
acceptor. "It hasn't happened in a while" without a verification window is not FIXED;
nobody deciding is not ACCEPTED RISK. The agent advances states only when exit criteria are
met on evidence, and recommends — humans own the accept-risk decision and fix
prioritization. Never mark FIXED on deployment alone; verification means observed
non-recurrence, and the note says what window was checked. A KNOWN ERROR whose incident
count is climbing should reopen the accept-vs-fix conversation — surface it. One problem per
signature; if investigation reveals two distinct root causes, split and
cross-link.
```
