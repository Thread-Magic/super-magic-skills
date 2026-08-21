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
decay as a single hygiene score and hand back the ranked fix list — so "clean up the board"
becomes a checklist instead of a vibe.

1. Scope the scan: which board(s) and which statuses count as open. Enumerate open tickets,
   splitting searches per defect signal per board so result caps don't hide defects; disclose any
   capped search.

2. Check each hygiene signal as its own pass:
   - Missing contact — no contact, or a catchall/placeholder contact.
   - Missing or implausible company — unassigned company on a board that requires one.
   - Stale status — status contradicts the thread ("scheduled" with no schedule entry; "waiting on
     client" where the last message is inbound; "new" but worked for days). Map the board's status
     semantics from the available statuses.
   - No notes — open beyond a grace window (default 2 business days) with zero notes beyond intake.
   - No owner — unassigned beyond the same grace window.
   - Blank classification — type/subtype or priority unset.
   - Ancient never-touched — so old and untouched they're probably noise candidates.

3. Compute the hygiene score: percentage of open tickets with zero defects, plus a per-signal
   defect count. Simple and repeatable beats clever — the value is week-over-week comparison, so
   state the formula in the output.

4. Build the fix list, ranked by effort-to-impact: quick wins first (set owner, set
   classification), then judgment fixes (correct stale statuses — link each to what the thread
   implies), then candidates for other skills (stale follow-ups → Stale Ticket Follow-Up Cadence;
   missing companies → catchall routing; noise → closure with sign-off).

5. Apply fixes only on explicit approval, ticket by ticket or as an approved batch: change
   owner/status/classification, resolve and set contacts for resolvable missing contacts (assign
   only on an unambiguous match — name similarity is never enough; low confidence means flag, not
   fix), and leave a plain-text note where a correction needs context. Never fix silently — a bulk
   status "correction" applied wrong is a worse mess than the dirt it replaced.

6. Output: score headline, per-signal table, top fix list, and — when a previous score is provided
   — the trend.

Any capped count is labeled "at least N". The score measures data hygiene, not tech performance —
don't present it as a people metric. If write tools are disabled, deliver score and fix list in
chat only.

Running unattended (from a scheduler): the entire reply is the artifact — score headline,
per-signal defect table, and top fix list in plain text. No narration. Board not supplied or not
found → output nothing. Permitted writes: none — every fix requires the attended sign-off path; a
scheduled score run never repairs data. The score formula is stated inside the artifact so runs
stay comparable; capped searches labeled "at least N" per signal. Zero open tickets in scope →
reply exactly "NO OPEN TICKETS IN SCOPE."
```
