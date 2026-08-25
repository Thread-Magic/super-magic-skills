<!--
Canonical Skill template. Copy this into skills/<category>/<slug>/SKILL.md and fill it in.
Every skill in this library follows this exact shape. See CONTRIBUTING.md for the rules and
the fixed lists of roles, outcomes, and connectors you may use. Delete this comment block in
your copy.
-->
---
name: Short Title Case Name
description: When to reach for this skill, in one line — this is the trigger the agent matches.
category: One of the existing folders in skills/
tools: [search_tickets, add_ticket_note]   # metadata for validation — do NOT name these in the prompt
connectors: []            # e.g. [NinjaOne]; [Zapier: Microsoft Teams]; [] if native-only
scope: both               # single | global | both — one ticket, across all tickets, or either
flow: yes                 # yes | no — can a Flow trigger this automatically on matching tickets?
role: [Technician]        # 1-2 values from the list in CONTRIBUTING.md — who reaches for this skill
outcome: [Faster Resolution & Response]   # 1-2 values from the list in CONTRIBUTING.md — what it's worth
---

# Short Title Case Name

**When to use:** One or two concrete situations, in the words a tech would actually use.

**Run it:** on one ticket · across all <relevant> tickets · or as a Flow (triggered on <event/condition>).
<!-- Keep only the modes that apply, matching the scope/flow frontmatter. -->

## Prompt

<!-- HARD LIMIT: this block must be under 3,000 characters (aim for ~2,900). Super Magic
     will not save a longer skill. Run `python3 tools/validate.py` to check. Too long?
     Cut hedging first, then compose with a base skill (CONTRIBUTING.md -> Base skills),
     then split. Never buy space by deleting a guardrail. -->

```
The runnable prompt — paste this whole block into Super Magic. Write it in plain, natural
English the way you'd actually talk to the agent: "read the ticket", "change the status to X",
"add an internal note", "draft a reply". Super Magic is native-English — do NOT name internal
tools (never write update_ticket / add_ticket_note; write "change the status" / "leave a note").

One prompt can take several actions in sequence (classify, then set priority, then note).
If the skill can run across many tickets, write it so it works on "this ticket, or each ticket
in the set I point you at". Bake every guardrail inline (confidence gates, show-me-before-send,
when-in-doubt-do-nothing, result-cap honesty, never invent data). If it can run as a Flow, add
a short line for the unattended path.

Don't restate a shared contract longhand — name the base skill and keep a short gloss so
a cold paste still works: "Notes are plain text, no markdown or emojis (apply the PSA Note
Discipline skill)."
```
