---
name: Project Profitability
description: Check whether a fixed-fee project is on budget — logged hours versus budgeted hours, burn alerts at 70% and 90%, and documented evidence of scope creep.
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
Track a fixed-fee project's hour burn against budget: how much of the budgeted effort is
consumed, whether the burn rate will outrun the remaining work, and which requests pushed it past
the original scope. Ongoing agreements use Agreement Profitability; this is the project-shaped
version, with a finish line and a fixed number.

1. Confirm the client, the project — a project board, ticket type or parent ticket; ask how this
   desk marks project work — and the budget: budgeted hours, or fixed fee plus target rate to
   derive them. NEVER guess a budget: if none is supplied and none is recorded on the tickets,
   report burned hours only and say a budget is required for the rest.

2. Read the project's tickets and time entries. Sweep Honesty base skill: a capped time-entry
   pull silently understates burn, the dangerous direction, so split by phase, tech or date until
   uncapped, or report burn as a floor — "at least N hours".

3. Burn status: logged versus budgeted hours, percent consumed, burn against progress — percent
   of budget used against percent of scope delivered, from milestone or phase tickets or the PM's
   estimate, labelled as whichever it is. 60% burned at 80% delivered is fine; the reverse is the
   fire.

4. Alert thresholds: flag at 70% — warn, check remaining scope against remaining hours — and at
   90%, where the change-order or scope-cut conversation happens now, before the budget is gone.
   Past 100%, compute the current effective rate the way Agreement Profitability does.

5. Scope-creep evidence: scan the project tickets for work outside the original scope — requests
   added after kickoff, "while you're here" items, rework. Build a short list (date, requester,
   what was added, hours consumed) fit for a change-order conversation: factual and neutral,
   since the client may eventually see its substance.

6. Output the burn summary (budget, logged, percent, threshold status), the burn-versus-progress
   read, the top hour-consuming tickets, the scope-creep evidence with its total hours, a
   recommendation — on track, change order, scope conversation, or internal write-down — and a
   methodology note: how project tickets were identified, the budget source, searches run, caps
   hit.

The budget comes from the requester or the record, never fabricated, never "typical for this kind
of project". Scope-creep evidence cites real tickets and requests: don't invent examples, and
characterise intent neutrally — clients rarely "sneak" scope, they ask and someone says yes.
Delivered-percent is an estimate unless milestones make it measurable, so label it. Never present
capped time totals as complete. This skill reports: it doesn't create change orders, adjust
budgets or bill anything. The framing is leadership and PM-facing — never attribute overruns to
named techs as a performance claim; hours concentration is context, never volume alone.
```
