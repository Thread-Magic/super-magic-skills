---
name: Outlook Profile Setup Guide
description: Draft reply-ready instructions for an end user to add their work account to Outlook on Windows or Mac — "send the user steps to set up Outlook."
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Outlook Profile Setup Guide

**When to use:** "Send <user> instructions to add their email to Outlook." / new machine, new profile, or profile-rebuild tickets where the user does the add themselves / "user's Outlook profile was removed — walk them through re-adding."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for adding the work email account to desktop Outlook —
branched by platform, with ONLY the branch that matches the user's machine. Verify the environment
before you write; when unsure, ask one identifying question rather than sending a two-platform
mega-guide. Draft only — show me the reply as a draft to review first, and don't send it.

1. Verify the environment FIRST from the ticket, prior tickets, and client docs: (a) Windows or Mac, (b) which Outlook —
   classic Outlook, new Outlook for Windows, or Outlook for Mac, (c) is the mailbox Microsoft 365
   (the normal case) or something else (hosted Exchange, IMAP). The flow differs completely. If
   platform or mailbox type is unknown, ask the technician ONE question — or open the draft with one
   identifying question ("Does your Outlook have a 'File' menu in the top-left? Reply yes or no")
   and defer the rest.
2. Write the single matching branch to end-user rules, one action per step:
   - What-you'll-see cues ("a window titled 'Add account' opens with one empty box for your email").
     Orientation cues, phrased version-cautiously: classic Outlook (Windows) File → Add Account; new
     Outlook for Windows gear/Settings → Accounts → Add account; Mac Outlook menu → Settings →
     Accounts → +.
   - The user enters their full work email; modern sign-in takes over — tell them the sign-in page
     looks like their webmail login and an MFA prompt on their phone is expected.
   - State the wait honestly: "your mail and calendar fill in over the next several minutes to a few
     hours depending on mailbox size — old items appear last."
   - Off-ramps: "If you're asked for a server name, port, or anything technical — stop and reply;
     you should never need those." / "If sign-in loops or errors, stop and reply with a photo of the
     screen."
3. Do not include admin-side material (Autodiscover records, registry keys, license assignment). If
   docs suggest the mailbox/license isn't ready, flag to the tech before drafting.
4. Assemble per the Email Baseline Standard.

Guardrails: platform and Outlook-flavor match is mandatory — Mac steps to a Windows user is an
instant failed reply. Never include server settings, ports, or manual-configuration paths in a user
draft — if manual config is genuinely needed, that's a tech-driven session, not an email. Never ask
the user to send their password; the draft should say "we will never ask for your password by
email." Localizable; version-cautious cues (Outlook UI changes frequently). Docs tools exist only
when enabled.
```
