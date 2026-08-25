---
name: PSA Closed Status Taxonomy
description: PSA closed-status taxonomy (ConnectWise, Autotask, HaloPSA): find every closed-family status leaking into open searches and maintain the exclusion list.
category: PSA-Specific
tools: [search_tickets, list_ticket_statuses, list_boards, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# PSA Closed Status Taxonomy

**When to use:** Any skill or report is about to run on "open tickets" for a PSA-synced desk, a sweep keeps flagging finished tickets ("why is this resolved ticket in my stale list?"), or building/refreshing the desk's closed-family status list per board.

**Run it:** across all boards on the desk (run manually when building or refreshing the exclusion list).

## Prompt

```
You are building and applying the per-board closed-family exclusion list for a PSA-synced desk
(ConnectWise, Autotask, HaloPSA). Every PSA has more "done" statuses than the one literally
named Closed — Completed, Resolved, Cancelled, Merged/Duplicate, ">Closed"-prefixed ConnectWise
statuses, post-resolution confirmation states — and some read as open to naive filters. Every
report, sweep and follow-up cadence built on an open-ticket search inherits that error: stale
counts, follow-ups fired at finished tickets, SLA panic over resolved work.

1. Pull the full status vocabulary per board, plus the board list. Statuses are board-scoped on
   ConnectWise and per-type on HaloPSA, so build the list per board, never globally.

2. Classify every status as open-family (work pending), closed-family (no work will happen —
   closed, completed, cancelled, merged or duplicate), or terminal-adjacent
   (resolved-pending-confirmation and client-review windows: finished for workload purposes,
   reopenable for cadence purposes). Naming varies by PSA and tenant: ConnectWise desks often
   prefix closed-workflow statuses (">Closed"), Halo desks commonly run a two-stage Resolved →
   Closed, Autotask desks use Complete plus cancellation and duplicate variants.

3. Verify by evidence, never by name — a status called "Review" can be either. Sample tickets
   in any ambiguous status: do they carry recent activity and open expectations, or are they
   finished? A wrong closed-family call silently drops live tickets out of every report. Mark
   unverifiable statuses explicitly and classify them conservatively: open for follow-up
   purposes, closed for workload counts, the direction that fails safe for each use.

4. Publish the list into the desk's field-mapping doc — find the existing one in the knowledge
   base and keep a single living copy. Format it per board: the closed-family list, the
   terminal-adjacent list, and the evidence level per row.

5. Apply it: filter every open-ticket query with the list and state in the output which
   statuses were excluded. Call terminal-adjacent statuses out separately rather than silently
   lumping them either way.

6. Maintain it: on each rerun, diff the live status lists against the doc. New statuses default
   to unclassified — treat them conservatively and flag them for the desk to classify.

Before acting on any individual ticket a filtered sweep surfaced — follow-up, closure,
reassignment — re-read its full detail; its status may have moved into the closed family since
the sweep ran. Filtered sweeps that hit result caps report floors, not totals (apply the Sweep
Honesty skill). The list is per board and per tenant, so never copy one desk's onto another,
even on the same PSA. This skill classifies and filters; it never changes a ticket's status.
Where a status stays unclassifiable, say so in every report that touches it.
```
