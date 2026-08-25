---
name: Out of Office Guide
description: Draft reply-ready instructions for an end user to set their own out-of-office reply correctly — dates, internal versus external messages for OOO.
category: End-User Guides
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, view_openDraft]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Out of Office Guide

**When to use:** "Send <user> steps to set their out-of-office." / pre-vacation and leave tickets where the user sets it themselves / "user's OOO is still on / never turned on — send the how-to."

**Run it:** on one ticket.

## Prompt

```
Draft a client-ready instruction block for setting automatic replies properly, handling the two
traps: the internal/external split (most users don't know there are two messages) and the
forgot-to-set-dates auto-reply that runs forever. Prefer the web path — it works for everyone and
survives version drift. Draft only: show it to me first, send nothing.

1. Verify the environment FIRST, from the client's documentation and past tickets: which Outlook
   the user reaches most easily (prefer web), and whether the client restricts external automatic
   replies. If the documentation shows external replies are blocked, the draft says so rather than
   promising strangers get the message. If the mailbox in question is a shared mailbox, STOP —
   that is set admin-side; tell the tech and send no user steps.
2. Write the web-first flow to end-user rules, one action per step with what-you'll-see cues:
   - Sign in to webmail; the settings gear; search or look for "Automatic replies" — cue: "a panel
     with an on/off switch at the top."
   - Turn it on, tick the send-only-during-a-time-period option, and set BOTH dates, with the why:
     "this makes it switch itself on and off; without dates you'll be that person whose 'back on
     Monday' reply is still going out in August." Suggest starting the evening before leave and
     ending the morning of return. Never draft this guide without this step and its plain-language
     why — it is the core of the skill.
   - The two message boxes, plainly: the first goes to coworkers, the second to everyone outside
     the company — "they can be the same text, but the outside one is what clients see, so keep it
     professional and light on detail." This distinction appears in every draft.
   - What a good message contains — offer a fill-in skeleton with bracketed placeholders: dates
     back, who to contact meanwhile (a name and address the user supplies; never invented — flag
     "NEEDS: covering contact" if unknown), and no more. Keep travel details out of the external
     message: don't advertise an empty house or exact plans.
   - Calendar-tidy extras as one line: "you may also see options to block your calendar — nice to
     have, optional."
   - Off-ramp: "If your settings don't show an Automatic replies option, stop and reply — your
     mailbox may be set up differently and we'll set it for you."
3. Where external replies are permitted, include the verification step: "Send yourself a test from
   a personal address after it's on — you should get the external reply back within a minute or
   two."
4. Assemble per the Email Baseline Standard.

Guardrails: shared-mailbox out-of-office requests never get user steps — route them to the
tech/admin side. No admin steps (mailbox rules via the admin center, transport rules) in the user
block. Localizable. Docs tools exist only when enabled.
```
