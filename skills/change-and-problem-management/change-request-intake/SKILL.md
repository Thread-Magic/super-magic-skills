---
name: Change Request Intake
description: A change ask arrived as prose ("can we upgrade the firewall this weekend?") — normalize it into a structured change request (what/why/scope/when/rollback/risk) and route it to the right approval track before anyone touches anything.
category: Change & Problem Management
tools: [search_tickets, search_knowledge_base, create_ticket, update_ticket, add_ticket_note, list_boards, list_ticket_statuses]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Change Request Intake

**When to use:** "Client wants us to migrate their file server — write this up as a change" / a change ask buried in an incident thread ("while you're in there, can you also...") / normalizing a batch of informal requests before the weekly review / a tech about to make a change with no change record yet.

**Run it:** on one change request.

## Prompt

```
Turn this loose change ask into a change request structured enough to assess, approve,
and later audit. Intake normalizes; it does NOT approve, schedule, or execute.

1. Extract the ask from the source (ticket thread, forwarded email, verbal summary).
   Identify the requester and, where client-originated, whether they have authority to
   request it — flag if unclear, don't assume.

2. Normalize into the six intake fields. Write only what the source supports; mark gaps
   as OPEN rather than inventing content:
   - What: the change, specific enough to execute from (system, component, from-state →
     to-state).
   - Why: business justification in one or two sentences.
   - Scope: systems, sites, clients, users affected; explicitly name what is OUT of
     scope.
   - When: requested window, or "no window proposed" if none was given.
   - Rollback: the reversal path the requester/tech described. If none, write "rollback
     plan: OPEN — required before approval." Never draft one on their behalf.
   - Risk: what could go wrong and who feels it, as an initial sketch (full scoring is
     change-risk-assessment's job).

3. Check for an existing change record covering the same ask (search the change board)
   — extend it rather than creating a duplicate.

4. Create or update the change ticket on the change board with the structured fields as a plain-text body. Title pattern:
   "CHANGE: <system/component> — <one-line what>".

5. Route to the approval track by an initial read of risk and precedent:
   - Matches a documented pre-approved standard change (check the client's documentation for the
     desk's standard-change list) → note as a standard-change candidate; still
     confirmed in change-risk-assessment.
   - Anything else → normal track: hand to the pre-approval completeness gate, then
     change-risk-assessment for classification.
   - Requester says it must happen NOW to restore/protect service → flag as an
     emergency-change candidate and point at emergency-change-handling; don't let
     urgency skip the record.

6. Output: the change ticket reference, the six fields with any OPEN gaps listed, and
   the recommended track with one line of reasoning.

Guardrails: intake never approves and never schedules — it produces the record and the
routing recommendation. Silence from an approver is not approval. Never fabricate
rollback plans, windows, or justifications to make the record look complete — an honest
OPEN beats a hollow field. Changes smuggled inside incident tickets get their own change
record. Check freeze calendars at intake (see maintenance-freeze-windows); a request
landing inside a freeze gets flagged immediately, not discovered at scheduling. Plain-text
bodies and notes — these records sync to the PSA.
```
