---
name: License Cost Optimization
description: When someone wants to find unused, duplicate, or oversized licenses for a client and get downgrade/reclaim recommendations with a savings estimate.
category: Finance & Billing
tools: [search_tickets, search_clients, web_search, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# License Cost Optimization

**When to use:** "Are we wasting money on licenses at <client>?" / "find unused M365 licenses before <client>'s renewal" / "the client asked us to cut their software spend — where's the fat?"

**Run it:** across all clients up for renewal, or on a single client you name — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Scan a client's license position for waste — unassigned licenses, licenses on inactive users,
duplicate coverage, oversized SKUs — and produce reclaim/downgrade recommendations with an
estimated monthly saving.

1. Get the license export from the requester (users, assigned SKUs, last-activity/sign-in
   date if available) and, if they have it, per-SKU unit cost. Look up the client.

2. Corroborate inactivity with tickets: read the client's offboarding/termination tickets in
   the last 6-12 months — a licensed user with an offboarding ticket is the strongest reclaim
   candidate. Note any result caps.

3. Classify each finding:
   - Reclaim: license assigned to an offboarded or long-inactive user, or purchased-but-
     unassigned seats.
   - Downgrade: user on a premium SKU whose observed usage fits a cheaper tier (only when the
     export includes usage signals; otherwise list as "review candidate").
   - Duplicate: overlapping products covering the same capability (e.g. two endpoint-security
     or two backup products on the same users), from the export only.

4. Price the savings: use unit costs the requester supplied; if absent, search the web for
   current public list prices and label every such figure "public list price — verify against
   your vendor/CSP pricing". Savings estimate = sum of monthly deltas, presented as a range
   when tiering is uncertain.

5. Output: findings table (user/SKU | finding | evidence | est. monthly saving), total
   estimated saving, and a recommended action list ordered by saving and risk (reclaims first,
   downgrades second, duplicates last — those need an architecture decision).

6. Offer to post the recommendation list as a plain-text internal note on the relevant ticket.
   Do not remove, downgrade, or change any license.

Guardrails: recommendations only — never present a recommendation as a completed action, and
never touch a license; removal happens through the client's change process, and mailbox/data
retention must be handled before any license removal. Cite evidence per finding (an export
row, a sign-in date, or an offboarding ticket); "looks unused" without a signal is a review
candidate, not a saving. Savings from public list prices are estimates — label them; MSP/CSP
pricing differs. Watch for licenses that look idle but are load-bearing (shared mailboxes,
service accounts, break-glass admins) — those go to "review", never "reclaim". If the desk
resells these licenses, reclaiming cuts the client's bill and the MSP's revenue — note that
trade-off for the account owner rather than optimizing silently in one direction.
```
