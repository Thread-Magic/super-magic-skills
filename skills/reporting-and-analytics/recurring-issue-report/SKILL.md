---
name: Recurring Issue Report
description: Someone asks which issues keep coming back — chronic problems hitting the same client or device repeatedly — and whether each has a root-cause fix underway.
category: Reporting & Analytics
tools: [search_tickets, search_clients, list_boards]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Recurring Issue Report

**When to use:** "What issues keep coming back?" / "show me our chronic problems," "has <client>'s server issue actually been root-caused or are we just closing tickets?", or a monthly problem-management sweep feeding the RCA backlog.

**Run it:** across all tickets in the period — manually on demand (Thread Flows are ticket-event triggered with no schedule, so this can't run itself).

## Prompt

```
Find the chronic issues — the same problem recurring on the same client, device, or
user — and report each with its recurrence count, cost, and root-cause-analysis status,
so repeat symptoms get fixes instead of another band-aid ticket.

This runs MANUALLY on demand — Thread Flows are ticket-event triggered with no
schedule/cron, so this is not a scheduled skill.

1. Confirm the period (default: trailing 30 days, with a 90-day lookback to catch slow
   repeaters) and pull resolved + open tickets with split searches per board per client
   segment; disclose caps (capped searches make counts "at least N").

2. Detect recurrence: 2 OR MORE tickets in 30 days for the same client tied to the same
   device/asset or the same evident root cause. Match on asset names, error signatures,
   and issue descriptions in thread text — categories alone under-match. The 2-in-30
   threshold is the trigger for INVESTIGATION, not proof.

3. Verify each candidate cluster by reading the threads: same underlying problem, not
   coincidentally similar symptoms. Drop weak matches rather than padding the list.

4. For each confirmed chronic issue report: client, asset/user affected, recurrence
   count and dates, cumulative time spent (logged time where present, conservative
   estimate labeled as such otherwise), and RCA STATUS:
   - Fixed — a root-cause fix shipped; recent recurrence predates it.
   - RCA in progress — a problem/project ticket exists and is active.
   - Band-aid loop — each occurrence closed symptomatically, no RCA anywhere.
   Never mark RCA status without evidence in the tickets (a linked problem ticket, a
   fix note); absence of evidence = band-aid loop, and say the classification basis.
   Exclude junk/NOC noise recurrences (a flapping monitor is an alert-tuning finding,
   not a chronic issue). AGGREGATE by issue; cite one representative ticket per issue,
   not the full recurrence list.

5. Rank by cost x recurrence, lead with the band-aid loops, and recommend the next step
   per issue (open a problem ticket, schedule the replacement, escalate to vendor,
   client conversation) — recommendations only; do not open problem tickets or merge
   recurrences without explicit confirmation.

6. Methodology note: period, matching criteria, searches, caps.
```
