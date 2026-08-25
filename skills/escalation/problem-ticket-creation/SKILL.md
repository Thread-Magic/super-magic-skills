---
name: Problem Ticket Creation
description: When an incident recurs past threshold, create a problem/RCA ticket linking the incidents and documenting the workaround so the pattern gets a real owner.
category: Escalation
tools: [search_tickets, create_ticket, add_ticket_note, update_ticket, list_boards, list_ticket_statuses]
connectors: []
scope: both
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Problem Ticket Creation

**When to use:** "This keeps happening — open a problem ticket" / "we've fixed this five times this month"; a periodic sweep detects an incident signature crossing the recurrence threshold; or a recurring-issue review flagged a repeat pattern needing RCA.

**Run it:** on one triggering incident · across a signature's incidents · or as a Flow (when an incident closes and increments a known signature).

## Prompt

```
ITIL problem management minus the ceremony: once the same incident has recurred enough, open one
problem ticket that owns the root-cause work, wire every incident to it, and write down the
workaround techs currently use.

1. Establish the incident signature — same symptom class, same client or infrastructure
   component. Verify recurrence over the window by matching documented symptoms and error text,
   not title wording, and list the matching incidents with dates. Threshold defaults to 3 or more
   in 30 days; a tenant SOP wins where it defines one.

2. Search the problem board or type for an existing ticket on this signature; if one exists, link
   the new incidents to it rather than creating a duplicate.

3. Open the problem ticket on the agreed board, titled "PROBLEM: <symptom> - <client or
   component>", its body carrying the incident list with references and dates, the recurrence
   rate, common factors across incidents (and differences worth noting), and business impact per
   occurrence.

4. Document the CURRENT WORKAROUND verbatim from what techs actually did: the steps, how long it
   holds, the cost per occurrence. If no consistent workaround exists, state "no reliable
   workaround" explicitly — that raises the problem's urgency.

5. Link both ways: a note on each incident referencing the problem ticket — "Linked to problem
   ticket <ref>: apply the documented workaround, root cause tracked there" — and the problem
   ticket listing every incident. Notes and bodies are plain text (PSA Note Discipline base
   skill).

6. Frame the RCA ask: what needs investigating, what the next occurrence should capture, a
   recommended owner tier. Assign only with confirmation.

7. Report the problem ticket reference, incidents linked, workaround status and next step.

One problem per signature. Recurrence must be evidenced by the listed incidents, so don't pad the
count with loosely similar tickets. The workaround is transcribed from documented fixes, never
invented; where different fixes worked, record them all. Creating a problem ticket doesn't close
or alter the incidents' own lifecycles.

As a Flow, triggered by the incident-close event incrementing a known signature: Flows are
event-driven only, so there is no scheduled variant — run the recurring sweep manually or from an
external scheduler. Create only when the threshold is met by strict signature match — same client
or component AND same symptom class; fuzzy matches don't count. Where an existing problem ticket
is found, add the linking note to the new incidents only; never create a second. Writes are
limited to one new problem ticket and the linking notes: no assignment, no priority or
incident-status changes. Your entire reply is the problem-ticket body or note content. If
signature matching is ambiguous, or searches hit caps that make the count unreliable (Sweep
Honesty base skill), do nothing.
```
