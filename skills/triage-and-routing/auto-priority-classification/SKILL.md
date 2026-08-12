---
name: Auto Priority Classification
description: Set a ticket's priority from its title and description against the partner's own priority definitions — built for alert boards and intake flows.
category: Triage & Routing
tools: [search_tickets, list_ticket_priorities, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Auto Priority Classification

**When to use:** "What priority should this be?" against the desk's own P1/P2/P3 definitions — an alert board that needs every incoming ticket stamped automatically, or a flow firing on create that needs one deterministic priority write.

**Run it:** on one ticket · across all tickets on a board · or as a Flow (when a ticket is created).

## Prompt

```
Read a ticket, match it against the desk's written priority definitions, and set exactly
one priority — or leave it untouched when the definitions don't clearly apply.

1. Read the ticket's title and description. If the description is empty, read the earliest
   message.

2. Look up the available priority levels and map them to the desk's priority definitions
   (as configured in this skill's install or provided in the prompt). Choose only from the
   priorities that actually exist on this desk — never invent a level.

3. Match the ticket against each definition in severity order, highest first. Use the
   described impact and scope (how many users, business-critical system, security
   implication), not tone or keywords alone.

4. Forcing rules override the match: confirmed security issues and multi-user/site-wide
   outages classify at the highest applicable priority. Never downgrade an existing
   priority that a human set higher than your match.

5. If exactly one definition fits, set that priority and leave a one-line plain-text note
   naming the definition that matched.

6. If none fits cleanly or two fit equally, do not change the priority; note that
   classification was inconclusive. Vague or empty tickets → no change, one note. Don't
   guess.

Priority is the only field this skill writes — no board, status, owner, or type changes.
Notes are plain text for PSA compatibility.

Running as a Flow: your entire reply is posted verbatim as the internal note — no
narration, no questions. Format: "PRIORITY: <name>. Matched definition: <one line>." or
"PRIORITY: unchanged. Reason: <one line>." Exactly one priority change per run, or none;
when in doubt, do nothing. If the ticket already has a priority note from this skill in
the current thread, stop without writing.
```
