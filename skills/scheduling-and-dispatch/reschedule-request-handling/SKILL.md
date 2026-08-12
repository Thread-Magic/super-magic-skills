---
name: Reschedule Request Handling
description: A client asks to move an appointment: find the schedule entry or booking, propose new slots that actually work, update it, and confirm to the client.
category: Scheduling & Dispatch
tools: [search_tickets, update_schedule_entry, schedule_ticket, add_ticket_note, get_timezest_scheduling_requests, create_timezest_scheduling_request]
connectors: [TimeZest]
scope: single
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Reschedule Request Handling

**When to use:** A client replies "Thursday doesn't work anymore, can we do next week?"; a tech asks to move a booked visit or session ("shift my 2pm to tomorrow"); or a conflict forces a change and the client needs new options.

**Run it:** on one ticket — propose new slots, move on confirmation.

## Prompt

```
You are handling "can we move our appointment?" end to end: locate the existing
commitment, offer real alternatives, move it once, and make sure both the ticket and the
client reflect the new time.

1. Find the commitment. From the ticket (search for it if needed), locate the existing
   schedule entry; also check for an existing TimeZest request — if it was TimeZest-booked,
   handle it in TimeZest terms rather than editing around it.

2. Confirm you have the right appointment: restate date, time, timezone, tech, and
   purpose. If multiple entries exist on the ticket, ask which one — never move the wrong
   appointment silently.

3. Get new availability for the same tech (calendar source if connected, else Thread
   schedule entries + load — see Calendar-Aware Scheduling) around the client's stated
   preference.

4. Propose 2–3 concrete alternative slots, timezone explicit, in a client-ready draft
   reply. If it was TimeZest-booked, prefer sending the client a fresh TimeZest booking
   link so they pick their own slot — after checking no open request already exists.

5. Once the client (or tech, for internal moves) confirms a slot: move the schedule entry
   (or schedule a new one if the original was cancelled). One move per confirmation — no
   speculative rebooking.

6. Record the change in a plain-text note: old time → new time, who requested it, and the
   reschedule count for this appointment.

7. Draft the confirmation reply with the new date/time/timezone for the tech to send.

Guardrails: never move an appointment before the new time is confirmed by the requesting
party; proposals are proposals. Restate the appointment being moved before touching it —
wrong-entry edits are the failure mode. Timezones explicit on every time you propose, book,
or confirm. TimeZest-booked appointments: work through TimeZest (new request/link) rather
than creating a parallel manual entry that disagrees with the booking system; no TimeZest →
proposing slots and moving the entry are the whole flow. Track repeat rescheduling in the
note trail; if this is the third-or-more client-driven move, surface it to the tech — do
not editorialize to the client. Client-facing messages are drafts for the tech to send;
courteous, no blame, no internal details.
```
