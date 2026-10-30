---
name: Staff Hours Lookup Refresh
description: When this week's staff working-hours report arrives as a ticket, update a saved lookup skill to point at it, so scheduling skills always read current shift times without anyone editing a prompt.
category: Scheduling & Dispatch
tools: [search_tickets, list_skills, update_skill, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, Dispatcher]
outcome: [Time & Cost Savings (Capacity), Always-On Coverage]
---

# Staff Hours Lookup Refresh

**When to use:** Your scheduling skills need each engineer's working hours, and those change week to week. Your PSA or HR tool can email a weekly report of start and end times, which lands as a ticket. You want the skills that schedule work to always read the newest report, with no human editing a prompt each Monday.

**Run it:** as a Flow (when the weekly report ticket is created, matched on its sender and title) · or on one ticket by hand. It maintains a small saved skill, for example "Staff Working Hours Lookup", whose only job is to say which ticket holds the current hours. `scheduling-and-dispatch/requested-time-auto-scheduler` loads that lookup.

## Prompt

```
This ticket is the new weekly staff working-hours report. Point the lookup skill at it.

Lookup skill name: <Staff Working Hours Lookup>

1. CHECK THE REPORT. Confirm this ticket is the hours report: its title matches <your report title> and the body lists engineers with start and end times. Count the engineers listed. Not the report, or fewer than <3> engineers: make no changes, add the internal note "HOURS LOOKUP: ticket does not look like a valid hours report. Lookup not changed." and stop.

2. READ THE CURRENT LOOKUP. Find the saved skill by its exact name. Not found: stop and say so; never create a new lookup unattended.

3. UPDATE IT. Replace its instructions with exactly this, filled in:
"The current staff working hours are in ticket #<number> (internal id <id>), received <date>. Open that ticket and read each engineer's start and end time from it. Treat hours as valid for the week of <week start date>. If that ticket cannot be opened, say the hours are unavailable; never assume a default shift."
Keep the skill's name and description unchanged. Change nothing else.

4. NOTE on this ticket (internal, plain text): "HOURS LOOKUP: updated <lookup skill name> to point at this ticket. Engineers listed: <count>. Previous report: #<old number or unknown>."

Never edit any skill other than the named lookup. Never copy the hours themselves into the skill; point at the ticket so the report stays the single source.

As a Flow: your entire reply is the note.
```
