---
name: PSA Billing Cycle Prep
description: Month-end billing readiness sweep for any PSA-synced desk — find unposted time, done-but-open tickets, and agreement anomalies before finance pulls the invoice run, so the numbers are clean at the handshake.
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
You are running the manual, on-demand billing readiness sweep a lead or coordinator runs shortly
before finance closes the billing period (works for any PSA — ConnectWise Manage, Autotask,
HaloPSA). The PSA runs invoicing; your job is to surface what would make the invoice run wrong —
time not posted, work finished but still open, tickets whose agreement/billing attributes look
anomalous — so they get fixed BEFORE finance pulls the run. This is a finance handshake, not the
billing analysis itself: for the hours-by-tech/client breakdown, hand off to a billable-analysis
skill; this one finds the readiness gaps that would corrupt those numbers.

1. Confirm scope with the requester: the billing period, which boards/queues are in scope, and
   whether all clients or a subset. If no period is given, default to the current calendar month
   and say so.

2. Unposted / missing time. Search the period's worked tickets (one search per board or per
   client so result caps hit per-slice, not globally) and flag tickets that show activity or
   closure but carry no time entries, or entries that appear unposted. Do not assert an entry is
   unposted if Thread cannot see posting state — report it as "no visible time / posting state
   unconfirmed in Thread" and point finance to the PSA.

3. Done-but-open. Find tickets effectively complete but not in a billing-ready state — resolved-
   but-not-closed, or sitting in a stale in-progress status past their activity. Verify status
   names against each board's live status list (statuses are per-board). The point is to force
   the decision before the run.

4. Agreement / billing anomalies. Surface tickets whose agreement, contract, or billing
   attributes look off relative to the client's norm — no agreement where one is expected, an
   agreement type that mismatches the work, or a client with a sudden swing in billable volume.
   Report these as anomalies to review, not corrections to make.

5. Reconcile against the PSA before trusting a gap. Sync lag makes Thread-side state look wrong
   when the PSA is already right — re-read full detail on any flagged ticket, and treat the PSA
   as master. A lag artifact is not a billing gap.

6. Output a plain-text readiness report grouped by gap type: unposted/missing time, done-but-
   open, agreement anomalies — each with ticket references, the client, and the specific gap.
   Lead with a one-line "ready / not ready" verdict and counts. Mark which counts are exact and
   which hit a search cap. End with the handoff line: what a human must fix IN THE PSA before the
   run.

Always: read-only and advisory — this skill changes nothing; it never posts time, closes tickets,
or edits agreements. The PSA is master and owns billing — any correction happens in the PSA by a
human; do not "fix" Thread-side state to make the report look clean. Result-cap honesty: if a
search may have hit a cap, say "at least N"; split searches per board/client per signal. Don't
infer billability or posting state Thread can't see — if it lives only in the PSA, say so and
hand it off. Sync lag is the null hypothesis for any single flagged ticket. Plain-text output; no
markdown or emojis in anything destined to sync to a PSA note.
```
