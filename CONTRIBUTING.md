# Contributing

Thanks for adding to the library. The bar here is **value that works** — a small set of
strong, runnable skills beats a long tail of near-copies or prompts that can't actually
execute. Every skill is a copy-paste prompt an MSP service desk runs in Super Magic.

**Two ways to contribute:**

- **No code — just an idea.** Open a [**Suggest a skill idea**](../../issues/new?template=skill-idea.yml)
  issue and describe the workflow in plain English. A maintainer (or the formatting agent in
  [`SKILL-FORMATTING-AGENT.md`](SKILL-FORMATTING-AGENT.md)) turns it into a `SKILL.md`. Great for
  "I wish Super Magic could…" when you don't want to write the prompt yourself.
- **Write or fix one yourself** — fork, add/edit a `SKILL.md`, open a PR. That's the 4 steps below.

## Add or update a skill in 4 steps

1. **Copy the template.** Start from [`TEMPLATE.md`](TEMPLATE.md) into
   `skills/<category>/<slug>/SKILL.md` (kebab-case slug, one of the categories in the
   [README](README.md)).
2. **Check the tools.** Every tool your prompt uses must be in
   [`research/tool-catalog.md`](research/tool-catalog.md). If it needs an integration, list
   it under `connectors:` and make the prompt degrade gracefully when it's absent. If a tool
   isn't in the catalog, it doesn't exist — don't use it.
2a. **Tag role and outcome.** Set `role:` and `outcome:` from the fixed enums in
   [`research/taxonomy.md`](research/taxonomy.md) — these power the docs site's browse
   filters, so don't invent new values. Tag from the skill's actual mechanism, not just its
   category; tag two values when genuinely both apply.
3. **Write the prompt.** One workflow, guardrails baked in (see below). Test it by pasting
   it into Super Magic against a real tenant.
4. **Open a PR.** Run `python3 tools/gen_catalog.py` first to refresh the catalog. A
   maintainer checks the trigger wording, the tools/connectors, the guardrails, and that
   nothing private slipped in. Merges to `main` auto-sync to the docs site.

## The format (required)

```markdown
---
name: Short Title Case Name
description: When to reach for this skill, in one line — the trigger the agent matches.
category: One of the existing categories
tools: [search_tickets, add_ticket_note]   # metadata only — never named in the prompt
connectors: []          # e.g. [NinjaOne]; [Zapier: Microsoft Teams]; [] if native-only
scope: both             # single | global | both
flow: yes               # yes | no
role: [Technician]      # 1-2 values from research/taxonomy.md
outcome: [Faster Resolution & Response]   # 1-2 values from research/taxonomy.md
---

# Short Title Case Name

**When to use:** One or two concrete situations.

**Run it:** on one ticket · across all <relevant> tickets · or as a Flow (on <event>).

## Prompt

​```
Plain natural-English instructions to the agent, with every guardrail inline. Paste-to-run.
​```
```

**Write prompts in natural language.** Super Magic is native-English — say "change the
status", "add an internal note", "draft a reply", not the tool names (`update_ticket`,
`add_ticket_note`). Tools live in frontmatter as metadata for validation; they are never
named in the prompt. **One prompt may take several actions** (classify → set priority →
note). Guardrails live **inside** the prompt: confidence gates before writes, "show me
before you send/close", "when in doubt, do nothing", result-cap honesty, "never invent data".

**Scope & Flow.** `scope`: `single` (acts on one ticket), `global` (sweeps across many), or
`both`. `flow`: `yes` if a Flow can trigger it automatically. Flows are **event-triggered**
(ticket created / updated / replied / status-changed) and filter on board, status, priority,
type/subtype/item, category, company & company-type, contact & contact-type, team, owner,
member, source, agreement, SLA, severity, sentiment, touchpoint, day-of-week, time-of-day —
but there is **no schedule/duration** trigger. A cadence/sweep skill is `flow: no` (run it
manually or globally); an event-driven single-ticket skill is `flow: yes`. Write the Prompt
so it works on one ticket by default and "each ticket in the set I point you at" when global.

## What gets a skill removed

Be ruthless. A skill is cut, not merged, if it:

- **Can't run** — its core needs a tool not in the catalog, or an unsupported capability
  (SMS, telephony control, RMM script execution). See the catalog's "NOT supported" list.
- **Isn't value-added for an MSP desk** — thin, generic, or something a tech wouldn't
  actually reach for.
- **Duplicates a stronger sibling** — extend the better one and cross-reference; don't ship
  a near-copy.
- **Over-claims Flows** — a cadence/duration/scheduled "unattended" trigger Flows can't do.
  Make it a manual skill or drop it.

## What makes a skill worth merging

- **One workflow.** If describing it needs "and" twice, it's two skills.
- **A real trigger.** `description` is *when to use this*, not a feature summary.
- **Runs in the real world.** Native-only works everywhere; connector-gated works where the
  integration is on (tag it, and degrade cleanly).
- **No private data.** No client/partner names, hostnames, credentials, ticket IDs, or
  environment-specific board/status names. Use placeholders.

The full authoring spec and capability ground truth is in
[`research/AUTHORING.md`](research/AUTHORING.md), and the exact structure/format/tagging rules the
docs site enforces — written so an AI agent can format a submission for you — are in
[`SKILL-FORMATTING-AGENT.md`](SKILL-FORMATTING-AGENT.md).
