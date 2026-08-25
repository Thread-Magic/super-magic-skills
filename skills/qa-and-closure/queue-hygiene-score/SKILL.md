---
name: Queue Hygiene Score
description: Scan a queue for hygiene defects — missing contacts, stale statuses, empty notes, unassigned owners, blank classifications — with score and fix list.
category: QA & Closure
tools: [search_tickets, list_boards, list_ticket_statuses, search_contacts, update_ticket, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Queue Hygiene Score

**When to use:** "How clean is the <board> queue?" / "give me a hygiene score for the service board" — before dispatch automation or SLA reporting goes live, a recurring weekly check comparing to last week, or after an alert storm or migration likely left malformed tickets behind.

**Run it:** across all open tickets on a board — run it manually; Flows are ticket-event triggered, so a sweep like this can't run itself on a cadence.

## Prompt

```
A queue's data quality decays quietly: contacts missing, statuses lying, notes empty. Measure the
decay as one hygiene score and hand back a ranked fix list, so "clean up the board" becomes a
checklist instead of a vibe.

1. Scope the scan — which boards, and which statuses count as open. Enumerate open tickets,
   splitting searches per defect signal per board so caps don't hide defects. Sweep Honesty base
   skill: label any capped count "at least N".

2. Check each hygiene signal as its own pass:
   - Missing contact: none set, or a catchall or placeholder contact.
   - Missing company: unassigned on a board that requires one.
   - Stale status: the status contradicts the thread — "scheduled" with no schedule entry,
     "waiting on client" where the last message is inbound, "new" but worked for days. Map status
     semantics from the board's available statuses.
   - No notes: open beyond a grace window (two business days by default) with nothing beyond
     intake.
   - No owner: unassigned beyond that same grace window.
   - Blank classification: type, subtype or priority unset.
   - Ancient and never touched: old enough to be noise candidates.

3. Compute the score: percentage of open tickets with zero defects, plus a per-signal defect
   count. Simple and repeatable beats clever, since the value is week-over-week comparison — so
   state the formula.

4. Build the fix list ranked by effort to impact: quick wins first (set owner, set
   classification), then judgment fixes (stale statuses, each linked to what the thread implies),
   then work for other skills — stale follow-ups to Stale Ticket Follow-Up Cadence, missing
   companies to catchall routing, noise to closure with sign-off.

5. Apply fixes only on explicit approval, ticket by ticket or as an approved batch: change owner,
   status or classification, set contacts that resolve unambiguously — name similarity is never
   enough, low confidence means flag not fix — and note anything needing context. Never fix
   silently: a bulk status "correction" applied wrong is a worse mess than the dirt it replaced.

6. Output the score headline, per-signal table, top fix list, and the trend where a previous
   score is supplied.

The score measures data hygiene, not tech performance — never present it as a people metric.
Notes are plain text, no markdown or emojis (PSA Note Discipline base skill). If write tools are
off, deliver score and fix list in chat.

Run unattended from an external scheduler: the entire reply is the artifact — score headline,
per-signal defect table and top fix list, plain text, no narration. If the board isn't supplied
or found, output nothing. No writes: every fix goes through the attended sign-off path, and a
scheduled run never repairs data. State the formula inside the artifact so runs stay comparable.
Zero open tickets in scope, reply exactly "NO OPEN TICKETS IN SCOPE."
```
