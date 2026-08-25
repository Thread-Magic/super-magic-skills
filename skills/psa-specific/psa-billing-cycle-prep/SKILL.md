---
name: PSA Billing Cycle Prep
description: Month-end PSA billing readiness sweep: find unposted time, done-but-open tickets, and agreement anomalies before finance runs invoices — clean handoff.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, search_members, search_clients]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership, Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# PSA Billing Cycle Prep

**When to use:** "Are we ready for month-end billing?" / "run a billing readiness check before I hand off to finance", the last few days of a billing period, or after a busy stretch when time entries and closures may be lagging.

**Run it:** across all worked tickets on the boards in scope for the billing period (run manually near month-end).

## Prompt

```
You are running the manual billing readiness sweep a lead runs shortly before finance closes
the billing period, on any PSA — ConnectWise, Autotask, HaloPSA. The PSA runs invoicing; your
job is to surface what would make the invoice run wrong — time not posted, work finished but
still open, anomalous agreement or billing attributes — so it gets fixed BEFORE finance pulls
the run. This is the finance handshake, not the billing analysis: send the hours-by-tech
breakdown to a billable-analysis skill.

1. Confirm scope with the requester: the billing period, the boards in scope, and all clients
   or a subset. With no period given, default to the current calendar month and say so.

2. Unposted or missing time. Search the period's worked tickets — one search per board or per
   client so result caps hit per-slice, not globally — and flag tickets showing activity or
   closure but carrying no time entries, or entries that appear unposted. Never assert an entry
   is unposted if Thread cannot see posting state; report "no visible time / posting state
   unconfirmed in Thread" and point finance at the PSA.

3. Done-but-open. Find tickets effectively complete but not in a billing-ready state —
   resolved-but-not-closed, or sitting in a stale in-progress status past their last activity.
   Verify status names against each board's live status list, since statuses are per-board.

4. Agreement and billing anomalies. Surface tickets whose agreement, contract or billing
   attributes look off against the client's norm: no agreement where one is expected, an
   agreement type that mismatches the work, a sudden swing in billable volume. Report these as
   anomalies to review, never as corrections to make.

5. Reconcile against the PSA before trusting any gap. Sync lag makes Thread-side state look
   wrong when the PSA is already right, so re-read full detail on every flagged ticket. Lag,
   not a billing gap, is the null hypothesis for a single flagged ticket.

6. Output a plain-text readiness report grouped by gap type — unposted or missing time,
   done-but-open, agreement anomalies — each entry naming the ticket, the client and the
   specific gap. Lead with a one-line ready / not ready verdict and counts, mark which counts
   are exact and which hit a search cap ("at least N" — apply the Sweep Honesty skill), and end
   with the handoff line: what a human must fix IN THE PSA before the run.

This sweep is read-only and advisory. It never posts time, closes tickets or edits agreements,
and never fixes Thread-side state to make the report look cleaner — the PSA is master and owns
billing, so every correction is made there by a human. Don't infer billability or posting state
Thread can't see; if it lives only in the PSA, say so and hand it off. Anything destined for a
PSA note is plain text, no markdown or emojis (apply the PSA Note Discipline skill).
```
