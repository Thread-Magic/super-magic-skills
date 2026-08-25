---
name: Offboarding Intent Design
description: Design the employee-termination intake intent with an authorized-requester check and urgency handling built in from the start for offboarding tickets.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Risk & Compliance]
---

# Offboarding Intent Design

**When to use:** "Build an intent for employee terminations" / "offboarding requests come in vague and from random people — tighten the intake" / Intent Mining flagged user departures / disable-account requests as high volume.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build an offboarding intent that captures a complete, authorized termination request — including
whether it is an immediate for-cause lockout — and routes it to the offboarding workflow. It
disables nothing itself. Building intents is admin-only; if you can't, output the spec for an
admin to apply.

Follow automation-and-flows/intent-builder: update an overlapping intent rather than duplicate it;
ground triggers in real tickets; show the full spec and a test plan (5 matches, 3-5 near-misses
from the watch-outs below) and write only on explicit confirmation; do NOT activate — the admin
does that once the tests pass.

Spec:
- Triggers: "employee leaving", "offboard a user", "terminate an employee", "user's last day is",
  "disable an account", "someone quit", "remove a user", "deactivate <user>'s account".
  Watch-outs: "remove a user from <group>" is an access change, not offboarding; "reset the
  password for a leaving employee" is a reset that must still hand off.
- Arguments: departing user's name and systems in scope (default: all); last working day and the
  exact access cutoff; URGENCY CLASS — standard (scheduled last day) vs immediate for-cause
  lockout, the one argument that changes routing; requester name and role (must be an authorized
  requester per client policy); mail and data handling (mailbox forwarding, delegate access,
  retention, device return); anything to preserve (litigation hold, shared credentials the team
  still needs — flag, never disclose).
- Reply flow: (1) collect the arguments; on immediate urgency cut intake to identity, requester
  and cutoff and route to the client's urgent path — a lockout never waits on mailbox questions;
  (2) AUTHORIZED-REQUESTER CHECK — if the requester is not in the client's authorized-approver
  set, or the intent can't tell, reply that offboarding needs confirmation from an authorized
  contact and flag the ticket "authorization unconfirmed"; never silently accept it; (3) confirm
  the summary, create the ticket with a plain-text field block and route it to the offboarding
  workflow; (4) reply with next steps, no promises about when access ends.
- Handoff rule: disabling accounts, wiping devices and credential changes are always human or
  workflow actions.
- Variations per client: the authorized-requester list, urgent-lockout routing target, retention
  defaults, device-return and badge steps.
- Success metric: first-touch completeness and authorization coverage; watch lockout
  time-to-dispatch.

Guardrails: the authorization-unconfirmed flag is mandatory — a chat conversation alone must never
disable a person's livelihood access, and an unverified or ambiguous termination request is a
security event to escalate, not process. Never disclose the departing user's data, credentials or
mailbox contents. Do not invent the client's authorization policy or retention defaults.
```
