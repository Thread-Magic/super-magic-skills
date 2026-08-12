---
name: SSPR Password Reset Guide
description: Draft reply-ready instructions an end user can follow to reset their own password via self-service password reset — "send the user steps to reset their password themselves."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# SSPR Password Reset Guide

**When to use:** "Send <user> instructions to reset their own password." / "User forgot their password — can they self-serve?" / a reset ticket where the client has SSPR enabled and the user just needs the steps.

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block the technician sends so the end user can reset their own
password through this client's self-service password reset (SSPR) — matched to the actual product,
not a generic walkthrough. Verify the stack before you write; when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's SSPR stack FIRST. Search client docs and prior tickets for what this client uses — Microsoft
   Entra SSPR, Duo, ADSelfService Plus, Okta, or something else — AND whether SSPR is actually
   enabled and this user is registered for it. If none of that is findable, ask the technician ONE
   question ("Which self-service reset does this client use, and is <user> registered?") — never
   send generic steps.
2. Confirm the entry point: the exact reset URL or "Forgot my password" path documented for that
   product for this client. Do not invent URLs; if the documented entry point is missing, flag it
   to the tech instead of guessing.
3. Write the instruction block to end-user rules:
   - Plain language, no jargon ("the sign-in page," not "the IdP portal").
   - Numbered, one action per step, each with a what-you'll-see cue ("a screen asks how you want to
     verify — text message or authenticator app").
   - Include the verification-method branch the user will actually hit (phone code, authenticator
     approval, security questions) based on what the product supports for this client.
   - Password requirements in plain terms only if documented for this client; never invent a policy.
   - Off-ramp: "If any screen looks different from this, or you get an error, stop here and reply —
     don't keep trying." (Too many failed attempts can lock the account — keep this in every draft.)
   - The aftermath step: sign back in on computer and phone with the new password, since saved
     passwords (wifi, mail app) will prompt again.
4. Assemble per the Email Baseline Standard: one context line, the instruction block, next steps.

Guardrails: never send steps for a product the client doesn't run — stack verification is mandatory,
not best-effort. If the user is NOT registered for SSPR, do not send this guide — tell the tech the
reset must be done admin-side, and offer to note that on the ticket; no admin-side steps ever appear
in the user block. Never include a password, a temporary password, or instructions to email one.
Localizable — if the thread is in another language, draft the block in that language. Docs tools
exist only when the integration is enabled; fall back to KB and ticket history.
```
