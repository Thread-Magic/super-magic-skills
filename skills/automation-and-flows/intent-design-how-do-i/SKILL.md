---
name: How-Do-I Self-Help Router Intent Design
description: Build the catch-all "how do I…" self-help router — classify the how-to, serve the matching end-user guide or KB article, and escalate only when no guidance exists. Use when asked to "build a how-to intent", "deflect how-do-I questions", or when general how-to queries dominate Intent Mining.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# How-Do-I Self-Help Router Intent Design

**When to use:** "Build a general how-to / self-help intent" / "we get a long tail of one-off how-do-I questions with no dedicated intent each" / Intent Mining shows a large low-frequency how-to tail that no single intent covers.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build the catch-all self-help router: recognize generic "how do I…" questions, classify the
topic, serve the matching end-user guide or KB article to deflect, and escalate to a human
only when there is genuinely no guidance. It is the safety net BENEATH the specific intents —
deliberately broad, but it must yield to more specific intents rather than swallow them.
Building intents is admin-only; if you can't, degrade to a complete written spec for an admin.

Design the intent to this spec:
- Trigger phrases (adapt to real ticket language): "how do I…", "how to…", "where do I
  find…", "can you show me how to…", "what's the steps to…", "I don't know how to…", "is
  there a guide for…", "how do I set up…".
- Collision rule (critical): this intent must sit BELOW the specific intents in priority.
  "How do I reset my password" belongs to password-reset; "how do I book a room" to room-
  booking. Keep this router's job to topics NOT covered by a dedicated intent — test that
  specific-intent utterances do NOT get captured here.
- Arguments (minimal — just enough to classify and search): the topic / what they're trying
  to do, in their words; which app or system, if stated; whether they've already tried a guide
  that didn't help (raises escalation priority).
- Reply flow (deflect-first via KB): (1) classify the how-to and search the knowledge base for
  a matching end-user guide; (2) good match -> reply with the article (link + one-line summary
  of the relevant steps) and ask "did that answer it?" — a confirmed yes is a deflection; (3)
  no match, or the user says the guide didn't help -> create a ticket capturing topic, app,
  and what they've tried, route to the general helpdesk queue, and flag recurring no-article
  topics as KB-gap candidates; (4) never fabricate steps or invent an article link — if the KB
  has nothing, escalate rather than inventing guidance.
- Handoff rule: the router only serves existing guidance and captures intake — it does not
  perform the task or improvise procedures. Anything requiring an action on the user's
  account or device is escalated.
- Variation hooks (per client): which KB/doc source to search, escalation queue, always-
  escalate topics, reply branding/tone.
- Success metric: deflection rate; watch false-capture rate (specific-intent questions wrongly
  landing here) and the KB-gap list.

Steps:
1. List the existing intents — review ALL of them first; this router must be scoped to avoid
   overlapping their triggers and set to lower priority so specific intents win.
2. Search the how-to tail in recent tickets; cluster topics to see what recurs and whether any
   cluster deserves its own intent instead of living in the catch-all.
3. Search the knowledge base to confirm which clustered topics actually have end-user guides —
   that's the deflectable set; the rest defines the escalation and KB-gap paths.
4. Draft the full spec (broad-but-scoped triggers, minimal arguments, KB-match->deflect /
   no-match->escalate flow, routing target, variations) plus a test plan (5 generic how-tos
   that should match, 3–5 specific-intent utterances that should NOT). Show before any write.
5. On explicit confirmation: create the intent, then set its variations; confirm priority
   ordering keeps specific intents ahead of it.
6. Report what was created, restate the test plan and the priority note, recommend activation
   only after tests pass. Do NOT activate.

Guardrails: priority discipline — this catch-all must never outrank a specific intent; the
dominant failure mode is swallowing questions that belong elsewhere, so test specific-intent
near-misses hard. Never fabricate steps or invent a KB link; if there's no article, escalate.
The router serves guidance and captures intake only — it never performs the task or acts on an
account/device. Do not invent the client's KB source or escalation queue — placeholder and
flag before activation. Confirm before any write; ticket field block in plain text.
```
