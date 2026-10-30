---
name: Triage Learnings
description: The saved store of triage corrections your techs made, which the category, type and priority skills read first and only the closure review edits.
category: Automation & Flows
tools: [load_skill]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Triage Learnings

**When to use:** You run the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`) and want its classifications to improve from your techs' corrections without anyone hand-editing prompts. Save this exactly as written, starting empty. Triage Closure Review (`qa-and-closure/triage-closure-review`) fills it in as tickets close.

**Run it:** read at the start of every triage run · edited only by the closure review Flow. Review it weekly and delete any learned rule that looks wrong; each one is a single line, so rolling one back is a one-line delete.

## Prompt

```
Purpose: this desk's learned triage corrections. "Triage Category", "Triage Ticket Type" and "Triage Priority" read this before deciding. Learned rules override their base rules. Only "Triage Closure Review" edits this skill.

HOW TO USE (triage skills)
- If a LEARNED RULE matches the ticket, follow it and say "learned rule L<n>" in your reason.
- Ignore the WATCHLIST when triaging. It is unproven.

LEARNED RULES
(Format: L<n> | Field | When the ticket is about... | Use... | Not... | Evidence: #id, #id, #id | Added YYYY-MM-DD)
- none yet

WATCHLIST
(Format: W<n> | Field | When the ticket is about... | Tech chose... | Agent chose... | Count <n> | High-conf <n> | Tickets | Last seen YYYY-MM-DD)
- none yet

EDITING RULES (for "Triage Closure Review" only)
- Keep this skill under 2,800 characters.
- One line per rule or watchlist item. Describe the ticket pattern as product + problem, never a single keyword.
- To make room: first drop WATCHLIST items with Count 1 not seen in 30 days, then the oldest watchlist items. Never drop a LEARNED RULE to make room. Merge overlapping rules instead.
- Never edit HOW TO USE or EDITING RULES.
```
