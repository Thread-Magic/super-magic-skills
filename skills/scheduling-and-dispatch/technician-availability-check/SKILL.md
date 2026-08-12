---
name: Technician Availability Check
description: Answer "who is the next available technician?" — combine today's schedules, priority-weighted open load, and shift/PTO context into a ranked availability answer.
category: Scheduling & Dispatch
tools: [search_members, search_tickets]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Technician Availability Check

**When to use:** "Who's the next available tech?" / "who can jump on this call right now?"; "is <tech> free this afternoon?"; or picking a warm-transfer target for a live client call.

**Run it:** across the active roster — a read-only availability answer.

## Prompt

```
You are giving a fast, honest answer to "who can take this?" — grounded in schedule
entries, current load, and who is actually on shift, with the numbers shown. Read-only:
you answer, you do not assign or book.

1. Build the pool: active technicians on the relevant team/board. Exclude inactive
   members, anyone flagged out/PTO, and — if this is for a specific ticket — that ticket's
   requester and anyone excluded by a client routing rule.

2. For each candidate, gather:
   - Now: are they inside a scheduled entry right now (onsite, booked session)? When does
     it end?
   - Load: open tickets, priority-weighted — someone with two Criticals isn't "available"
     even with a clear calendar.
   - Shift context: on shift, near end of shift, or after-hours/on-call? Use the desk's
     stated hours; if shift data is unknown, say so instead of assuming.

3. Rank into three buckets: free now (on shift, no current block, light load), free soon
   (current block ends within the hour, or moderate load), not today (heavy load, out,
   off shift).

4. Answer the actual question first ("Next available: <tech> — free now, 2 open tickets,
   nothing scheduled until 3pm"), then show the ranked table with the numbers per
   candidate.

5. For a single-tech question ("is <tech> free?"), answer for that tech with the same
   evidence, plus their next free window.

Guardrails: read-only — offer the follow-on ("want me to assign / schedule it?") and hand
off. Show the evidence, never a bare name. Availability without external-calendar data is
partial: if the member hasn't connected a calendar source, say the view covers Thread
schedules and load only. Tied candidates → present both, let the human pick. Never mark
someone available near or past end of shift without flagging it; after-hours handoff rules
beat raw availability. Result caps → load figures are "at least"; say so.
```
