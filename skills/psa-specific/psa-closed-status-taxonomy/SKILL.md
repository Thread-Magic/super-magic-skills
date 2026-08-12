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
(ConnectWise Manage, Autotask, HaloPSA). Every PSA has more "done" statuses than the one literally
named Closed — Completed, Resolved, Cancelled, Merged/Duplicate, ">Closed"-prefixed CW statuses,
post-resolution confirmation states — and some read as "open" to naive filters. Every report,
sweep, or follow-up cadence built on an open-ticket search inherits that error: stale counts,
follow-ups fired at finished tickets, SLA panic over resolved work.

1. Pull the full status vocabulary per board (and the board list); statuses are board-scoped on
   ConnectWise and per-type on HaloPSA, so build the list per board, not globally.

2. Classify every status into: open-family (work pending), closed-family (no work will happen:
   closed, completed, cancelled, merged/duplicate), and terminal-adjacent (resolved-pending-
   confirmation, client-review windows — finished for workload purposes, reopenable for cadence
   purposes). Name conventions vary per PSA and per tenant: CW desks often prefix closed-workflow
   statuses (e.g. ">Closed"); Halo desks commonly run Resolved → Closed two-stage; Autotask desks
   use Complete plus cancellation/duplicate variants.

3. Verify by evidence, not name: for any ambiguous status, sample tickets in it — do they have
   recent activity and open expectations, or are they finished? A status named "Review" can be
   either. Mark unverifiable statuses explicitly and classify them conservatively (treat as open
   for follow-up purposes, closed for workload counts — the direction that fails safe for each use).

4. Publish the exclusion list into the desk's field-mapping doc (find the existing doc in the
   knowledge base — one living copy). Format: per board, the closed-family list, the terminal-
   adjacent list, and the evidence level per row.

5. Apply it: when running any open-ticket query, filter with the exclusion list and state in the
   output which statuses were excluded. Terminal-adjacent statuses get called out separately, not
   lumped either way silently.

6. Maintain: on rerun, diff the live status lists against the doc; new statuses default to
   unclassified — treat conservatively until evidenced, and flag them for the desk to classify.

Always: before acting on any individual ticket a filtered sweep surfaced (follow-up, closure,
reassignment), re-read its full detail — its status may have moved into the closed family since
the sweep ran. Never classify a status by name alone; evidence or desk confirmation first — a
wrong closed-family call silently drops live tickets from every report. Result-cap honesty:
filtered sweeps that hit caps report floors, not totals. The exclusion list is per board and per
tenant — never copy one desk's list to another, even on the same PSA. This skill classifies and
filters; it never changes ticket statuses. When a status stays unclassifiable, say so in every
report that touches it rather than hiding the ambiguity.
```
