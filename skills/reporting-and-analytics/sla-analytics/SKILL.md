---
name: SLA Analytics
description: Someone asks how the desk is doing against SLA — first-response and resolution performance versus targets, and which tickets breached and why.
category: Reporting & Analytics
tools: [search_tickets, list_boards, list_ticket_priorities, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Faster Resolution & Response]
---

# SLA Analytics

**When to use:** "How did we do against SLA last month?" / "what's our first-response time?", "show me every SLA breach this week and why," or investigating whether a specific board, client, or priority tier is slipping.

**Run it:** across all tickets in the period — manually on demand (Thread Flows are ticket-event triggered with no schedule, so this can't run itself).

## Prompt

```
Report first-response and resolution performance against the desk's targets for a
period, with a breach list that explains causes — so the follow-up is fixing the
driver, not just staring at a percentage.

This runs MANUALLY on demand — Thread Flows are ticket-event triggered with no
schedule/cron, so this is not a scheduled skill.

1. Confirm the period, the boards in scope, and the SLA targets per priority.
   If targets are not configured or stated, ASK for them — do not assume industry
   defaults silently, and never invent targets.

2. Run split searches per priority tier per board (result-cap honesty: many small
   searches, not one big one; disclose caps — never present a capped search as a
   complete breach census).

3. Report per tier: tickets in scope, first-response attainment, resolution
   attainment, and the trend vs the prior period if available. Exclude junk/NOC boards
   and auto-closed statuses; a monitoring auto-close is neither a response nor a
   resolution. Distinguish paused clocks (waiting-on-client, scheduled) from running
   ones; if the data can't distinguish them, say the number is approximate and why.

4. Build the BREACH LIST: for each breached ticket, one line — ticket, client, tier,
   which clock breached, by how much, and the apparent cause read from the thread (no
   owner assigned, waiting-on-client misuse, after-hours arrival, vendor hold, alert
   storm). Do not invent ticket numbers or breach timestamps.

5. Group breach causes and rank them: "60% of breaches trace to unassigned overnight
   intake" is the actionable output. Do not name-and-shame individual techs — attribute
   causes to process patterns and leave person-level follow-up to the manager.

6. Recommend 2-3 fixes matched to the top causes, and close with a methodology note
   (targets used, boards, searches, caps, exclusions). Fixed sections: Attainment /
   Breaches / Causes / Actions / Methodology. If targets are unavailable, output only
   the timing distributions and a line stating targets were not provided.
```
