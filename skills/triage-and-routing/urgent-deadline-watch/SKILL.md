---
name: Urgent Deadline Watch
description: Catch a client-stated deadline inside four hours or already passed, raise the priority, and flag it internally. Availability is not a deadline.
category: Triage & Routing
tools: [search_tickets, list_ticket_priorities, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Urgent Deadline Watch

**When to use:** A client wrote a real completion deadline into a ticket ("needs to work before payroll runs at 4") and nobody has noticed it is nearly up. Most of this skill's value is what it refuses to flag: "I am free until 1:30" is scheduling, not a deadline, and a watch that cannot tell the difference raises priority on everything and gets ignored.

**Run it:** on one ticket · or as a Flow (when a ticket is created or a client replies).

## Prompt

```
On this ticket, decide whether the client stated a DEADLINE. If it is close or has
passed, raise the priority and flag it internally. Never contact the client: the
internal note is your only output.

1. LOAD. Read the ticket with its full message history, and note the current time in
the desk's timezone (set yours here: America/New_York). If an internal note containing
"URGENT DEADLINE - PRIORITY RAISED" already exists, stop and change nothing. Read only
messages FROM THE CLIENT; ignore technician, status, and system messages.

2. AVAILABILITY IS NOT A DEADLINE. A deadline is a time by which the work must be
COMPLETE. When a client is reachable is scheduling, never a deadline. Go to step 5 if
the client only gave:
- free or busy windows: "free until 1:30, again after 2", "meeting 12:30 to 1"
- leaving or unreachable: "I am leaving for the day", "out tomorrow"
- any scheduled call, meeting, or appointment time
- ticket age, or urgency with no time: "pending two weeks", "ASAP"
A meeting counts ONLY if the client says the work must be done before it.

3. RESOLVE AND DECIDE. Act only on a stated completion time ("by 10am", "end of day"),
a hard event anchor ("before payroll runs"), or consequence language ("too late after
that"). Resolve it to one time in the desk's timezone, anchored to that message's
timestamp. Defaults: morning = 12 PM; afternoon, end of day, close of business = 5 PM;
first thing tomorrow = 9 AM next business day. Two or more: earliest still relevant.
Act only if 4 hours or less remain, or the deadline passed and the ticket is open.
Otherwise, or if you cannot resolve it confidently, go to step 5. Never guess.

4. APPLY. 4a, 4b and 4c are all mandatory, in that order. One does not satisfy the
others.
4a. Change ONLY the summary: the existing summary verbatim plus " | Urgent Deadline".
Never reword or truncate it. Already suffixed: skip. Re-read to confirm; retry once.
4b. As a separate edit, set the priority to the desk's quick-response tier (typically
P2). Never lower one: already at or above it, leave it.
4c. Leave an INTERNAL note, reproduced exactly, every emoji and blank line:

🚨🚨 **URGENT DEADLINE - PRIORITY RAISED** 🚨🚨

⏰ **DEADLINE:** [date, time]
⏳ **TIME LEFT:** [X h Y m, or 🔴 **PASSED BY X** 🔴]

💬 **CLIENT SAID** ([timestamp])
> "[quote, max 25 words]"

✅ **ACTION NEEDED:** [what, by when]

*Triggered by Agent - Urgent Deadline Watch*

5. NO ACTION. Post nothing, change nothing, explain nothing. Silence is correct.

Guardrails:
- NEVER COMMUNICATE WITH THE CLIENT. The note must be internal. If you cannot post it
internally, post nothing.
- Never downgrade priority. Never change status, board, or assignee.
- The step 4 actions happen at most once per ticket.
- Where a PSA strips formatting from notes, send the same fields as plain-text lines
with no markdown or emojis (apply the PSA Note Discipline skill).
```
