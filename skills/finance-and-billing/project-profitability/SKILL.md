---
name: Project Profitability
description: Someone wants to know whether a fixed-fee project is on budget — logged hours versus budgeted hours, burn alerts at 70% and 90%, and documented evidence of scope creep.
category: Finance & Billing
tools: [search_tickets, search_clients, search_members]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Project Profitability

**When to use:** "How's the <client> migration project tracking against budget?" / a recurring burn check on active fixed-fee projects ("anything past 70%?") / a PM suspects scope creep and needs evidence before the change-order conversation.

**Run it:** across all active fixed-fee projects, or on a single project you name — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Track a fixed-fee project's hour burn against its budget: how much of the budgeted effort is
consumed, whether the burn rate will outrun the remaining work, and what specific requests
pushed it past the original scope. (Ongoing all-you-can-eat agreements use Agreement
Profitability; this is the project-shaped version, with a finish line and a fixed number.)

1. Confirm the client, the project (a project board, ticket type, or parent ticket — ask how
   this desk marks project work), and the budget: budgeted hours, or fixed fee plus target
   rate to derive them. NEVER guess a budget — if none is provided and none is recorded on the
   tickets, report burned hours only and say a budget is required for the rest.

2. Read the project's tickets and their time entries. Record caps — a capped time-entry pull
   silently understates burn, which is the dangerous direction; if capped, split by
   phase/tech/date until uncapped or report burn as a floor ("at least N hours").

3. Burn status — logged vs budgeted hours, percent consumed, and burn-vs-progress: percent of
   budget used against percent of scope delivered (from milestone/phase tickets or the PM's
   estimate — labeled whichever it is). 60% burned at 80% delivered is fine; the reverse is
   the fire.

4. Alert thresholds — flag at 70% (warn: check remaining scope vs remaining hours) and 90%
   (act: change order or scope-cut conversation now, before the budget is gone). If burn
   already exceeds 100%, compute the current effective rate the same way Agreement
   Profitability does.

5. Scope-creep evidence — scan the project tickets for work outside the original scope:
   requests added after kickoff, "while you're here" items, rework. Build a short evidence
   list (date, requester, what was added, hours it consumed) suitable for a change-order
   conversation — factual and neutral, since the client may eventually see its substance.

6. Output: burn summary (budget / logged / % / threshold status), burn-vs-progress read, top
   hour-consuming tickets, the scope-creep evidence list with its total hours, a
   recommendation (on track / change order / scope conversation / internal write-down
   decision), and a methodology note — how project tickets were identified, budget source,
   searches run, caps hit.

Guardrails: the budget number must come from the requester or the record — never fabricated,
never "typical for this kind of project". Scope-creep evidence must cite real tickets and
requests; do not invent examples, and characterize intent neutrally (clients rarely "sneak"
scope — they ask, and someone says yes). Delivered-percent is an estimate unless milestones
make it measurable — label it. Never present capped time totals as complete; burn
understatement is the costly failure mode here. This skill reports; it does not create change
orders, adjust budgets, or bill anything. Financial framing is leadership/PM-facing — do not
attribute overruns to named techs as a performance claim; hours concentration is context, and
never volume alone.
```
