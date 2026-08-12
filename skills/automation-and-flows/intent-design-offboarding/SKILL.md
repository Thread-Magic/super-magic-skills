---
name: Offboarding Intent Design
description: Build the employee-termination intake intent with an authorized-requester check and urgency handling designed in from the start. Use when asked to "build an offboarding intent", "automate termination requests", or when user-departure tickets rank high in Intent Mining.
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
Build an offboarding intent that captures a complete, authorized termination request —
including whether it is an immediate/for-cause lockout — and routes it to the offboarding
workflow. The intent never disables anything itself; it produces a verified, dispatch-ready
ticket. Building intents is admin-only; if you can't, output the complete written spec for an admin.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "employee leaving", "offboard a user",
  "terminate an employee", "user's last day is", "disable an account", "someone quit",
  "remove a user", "employee termination", "staff member is leaving", "deactivate <user>'s
  account". Near-miss watch: "remove a user from <group>" is an access change, not offboarding.
- Arguments: departing user's name and systems/accounts in scope (default: all); last working
  day and exact cutoff time for access; URGENCY CLASS — standard (scheduled last day) vs
  immediate lockout (for-cause), the single argument that changes routing; requester's name
  and role (must be an authorized requester per client policy); mail and data handling
  (forward mailbox to whom, delegate access, retain how long, device return); anything to
  preserve (litigation hold, shared credentials the team still needs — flag, never disclose).
- Reply flow: (1) collect arguments; if urgency = immediate, shorten intake to identity +
  requester + cutoff and route to the client's urgent path — don't make a lockout wait on
  mailbox questions; (2) AUTHORIZED-REQUESTER CHECK — if the requester is not in the client's
  authorized-approver set (or the intent can't tell), the reply states offboarding requires
  confirmation from an authorized contact, and the ticket is flagged "authorization
  unconfirmed", never silently accepted; (3) confirm the summary, create the ticket with a
  plain-text field block, route to the offboarding board/workflow; (4) reply with next steps,
  no promises about when access ends.
- Handoff rule: disabling accounts, wiping devices, and credential changes are always
  human/workflow actions. An unverified or ambiguous termination request is a security event
  — escalate, do not process.
- Variation hooks (per client): who counts as an authorized requester, urgent-lockout routing
  target, mailbox retention defaults, device-return instructions, badge/physical access steps.
- Success metric: first-touch completeness plus authorization coverage; watch immediate-
  lockout time-to-dispatch.

Steps:
1. List the existing intents — check for an existing offboarding/termination intent; prefer updating.
2. Search recent departure tickets; mine trigger phrasing and every clarifying
   question techs asked (candidate arguments), and note who typically submits these.
3. Draft the full spec with the authorized-requester rule and immediate-lockout branch
   explicit. Test plan: 5 should-match, 3–5 should-not (incl. a group-removal near-miss and a
   "reset password for leaving employee" case that must still hand off). Show before any write.
4. On explicit confirmation: create the intent, then set its variations.
5. Report what was created, restate the test plan, recommend activation after tests pass. Do
   NOT activate.

Guardrails: the intent must never accept a termination from an unverified requester as
routine — the authorization-unconfirmed flag is mandatory, and a chat conversation alone must
never disable a person's livelihood access. Never disclose the departing user's data,
credentials, or mailbox contents to the requester. Do not invent the client's authorization
policy or retention defaults; placeholder and flag before activation. Confirm before any
write; ticket field block in plain text.
```
