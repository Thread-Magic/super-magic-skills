---
name: Priority Downgrade Guard
description: On a priority change, if AI triage lowered a priority that a human or the client had explicitly set higher, restore the higher priority — deterministic, restore-only, never an upgrade of its own.
category: Triage & Routing
tools: [search_tickets, update_ticket, list_ticket_priorities, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Priority Downgrade Guard

**When to use:** Auto-triage sometimes downgrades tickets a client or tech marked urgent — "don't let the AI lower a priority a human set", or protecting VIP/critical flags from being overwritten by automated categorization.

**Run it:** on one ticket · or as a Flow (when a ticket's priority changes).

## Prompt

```
Watch priority changes and, when an automated downgrade overrode a human's explicit higher
setting, put the higher priority back. This skill only ever restores; it never raises a priority
on its own judgment.

1. Read the ticket: the current priority, the prior priority, and the history of what changed
   it — specifically whether the drop was made by automated triage/auto-prioritization vs. a
   person.

2. Confirm two things from evidence: (a) the higher priority was set by a human or the client
   explicitly (a person's action or a clear client statement of urgency in the thread), and (b)
   the downgrade was made by automation, not a human deliberately lowering it.

3. If both hold, restore the human-set higher priority (confirm the priority value exists among
   the available levels).

4. Leave a plain-text note: what the human-set priority was, that automation downgraded it, and
   that it was restored.

5. In every other case, do nothing.

Restore-only, deterministic: never set a priority higher than the human previously set, and never
raise priority on your own assessment — the only move is putting back a human-set level that
automation lowered. If a human lowered the priority, leave it — people are allowed to downgrade.
If it's unclear whether the higher priority was human-set or whether automation did the
downgrade, do nothing. The priority restore + one note are the only writes. Notes plain text (PSA
compatibility).

Running as a Flow: fires on the priority-change event. Your entire reply is the note, verbatim:
"PRIORITY RESTORED to <level> (human-set; downgraded by automation)." or "NO ACTION."
Deterministic stops: higher priority not clearly human/client-set → no action; downgrade made by
a human → no action; ambiguous provenance → no action. Restore at most once per downgrade event;
never escalate beyond the prior human-set level.
```
