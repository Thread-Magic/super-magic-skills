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
Build a password-reset intent that pushes users to self-service reset (SSPR) first and routes
everything else to a verified human handoff. Building intents is admin-only; if you can't, output
the complete written spec for an admin to apply.

Follow automation-and-flows/intent-builder: check the existing intents and prefer updating a
password/login intent over duplicating it; ground triggers in 5-10 recent real password and
lockout tickets; reference the client's existing SSPR knowledge-base article rather than restating
steps that drift; show the full spec plus a test plan (5 should-match, 3-5 near-misses — "reset
the printer", "password for the wifi" — that should not) and write only on explicit confirmation;
report what was created and recommend the admin activate once the tests pass. Do NOT activate.

Spec:
- Triggers: "forgot my password", "reset my password", "can't log in", "cant login", "locked out
  of my account", "password expired", "my password isn't working", "account locked", "pw reset",
  "need a new password", "login not working", "I keep getting invalid password". Keep them generic
  to account and directory sign-in — "can't log in to <specific app>" may belong to an
  application-specific intent.
- Arguments: which system or account (directory/M365 vs a specific application — it routes the
  reply); whether they can still receive MFA or reach their registered recovery method (it decides
  SSPR vs handoff); device context only where the client's SSPR flow differs by device.
- Reply flow, SSPR first: (1) directory/M365 and the recovery method works -> reply with the
  client's SSPR link and exact steps, then ask "did that work?"; (2) it worked -> confirm and close
  as deflected; (3) SSPR failed, no recovery method, or no SSPR at all -> create a ticket flagged
  "identity verification required" carrying the collected arguments, and tell the user a technician
  will verify identity before any reset.
- Handoff rule, non-negotiable: any path ending in a human changing a credential must state that
  identity verification happens first. The intent never communicates a password, never resets one,
  never bypasses MFA.
- Variations per client: SSPR portal URL, identity provider, whether SSPR is enabled at all (if
  not, go straight to the verified-ticket path), verification-policy wording.
- Success metric: deflection rate — matched conversations ending without a ticket; watch the
  false-match rate on the near-miss set.

Guardrails: credential actions ALWAYS hand off to a verified human path — never reveal, set or
reset a password, or walk a user around MFA. Do not invent the client's SSPR URL or verification
policy; placeholder and flag it as required before activation. Replies are customer-facing: plain,
localizable, no jargon, no fabricated turnaround promises.
```
