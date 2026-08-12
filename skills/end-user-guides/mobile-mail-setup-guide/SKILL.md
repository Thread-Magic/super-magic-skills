---
name: Mobile Mail Setup Guide
description: Draft reply-ready instructions for an end user to get work email on their phone — Outlook mobile app first, matched to the client's mobile policy.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Mobile Mail Setup Guide

**When to use:** "Send <user> instructions to get email on their phone." / new hire or new phone tickets where mobile mail is part of setup / "user's phone stopped getting mail after the security rollout."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for setting up work mail on a phone. Default path is the
Outlook mobile app (same on iPhone and Android, plays well with security policies); native mail
apps only if the client's policy explicitly allows them. Verify the mobile policy before you write;
when unsure, ask. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the client's mobile policy FIRST by checking the client's documentation and past tickets: is there MDM/app protection (e.g., Intune) that requires a companion app or
   blocks native mail? Are personal devices allowed at all? Is this a corporate-managed phone (mail
   may deploy automatically — no guide needed)? If policy is unknown, ask the technician ONE
   question — native-app steps sent to a client that blocks native mail create a "broken"
   experience the user blames on IT.
2. Write the Outlook-app path (the default) to end-user rules, one action per step:
   - Install "Microsoft Outlook" from the official app store (name the store per platform; describe
     the icon), open it, enter the full work email, complete the same sign-in they use for webmail,
     expect the MFA prompt.
   - What-you'll-see cues throughout ("the first screen asks only for your email — nothing else").
   - If the client uses app protection, warn plainly: "you may be asked to install a second app or
     set a PIN for the mail app — that's our security policy, it's expected, go ahead."
   - Honest wait note: recent mail in minutes; the full mailbox trickles in.
   - Off-ramps: "If you're asked for server names or ports, stop and reply." / "If your phone says
     the app is 'managed' and you're not comfortable, stop and reply — we'll explain first."
3. Include the native-mail branch ONLY if client docs confirm it's permitted, and even then as a
   secondary "if you strongly prefer the built-in mail app" section — never the lead.
4. Personal-device consent: if this is a personal phone and the client requires enrollment/app
   protection, say plainly what the company can and cannot do on their phone per the client's
   documented policy — and if that policy text isn't documented, flag to the tech rather than
   improvising a privacy statement.
5. Assemble per the Email Baseline Standard.

Guardrails: policy verification is mandatory — the failure mode isn't wrong steps, it's steps that
silently hit a policy wall and generate a frustrated callback. Never draft privacy/consent claims
about MDM beyond what the client's documentation states. No admin-side steps (Intune console,
conditional-access) in the user block. No server settings, app passwords, or "less secure app"
workarounds — ever. Localizable; version-cautious cues. The client's documentation is available only when those integrations are enabled.
```
