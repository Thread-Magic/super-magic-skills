---
name: Agreement Profitability
description: Compute the effective hourly rate on an all-you-can-eat fixed-fee agreement — agreement revenue divided by logged hours — or scan for loss-making clients.
category: Finance & Billing
tools: [search_tickets, search_clients]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Agreement Profitability

**When to use:** "What's our effective hourly rate on <client>'s AYCE agreement?" / "which managed clients are we losing money on?" / "rank all-you-can-eat clients by effective rate this quarter."

**Run it:** across all fixed-fee-agreement clients, or on a single client you name — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Compute the effective hourly rate each fixed-fee agreement is actually earning (monthly
agreement revenue / hours logged against that client) and flag clients whose effective rate
has fallen below the desk's cost or floor rate.

1. Get the revenue side from the requester: per-client monthly agreement revenue (a pasted
   list or figures for the clients in scope), plus their internal floor/cost rate if they
   want loss flagging. Agreement revenue lives in the PSA/accounting system, not Thread —
   never estimate it.

2. Confirm the period (default: last 3 full months, stated) and look up each client.

3. For each client, read the tickets with time entries for the period — one search per
   client so result caps are per-client. Sum ALL logged hours against the client (billable
   and unbillable both consume delivery capacity on a fixed-fee agreement); exclude tickets
   explicitly worked under a separate project/T&M arrangement if the requester identifies them.

4. Compute: effective rate = agreement revenue for the period / logged hours. Also report
   hours/month trend (rising consumption is the early warning).

5. Output a table: client | agreement revenue | logged hrs | effective rate | trend | flag.
   Flag clients under the floor rate, and clients whose search hit a result cap (their true
   rate is lower than shown — more hours, same revenue).

6. Close with the 2-3 worst clients and concrete next steps the requester could take (rate
   review, scope conversation, noisy-asset cleanup) — as recommendations only.

Guardrails: never state what an agreement covers or costs as fact without the agreement
evidence in hand — revenue figures come from the requester or an export they provide, and the
output must say where each number came from. Time-entry evidence is the source of truth for
hours; if a client's techs under-log time, the effective rate is overstated — say so when
logged hours look implausibly low against ticket volume. Result-cap honesty: a capped hours
total means the effective rate is an upper bound; label it. "Loss-making" is a judgment for
the business owner — present the rate versus their floor, don't declare clients fire-worthy.
Read-only; change nothing and leave no notes. Do not share one client's economics inside
another client's ticket or any client-facing surface.
```
