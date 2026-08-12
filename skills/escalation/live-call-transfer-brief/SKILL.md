---
name: Live Call Transfer Brief
description: One-minute brief for transferring a live in-progress call to another technician — caller context, what's been tried, sentiment alert, and a verbal opener.
category: Escalation
tools: [search_tickets, search_contacts, add_ticket_note, run_assistive_ai]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Live Call Transfer Brief

**When to use:** "I need to transfer this call to <member> — brief them"; a call is being escalated mid-conversation to a senior tech or specialist; or a dispatcher is warm-transferring a caller and needs to prep the receiver fast.

**Run it:** on one ticket (a live, in-progress call).

## Prompt

```
The receiving technician has seconds, not minutes — the caller is on hold. Produce a
brief they can absorb before they pick up.

1. Identify the caller and ticket. Pull the ticket thread and the caller's details; note
   VIP status and recent history with this issue.

2. Build the brief, hard-capped at a one-minute read, in this order:
   - Caller: <user> at <client>, role, callback number on file.
   - Issue: one sentence, in the caller's terms.
   - Done on this call: the steps already walked through and their results — so the
     receiver never repeats them.
   - Sentiment alert: flag prominently if the caller is frustrated, has called
     repeatedly, mentioned management, or the ticket sentiment is negative (use a
     sentiment read when available). State WHY, e.g. "third call this week on the same
     issue."
   - Next step: the single thing the receiver should do first.

3. Write the ready-to-say opening line — a verbatim sentence the receiver can speak as
   they pick up, proving the handoff worked and nothing must be repeated: "Hi <user>,
   this is <member> — I've got everything from your call so far, I can see the reinstall
   didn't take, so let's go straight to checking your profile."

4. Show the brief in chat for the transfer. Offer to also post it as a plain-text
   internal note so the call record survives — post only on confirmation.

Guardrails: never make the caller repeat themselves — everything already tried on the
call must be in the brief. The opening line claims only what is documented — no
scripted promises ("we'll fix this today") or invented familiarity. Sentiment alerts
state evidence, not diagnosis; keep language factual and respectful — the note may be
read later by the client. If the ticket can't be found, brief from what the technician
tells you and say the history could not be pulled — do not invent prior context.
Notes posted to the ticket are plain text.
```
