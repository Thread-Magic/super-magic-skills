---
name: Appointment No-Show Follow-Up
description: A client missed a scheduled appointment: log the no-show on the ticket, draft a courteous rebooking email, and apply the repeat-no-show policy on miss #3.
category: Scheduling & Dispatch
tools: [search_tickets, add_ticket_note, update_ticket, schedule_ticket, create_timezest_scheduling_request, get_timezest_scheduling_requests]
connectors: [TimeZest]
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Appointment No-Show Follow-Up

**When to use:** "Client no-showed our 10am — handle it"; a tech reports waiting on a session/onsite where the contact never appeared; or reviewing a ticket whose scheduled window passed with no client contact.

**Run it:** on one ticket · or as a Flow (on a no-show status/event) that logs the miss. Flows can't time-trigger it — run the rebooking side manually.

## Prompt

```
Recover a missed appointment without friction: record what happened, get a friendly rebooking in
front of the client, and keep an honest count so a pattern gets handled by policy.

1. Confirm the miss on the right appointment — the ticket's schedule entry (date, time, timezone,
   tech) and the tech's account: how long they waited, whether they called. If it's ambiguous
   whether the client really no-showed (the tech had the wrong bridge, say), pause and ask; a
   false no-show damages the relationship record.

2. Log it in an internal note — plain text, no markdown or emojis (PSA Note Discipline base
   skill): appointment date and time, type, who no-showed, what the tech attempted, minutes
   waited. Count prior no-shows for this engagement from the note trail and include the running
   count ("2nd missed appointment for this engagement").

3. If the tech waited billable time and the desk bills for no-shows, remind them to log it; don't
   create the time entry unless asked.

4. Rebook, preferring self-service: where TimeZest is enabled, check for an existing request and
   send the client a fresh booking link. Otherwise propose two or three concrete slots and
   schedule once the client confirms — with no TimeZest, that is the whole rebook path.

5. Draft the courteous rebooking email for the tech to send: no blame — "we missed you", not "you
   missed us" — what the appointment was for, the link or proposed times, what the client should
   have ready. Warm, short, zero passive aggression.

6. On the third miss, or the desk's stated threshold, add the policy note internally: the pattern
   summary with dates and the desk's prescribed action — notify the account manager, move to a
   waiting status, or flag a per-policy fee. The client-facing draft stays courteous, and any
   policy consequence is quoted in the desk's own wording, never invented.

Verify before logging: a no-show note is a small accusation. The client-facing message is
blame-free and stays a draft the tech sends. No policy threats unless the desk's written policy
text is supplied: never invent policy wording or fees. Status and priority changes happen only
per the desk's process, confirmed first, and a recommendation never becomes a completed action.

As a Flow: your entire reply is the no-show log note, posted verbatim — date, time and type, who
no-showed, what the tech attempted, minutes waited, running count from the note trail. No
narration. Judging whether a no-show really happened cannot run unattended: on any ambiguity
about the entry, the timezone or the tech's account, output nothing. If the count can't be
derived, the note says "prior count unverified". At the threshold it flags "POLICY THRESHOLD
REACHED - notify account manager". Only the log note is written unattended: the rebooking email,
TimeZest link, time entries, status changes and policy consequences stay attended.
```
