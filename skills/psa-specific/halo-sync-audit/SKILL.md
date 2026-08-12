---
name: Halo Sync Audit
description: Sweep Thread ↔ HaloPSA divergence — especially the known pattern of statuses not carrying over — and reconcile toward Halo as the master system.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Halo Sync Audit

**When to use:** "Thread says open, Halo says resolved" and you want the blast radius, a periodic Thread↔Halo hygiene sweep (or after an integration outage / Halo upgrade), or before trusting Thread-side reports that depend on Halo-synced status.

**Run it:** across all recently-touched tickets on the teams/boards in scope (run manually or on a cadence).

## Prompt

```
You are sweeping a HaloPSA desk for Thread↔Halo divergence, filtering out transient lag, and
reconciling the rest toward the PSA. Halo's action-driven status model means a Halo-side action
can change status, visibility, and assignment in one move — and the status leg is the piece most
often observed not carrying over into Thread.

1. Scope: which teams/boards, what window (default: tickets touched in the last 14 days). Pull
   the live board and status lists.

2. Sweep the tickets, one search per signal per team: (a) the signature pattern — tickets whose
   last activity is a resolution-shaped note but whose Thread status is still open-family; (b)
   tickets on hold-type statuses with no stated wait reason (suggesting a Halo action synced
   partially); (c) owner/team mismatches; (d) tickets stale in Thread but with recent Halo-
   originated notes. Disclose result caps — capped sweeps are samples.

3. For each candidate, re-read the full ticket detail individually before calling it divergent.
   Sync lag is the null hypothesis; only tickets that still disagree on a fresh full-detail read
   count.

4. Classify confirmed divergences: status drift (resolved/closed in Halo, open in Thread — the
   known pattern), assignment drift, team drift. Note age and whether client-visible activity is
   pending.

5. Propose reconciliation with Halo as master: align Thread, each with a plain-text note:
   "reconciled to PSA state on <date>; Thread showed <X>". Never push Thread state back into Halo
   during an audit, and never reconcile a ticket carrying an unanswered client message — flag
   those for a human.

6. Output the report: per-team counts, confirmed divergence list (ticket, field, Thread vs Halo
   value, age), proposed fixes, excluded/uncertain tickets listed separately. Apply only after
   the reviewer confirms; if the same pattern recurs sweep after sweep, recommend the integration
   mapping itself be reviewed (statuses missing from the mapping table are the usual root cause).

Always: sync lag is the null hypothesis — no divergence call without an individual fresh re-read
at full detail. The PSA is always master — Thread moves toward Halo; a believed Halo-side error
is a manual human fix, not a reconciliation target. Never bulk-apply; the confirmed list is a
proposal until a human approves it. Result-cap honesty in every count you report. Plain-text
notes only. When in doubt on any ticket, exclude and report separately — a wrong reconciliation
is worse than a listed uncertainty.
```
