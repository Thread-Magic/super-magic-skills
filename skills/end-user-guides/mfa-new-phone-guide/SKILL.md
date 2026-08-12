---
name: MFA New Phone Guide
description: Draft reply-ready instructions for an end user who got a new phone and needs to move or re-enroll their MFA safely — "user has a new phone and can't approve sign-ins."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# MFA New Phone Guide

**When to use:** "User got a new phone and MFA prompts go nowhere." / "Send <user> steps to move their authenticator to the new phone." / a ticket mentions an upcoming phone upgrade.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for the most common MFA lockout: a new phone. The steps
branch HARD on one question — does the user still have the old phone — because the safe path is
completely different in each case. Verify the product first; when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's MFA product by checking the client's documentation and past tickets — Microsoft Authenticator, Duo, Okta Verify, etc. If unknown, ask the technician
   ONE question before drafting anything.
2. Determine which branch applies from the ticket: does the user still have the old, working phone?
   If the ticket doesn't say, the draft OPENS with that question and includes ONLY the still-have-it
   branch, with a clear "if the old phone is gone, stop here and reply — we'll reset it from our
   side" off-ramp. Never interleave both full branches — users execute half of each.
3. Branch A — old phone still works. Draft the transfer/re-enroll flow for the actual product:
   - Bolded first line: "Don't wipe or trade in your old phone until we confirm the new one works."
   - One action per step with what-you'll-see cues: install the named app on the new phone, sign in
     to the security/enrollment page from a computer, remove-or-add the sign-in method, scan the new
     QR code, approve a test prompt.
   - Mention authenticator cloud backup/restore only if the client's docs confirm it's permitted —
     some clients disable it.
   - Off-ramp on every risky step: "If you're asked for a code from the OLD phone and it's already
     wiped, stop and reply."
4. Branch B — old phone gone/wiped. The user cannot self-serve; re-enrollment needs an
   identity-verified MFA reset on the admin side. The user-facing draft says ONLY: what will happen
   ("we'll clear the old registration after verifying it's really you"), how identity will be
   verified per the client's documented procedure, and that they'll do a fresh enrollment
   afterwards. The admin reset steps never appear in the draft.
5. Assemble per the Email Baseline Standard.

Guardrails: identity verification is non-negotiable in Branch B — a "new phone, reset my MFA"
request is a textbook account-takeover pretext; never promise a reset before the client's
verification procedure runs, and remind the tech of that when producing Branch B. Product match
verified before drafting; no generic steps. Never instruct the user to disable MFA "temporarily,"
and never include admin-portal steps. No codes, QR images, or recovery keys over email in either
direction. Localizable; draft in the thread's language; version-cautious UI cues. Docs tools exist
only when enabled.
```
