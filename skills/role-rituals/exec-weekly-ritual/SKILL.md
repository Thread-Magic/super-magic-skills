---
name: Exec Weekly Ritual
description: An owner/exec's weekly 20-minute runbook — exec scorecard, resolve one decision ask, and check what's been escalated to me — run when an exec says "run my weekly", "how's the desk", or on a scheduled Monday flow.
category: Role Rituals
tools: [search_tickets, list_boards]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Exec Weekly Ritual

**When to use:** "Run my exec weekly" / "how's the service desk this week" / "what needs a decision from me" — Monday morning before the leadership meeting.

**Run it:** across the whole desk — run it manually (not a Flow; Flows can't schedule a weekly cadence).

## Prompt

```
You are running my exec weekly ritual as a chain of existing skills, in a fixed sequence. Target 20 minutes — built for someone who will skip anything longer. Propose, don't apply: surface the read and the decision framing, show me before anything is communicated on my behalf, and when in doubt, do nothing.

Run these skills IN ORDER:
(1) Run the reporting-and-analytics/ceo-service-desk-brief skill: the week's numbers against target — revenue-relevant metrics, desk health, one trend arrow per line. Numbers come from the skill's real queries — never let a flat week get smoothed into "on track".
(2) One decision ask resolved: from the scorecard and standing asks (pricing exception, hire req, tooling spend, policy call), pick the ONE decision the team is most blocked on and resolve it now — decide, or name exactly what's missing to decide and who provides it by when. "Noted" is not a resolution. The decision gets communicated to the person waiting on it as part of the ritual (show me the message first), not left in my notes.
(3) Escalations-to-me check: search for tickets/threads escalated to me or waiting on owner input, on the relevant status/board. Anything older than a week gets decided, delegated with authority, or explicitly killed — the exec queue is where escalations go to die unless this step exists.
(4) Output the exec card: scorecard headline (3–5 lines), the decision made and who was told, and the escalation queue disposition (count to zero, or the named survivors with checkpoint dates).

Time-short version: step 2 only — the scorecard can be read async; the one decision is the part that needs me present. Note the skips.

Guardrails, all inline:
- One decision means one, resolved — the value is throughput of decisions, not review of dashboards.
- Skip-with-note beats fake completion.
- Disclose result caps: if a search may have truncated, say so rather than presenting a partial list as complete.
- Never invent tickets, ticket numbers, links, or scorecard figures — report only what the underlying skills and searches return.
- If a chained skill's connector is unavailable for this tenant, note the degradation and continue with the rest.
- Any note that may sync to the PSA is plain text — no markdown, no emojis.
```
