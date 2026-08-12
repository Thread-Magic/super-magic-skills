---
name: View Builder
description: Create or duplicate an inbox view from a plain-English spec — "a view of my open P1s", "duplicate the dispatch view but filtered to <client>". Use when a member asks for a new view, a saved filter, or a variant of an existing view.
category: Automation & Flows
tools: [view_list, view_save, view_duplicate, view_getCurrent, view_listFilterAttributes, view_searchFilterValues]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, Dispatcher]
outcome: [Time & Cost Savings (Capacity)]
---

# View Builder

**When to use:** "Make me a view of unassigned tickets on the alerts board older than a day" / "duplicate the VIP view but only show tickets waiting on us" / "I want a saved filter for my open P1s and P2s."

**Run it:** as a build task on request — you're saving an inbox view, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Turn a plain-English description of "the tickets I want to see" into a saved inbox view,
mapping every filter to the tenant's real attribute values. The views family is in-app
SuperAgent only — DEGRADATION: when view-building isn't available (external MCP), do not
pretend to save anything; output the complete filter recipe (attribute, operator, exact
value, sort) as a numbered list the member can click through in the Views UI in under a
minute, and say that is what you are doing.

1. Parse the spec into filter conditions, sort, and a short view name.

2. List the existing views first. If one is close, propose duplicating it + adjusting the
   filters instead of building from scratch; if the member says "like my current view
   but…", start from their current view. Never overwrite or modify a shared/team view
   without explicit confirmation — prefer a personal copy.

3. Map every condition through the real filter attributes and their exact values —
   exact value strings only, never guessed. If a requested filter has no matching
   attribute, say so and offer the nearest real attribute; do not silently approximate.

4. Show the recipe before saving: view name, each filter with its exact value, sort order.
   Confirm. Name views descriptively and neutrally — no client nicknames or internal slang
   that won't translate across the team.

5. Save the view. Report the saved view's name and restate what it shows, including what it
   deliberately excludes.
```
