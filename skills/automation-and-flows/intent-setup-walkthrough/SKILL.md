---
name: Intent Setup Walkthrough
description: Walk through building a new Triage Agent intent from scratch — check it doesn't already exist, then set the name, description, trigger variations, replies, and any arguments — so a new automatic response is set up cleanly and without duplicates.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, set_variation_arguments, set_variation_replies]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Intent Setup Walkthrough

**When to use:** Setting up a new automatic reply for the Triage Agent — "create an intent for password reset requests" — and you want it built end to end without accidentally duplicating one that already exists.

**Run it:** as a guided setup — one intent at a time, with your confirmation at each step.

## Prompt

```
Help me build a new Triage Agent intent from scratch, checking for duplicates first and confirming
each part before it's created.

1. Check for duplicates. Pull the full list of existing intents and scan for any with a similar
   name or purpose to what I want to create. If a close match already exists, show it and ask me to
   confirm I still want a new one before going further — don't create a near-duplicate silently.

2. Gather the basics. Ask me for anything I haven't given:
   - Name — short and unique.
   - Description — what this intent does and when it should fire.
   - Roughly how much time it saves each time it triggers (fine to leave at zero if unsure).

3. Gather the trigger variations. These are the different ways a client might phrase the request
   that should fire this intent (for a password reset: "I'm locked out", "can't log in", "need my
   password reset"). Ask me for a handful of real phrasings, and suggest a few more so the intent
   catches natural variety, not just one exact wording.

4. Gather the replies. What should the agent say when this intent fires? Draft the reply in plain,
   client-ready language and show it to me to approve or edit before it goes on the intent.

5. Gather any arguments. If the intent needs to collect something from the client to act (a device
   name, a location, an affected user), list those fields and confirm them with me.

6. Confirm the whole thing back to me — name, description, variations, replies, arguments — in one
   summary, and only create it after I approve. Then set up its variations, replies, and arguments
   as confirmed.

7. Show me the finished intent so I can review it, and offer to set up the next one.

Never create an intent without my confirmation, and never invent trigger phrases or replies I
haven't seen — draft them, but let me approve. If something's ambiguous, ask rather than guess.
```
