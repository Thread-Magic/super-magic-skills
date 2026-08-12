---
name: Autotask Service Call Scheduling
description: Autotask Service Calls: know when work is a scheduled visit object vs a plain ticket, and follow dispatch scheduling conventions so calendars stay right.
category: PSA-Specific
tools: [search_tickets, schedule_ticket, update_schedule_entry, add_ticket_note, search_members, search_contacts]
connectors: []
scope: both
flow: no
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Autotask Service Call Scheduling

**When to use:** Scheduling onsite or appointment-based work on an Autotask desk, "put this on the calendar" after a client agreed to a visit window, or auditing tickets that promise a visit in the thread but show nothing scheduled.

**Run it:** on one ticket · or across all tickets that promise a visit but show nothing scheduled.

## Prompt

```
You are scheduling work on an Autotask desk. Autotask separates the ticket (the work record)
from the Service Call (a scheduled block of time, possibly covering several tickets, that
drives the dispatch calendar and onsite logistics). Desks that schedule by dropping a due date
on the ticket instead of creating the scheduled entry end up with invisible commitments and
double-booked techs.

1. Re-read the ticket at full detail — confirm it is open and that no schedule entry already
   exists (double-booking the same visit is the most common failure).

2. Decide if this is service-call-shaped work: onsite visit, fixed appointment with the
   client, or a time-blocked remote session. Routine queue work does not get a schedule entry
   — scheduling everything destroys the calendar's signal.

3. Gather the scheduling facts before writing: confirmed date/window with the client (from the
   thread — never assume a proposed time was accepted), duration estimate, assigned resource
   (confirm the tech), onsite contact and site details (look up the contact). Missing
   confirmation → chase it (field-visit scheduling or TimeZest) rather than penciling in a guess.

4. Create the schedule entry (or amend the existing one for reschedules). Per Autotask
   convention, one schedule entry per discrete visit; if one visit covers several tickets,
   schedule the primary ticket and cross-reference the others in notes.

5. Leave a plain-text note stating the scheduled window, resource, and onsite contact — this
   is what the client-facing record and the next tech read.

6. Output: what was scheduled (or proposed), for whom, evidence the client confirmed the
   window, and any reschedule trail. Reschedules always note the old window and the reason.

Always: never schedule an unconfirmed time — a proposed window in the thread is not an
agreement; scheduling it fabricates a commitment. Re-read full ticket detail before creating
or moving a schedule entry — the visit may already be scheduled, completed, or the ticket
closed in Autotask. One visit, one entry; never stack duplicate entries to "block extra time"
— extend the duration instead. Reschedules edit the existing entry; creating a second entry
leaves a ghost booking. Time worked is logged separately (per desk convention); a schedule
entry is a plan, not a time record. If scheduling isn't available for this tenant, output the
complete scheduling packet (window, resource, contact, site) as a note for a human dispatcher
instead.
```
