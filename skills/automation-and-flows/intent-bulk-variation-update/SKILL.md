---
name: Intent Bulk Variation Update
description: Apply a shared argument or reply block across all of an intent's client variations at once, with a per-variation diff preview and explicit confirmation before any write. Answers the "change this everywhere without editing each client by hand" workflow; runs manually on demand.
category: Automation & Flows
tools: [get_intent, set_variation_arguments, set_variation_replies, update_variation]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Intent Bulk Variation Update

**When to use:** "Add this argument to every variation of the <intent>" / "update the reply block across all client variations at once" / "roll this change out to every variation, not just one" — standardizing a shared change while keeping client-specific bits intact.

**Run it:** across all of an intent's variations — manually on demand (Flows can't schedule bulk config edits, so there's no Flow trigger for this one).

## Prompt

```
Apply the same change across every variation of an intent in one pass — but only after
showing exactly what changes where. Member-invoked only; there is no unattended variant
(Flows can't schedule bulk config edits).

1. Load the intent and all its variations. Identify which variations are in
   scope (all of them, or a named subset).

2. Build the change set: the exact argument(s) or reply block to apply, and whether it ADDS
   TO or REPLACES what each variation currently has. Default to additive unless the member
   explicitly says replace.

3. Diff preview, per variation. For each in-scope variation show current -> proposed so
   client-specific content that would be overwritten is visible. Flag (don't silently
   overwrite) any variation whose existing arguments/replies are distinct from the shared
   block, so the member can exclude it.

4. Wait for explicit confirmation on the previewed diff. Let the member exclude specific
   variations before proceeding.

5. On confirm, apply the change variation by variation — updating each variation's
   arguments and replies — tracking each result. Act only on what the intent actually
   contains — no fabrication of variations or content.

6. Report a summary: which variations were updated, which were skipped/excluded, which
   failed. Report partial success honestly. Re-preview before re-running on failures.
```
