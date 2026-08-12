---
name: Tech Utilization Report
description: Leadership wants billable utilization per technician — logged billable hours against capacity — with role-aware targets and explicit framing that utilization measures workload economics, not a person's worth. Leadership-only.
category: Finance & Billing
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Tech Utilization Report

**When to use:** "What's our utilization by tech? / who has capacity?" / pricing, hiring, or capacity planning ("can we absorb this new client?") / a quarterly economics review of the bench.

**Run it:** across the whole roster (or a team you name) for a period — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Compute billable utilization per technician for a period — billable hours logged over
available capacity — against role-appropriate targets. This is a leadership economics
instrument for pricing, hiring, and workload decisions. (Billable Analysis slices the billable
hours themselves; this skill divides them by capacity and compares to targets.)

1. Confirm the period (default: last full month), the roster (look up the members), each
   person's capacity baseline (default 40h/week minus known PTO — ask; do not guess PTO), and
   the role-aware targets. If leadership has no targets, propose the conventional bands and
   label them conventions, not benchmarks: dedicated reactive tech 70-80%, escalation/senior
   50-65%, lead with management duties 30-50%, dispatcher/coordinator near 0% by design.

2. Read the time entries per tech for the period, split billable vs non-billable as this desk
   marks them. Record caps — capped pulls understate utilization; split by week or client
   until uncapped, or report floors.

3. Compute per tech: billable hours, total logged hours, capacity, billable utilization, and
   logging coverage (total logged / capacity). LOW utilization with LOW logging coverage is a
   time-entry compliance question, not a utilization finding — route those rows to time-entry
   compliance before anyone reads them as idle time.

4. Compare each tech to their ROLE's target band, never to the desk average. Flag over-target
   as sustainability risk (a tech at 95% has no slack for escalations, training, or a bad week
   — that is a burnout and quality flag, not a gold star).

5. Aggregate view: blended utilization, trend vs prior period if available, and the capacity
   headroom answer in hours ("roughly N billable hours/month of absorbable capacity,
   concentrated in <roles>").

6. Output: per-tech table (role / capacity / billable / utilization / role target / coverage
   flag), the sustainability and compliance flags, the aggregate read, and a methodology note
   — capacity assumptions, billable definition used, targets source, searches run, caps hit.

Guardrails: LEADERSHIP-ONLY — this report prices people's time; it must not circulate as a team
leaderboard. Say so in the output header. Utilization ≠ worth, stated in the report itself:
mentoring, documentation, automation-building, and presales are low-billable and high-value; a
utilization number captures none of it. Never rank techs by utilization alone, never volume
alone. Role-aware targets are mandatory — comparing a dispatcher or escalation engineer to a
reactive-bench target is a category error this report must refuse to make. Low numbers get the
compliance check before the idle interpretation, every time. Never present capped time totals
as complete; disclose caps and direction of bias. PTO and part-time capacity come from the
requester — never assumed silently.
```
