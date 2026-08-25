---
name: Problem Record Lifecycle
description: Drive a problem record through its states — opened from an incident cluster, investigating, known error, then fixed or accepted-risk closure.
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
Move this problem through explicit states, with evidence at each transition, toward one of
only two legitimate endings: fixed and verified, or risk accepted by a named human who has
the authority. A problem stuck in "open" forever is worse than none.

1. Locate the problem record on the problem board. If the pattern has no record yet, hand
   creation to the problem-ticket-creation skill — this one owns everything after.

2. Identify the current state (map to the nearest status the desk has) and run its exit
   criteria — advance, or record what is blocking:
   - OPEN / INVESTIGATING: root cause unknown, owner named. Exits to KNOWN ERROR on a
     root-cause statement backed by evidence from the linked incidents, plus a documented
     workaround or an explicit "no workaround exists".
   - KNOWN ERROR: cause identified, permanent fix not yet in place, workaround documented
     (feeds the known-error-database). Exits to FIX IN PROGRESS on a change/fix ticket
     with an owner, or to ACCEPTED RISK on cost-of-recurrence vs. cost-of-fix stated and
     the named acceptor recorded. Silence from management is not acceptance.
   - FIX IN PROGRESS: a fix is committed and a change ticket exists — link it; the fix
     travels the change track. Exits to CLOSED: FIXED on the change completed to the
     change-completion-verification standard plus a recurrence check — search for matching
     incidents since deployment; zero recurrence over the verification window (default 30
     days) closes it.

3. On every transition, change the status and leave a state-change note: from-state ->
   to-state, the evidence that met the exit criteria, and the next action with its owner
   (apply the PSA Note Discipline base skill — plain text, no markdown or emojis). On
   CLOSED: FIXED, retire the known-error entry and its workaround so techs stop working
   around a solved problem. On CLOSED: ACCEPTED RISK the entry stays, marked permanent,
   with a review date — acceptances rot; re-confirm annually or when the recurrence cost
   changes.

4. Review-sweep variant: list every open problem with state, days in state, and incidents
   since the last transition; flag stalled ones (no transition in 30+ days) with a
   recommended decision — advance, accept, or escalate. Stalled and still collecting
   incidents ranks first.

Guardrails: advance a state only when its exit criteria are met on evidence; humans own
the accept-risk decision and fix prioritization. Never mark FIXED on deployment alone —
verification means observed non-recurrence over a window the note names. "It hasn't
happened in a while" is not FIXED; nobody deciding is not ACCEPTED RISK. A KNOWN ERROR
whose incident count is climbing reopens the accept-vs-fix conversation — surface it. One
problem per signature: if investigation turns up two distinct root causes, split the
record and cross-link.
```
