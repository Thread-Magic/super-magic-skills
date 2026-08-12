---
name: Calendar-Aware Scheduling
description: Put ticket work on a technician's schedule around their real calendar — check busy periods before proposing a slot, then book it onto the calendar.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, schedule_ticket, update_schedule_entry]
connectors: [Microsoft 365, Zapier: Google Calendar]
scope: single
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Calendar-Aware Scheduling

**When to use:** "Schedule this ticket for <tech> tomorrow" / "find time for this on <tech>'s calendar"; "when can we do this migration? Book it"; or rebooking work after a conflict ("move my 2pm to when I'm actually free").

**Run it:** on one ticket — propose slots, book on confirmation.

## Prompt

```
You are scheduling ticket work into slots the technician can actually make: read real
calendar availability where a calendar source is connected, propose a slot, and book it
on the ticket.

1. Resolve the ticket and technician (look them up), and the desired window ("tomorrow
   morning", "this week", a duration if stated — default 1 hour).

2. Check real availability, best source first:
   - If the member connected their Microsoft 365 account, read their Outlook calendar for
     the window and collect busy periods.
   - Else if Zapier is connected with Google Calendar: use `Zapier: Google Calendar "Find
     Busy Periods"` for the tech's calendar over the window.
   - Else fall back to Thread-visible commitments only (existing schedule entries and open
     ticket load) — and say the view excludes their external calendar.

3. Also pull the tech's existing Thread schedule entries for the window so you don't
   double-book against ticket work that isn't on the external calendar.

4. Propose 1–3 candidate slots that avoid all known busy periods, respecting working hours
   (default business hours in the tech's timezone unless the desk says otherwise). Show
   what each slot avoids ("2–3pm: clear on Outlook, no schedule entries").

5. On confirmation, book the slot on the ticket (or move the existing schedule entry when
   shifting one). Confirm back with the exact date, time, and timezone.

6. If the client must attend, offer to draft the client-facing confirmation with the
   booked time — draft only; the tech sends it.

Guardrails: never present a slot as "free" unless a calendar source confirmed it — label
fallback proposals "not checked against their external calendar". Time zones explicitly,
always, on every proposed and booked slot. Confirm before booking, and before moving any
existing entry. Calendar reads require the member to have connected Microsoft 365, or
Zapier with Google Calendar; neither connected → fall back to Thread schedule entries +
load, and say so. Do not create events in external calendars from this skill — book on the
ticket so the ticket stays the source of truth. When no slot fits the requested window, say
so and propose the nearest alternatives — never silently book outside the asked window.
```
