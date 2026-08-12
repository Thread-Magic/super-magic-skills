---
name: Closure Note Completeness
description: Check a ticket's closure note against the house standard before the close sticks — issue, cause, actions, outcome, confirmation reference — and draft the compliant version when it falls short.
category: QA & Closure
tools: [search_tickets, add_ticket_note, update_ticket, run_assistive_ai]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Closure Note Completeness

**When to use:** "Check my closure note" / "is this ticket documented well enough to close?" — the documentation companion to Ticket QA Review when only note quality is in question, bulk-checking pending closures before EOD, or "draft a compliant closure note for this ticket."

**Run it:** on one ticket · across all pending closures · or as a Flow (when a ticket reaches ready-to-close).

## Prompt

```
The closure note is what the desk knows in six months: the next tech's starting point, the
client's record, the billing narrative. Grade the note against the house standard and, unlike a
pure gate, draft the missing pieces from the thread so compliance costs seconds.

1. Retrieve the ticket: full thread, time entries, classification, and the current
   closure/resolution note.

2. Grade the closure note against the house standard (override with the desk's own where
   provided):
   - Issue — what was wrong, in the client's terms, one or two lines.
   - Cause — what turned out to be behind it (or "root cause not determined" stated honestly).
   - Actions — what was actually done, specific enough to repeat or reverse.
   - Outcome — the state at close, in observable terms ("user logging in successfully"), not
     intentions ("should be fine").
   - Confirmation reference — who confirmed resolution and how, pointing at the confirmation in
     the thread (or the validation record for no-contact ticket classes).
   - Follow-ups — anything deferred, scheduled, or recommended, or explicitly "none."

3. Score each element PRESENT or MISSING, strictly from what the note says — an element buried in
   mid-thread notes but absent from the closure note is MISSING (the closure note must stand
   alone).

4. If everything is PRESENT: report pass, one line per element, and let the close stick.

5. If anything is MISSING: draft the compliant closure note from evidence already in the thread —
   an assistive summary/recap can produce the base, then structure it to the standard. Every
   sentence must trace to a thread entry; where the thread itself lacks the fact (no cause
   anywhere, no confirmation), leave an explicit placeholder like "CONFIRMATION: not yet obtained
   - confirm with <user> before closing" rather than papering over the gap. The draft documents
   what happened; it never invents what should have happened.

6. Present the draft. On approval, post it as a plain-text note (no markdown/emojis — it syncs to
   the PSA and is often client-visible in exports). Where the desk's process requires it and the
   confirmation element is genuinely missing, recommend holding the close (move it back to
   ready-to-close) until it exists.

7. For batches, output a compliance table (ticket, missing elements) and offer drafts ticket by
   ticket.

"Should be working" and other intention phrasings aren't an Outcome; require observable state or
an honest "unverified." Don't overwrite or edit the tech's existing note; post the compliant
version as an additional note and say so. Keep language simple and localizable. Posting and any
status hold require explicit approval; grading alone is read-only. This gates documentation only
— resolution truth belongs to Ticket QA Review and the Premature Confirmation Detector.
```
