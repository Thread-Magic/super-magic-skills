---
name: CW Type / Subtype / Item Classification
description: For desks synced to ConnectWise Manage — classify tickets with CW's three-level Type → Subtype → Item taxonomy using only values that exist in the board's configuration, never invented ones.
category: PSA-Specific
tools: [search_tickets, list_boards, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# CW Type / Subtype / Item Classification

**When to use:** Classifying a new ticket on a CW-synced board ("set the type/subtype", "categorize this"), a closure QA gate requiring Type/Subtype/Item, or auditing recently closed tickets for missing or defaulted classification.

**Run it:** on one ticket · across all recently closed tickets on a board · or as a Flow (triggered when a ticket is created).

## Prompt

```
You are applying ConnectWise Manage's three-level, board-scoped taxonomy: Type → Subtype →
Item. Only combinations configured on the board are valid; an invalid combo either fails the
sync or silently drops.

1. Re-read the ticket and its full thread — classify from the body of the request, never the
   title alone.

2. Establish the valid value set. Thread does not expose CW's setup tables directly, so derive
   it from evidence, in order of preference: the desk's documented taxonomy sheet; values
   observed on recently closed tickets on the same board; or ask the reviewer. Never guess a
   value you have not seen.

3. Pick Type first, then Subtype, then Item — each level narrows the previous one. Do not pick
   an Item you have not seen paired with that Subtype: CW combos are configured pairwise, and
   unpaired combos are invalid even when each value exists individually.

4. If the ticket genuinely spans two types, classify by the primary actionable issue and note
   the secondary one; consider splitting the ticket instead of a mushy classification.

5. If no observed combination fits, say so explicitly and leave classification to a human. A
   wrong classification poisons CW reporting and agreement routing; an empty one is at least
   visible.

6. Propose Type/Subtype/Item with a one-line justification; apply only after confirmation.

Always: never invent values — only use Type/Subtype/Item values evidenced from the board's own
tickets or the desk's documented list; CW rejects or mangles unknown values on sync. Re-read
full ticket detail before writing — the ticket may have been classified, moved, or closed in CW
since you last saw it. Taxonomy is board-scoped: values valid on one CW board are not valid on
another; re-derive when the ticket moves boards. Do not default to a catch-all value ("General
/ Other / Other") to get past a gate — flag the gap instead. If classification drives agreement
or billing routing on this desk, say so in the proposal and get explicit confirmation.
```
