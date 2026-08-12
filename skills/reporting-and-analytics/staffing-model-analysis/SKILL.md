---
name: Staffing Model Analysis
description: Someone asks whether the desk is staffed right — ticket arrival patterns by hour and day versus coverage, and where the desk is under- or over-staffed.
category: Reporting & Analytics
tools: [search_tickets, search_members, list_boards]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Staffing Model Analysis

**When to use:** "Are we staffed correctly for our ticket volume?", "do we need another tech on mornings / should we add weekend coverage?", or an owner testing a staffing change against arrival data before committing.

**Run it:** across all tickets in the period — manually on demand (an arrival-pattern analysis has no ticket event for a Flow to trigger on).

## Prompt

```
A queueing-style read of staffing: when work actually arrives (by hour and weekday) vs
when people are on, and where the mismatches are — under-covered windows where response
suffers, over-covered ones where capacity idles. Staffing recommendations affect
livelihoods — frame everything as analysis for a human staffing decision, especially
anything that could read as "reduce hours".

1. Confirm the period (default: trailing 8-12 weeks for a stable pattern) and gather
   arrivals: created-tickets with timestamps via split searches per board per week
   (disclose caps — an undercounted arrival heatmap corrupts every downstream
   conclusion). Exclude junk/NOC noise unless someone must actually touch those alerts.

2. Build the ARRIVAL HEATMAP: average tickets per hour-of-day per day-of-week, plus an
   effort weighting (priority mix and rough handle-time from thread/time-entry
   evidence) since ten password resets != ten server-down calls.

3. Establish COVERAGE: who is on when — from stated shift schedules if provided;
   otherwise infer working windows from activity timestamps and MARK the inference
   explicitly. Inferred coverage must be labeled inferred and confirmed before anyone
   acts on it.

4. Compare arrivals-weighted-by-effort against coverage per window. Flag:
   - Under-staffed — arrival load consistently outpaces the people on. Corroborate
     every under-staffing claim with an outcome signal (slower first response, morning
     backlog inheritance) — arrival volume alone is not the case.
   - Over-staffed — coverage with persistently little arriving work.

5. Recommend 2-3 staffing moves ranked by impact (shift a start time, add partial
   weekend coverage, move a body from an over-covered window) — each framed "if the
   pattern holds," with the response-time evidence that corroborates it. This is a
   heuristic queueing read, not an Erlang model — say so, and never output a precise
   "you need exactly N techs". Role-aware: escalation engineers and PMs are not
   interchangeable coverage units with L1 intake; analyze the intake-capable pool.

6. Close with a methodology note: period, weighting assumptions, whether coverage was
   stated or inferred, caps.
```
