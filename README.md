# Thread Skills

A community library of ready-to-use skills for **Super Magic** and Super Magic Agents. Each skill is a small, reusable prompt that tells the agent how to run one MSP workflow well: triaging a ticket, drafting a client reply, prepping a QBR, responding to a phishing report.

Read a skill, adapt the specifics to your stack, and paste it into Super Magic. Nothing here contains partner names, client data, or environment-specific detail.

**Browse every skill** — searchable by category, connector, role, and outcome — on the [Thread docs site](https://docs.getthread.com/skill-library/overview). Or explore the [`skills/`](skills) folder directly.

## How a skill works

A skill is a folder with a `SKILL.md`. The frontmatter carries the metadata; the body is a copy-paste **Prompt** you run in Super Magic. Every skill follows one shape — the canonical [`TEMPLATE.md`](TEMPLATE.md):

```
---
name: Ticket Triage
description: When to reach for this skill, in one line — the trigger the agent matches.
category: Triage & Routing
tools: [search_tickets, list_boards, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Ticket Triage

**When to use:** A new or unassigned ticket needs classifying and routing.

## Prompt
​```
...the runnable prompt, with guardrails baked in...
​```
```

- **name** shows in the skills picker.
- **description** is the trigger — write it as *when to use this*.
- **tools** are the tools the prompt uses — metadata only, never named in the prompt.
- **connectors** lists any integration the skill needs (NinjaOne, Liongard, IT Glue, Hudu, TimeZest, Notion, Linear, Zapier, and more). `[]` means native — runs on any tenant.
- The **Prompt** is the whole artifact: paste it into Super Magic and it runs. Guardrails live inside the prompt, not in a separate list.

## Using a skill

Open a `SKILL.md`, copy the **Prompt** block, and paste it into Super Magic (or save it as a skill in Thread). Adjust the specifics that are yours — board names, status names, tone. If it lists a connector, it runs where that integration is on and degrades gracefully otherwise.

## Contribute

This library is **crowdsourced** — built by and for the community. Have a skill your peers would love, or a fix for an existing one? Fork the repo, add or edit a `SKILL.md`, and open a pull request; once it's merged it goes live on the docs site.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the four steps and the format. The bar: a skill solves one real MSP workflow, carries its own guardrails, and contains no client or partner data.
