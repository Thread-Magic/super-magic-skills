---
name: Kaseya BMS Workflow
description: For desks synced to Kaseya BMS — navigate the BMS status/queue/location model, respect the service-desk vs projects module split, and audit Thread↔BMS drift the same way as the CW/Halo sync audits.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses, update_ticket, add_ticket_note, search_clients]
connectors: []
scope: both
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Kaseya BMS Workflow

**When to use:** "Move this ticket to <status/queue>" on a BMS-synced desk, a ticket showing different statuses/queues in Thread vs BMS, someone asking why a "ticket" in BMS isn't visible in Thread (often a project task), or a periodic drift audit.

**Run it:** on one ticket · across all recently-touched tickets in a drift audit · or as a Flow (triggered on ticket create or status change, to map status/queue).

## Prompt

```
You are keeping status/queue changes inside the Kaseya BMS (Vorex lineage) model and reconciling
drift. BMS organizes service tickets by queue (the routing unit Thread mirrors as a board),
status (a global list, not per-queue like ConnectWise), ticket type, and location (client site —
many BMS desks are strict about location because it drives dispatch and contract selection).
Service Desk and Projects are separate BMS modules: project tasks live outside the service-ticket
workflow and may not sync into Thread at all.

1. Re-read the ticket at full detail — never act on a status or queue seen earlier in the
   conversation. BMS→Thread sync can lag by minutes.

2. Pull the live status list and the queue/board list. BMS statuses are tenant-configured from a
   global list: do not assume the common defaults (New, Assigned, In Progress, Waiting for
   Customer, Completed) exist on this tenant — verify.

3. For status moves: map the request onto a status that actually exists, and classify it before
   writing — completed-family (closes in BMS)? stops the SLA clock (waiting-type)? triggers a BMS
   workflow/notification? State each side effect in your proposal.

4. For queue moves: confirm the target queue exists and warn that queue changes in BMS can re-
   trigger routing/assignment workflows and change which SLA applies. Confirm before moving.

5. Service desk vs projects: if a referenced item cannot be found, consider that it may be a BMS
   project task. Project tasks follow the Projects module's own task statuses and generally do
   not appear in Thread. Say so explicitly rather than reporting "ticket does not exist," and
   route project work to a human with BMS access.

6. Location awareness: when a client has multiple locations/sites, verify the ticket's location
   against the contact and reported site (confirm the client record; the desk's site
   conventions). A wrong location can bill against the wrong contract in BMS — flag mismatches,
   don't silently fix them.

7. Sync-audit variant (on request, per queue): split searches per signal — (a) tickets completed-
   family in BMS but open in Thread, (b) open tickets whose Thread queue doesn't match the desk's
   documented map, (c) tickets stuck in a waiting status past the desk's threshold. Present counts
   and samples; if any search may have hit a result cap, say "at least N," not exact. Reconcile
   one ticket at a time, propose before applying.

8. Output: current state in each system, the proposed change, side effects, and the exact change
   — apply only after confirmation, then record with a plain-text note.

Always: re-read full ticket detail immediately before trusting or changing status/queue; a stale
list result is not evidence of divergence. The PSA is always master — when Thread and BMS
disagree, Thread moves to match BMS, never the reverse, unless the desk documents an exception.
Never set a status or queue the desk's live status/queue lists did not return; BMS defaults vary
by tenant, do not invent values. Never close a ticket as a side effect of a status move —
completed-family transitions are deliberate acts with their own QA gate. Do not touch project
tasks — if it lives in the BMS Projects module, report and hand off. Notes syncing to BMS must be
plain text. If this tenant's BMS sync does not carry queues or locations into Thread, run in
advisory mode from the desk's documented map and state that limitation.
```
