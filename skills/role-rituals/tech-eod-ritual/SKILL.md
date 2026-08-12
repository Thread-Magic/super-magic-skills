---
name: Tech End-of-Day Ritual
description: A technician's close-of-day runbook: EOD wrap-up, time-entry compliance self-check, and lining up tomorrow's first move before logging off for the day.
category: Role Rituals
tools: [search_tickets, log_time_entry]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Tech End-of-Day Ritual

**When to use:** "Wrap up my day" / "run my EOD" / "am I good to log off?" — end of shift, especially before a day off or handoff.

**Run it:** across your own tickets and today's time — run it manually (not a Flow; Flows can't schedule an end-of-shift cadence).

## Prompt

```
You are running my end-of-day ritual as a chain of existing skills, in a fixed sequence. Scope everything strictly to MY own tickets and MY time today. Target ~10 minutes. Propose, don't apply: show me before you write anything, and when in doubt, do nothing.

Run these skills IN ORDER:
(1) Run the personal-productivity/eod-wrapup skill: what closed today, what's still open with a client waiting, and anything that must not sit overnight. If something must not sit overnight and after-hours coverage exists, flag it as a candidate for the escalation/shift-handoff skill; if there is NO coverage, say that explicitly rather than burying it in a list.
(2) Time-entry self-check: for every ticket I touched today, verify a time entry exists (same lens as the finance-and-billing/time-entry-revenue-audit skill, scoped to just me, just today). List the gaps. Offer to log the missing time, but only with my confirmation of the durations — never guess or fabricate hours; unconfirmed gaps stay listed as gaps.
(3) Tomorrow's first move: pick the single ticket tomorrow starts with and one line on why (SLA clock, promised callback, easiest unblock). Write it into the wrap-up output so morning-me (or the role-rituals/tech-morning-ritual skill) inherits it.
(4) Output the EOD card: closed / still-hot / handed-off, time-entry gaps and what was logged, and tomorrow's first move.

Time-short version: do step 2 (time gaps — the only thing hard to reconstruct later), the "must not sit overnight" line from step 1, and tomorrow's first move. Mark everything else "skipped: time".

Guardrails, all inline:
- Never fabricate time entries — durations come from me, not from estimates. The only writes are the time entries I have confirmed.
- Skip-with-note beats fake completion: a skipped step is printed as skipped with a reason.
- Disclose result caps: if a search may have truncated, say so rather than presenting a partial list as complete.
- Never invent tickets, ticket numbers, or links — report only what the searches return.
- If a chained skill's connector is unavailable for this tenant, note the degradation and continue with the rest.
- Any time-entry note or ticket note that may sync to the PSA is plain text — no markdown, no emojis.
```
