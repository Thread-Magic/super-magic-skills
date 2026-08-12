---
name: Field Visit Scheduler
description: Schedule an onsite visit and make the trip count — sweep for other open onsite-worthy tickets at the same site, group travel sensibly, book the visit, and draft the client confirmation.
category: Scheduling & Dispatch
tools: [search_tickets, search_clients, search_contacts, search_members, schedule_ticket, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Dispatcher]
outcome: [Time & Cost Savings (Capacity)]
---

# Field Visit Scheduler

**When to use:** "This needs an onsite — schedule <tech> to go out to <client>"; "we're going to <site> Thursday, what else should we knock out?"; or planning a field day by grouping visits by location.

**Run it:** on one ticket — book the visit and bundle nearby onsite work on confirmation.

## Prompt

```
Onsite time is expensive. When a ticket needs a field visit, book it and consolidate:
every other open ticket at that site that needs hands-on work rides along on the same trip.

1. Resolve the anchor ticket, the client/site (look up the client and the onsite contact),
   and the field tech. Confirm the site address from the client record — never guess
   between multiple locations; if the client has several sites, ask which one.

2. Consolidation sweep. Search for other open tickets for the same client/site and flag
   the onsite-worthy ones: hardware replacements, physical installs, cabling,
   printer/device work, anything previously deferred as "needs onsite". Present the list
   with ticket numbers and a rough per-ticket time estimate so the dispatcher chooses what
   to bundle.

3. Travel grouping (when scheduling multiple visits): order sites to avoid crossing back
   and forth, and note when another client's pending onsite sits nearby — offer to book it
   the same day. Present grouping as a suggestion with reasoning; the dispatcher decides.

4. Size the visit window from the bundled work (sum of estimates + travel buffer). Check
   the tech's availability for the day (see Calendar-Aware Scheduling; use their calendar
   source if connected).

5. On confirmation, book the visit window on the anchor ticket, and add a plain-text note
   to each bundled ticket ("Scheduled for onsite visit <date> with ticket <anchor>").

6. Draft the client confirmation email for the tech to send: date, arrival window, who is
   coming, what will be worked on (the bundled list in client-friendly terms), and what the
   site should have ready (access, credentials contact, parts). Do not send it yourself
   unless the desk has opted in.

Guardrails: confirm the exact site before booking — multi-location clients are the classic
wasted-trip failure. Bundling is opt-in per ticket: propose the ride-along list, let the
dispatcher pick; never silently expand scope the client wasn't told about. Time estimates
are estimates — label them; don't present a packed zero-slack schedule as feasible. Confirm
before booking and before adding notes to bundled tickets. Client-facing confirmation is a
draft for the tech to send — plain, professional, no internal jargon. Respect client rules
(site access hours, required escorts, named-tech-only sites) over convenience grouping. If
the ticket search may have capped, say the ride-along list might be incomplete.
```
