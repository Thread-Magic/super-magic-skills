---
name: Intent Builder
description: Build or update a customer-facing intent — trigger phrases, arguments, replies, and variations — with a test plan before anything goes live. Use when asked to "create an intent", "add trigger phrases", "update the replies for an intent", or after Intent Mining picks a candidate.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Intent Builder

**When to use:** "Build an intent for password reset requests" / "add more trigger phrases to the new-user intent — it keeps missing" / "change what the office-move intent asks for."

**Run it:** as a build task on request — you're authoring a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Take an intent from concept to a fully specified, tested draft — activated only after the
admin explicitly says go. Building intents is admin-only; if you can't (the member lacks
admin rights), output the full spec for an admin to apply instead.

1. List the existing intents and check for overlap. If a similar intent exists, propose
   updating it instead of creating a near-duplicate.

2. Ground the language: pull 5–10 real ticket examples of the request and mirror
   the end users' actual phrasing in the trigger set.

3. Draft the full spec and SHOW IT before touching any write tool:
   - Trigger phrases — 8–15, varied in vocabulary and length; include misspellings and
     short forms users actually type.
   - Arguments — only what the workflow genuinely needs (who, what system, when). Every
     argument adds friction.
   - Replies per variation — plain, localizable language; no idioms, no fabricated policy
     answers. If a reply states a policy (turnaround time, approval requirement) it must
     come from the member, not be invented. No internal jargon, no client or staff names,
     no promises the member did not approve.

4. Include a test plan in the draft: 5 utterances that should match, and 3–5 near-miss
   utterances that should NOT match. Check the "should NOT match" list against existing
   intents' trigger phrases and flag any collision before creating.

5. On explicit confirmation ONLY: create (or update) the intent, then set its variation
   arguments and replies as needed. Never write without showing the complete draft and
   getting a clear yes.

6. Report exactly what was created/changed and restate the test plan for the member to
   verify in a test conversation. Do NOT activate the intent — recommend the member
   activate it after the test utterances pass.
```
