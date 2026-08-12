# Skill formatting agent

**This is a prompt.** Give it (and the submission) to an AI agent to turn a rough skill idea — a
GitHub issue, a pasted prompt, or a draft — into a `SKILL.md` that matches this library exactly and
renders cleanly on the Thread docs site ([docs.getthread.com/skill-library](https://docs.getthread.com/skill-library/overview)).
A human maintainer can follow it just as well. It restates, as rules, the structure/categorization/
tagging the docs site enforces. Ground-truth references: [`research/tool-catalog.md`](research/tool-catalog.md)
(what tools/connectors exist), [`research/taxonomy.md`](research/taxonomy.md) (roles/outcomes), and
[`research/AUTHORING.md`](research/AUTHORING.md) (the deep authoring spec). If those disagree with
this file, **they win** — they're the source of truth; this file is the operating summary.

---

## Your job

Take the submission and produce exactly one `skills/<category-slug>/<skill-slug>/SKILL.md` that:
1. is one focused workflow, written as a runnable natural-English prompt with guardrails inline;
2. carries valid frontmatter with the right category, tools, connectors, role(s), and outcome(s);
3. contains no private data and no unsupported capabilities;
4. would survive the "what gets a skill removed" bar below.

If the submission is too thin, too broad ("and" twice = two skills), or needs a tool/capability that
doesn't exist, **say so and stop** — don't invent a skill that can't run. Ask for the missing detail
rather than guessing at client-specific specifics (board names, statuses, tone).

---

## Output shape (copy this exactly)

```markdown
---
name: Short Title Case Name
description: When to reach for this skill, in one line — this is the trigger the agent matches.
category: Human Readable Category
tools: [search_tickets, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Short Title Case Name

**When to use:** One or two concrete situations, in the words a tech would actually use.

**Run it:** on one ticket · across all <relevant> tickets · or as a Flow (triggered on <event>).

## Prompt

​```
The runnable prompt — natural English, paste-to-run, every guardrail inline.
​```
```

- **File path is the identity.** `<category-slug>` must be one of the slugs in the table below;
  `<skill-slug>` is kebab-case. The on-disk category directory (not the `category:` string) is what
  routes the skill on the site.
- **Body order is fixed:** `# Title` → `**When to use:**` → `**Run it:**` → `## Prompt` fenced block.
  Keep only the "Run it" modes that match `scope`/`flow`.

---

## Frontmatter rules (these are parsed mechanically — get them exactly right)

| Field | Rule |
| --- | --- |
| `name` | Short Title Case. Shows in the Skills picker and as the page title. |
| `description` | **The trigger**, one line — *when to use this*, not a feature summary. The agent matches against it. |
| `category` | The human-readable title (e.g. `Triage & Routing`). Must correspond to the directory slug you place the file under. |
| `tools` | **Inline flow list** `[a, b]`. Every value must exist in `research/tool-catalog.md`. **Metadata only — never name a tool in the prompt.** |
| `connectors` | Inline flow list. `[]` = native (buckets under **Thread**). Quote compound values: `"Zapier: Microsoft Teams"`. |
| `scope` | `single` \| `global` \| `both` — one ticket, a sweep across many, or either. |
| `flow` | `yes` \| `no` — can a ticket-**event** Flow trigger it automatically? |
| `role` | 1–2 values, **only** from the Roles list. |
| `outcome` | 1–2 values, **only** from the Outcomes list. |

**Parsing gotchas that silently break the site:**
- List fields **must be one-line inline flow lists** (`role: [Technician, Dispatcher]`). Multi-line
  YAML block lists (`- Technician` on the next line) **do not parse** — the field comes through empty.
- A `role`/`outcome` value that isn't in the fixed lists is **silently dropped** — the skill just
  won't appear under that filter. Spell them exactly, including `&` and spacing.
- A connector value with a colon (Zapier apps) **must be quoted**, or it breaks the list.

---

## Controlled vocabularies

### Category directory slugs → titles (place the file under the slug)

| slug | Title | | slug | Title |
| --- | --- | --- | --- | --- |
| `triage-and-routing` | Triage & Routing | | `liongard-inspectors` | Liongard Inspectors |
| `qa-and-closure` | QA & Closure | | `compliance-and-audit` | Compliance & Audit |
| `scheduling-and-dispatch` | Scheduling & Dispatch | | `troubleshooting-playbooks` | Troubleshooting Playbooks |
| `communication` | Communication | | `alert-runbooks` | Alert Runbooks |
| `documentation` | Documentation | | `end-user-guides` | End-User Guides |
| `escalation` | Escalation | | `role-rituals` | Role Rituals |
| `onboarding-and-access` | Onboarding & Access | | `localized` | Localized |
| `devices-and-infrastructure` | Devices & Infrastructure | | `m365-administration` | Microsoft 365 Administration |
| `security` | Security | | `psa-specific` | PSA-Specific Workflows |
| `vendor-runbooks` | Vendor Runbooks | | `change-and-problem-management` | Change & Problem Management |
| `voice-and-messenger` | Voice & Messenger | | `msp-business-operations` | MSP Business Operations |
| `industry-packs` | Industry Packs | | `reporting-and-analytics` | Reporting & Analytics |
| `account-management` | Account Management | | `client-lifecycle` | Client Lifecycle |
| `finance-and-billing` | Finance & Billing | | `sales-and-quoting` | Sales & Quoting |
| `automation-and-flows` | Automation & Flows | | `connectors` | Connectors |
| `training-and-enablement` | Training & Enablement | | `personal-productivity` | Personal Productivity |

Pick the category by the skill's **primary mechanism**. A new slug is allowed only if none fit — it
renders, but with a generic icon and sorts last, so prefer an existing one.

### Roles (`role:` — pick 1–2)
`Technician` · `Dispatcher` · `Service & Ops Manager` · `CSM / Account Manager` · `Security & Compliance Owner` · `Sales & Business Development` · `MSP Owner / Leadership`

### Outcomes (`outcome:` — pick 1–2)
`Faster Resolution & Response` · `Fewer Escalations & Less Noise` · `Time & Cost Savings (Capacity)` · `Always-On Coverage` · `Risk & Compliance` · `Retention & Growth (CSAT/Expansion)`

> Tag role/outcome from the skill's **actual mechanism**, not its category. Tag both values when both
> genuinely apply; don't pad to two.

### Connectors (`connectors:`)
List any integration the prompt needs turned on. `[]` = native (works on any tenant → shows as a
"Thread" tag on the site). The recognized set the site groups by: **IT Glue, Hudu, Liongard, NinjaOne,
Zapier, ConnectWise RMM, Notion, TimeZest, Linear, ImmyBot, Microsoft 365, Runbooks**. Zapier entries
are written `"Zapier: <App>"` (e.g. `"Zapier: Slack"`) and all group under Zapier. Only list a
connector whose tools are in `research/tool-catalog.md`, and make the prompt **degrade gracefully**
when it's absent.

---

## Writing the prompt (the body)

- **Natural English only.** Say "read the ticket", "change the status to X", "add an internal note",
  "draft a reply for me to review". **Never** name a tool (`update_ticket`, `add_ticket_note`) —
  tools live in frontmatter for validation and are stripped from the page.
- **One prompt, several actions** is fine (classify → set priority → note → status). One *workflow*,
  though — if you need "and" twice to describe it, split it.
- **Guardrails are the product — bake them inline:** a confidence gate before any write; "show me
  before you send/close" for anything client-facing or destructive; "when in doubt, do nothing";
  result-cap honesty (don't present a capped search as complete); never invent links, ticket numbers,
  or data; never turn a recommendation into a completed action without confirmation.
- **PSA-bound notes are plain text** — no markdown or emoji in anything that syncs to a PSA.
- **Scope/Flow honesty.** Write it to work on one ticket by default and "each ticket in the set I
  point you at" when global. Flows are **event-triggered only** (created / updated / replied /
  status-changed, filtered on board, status, priority, type/subtype/item, category, company, contact,
  team, owner, member, source, agreement, SLA, severity, sentiment, touchpoint, day/time) — there is
  **no schedule/duration** trigger. A cadence/digest/sweep is `flow: no` (manual/global)
---

## Hard limits — never build on these (see `research/tool-catalog.md` "NOT supported")
- **SMS / texting** — no send path. May only appear as an audited weak-MFA factor, never a send.
- **Telephony control** — dialing/routing/porting. Voice AI is a product surface, not an agent tool.
- **RMM script execution / software deploy / policy push** — remediation is a deep-link handoff only.
- **Any tool not in `research/tool-catalog.md`** — it doesn't exist; don't use it.

## What gets a skill removed (hold the submission to this)
- **Can't run** — needs a missing tool or an unsupported capability.
- **Not value-added** — thin, generic, or something a tech wouldn't actually reach for.
- **Duplicates a stronger sibling** — improve the existing one and cross-reference; don't ship a near-copy.

## Sanitize
No client or partner names, no people, no hostnames, no credentials, no ticket IDs, no
environment-specific board/status names. Use placeholders: `<client>`, `<user>`, `<device>`, "the VIP
board", "the desk's closed status".

---

## Before you're done
1. File is at `skills/<known-slug>/<kebab-slug>/SKILL.md`, body in the fixed order.
2. Frontmatter parses: inline lists, quoted Zapier values, role/outcome spelled exactly.
3. Every `tools:` entry is in the catalog; none appear in the prompt.
4. Guardrails inline; nothing private; no unsupported capability.
5. If you added or renamed a skill, the README catalog is regenerated with `python3 tools/gen_catalog.py`.
