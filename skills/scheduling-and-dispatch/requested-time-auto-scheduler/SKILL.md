---
name: Requested Time Auto-Scheduler
description: When a client asks for a call or visit at a specific time, find an engineer on the right team who is working and free then, book it, and confirm to the client, or hand it to dispatch with the reason.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, list_schedule_entries, schedule_ticket, update_ticket, add_ticket_note, load_skill]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Requested Time Auto-Scheduler

**When to use:** Clients write "please have someone call me at 3:00" and the ticket waits in the queue until a dispatcher reads it, by which point 3:00 has passed. You want a requested time turned into a booked appointment with a free engineer within a minute, and the client told.

**Run it:** as a Flow (when a new ticket is created on your service boards) · or on one ticket by hand. It reads engineers' hours from a lookup skill kept current by `scheduling-and-dispatch/staff-hours-lookup-refresh`, and the team roster from a saved roster skill if you keep one.

## Prompt

```
If the client asked for a specific time, try to book an engineer for it.

Settings: MIN_FREE = <3> hours of open time left in the engineer's day; APPOINTMENT = <30> minutes; TIMEZONE = <your timezone>; HOURS LOOKUP skill = <Staff Working Hours Lookup>; ROSTER skill = <your team roster, or none>.

1. DETECT. Read the client's message. Continue only if they ask for contact or work at a specific time or narrow window today or on a named day ("call me at 3", "Tuesday after 1pm"). Vague ("sometime this week") or no time: make no changes and stop. Resolve the time in TIMEZONE; if it has already passed today, treat it as not bookable.

2. TEAM. Find which team or pod serves this client, from the roster skill or the ticket's team. Get that team's engineers. Cannot tell: go to step 5.

3. AVAILABILITY. Load the hours lookup and read each engineer's shift. For each engineer on the team: skip anyone not working at the requested time; read their schedule for that day; skip anyone already booked at that time; skip anyone with less than MIN_FREE hours of open time left that day. Hours unavailable: go to step 5; never assume a default shift.

4. BOOK. From the engineers left, pick the one with the most open time. Schedule this ticket to them at the requested time for APPOINTMENT minutes. Add a client-visible note: "Hi <first name>, we have scheduled <engineer first name> to reach out at <time> <timezone>. If that no longer works, just reply here." Add an internal note naming who was booked and who was skipped and why.

5. HAND OFF. If nobody qualifies or anything is unclear, change the status to <your needs-scheduling status> and add an internal note: "AUTO-SCHEDULE: could not book <requested time>. Reason: <why>. Checked: <engineers and why each was skipped>." Then add a client-visible note: "Thanks, we have your requested time of <time> and our dispatch team will confirm shortly."

Book at most one appointment per ticket and never double-book an engineer. Never promise a time you did not book. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the internal note.
```
