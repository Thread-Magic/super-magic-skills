---
name: TimeZest Booking
description: Create a TimeZest scheduling request from a ticket — pick the right appointment type and resource, and drop the self-service booking link into the client reply.
category: Scheduling & Dispatch
tools: [search_tickets, get_timezest_scheduling_requests, list_timezest_appointment_types, list_timezest_resources, create_timezest_scheduling_request, add_ticket_note]
connectors: [TimeZest]
scope: single
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# TimeZest Booking

**When to use:** A client asks for a call, screen share, or remote session and the desk uses TimeZest; a tech says "send them my booking link" or "set up a TimeZest for this ticket"; or a scheduling-intent detector routed a "get on a call" thread here.

**Run it:** on one ticket — create the booking request and drop the link in the reply draft.

## Prompt

```
You are turning "can we get on a call?" into a TimeZest scheduling request: the client
picks their own slot from the tech's real availability, and the ticket gets the link and
a record of what was sent.

1. Identify the ticket (from context or by searching) and confirm who needs to meet:
   which technician (or team resource) and which client contact.

2. Check for existing requests first: look up the ticket's TimeZest requests. If an open
   request already exists, report it — do not create a duplicate; offer the existing link
   instead.

3. Pick the appointment type that matches the ask (remote support session vs. phone call
   vs. onsite). If none clearly fits, list the options and ask rather than guessing.

4. Pick the resource: the assigned technician by default, or the team/round-robin resource
   if the desk schedules that way. If the intended tech is not a TimeZest resource, say so
   and list who is.

5. Send the client a TimeZest booking link for the ticket with the chosen appointment type
   and resource.

6. Add a plain-text internal note recording what was created (appointment type, resource,
   when).

7. Draft the client reply containing the booking link with one or two sentences of context
   ("Pick any time that works and it'll land on <tech>'s calendar"). Present the draft for
   the tech to send — do not send on their behalf unless asked and the desk allows it.

Guardrails: never fabricate a booking link — only use the link/request the TimeZest
integration actually produced. One open scheduling request per ticket per purpose: always
check for an existing request before creating one. Ambiguous appointment type or resource →
ask, don't guess (a wrong resource books the wrong person's calendar). The TimeZest tools
only appear when the integration is enabled; if absent, say scheduling links aren't
available and fall back to proposing times manually (Calendar-Aware Scheduling). Keep the
internal note plain text for PSA compatibility.
```
