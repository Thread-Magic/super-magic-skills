---
name: Time Entry Revenue Audit
description: When someone wants to find tickets that were worked with no time logged — revenue leakage by technician or period — and get the gaps fixed the right way.
category: Finance & Billing
tools: [search_tickets, search_members, log_time_entry, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Time Entry Revenue Audit

**When to use:** "Which tickets got worked last week with no time entry?" / "how much time are we failing to capture, by tech?" / "audit <tech>'s closed tickets for missing time."

**Run it:** across a tech, a team, or the whole desk for a period — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Find tickets with clear work activity but zero (or implausibly little) logged time, quantify
the likely revenue leakage by technician and period, and route the gaps back to the techs who
can truthfully fill them.

1. Confirm scope: period (default last full week, stated), and whether one tech, a team, or
   the desk. Look up the techs.

2. Read the worked tickets per tech per period — separate searches per tech (closed/updated in
   period), noting result caps.

3. For each ticket, compare activity to logged time. Leakage signals: replies or internal
   notes from the tech but zero time entries; a resolution note with no entry that day; long
   threads with a single token entry (e.g. 0.1h on a multi-day back-and-forth); status moved
   to resolved with no time at all.

4. Estimate the gap conservatively: count each no-time worked ticket at the desk's minimum
   increment (ask if unknown; default 0.25h and say so). Do NOT estimate from thread length —
   the point is to surface gaps, not to fabricate hours.

5. Output: per-tech table (tickets worked | tickets with no time | estimated uncaptured hours
   | worst examples with ticket refs), then a period total and, if the requester supplies an
   average rate, a leakage dollar range labeled as an estimate.

6. Remediation path: for each gap ticket, offer to leave a plain-text note asking the assigned
   tech to add their actual time. Only log time when the tech (or requester who did the work)
   explicitly confirms the real duration and description for a specific ticket — never
   backfill in bulk from estimates.

Guardrails: time-entry evidence is the source of truth — a ticket with no entry is
"uncaptured", not "unbilled revenue owed"; whether the time was billable depends on the
agreement, which you have not seen. Never log time on someone's behalf from an estimate;
logged time is a legal/billing record — only write an entry the human doing the work
confirmed, attributed correctly. Estimated leakage totals are labeled estimates with the
assumption shown (minimum increment × ticket count); result caps → "at least". Present
per-tech findings as a capture-hygiene issue, not an accusation; some gaps are legitimate
(duplicate tickets, no-work closes, covered-by-another-entry). Auto-generated activity (flows,
agents, system notes) is not tech work — exclude it from "worked with no time" detection.
```
