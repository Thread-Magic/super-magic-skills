---
name: Major Incident Declaration
description: Run the criteria check, declare or explicitly decline a major incident, assign incident roles, and start the comms clock from one declaration checklist.
category: Change & Problem Management
tools: [search_tickets, update_ticket, add_ticket_note, create_ticket, list_ticket_priorities, search_members]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Faster Resolution & Response]
---

# Major Incident Declaration

**When to use:** "I think this is a major — declare it / should we declare on this?" / multiple tickets flooding in for the same client-wide or multi-client outage / a P1 that has outgrown single-ticket handling (multiple workstreams, exec attention, client comms pressure).

**Run it:** on one incident · or as a Flow (triggered when a matching outage cluster forms).

## Prompt

```
Declaring a major incident is a mode switch: normal queue rules stop, roles and a comms
cadence start. Run the declaration checklist fast and identically every time — including
the times the right answer is "this is a P1, not a major."

1. CRITERIA CHECK — declare when any is true, and record which one(s):
   - Client-wide loss of a core service (auth, email, primary LOB app, network) with no
     workaround.
   - Multiple clients impacted by a shared cause.
   - Active security incident with spreading or destructive behavior (also engage the
     security runbooks).
   - Contractual/regulatory trigger.
   - A lead's judgment call — the checklist supports judgment, it doesn't replace it.
   If none hold: explicitly record "assessed, not declared, because <reason>" on the
   ticket and continue as P1. A documented non-declaration prevents the 3am
   re-litigation.

2. DECLARE: designate one ticket as the master incident record (create one if the
   cluster has no natural master; link the rest to it). Set priority to the desk's
   highest and mark the declaration in a plain-text note:
   declared-at time, declared-by, criteria met, known impact so far.

3. ASSIGN ROLES — named humans, confirmed available, recorded on the master ticket:
   Incident Commander (owns decisions; see incident-commander-brief), Comms lead (owns
   the update clock; see incident-comms-cadence), Technical lead(s) per workstream. One
   person may hold multiple roles on a small desk, but every role has a name. Suggest
   candidates via the team directory / on-call records; a human confirms assignments.

4. START THE COMMS CADENCE: record the update interval (default internal every 30 min,
   client every 60 min, or the client's contractual terms if stricter) and the time of
   the first due update. Hand execution to incident-comms-cadence; the first client
   notification pairs with outage-notification.

5. OPEN THE TIMELINE: from declaration onward, timestamped notes on the master ticket for
   every significant event — this feeds the IC brief, the RFO letter, and the
   post-mortem. Start it now, not retroactively.

6. Output the declaration summary: master ticket, criteria, roles, cadence, next update
   due.

Guardrails: declaration is a human decision — the agent runs the checklist and
recommends; a named person declares (same for stand-down). Never let declaration wait on
complete information: declare on impact, refine the cause later. A non-declaration is
recorded with reasoning, never silent. No client-facing statements from this skill —
that's the comms lead's lane. Roles must be named individuals who acknowledged; "the team
is on it" is not a role assignment.

Running unattended (Flows): the agent NEVER declares unattended. Its entire reply is one
plain-text internal note on the candidate master ticket: "MAJOR INCIDENT CANDIDATE:
<criteria matched, counts, clients affected>. Declaration checklist ready — needs a human
declare/hold decision from <on-call lead role>." Nothing else — no priority changes, no
role assignments, no client comms. If the cluster already has a declaration note or an
existing major-incident master ticket, do nothing. When signal confidence is below
certain, do nothing.
```
