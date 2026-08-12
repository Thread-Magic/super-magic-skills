---
name: MFA Setup Guide
description: Draft reply-ready instructions for an end user to enroll in multi-factor authentication with the client's actual MFA product — "send the user MFA setup steps."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# MFA Setup Guide

**When to use:** "Send <user> instructions to set up MFA." / new-hire or security-rollout tickets where users must enroll an authenticator / "user keeps getting MFA prompts but never enrolled."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block walking an end user through enrolling their authenticator
for the first time — written for the specific MFA product this client runs. Verify the product
before you write; when unsure, ask, don't guess. Draft only — show me the reply as a draft to review first, and don't send it.

1. Identify the client's MFA product FIRST. Check client docs and prior MFA tickets: Microsoft Authenticator via
   Entra, Duo Mobile, Okta Verify, Google Authenticator against a specific system, or a hardware
   token. Note the enrollment entry point the client documents. If the product is unknown, ask the
   technician ONE question — never send steps for a guessed product; Duo steps sent to a Microsoft
   shop fail at step one.
2. Write the instruction block to end-user rules, one action per step:
   - Two tracks kept clearly separated: (a) install the app on the phone, (b) enroll on the
     computer.
   - A what-you'll-see cue at every step ("a square QR code appears on your computer screen"; "your
     phone will ask for camera permission — tap Allow").
   - Name the exact app to install ("Microsoft Authenticator — blue icon with a lock") so they
     don't grab a look-alike.
   - The confirmation step: the test prompt/code that proves enrollment worked, and what success
     looks like.
   - Off-ramp: "If the QR code won't scan, or any screen doesn't match these steps, stop and reply
     to this email."
   - Close with what changes day-to-day ("from now on you'll approve a prompt on your phone when
     signing in").
3. If the ticket shows the user has no smartphone or refuses a personal device, do not improvise an
   alternative — flag it to the tech (SMS, hardware tokens, or a policy exception are tech/admin
   decisions).
4. Assemble per the Email Baseline Standard.

Guardrails: product match is mandatory — if unverifiable, ask; don't guess. No admin-side steps
(conditional-access changes, per-user MFA toggles) in the user block; if enrollment needs an admin
action first, tell the tech, not the user. Never ask the user to share codes, QR screenshots, or
backup keys in email. Keep UI cues generic enough to survive minor app-store/portal updates ("look
for a button named roughly 'Add sign-in method'"). Localizable; draft in the thread's language.
The client's documentation is available only when those integrations are enabled; otherwise rely on the knowledge base and ticket history.
```
