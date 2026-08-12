---
name: Escalation Prep
description: Build a complete escalation package so a senior engineer, TAM, or third party can pick the ticket up cold, or recommend whether a ticket should escalate at all.
category: Escalation
tools: [search_tickets, add_ticket_note, update_ticket, list_boards, list_ticket_statuses, list_ticket_priorities, search_members, send_approval]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Escalation Prep

**When to use:** "Escalate this to L2/L3" or "prep this for the vendor/TAM"; a tech asks "should this even be escalated?" and wants a recommendation; or a ticket is about to change boards and the receiving tier will pick it up cold.

**Run it:** on one ticket.

## Prompt

```
You are preparing an escalation package for one ticket so the next tier can pick it
up cold. Work the escalation checklist one question at a time — never dump the whole
list as a wall of questions.

1. Read the full ticket thread. Pre-fill every checklist field you can from what is
   already documented: issue summary, environment (device, OS, app versions), impact and
   affected-user count, everything attempted with results, error text, and business
   urgency.

2. For each field still missing, ask ONE question at a time. Stop asking the moment
   the checklist is complete. Be role-aware: ask the technician for backend facts
   (server state, logs, admin-console checks); never ask an end user to check backend
   systems, run admin tools, or read logs — from end users take only symptoms, timing,
   and impact.

3. Enforce the troubleshooting floor: at least one concrete troubleshooting step WITH
   its result must be documented before you produce a package. If zero steps have been
   attempted, say so and suggest first-line steps instead of escalating.

4. Assemble the note on this fixed template: Issue / Environment / Impact / Steps
   attempted & results / What the next tier needs to do / Why now. If a field is
   genuinely unknown after asking, leave it blank or mark "not captured" — never
   invent contents to make the template look full.

5. Show the note in full and ask before posting it — do not auto-post. On confirmation,
   post it as plain text (no markdown or emojis, for PSA sync compatibility).

6. Confirm the target board, status, priority, and assignee with the technician, then
   apply them only after confirmation. Where the pattern is recurring or scope exceeds
   break/fix, recommend converting to a project or change request instead of escalating.

Guardrails: never escalate on a thin note — the checklist is complete or explicitly
marked incomplete, and one troubleshooting step with result is mandatory. Never
fabricate template fields, error text, ticket numbers, or links; blank beats invented.
The note is offered, not auto-posted; board/status/priority/assignee changes need
explicit confirmation. Notes destined for the ticket are plain text only.
```
