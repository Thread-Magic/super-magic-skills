---
name: Super Magic Enablement
description: Prep a show-and-tell of the highest-value Super Magic use cases for a specific team, grounded in their own recent tickets so every example is recognizable.
category: Training & Enablement
tools: [search_tickets, search_thread_docs, search_members]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Staff Enablement, Time & Cost Savings (Capacity)]
---

# Super Magic Enablement

**When to use:** "Help me show the team what Super Magic can do" / running a lunch-and-learn or all-hands AI-adoption segment / "which Super Magic features would help us most?"

**Run it:** across the team's recent tickets to build the demo plan — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
You are building a team-specific Super Magic demo plan. Not a generic feature tour — mine THIS team's own recent tickets to find where Super Magic would have saved the most time, and package the top use cases as demo-ready examples the audience will recognize.

1. Confirm the audience (whole desk, dispatchers, a specific pod) and session length. Default: 20 minutes, 4-5 use cases. Look up the members if you need to scope to a particular pod.

2. Mine the team's recent tickets (last 30 days) for the patterns Super Magic serves best, and estimate ROUGH frequency for each — disclose result caps rather than presenting exact-sounding counts:
   - Repetitive drafting (many similar client replies) -> reply drafting and tone polish
   - Long multi-touch threads -> summarize-and-next-steps
   - "Has this happened before?" digging -> similar-ticket and history search
   - Drive-by capture (work done, ticket created after) -> create-ticket-with-time-entry by chat
   - Queue questions -> daily digest / what-should-I-work-on
   - Repeat manual routines -> candidates for skills and Flows

3. For each selected use case, build a demo card:
   - The recognizable pain: "Last month you had roughly N tickets like <sanitized example>"
   - The exact prompt to type, word for word
   - What the audience will see happen
   - The time saved estimate, stated conservatively and labeled as an estimate

4. Order the cards: open with the most universally felt pain, put the most impressive-looking demo second, end with one "builder" example (a skill or Flow) as the where-this-goes moment.

5. Verify each demo prompt is safe to run live. Prefer read-only demos (summaries, digests, searches) on real tickets. For any write demo (notes, time entries, status changes), script it against a test or sandbox ticket — never a real client ticket.

6. Output the session plan: agenda with timings, the demo cards, a one-slide-equivalent "what to try this week" (3 prompts per role), and speaker notes on likely questions. Reference official capability descriptions from the Thread docs where precision matters.

Guardrails: Every use case must trace to observed ticket patterns from THIS team — no generic marketing claims presented as their data, and never invent ticket examples or frequencies. Time-saved figures are estimates; label them as such and keep them conservative. If a search may have hit a result cap, disclose it rather than presenting an estimate as exact. Sanitize every example ticket shown to a group: replace client, contact, and staff names with placeholders (<client>, <user>, <device>) and strip credentials, ticket IDs, hostnames, phone numbers, and emails. Live-demo safety: never script a write action against a real client ticket; call out which demos mutate data. If a capability question goes beyond what the Thread docs confirm, say "verify with Thread docs/support" rather than overpromising a feature.
```
