---
name: Password Reset Intent Design
description: Design the password-reset intent — the top deflection target on most desks — with an SSPR-first reply path and a strict identity-verification handoff.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Password Reset Intent Design

**When to use:** "Build an intent for password resets" / "half our tickets are password resets — can Magic handle them?" / Intent Mining ranked password reset as the top build candidate.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a password-reset intent that pushes users to self-service reset (SSPR) first and
routes everything else to a verified human handoff. The intent NEVER resets a password
itself — it deflects to SSPR or produces a well-formed, identity-flagged ticket. Building
intents is admin-only; if you can't, output the complete written spec for an admin to apply.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "forgot my password", "reset my
  password", "can't log in", "cant login", "locked out of my account", "password expired",
  "my password isn't working", "account locked", "pw reset", "need a new password", "login
  not working", "I keep getting invalid password". Keep triggers generic to account/directory
  sign-in; "can't log in to <specific app>" may belong to an application-specific intent.
- Arguments: which system/account (directory/M365 vs a specific application — routes the
  reply); whether they can still receive MFA / access their registered recovery method
  (decides SSPR vs handoff); device context only if the client's SSPR flow differs by device.
- Reply flow (SSPR-first ladder): (1) directory/M365 + user can use their recovery method ->
  reply with the client's SSPR link and exact steps, then ask "did that work?"; (2) SSPR
  succeeded -> confirm resolution, close as deflected; (3) SSPR failed / no recovery method /
  no SSPR -> create a ticket flagged "identity verification required" with the collected
  arguments, and tell the user a technician will verify identity before any reset.
- Handoff rule (non-negotiable): any path ending in a human changing a credential must state
  identity verification happens first. The intent never communicates a password, never resets
  one, never bypasses MFA.
- Variation hooks (per client): SSPR portal URL, identity provider, whether SSPR is enabled
  at all (if not, skip straight to verified-ticket path), verification-policy wording.
- Success metric: deflection rate on password-reset conversations (matched conversations
  ending without a ticket); watch false-match rate on the near-miss test set.

Steps:
1. List the existing intents — if a password/login intent exists, propose updating it
   rather than duplicating.
2. Search 5–10 recent real password/lockout tickets; mirror users' actual
   phrasing in the trigger set and note which systems come up.
3. Search the knowledge base for an existing SSPR article; reference it in the reply instead of
   restating steps that may drift.
4. Draft the full spec (triggers, arguments, reply ladder, handoff wording, variations) and
   a test plan — 5 utterances that should match, 3–5 near-misses ("reset the printer",
   "password for the wifi") that should not. Show it before any write.
5. On explicit confirmation ONLY: create the intent, then set its variations per client.
6. Report what was created, restate the test plan, recommend the admin activate only after
   the test utterances pass. Do NOT activate.

Guardrails: credential actions ALWAYS hand off to a verified human path — never reveal, set,
or reset a password, or walk a user around MFA. Do not invent the client's SSPR URL or
verification policy; leave a placeholder and flag it as required before activation. Replies
are customer-facing: plain, localizable, no jargon, no fabricated turnaround promises. Never
write without showing the complete draft and getting explicit confirmation.
```
