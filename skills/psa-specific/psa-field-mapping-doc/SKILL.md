---
name: PSA Field Mapping Doc
description: For any PSA-synced desk (ConnectWise, Autotask, HaloPSA) — build and maintain the desk's Thread↔PSA field-mapping cheat sheet (statuses, boards/queues, priorities, classification values) from observed tickets, not assumptions.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, list_ticket_priorities, search_knowledge_base, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# PSA Field Mapping Doc

**When to use:** Another PSA skill hit an unmapped value ("what does 'Pending Review' correspond to in the PSA?"), onboarding a new desk or after PSA config changes (new board, renamed statuses), or a sync audit keeps finding the same divergence and the mapping table is the suspected root cause.

**Run it:** across all boards on the desk (run manually when building or refreshing the mapping doc).

## Prompt

```
You are building and maintaining the desk's Thread↔PSA field-mapping cheat sheet (works for any
PSA — ConnectWise Manage, Autotask, HaloPSA). Nearly every PSA-specific skill needs the same
artifact: a trustworthy map of how Thread's boards, statuses, priorities, and classification
values correspond to the PSA's. Build it empirically — from the tenant's live lists and observed
tickets — and keep it current.

1. Pull the tenant's live vocabulary: the board list, the status list (per board where board-
   scoped), the priority list. These lists are the Thread-side ground truth — a mapping doc
   containing values these lists do not return is fiction.

2. Enrich per-board with observed usage: sample recent tickets per board (disclose caps) and
   record which classification values (CW Type/Subtype/Item, Autotask Issue/Sub-Issue, Halo
   categories) actually appear, and which statuses tickets really flow through vs merely exist.

3. Structure the cheat sheet per section, marking each row's evidence level (live-list / observed
   / desk-stated / unverified):
   - Boards ↔ PSA boards/queues/teams, and what work belongs on each.
   - Statuses per board ↔ PSA statuses, flagged: closed-family? clock-pausing? notification-
     firing?
   - Priorities ↔ PSA priorities and any SLA linkage.
   - Classification values observed, with valid parent-child pairings.
   - Known sync quirks for this tenant (fields that lag, values that don't carry — feed from the
     sync-audit findings).

4. Cross-check with the desk: anything only inferable ("does 'Scheduled' pause your SLA clock?")
   goes in as a question, not an answer. Never promote an inference to fact without confirmation.

5. Publish where the desk keeps standards — search the knowledge base to find an existing doc to
   update rather than fork; keep exactly one living copy. If the desk stores docs in a connected
   tool, route there.

6. Maintain: on each rerun, diff live lists against the doc, flag added/renamed/removed values,
   and mark stale rows rather than silently deleting them.

Always: evidence-labeled rows only — every mapping row carries its evidence level; "unverified"
rows exist to be visible, not trusted. When sampling tickets to observe values, re-read full
detail on anything you cite as an example — a stale sample poisons the doc. No tenant identifiers
beyond what the desk's own doc needs; never paste client names or people into example rows — use
placeholders. Result-cap honesty: observed-value coverage from capped samples is partial; say so
in the doc header. One living document — update in place and date the revision, never generate a
fresh doc per run. This skill documents the mapping; it never changes tickets to match the doc.
```
