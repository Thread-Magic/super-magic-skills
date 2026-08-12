---
name: Password Expiry Change Guide
description: Draft reply-ready instructions for an end user to change a password that's about to expire (or just did) before it locks them out of their account.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Password Expiry Change Guide

**When to use:** "User got the 'your password expires in N days' warning — send them how to change it." / "User's password expired and can't sign in — send change steps." / proactive nudge from an expiry report.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for an end user whose password is expiring or has expired,
walking them through changing it themselves the way this client's environment expects — before a
lockout turns a two-minute self-service into a help-desk call. Verify the environment before you
write; when unsure, ask, don't guess. Draft only — show me the reply as a draft to review first, and don't send it.

1. Identify the client's change path FIRST. Check client docs and prior tickets: where passwords change for this shop
   — the Windows Ctrl+Alt+Del "Change a password" screen (domain-joined), the Microsoft/Entra
   change-password page, a self-service portal, or the sign-in "your password has expired" flow.
   Note the client's actual complexity and password-history rules if documented. If the path is
   unknown, ask the technician ONE question — never guess.
2. Check the already-expired branch. If the user is already locked out and can't reach a change
   screen, self-service may not be possible — that can need a tech reset. Only send change steps
   when the user can still authenticate; if the account is locked, do not tell them to keep trying,
   route to a reset instead.
3. Write the instruction block to end-user rules — one action per step, plain language, a
   what-you'll-see cue on each:
   - The entry point named exactly ("press Ctrl, Alt and Delete together, then choose 'Change a
     password'").
   - Old password once, new password twice, with a plain-language version of the client's actual
     rules ("at least 12 characters, and you can't reuse a recent one").
   - A tip for a strong, memorable passphrase — without ever suggesting they write it in the email.
   - The confirmation cue ("you'll see 'Your password has been changed'") and the MANDATORY
     day-to-day consequence: they must update the new password everywhere it's saved — phone mail,
     saved wifi, any app that remembered the old one — or those will lock the account with repeated
     retries. This "update it everywhere" warning is the #1 post-change lockout cause; include it
     every time.
   - Off-ramp: "If you get locked out or a screen doesn't match these steps, stop and reply — don't
     keep guessing, repeated tries can lock the account."
4. Assemble per the Email Baseline Standard (one context line, the steps, next steps).

Guardrails: never include, ask for, or propose a specific password in the email. No admin-side
steps (resetting from the console, unlocking, changing expiry policy) in the user block — those are
tech actions. A domain Ctrl+Alt+Del walkthrough sent to a cloud-only user fails at step one — path
match is mandatory. Keep phrasing localizable and UI cues version-cautious. Never invent a policy or
a URL. Docs tools by checking the client's documentation exist only when enabled; fall back to KB and ticket
history.
```
