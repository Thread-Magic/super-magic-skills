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
cadence start. Run the checklist identically every time — including the times the right
answer is "P1, not major".

1. CRITERIA CHECK — declare when any of these is true and record which; if none hold,
   record "assessed, not declared, because <reason>" and continue as P1 — a documented
   non-declaration prevents the 3am re-litigation:
   - Client-wide loss of a core service (auth, email, primary LOB app, network), no
     workaround.
   - Multiple clients hit by a shared cause.
   - Active security incident, spreading or destructive (engage the security runbooks).
   - A contractual or regulatory trigger.
   - A lead's judgment call — the checklist supports judgment, not replaces it.

2. DECLARE: designate one ticket as the master incident record (create one if the cluster
   has no natural master; link the rest to it). Set priority to the desk's highest and
   note the declaration: declared-at, declared-by, criteria met, known impact so far.

3. ASSIGN ROLES — named humans, available, recorded on the master ticket: Incident
   Commander (owns decisions; see incident-commander-brief), Comms lead (owns the update
   clock; see incident-comms-cadence), and a technical lead per workstream. One person may
   hold several roles on a small desk, but every role has a name. Suggest candidates from
   the team directory; a human confirms.

4. START THE COMMS CADENCE: record the update interval (default internal every 30 min,
   client every 60, or the client's contractual terms if stricter) and when the first
   update is due. Execution goes to incident-comms-cadence; the first client notification
   pairs with outage-notification.

5. OPEN THE TIMELINE now, not retroactively: timestamped notes on the master ticket for
   every significant event from declaration onward. Then output the summary: master
   ticket, criteria, roles, cadence, next update due. Notes are plain text, no markdown or
   emojis (apply the PSA Note Discipline base skill).

Guardrails: declaration — and stand-down — is a human decision; you run the checklist and
recommend, a named person declares. Never wait on complete information: declare on impact,
refine the cause later. No client-facing statements from this skill — that's the comms
lead's lane. Roles are named individuals who acknowledged — "the team is on it" is not a
role assignment.

As a Flow: you NEVER declare unattended. Your entire reply is one plain-text internal note
on the candidate master ticket: "MAJOR INCIDENT CANDIDATE: <criteria matched, counts,
clients affected>. Checklist ready — needs a human declare/hold decision from <on-call
lead role>." Nothing else: no priority changes, no role assignments, no client comms. If
the cluster already has a declaration note or a master ticket, or confidence is below
certain, do nothing.
```
