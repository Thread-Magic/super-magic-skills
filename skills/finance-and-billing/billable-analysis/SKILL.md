---
name: Billable Analysis
description: When someone asks how billable hours break down by technician, client, or period, or wants to see unbilled-work exposure from time entries.
category: Finance & Billing
tools: [search_tickets, search_members, search_clients]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Billable Analysis

**When to use:** "How many billable hours did <tech> log last month?" / "show billable vs unbillable by client this quarter" / "how much billable time is sitting uninvoiced?" / "which techs have the lowest billable ratio this period?"

**Run it:** across all techs or clients for a period, or sliced to the set you point me at — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Analyze logged time entries to show billable vs unbillable hours by technician, client, or
period, and quantify unbilled-work exposure — hours logged as billable that have not yet been
invoiced.

1. Confirm scope with the requester: period, and whether to slice by technician, client, or
   both. If no period given, default to the last full calendar month and say so.

2. Read the tickets with time entries for the period. Run one search per technician (look up
   the techs) or per client (look up the clients) rather than one giant query, so result caps
   hit per-slice, not globally.

3. From each ticket's time entries, sum hours by billable flag. Time entries are the source
   of truth — do not infer billability from ticket type, board, or agreement name.

4. Compute per-slice: total hours, billable hours, unbillable hours, billable ratio. For
   unbilled exposure, list billable entries on tickets not yet marked invoiced/closed-billed
   (or, if invoicing status isn't visible in Thread, report billable hours and state that
   invoiced-vs-not must be confirmed in the accounting system).

5. Output a plain table: slice | total hrs | billable | unbillable | ratio | unbilled
   exposure, followed by 2-3 observations (largest exposure, biggest ratio change if a prior
   period was compared). Flag which numbers are exact and which hit a search cap.

Guardrails: time-entry evidence is the source of truth for billability — never reclassify an
entry's billable flag in your math; report it as logged. If a search may have hit a result
cap, say "at least N hours" — never present a capped total as exact. Do not state that
unbilled hours "will be invoiced" or represent revenue owed; whether they are billable
depends on the agreement, which lives outside Thread — label exposure as "logged-billable,
invoicing status unconfirmed." Read-only: this skill changes nothing. Do not name-and-shame:
when slicing by technician for a lead, present numbers neutrally and note that low billable
ratios can reflect assignment mix, not effort.
```
