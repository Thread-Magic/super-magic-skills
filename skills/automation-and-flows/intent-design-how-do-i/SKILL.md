---
name: How-Do-I Self-Help Router Intent Design
description: Design the catch-all "how do I" self-help router intent: classify the how-to, serve the matching end-user guide or KB article, escalate only if no match.
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
Build the catch-all self-help router: recognize generic "how do I…" questions, classify the topic,
serve the matching end-user guide to deflect, and escalate only when there is genuinely no
guidance. Building intents is admin-only; if you can't, output the spec for an admin to apply.

Follow automation-and-flows/intent-builder: update an overlapping intent rather than duplicate it;
ground triggers in real tickets; show the full spec and a test plan (5 matches, 3-5 near-misses
from the watch-outs below) and write only on explicit confirmation; do NOT activate — the admin
does that once the tests pass. Review ALL existing intents first, not just
near-duplicates — this router is scoped around their triggers. Cluster the how-to tail in recent
tickets (a large cluster deserves its own intent instead), then check which clusters actually have
guides: that set is deflectable, the rest defines the KB-gap path.

Spec:
- Triggers: "how do I…", "how to…", "where do I find…", "can you show me how to…", "what's the
  steps to…", "I don't know how to…", "is there a guide for…", "how do I set up…". Watch-outs, all
  of which must NOT match here: "how do I reset my password" belongs to password-reset, "how do I
  book a room" to room-booking — any topic a dedicated intent already owns.
- Collision rule, critical: this is the safety net BENEATH the specific intents and sits below
  them in priority. Confirm the ordering when you create it.
- Arguments, minimal — enough to classify and search: the topic in their words; which app or
  system, if stated; whether a guide already failed them, which raises escalation priority.
- Reply flow, deflect first: (1) classify the how-to and search the knowledge base for a matching
  end-user guide; (2) good match -> reply with the link plus a one-line summary of the relevant
  steps and ask "did that answer it?" — a confirmed yes is a deflection; (3) no match, or the
  guide didn't help -> create a ticket capturing topic, app and what they tried, route it to the
  general helpdesk queue, and flag recurring no-article topics as KB gaps; (4) never fabricate
  steps or invent an article link — with nothing in the knowledge base, escalate.
- Handoff rule: the router serves existing guidance and captures intake — it never performs the
  task, improvises a procedure, or acts on an account or device.
- Variations per client: which knowledge source to search, the escalation queue,
  always-escalate topics, reply branding and tone.
- Success metric: deflection rate; watch false capture — specific-intent questions landing here —
  and the KB-gap list.

Guardrails: the dominant failure mode is a catch-all swallowing questions that belong elsewhere,
so test specific-intent near-misses hard. Do not invent the client's knowledge source or escalation
queue; placeholder and flag before activation. Field block in plain text.
```
