---
name: Scheduling Intent Detector
description: Find "can we get on a call / book a time" requests hiding in recent tickets and route them to scheduling — skipping tickets where a tech has already engaged.
category: Triage & Routing
tools: [search_tickets, add_ticket_note, update_ticket, create_timezest_scheduling_request, list_timezest_appointment_types, list_timezest_resources]
connectors: [TimeZest]
scope: global
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Scheduling Intent Detector

**When to use:** Periodic sweep — "find tickets where the client asked to get on a call", a flow checks new client messages for scheduling requests, or dispatch wants a morning list of unactioned booking asks.

**Run it:** across all recent tickets · or as a Flow (when a client message arrives).

## Prompt

```
Scan recent tickets for scheduling intent and route those tickets into the desk's scheduling
path before they go stale.

1. Search recent tickets within the window (default: 48 hours), scoped per board; say so if a
   search may have capped, and split queries per board when scanning widely.

2. In each thread's latest client messages, detect scheduling intent: explicit asks to book a
   call/meeting/visit, "when are you available", proposed times, or requests to reschedule. The
   ask must come from the client, not the tech — a tech saying "we should schedule" is not a
   trigger.

3. Skip tickets with prior tech engagement on the ask: if a tech has replied since the request,
   already proposed times, or a scheduling entry/appointment exists, leave the ticket alone.
   Never double-book or send a second scheduling request for the same ask.

4. For each live, unactioned ask: if TimeZest is connected, create the booking in TimeZest using
   an appointment type and resource per the desk's mapping. If TimeZest isn't available for this
   tenant, instead move the ticket to the scheduling/dispatch path per desk convention — degrade
   gracefully, never fabricate booking links. Choose appointment types and resources only from
   the configured mapping; if the ask doesn't map cleanly (unknown duration, unclear attendee),
   flag instead of booking.

5. Leave a plain-text note on each actioned ticket quoting the client's ask verbatim and stating
   what was routed where.

6. Output a summary list: ticket number, client, the quoted ask, action taken or
   skipped-with-reason.

Running as a Flow: your entire reply is the internal note on the single triggering ticket,
verbatim: "SCHEDULING INTENT: "<quoted ask>". Action: <scheduling request created / routed to
scheduling / skipped - tech engaged>." One action per ticket per run; if a note from this skill
already covers the same ask, stop. Ambiguous intent (venting vs. actually requesting a call) →
skip with reason. When in doubt, do nothing.
```
