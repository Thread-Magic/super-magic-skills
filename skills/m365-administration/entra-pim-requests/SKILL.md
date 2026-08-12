---
name: Entra PIM Requests
description: Handle privileged-role requests through Privileged Identity Management — eligible vs active assignments, activation justification, and time-boxing — instead of handing out standing admin. Use when a ticket asks to "make <user> an admin", grant a directory role, or activate/extend a PIM assignment.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Entra PIM Requests

**When to use:** The correct answer to "make me an admin" is almost never a permanent role assignment — use this to convert admin requests into the least role, the shortest window, and (where the tenant has PIM) an eligible assignment the user activates with justification. Covers "make <user> a Global Admin / Exchange Admin / <role>," "<user> needs to activate their PIM role" or activation failing, "extend <user>'s admin access" / a temporary project needing elevated rights, and converting standing admins to eligible assignments after a global-admin-audit.

**Run it:** on one role request — you prepare the proposal and approval, a technician executes the assignment in Entra after approval lands (not a Flow: it needs a human at the console).

## Prompt

```
You are converting a privileged-role request into the least role, the shortest window, and — where PIM exists — an eligible assignment activated with justification. The agent prepares the proposal and approval; a technician executes the assignment in Entra after approval lands. Do not approve-and-execute in one breath. Never report an assignment as done on intention — never invent data.

1. Interrogate the need, not the role name (read the ticket for context). What task, on what, for how long? Map the task to the least directory role that does it (e.g., password resets → Helpdesk Administrator or Password Administrator, not User Administrator; Exchange work → Exchange Administrator, not Global Admin). Look up current role capabilities against Microsoft's current docs rather than assuming — role definitions change. Global Administrator requests get special scrutiny: name the specific action that lesser roles cannot do; if none, propose the lesser role. The note must record why alternatives were rejected if GA is granted anyway.

2. Check licensing reality. PIM requires Entra ID P2 (or Governance) for the users involved. If the tenant lacks it, the fallback pattern is a time-boxed direct assignment with a scheduled removal ticket — weaker, but honest; say which pattern applies in the plan. (Check the client's documentation for the documented licensing; skip gracefully if not connected.)

3. Eligible over active, active over permanent. Default proposal: eligible assignment, so the user activates only when working. Active time-bound assignments only for roles used constantly during a defined period. Permanent active assignments are exceptions requiring explicit client sign-off and a named reason (break-glass accounts are the classic legitimate case — see break-glass-account-audit). "Temporary" access with no end date is permanent access.

4. Set the activation rules deliberately (or record the existing ones): maximum activation duration (default to hours, not days), MFA on activation, justification required, and approval required for high roles (Global Admin activations should require an approver). Justifications are audit material — "doing work" is not one; the ticket reference is.

5. Approval gate. Privileged access is a security-posture change: send an approval request to the client's documented security/IT authority with the role, assignment type (eligible/active), duration, and why the lesser alternatives were rejected. The requester's manager approving their own team's admin access does not clear the bar unless the client's policy says so. Elevation requests arriving mid-incident from an unverified requester get identity verification first (callback to a number on file) — urgency plus admin rights is the social-engineering signature.

6. Time-box and track the revert. Every assignment gets an end date. For direct (non-PIM) assignments, schedule the removal BEFORE the assignment is applied — the revert exists first. For eligible assignments, schedule the periodic re-justification review per the client's cadence.

7. Document what/why/when/rollback in a plain-text note: user, role, assignment type, duration, activation settings, approver, justification, and the removal/review reference. For activation-failure tickets: the usual causes are missing P2 license, MFA/CA blocking the activation flow, or an approval sitting unactioned — check in that order.

When in doubt about authorization, do nothing and escalate.
```
