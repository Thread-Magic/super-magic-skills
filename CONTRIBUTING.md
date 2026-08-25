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
2. **Write the prompt in plain language, under 3,000 characters.** One workflow, guardrails
   baked in (see below). Super Magic is native-English — say "change the status", "add an
   internal note", "draft a reply", not tool names. Test it by pasting it into Super Magic
   against a real tenant.
3. **Fill in the frontmatter.** Set `name`, `description` (the *trigger* — when to use this),
   `category`, `tools`, `connectors`, `scope`, `flow`, `role`, and `outcome`. Use real Super
   Magic tools and supported connectors — a maintainer validates these in review — and pick
   `role`/`outcome` from the fixed lists below.
4. **Open a PR.** Run `python3 tools/validate.py` first — it checks the length limit, the
   frontmatter, and the fixed lists, and CI runs it on every PR. A maintainer then checks the
   trigger wording, the tools/connectors, the guardrails, and that nothing private slipped in.
   Merges to `main` sync to the docs site automatically.

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
  Hudu · TimeZest · Notion · Linear · Zapier (written `"Zapier: <App>"`, or bare `Zapier` for
  an app-agnostic skill) · ConnectWise RMM · ImmyBot · Microsoft 365 · Runbooks. Make the
  prompt **degrade gracefully** when a connector is absent.

## Write prompts in natural language

Super Magic is native-English — say "change the status", "add an internal note", "draft a
reply", not the tool names (`update_ticket`, `add_ticket_note`). Tools live in frontmatter as
metadata; they are never named in the prompt. **One prompt may take several actions** (classify
→ set priority → note). Guardrails live **inside** the prompt: confidence gates before writes,
"show me before you send/close", "when in doubt, do nothing", result-cap honesty, "never invent
data".

## The 3,000-character limit

**A prompt block may not exceed 3,000 characters.** Super Magic caps skill instructions and
Flow agent prompts at 3,000; a longer skill still runs if it was saved before the cap, but it
**cannot be saved again** until it is shortened. A skill over the limit here is a skill nobody
can actually install, so `tools/validate.py` fails the PR.

Only the **prompt block** counts — the fenced block under `## Prompt`, which is what a person
pastes into the skill editor. Frontmatter and the "When to use" / "Run it" lines never leave
the repo and are not measured.

**Aim for ~2,900** so a partner has room to adapt it to their desk without immediately hitting
the ceiling.

Three ways to fit, in order of preference:

1. **Cut hedging and restated rationale.** Most over-limit prompts explain *why* a step matters
   three times. Say it once, in the imperative.
2. **Compose with a base skill** (below) instead of restating a shared guardrail longhand.
3. **Split it.** If it needs "and" twice to describe, it was always two skills.

Never buy space by deleting a guardrail that has no base-skill equivalent — a confirmation
gate before a destructive write, a data-loss consent step, an escalation trigger. If a skill
cannot fit without losing one of those, split it instead.

## Base skills

A **base skill** carries one shared contract that many skills need — how a PSA-bound note is
written, what an unattended Flow may output, how to behave when a connector is off. Instead of
restating it, name it:

> Notes are plain text — no markdown or emojis (apply the **PSA Note Discipline** skill).

Roughly eight words replace sixty.

**Where the name actually resolves — this decides how much the gloss has to carry.** In Super
Magic, a member working conversationally, the agent can reach your other saved skills, so
naming one pulls in its full contract. A **Super Magic Agent** is different: a Flow fires a
*prompt*, and that prompt is all the agent gets. There is no skill lookup in a Flow, so a
named base skill there is just words on the page.

That makes the gloss the whole contract for anything a Flow runs. **Always keep it** — a bare
"apply the PSA Note Discipline skill" does nothing in a Flow and nothing for a person pasting
the prompt for the first time. Write the reference so the sentence still stands on its own
with the name deleted:

> ✅ `Notes are plain text — no markdown or emojis (apply the PSA Note Discipline skill).`
> ❌ `Apply the PSA Note Discipline skill.`

If a skill is `flow: yes` and a guardrail is genuinely load-bearing for the unattended path,
spell it out inline rather than delegating it to a name.

The base skills available today:

| Base skill | Carries |
|---|---|
| `automation-and-flows/psa-note-discipline` | Plain-text notes: no markdown, no emojis, raw URLs, internal vs client |
| `automation-and-flows/write-guardrails` | Confidence gate · show-me-before-send · when-in-doubt-do-nothing · never invent |
| `automation-and-flows/connector-degradation` | What to do when an integration isn't on |
| `automation-and-flows/sweep-honesty` | Result caps, partial coverage, "note what you couldn't check" |
| `automation-and-flows/unattended-output-discipline` | The output contract for anything a Flow runs |
| `automation-and-flows/json-api-response-pattern` | Machine-readable output |
| `automation-and-flows/intent-builder` | Designing a Messenger intent: triggers, variations, replies, and the show-the-spec-never-activate contract |
| `troubleshooting-playbooks/troubleshooting-ladder` | Context → history → verbatim error → branch → verify & note |
| `liongard-inspectors/inspector-read-discipline` | Finding the inspector, dating the dataprint, verifying field angles |
| `industry-packs/industry-pack-frame` | Layering a vertical on the LOB Application Framework |

Write a cross-reference as `<category>/<slug>` when you want it verified — `validate.py`
checks those resolve. A bare slug in prose is fine and common, but can't be checked (it's
indistinguishable from ordinary hyphenated English).

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
