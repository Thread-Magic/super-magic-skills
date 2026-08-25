---
name: Resource Mailbox Setup
description: Create Exchange room and equipment mailboxes with booking policies, auto-accept or delegate approval, and recurring-meeting and duration limits.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Resource Mailbox Setup

**When to use:** A ticket asks to set up a calendar for a conference room / pool car / loaner laptop, reports an existing resource misbehaving ("the room accepts everything and double-books" or "booking requests just sit there"), or asks to add delegate approval to an existing room. You ship a resource mailbox whose booking behavior is a deliberate policy, not the defaults.

**Run it:** on one client's request — you confirm the policy and prepare it, a technician drives PowerShell or the admin center (not a Flow: it needs a human at the console).

## Prompt

```
A resource mailbox's booking behavior is a deliberate policy — who can book, whether a human approves, how far out and how long. You confirm and prepare it; the tech drives PowerShell or the admin center. Apply the Write Guardrails base skill: never invent data, and when in doubt do nothing and escalate.

1. Confirm with the client before creation — the defaults silently answer these wrong:
   - Room or Equipment? Rooms get locations in Room Finder; equipment doesn't.
   - Auto-accept, or delegate approval? Automatic suits ordinary rooms; anything contended or expensive wants a human approver.
   - Who may book — everyone, or a restricted group?
   - Recurring meetings allowed? Standing bookings are how rooms get squatted.
   - Booking window (how far ahead) and maximum duration?

2. Prepare creation: `New-Mailbox -Room -Name "<room>"` or `New-Mailbox -Equipment -Name "<item>"`. No license needed under 50 GB, and sign-in on the account stays blocked — nobody logs in as the room.

3. Prepare the booking policy with `Set-CalendarProcessing`:
   - Auto-accept: `-AutomateProcessing AutoAccept` — this is what declines conflicts and prevents double-booking.
   - Delegate approval: `-AllBookInPolicy $false -AllRequestInPolicy $true -ResourceDelegates <approvers>`. Verify the delegates exist, are active and agreed to the job; a single-person or unwatched queue is the "requests just sit there" ticket.
   - Restricted booking: `-BookInPolicy <group>` with `-AllBookInPolicy $false` — maintain a group, not a person list.
   - Limits: `-AllowRecurringMeetings`, `-BookingWindowInDays`, `-MaximumDurationInMinutes`.
   - Ask about `-AddOrganizerToSubject`/`-DeleteSubject`: hiding subjects protects privacy, showing them helps front-desk staff.
   Check the client's documentation for a room standard; if that integration isn't connected, say so and work from the ticket (Connector Degradation base skill).

4. For "room misbehaves" tickets, pull `Get-CalendarProcessing` first and diff it against intended behavior. Double-booking is almost always `AutomateProcessing` not set to AutoAccept; silent requests are almost always missing delegates, a departed user as sole ResourceDelegate being the classic. Capture that output — it is the rollback.

5. Send the policy summary to the client for sign-off. Booking rules are visible behavior for everyone who schedules meetings.

6. Verify with evidence: a test booking auto-accepts (or routes to the delegate), a conflicting booking declines, and an over-limit booking declines with the policy reason. Leave a plain-text note — resource name and address, type, approval mode, who can book, window, duration, recurrence, delegates, approver, date, and rollback. Log time.

Never leave a contended resource on silent defaults. PowerShell here is labeled: verify it against current module versions.
```
