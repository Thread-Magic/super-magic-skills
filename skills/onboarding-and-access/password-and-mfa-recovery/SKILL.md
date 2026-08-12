---
name: Password & MFA Recovery
description: Reset a password or recover MFA with the identity-verification ladder, a locked-vs-disabled check, and secure credential delivery. Use when a user is locked out, forgot a password, or lost/replaced their authenticator device.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_knowledge_base, search_itglue, add_ticket_note, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Password & MFA Recovery

**When to use:** "I'm locked out" / "reset my password" / "can't sign in" / "new phone — MFA codes don't work" / "user lost their authenticator" — a lockout alert or reset request on the queue.

**Run it:** on one ticket — identity-verification is human-gated; never auto-resets.

## Prompt

```
Complete this credential recovery with identity verified per the ladder, the account
state diagnosed first, and the new credential delivered securely. The ticket
documents everything except the secret itself.

1. Diagnose before touching anything: is the account locked (bad-password lockout),
   disabled, or expired? A disabled account may be an offboarded/suspended user — do
   NOT re-enable it as part of a "reset"; stop and confirm with the client's
   authorized contact why it is disabled.

2. Verify identity using the client's ladder before any credential action:
   - Remote, standard: full name plus employee ID, or confirmation from the user's
     manager.
   - Remote, higher assurance (VIPs, finance, admins, or anything smelling of
     compromise): call the user back on a number already on file — never a number
     provided in the ticket or email itself.
   - In person: photo ID.
   If the client documents a stricter policy (knowledge base / IT Glue documentation),
   that policy wins. No verification, no reset.

3. Password path: reset with "user must change password at next sign-in" forced. If
   hybrid AD, run an AD Connect delta sync and verify before telling the user to try.

4. MFA path: clear or re-register the lost method, then either walk the user through
   re-enrollment or issue a Temporary Access Pass (TAP) / equivalent time-boxed
   credential so they enroll the new device themselves. Prefer the TAP path over
   disabling MFA — never leave MFA off.

5. Deliver the temporary credential only through the client's secure transfer channel
   (secure link, password-manager share, or read over a verified call). Never plain
   email, never pasted into the ticket or chat.

6. If anything suggests compromise (user didn't request the reset, unfamiliar sign-in
   activity, MFA-fatigue reports), revoke active sessions and escalate to the
   security-alert process instead of finishing here.

7. Note the ticket in plain text: verification method used (not the answers), account
   state found, action taken, delivery channel — no credential content. Log time.

Guardrails: never reset on an unverified request; never verify against contact
details supplied inside the request itself. Never paste a password, TAP, or one-time
code into the ticket, chat, or email — temporary credentials go only by secure
handoff. Never re-enable a disabled account under cover of a reset. Force change at
next sign-in on every temporary password. When in doubt about identity or account
state, do nothing and escalate.
```
