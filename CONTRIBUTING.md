# Contributing

Thanks for adding to the library. The bar here is **value that works** — a small set of
strong, runnable skills beats a long tail of near-copies or prompts that can't actually
execute. Every skill is a copy-paste prompt an MSP service desk runs in Super Magic.

Contributions come in through the repo: fork it, add or edit a `SKILL.md`, and open a pull
request — the four steps below.

## Add or update a skill in 4 steps

1. **Copy the template.** Start from [`TEMPLATE.md`](TEMPLATE.md) into
   `skills/<category>/<slug>/SKILL.md` — a kebab-case slug under one of the existing category
   folders in [`skills/`](skills).
2. **Write the prompt in plain language.** One workflow, guardrails baked in (see below).
   Super Magic is native-English — say "change the status", "add an internal note", "draft a
   reply", not tool names. Test it by pasting it into Super Magic against a real tenant.
3. **Fill in the frontmatter.** Set `name`, `description` (the *trigger* — when to use this),
   `category`, `tools`, `connectors`, `scope`, `flow`, `role`, and `outcome`. Use real Super
   Magic tools and supported connectors — a maintainer validates these in review — and pick
   `role`/`outcome` from the fixed lists below.
4. **Open a PR.** A maintainer checks the trigger wording, the tools/connectors, the
   guardrails, and that nothing private slipped in. Merges to `main` sync to the docs site
   automatically.

## The format (required)

```markdown
---
name: Short Title Case Name
description: When to reach for this skill, in one line — the trigger the agent matches.
category: One of the existing folders in skills/
tools: [search_tickets, add_ticket_note]   # metadata only — never named in the prompt
connectors: []          # e.g. [NinjaOne]; [Zapier: Microsoft Teams]; [] if native-only
scope: both             # single | global | both
flow: yes               # yes | no
role: [Technician]      # 1-2 values from the list below
outcome: [Faster Resolution & Response]   # 1-2 values from the list below
---

# Short Title Case Name

**When to use:** One or two concrete situations.

**Run it:** on one ticket · across all <relevant> tickets · or as a Flow (on <event>).

## Prompt

​```
Plain natural-English instructions to the agent, with every guardrail inline. Paste-to-run.
​```
```

## Roles, outcomes & connectors

Tag `role` and `outcome` from these fixed lists — they power the docs site's browse filters,
so don't invent new values. Use 1–2 of each, chosen from the skill's actual mechanism (not
just its category); tag two when both genuinely apply.

- **Roles:** Technician · Dispatcher · Service & Ops Manager · CSM / Account Manager ·
  Security & Compliance Owner · Sales & Business Development · MSP Owner / Leadership
- **Outcomes:** Faster Resolution & Response · Fewer Escalations & Less Noise ·
  Time & Cost Savings (Capacity) · Always-On Coverage · Risk & Compliance ·
  Retention & Growth (CSAT/Expansion) · Staff Enablement
  <br>*Staff Enablement is for skills whose value is making your **own people** better or faster
  at the job — training, coaching, ramp. Not client or end-user onboarding: provisioning a
  customer's new starter belongs in `onboarding-and-access`.*
- **Connectors** (list any the prompt needs; `[]` if native): NinjaOne · Liongard · IT Glue ·
  Hudu · TimeZest · Notion · Linear · Zapier (written `"Zapier: <App>"`) · ConnectWise RMM ·
  ImmyBot · Microsoft 365. Make the prompt **degrade gracefully** when a connector is absent.

## Write prompts in natural language

Super Magic is native-English — say "change the status", "add an internal note", "draft a
reply", not the tool names (`update_ticket`, `add_ticket_note`). Tools live in frontmatter as
metadata; they are never named in the prompt. **One prompt may take several actions** (classify
→ set priority → note). Guardrails live **inside** the prompt: confidence gates before writes,
"show me before you send/close", "when in doubt, do nothing", result-cap honesty, "never invent
data".

## Scope & Flow

`scope`: `single` (acts on one ticket), `global` (sweeps across many), or `both`. `flow`: `yes`
if a Flow can trigger it automatically. Flows are **event-triggered** (ticket created / updated
/ replied / status-changed) and filter on board, status, priority, type/subtype/item, category,
company & company-type, contact & contact-type, team, owner, member, source, agreement, SLA,
severity, sentiment, touchpoint, day-of-week, time-of-day — but there is **no schedule/duration**
trigger. A cadence/sweep skill is `flow: no` (run it manually or globally); an event-driven
single-ticket skill is `flow: yes`. Write the Prompt so it works on one ticket by default and
"each ticket in the set I point you at" when global.

## What gets a skill removed

Be ruthless. A skill is cut, not merged, if it:

- **Can't run** — its core needs a tool that doesn't exist, or an unsupported capability (SMS,
  telephony control, RMM script execution/software deploy/policy push).
- **Isn't value-added for an MSP desk** — thin, generic, or something a tech wouldn't actually
  reach for.
- **Duplicates a stronger sibling** — extend the better one and cross-reference; don't ship a
  near-copy.
- **Over-claims Flows** — a cadence/duration/scheduled "unattended" trigger Flows can't do.
  Make it a manual skill or drop it.

## What makes a skill worth merging

- **One workflow.** If describing it needs "and" twice, it's two skills.
- **A real trigger.** `description` is *when to use this*, not a feature summary.
- **Runs in the real world.** Native-only works everywhere; connector-gated works where the
  integration is on (tag it, and degrade cleanly).
- **No private data.** No client/partner names, hostnames, credentials, ticket IDs, or
  environment-specific board/status names. Use placeholders.
