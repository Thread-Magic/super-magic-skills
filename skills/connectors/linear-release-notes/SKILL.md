---
name: Linear Release Notes
description: Turn a completed Linear cycle's issues into client-safe release notes, then post the relevant fix notice to each affected ticket. Use for "write release notes from the last cycle", "tell clients their bug is fixed", or "close the loop on shipped escalations".
category: Connectors
tools: [search_tickets, add_ticket_note, update_ticket]
connectors: [Linear]
scope: global
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Linear Release Notes

**When to use:** "Cycle just ended — draft the release notes," or "the <symptom> bug shipped; notify all the tickets waiting on it."

**Run it:** across all tickets waiting on the shipped issues (run manually after a cycle closes).

## Prompt

```
Close the loop MSPs usually drop: engineering ships the fix, but the clients who reported it
never hear. Convert a completed Linear cycle into plain-language release notes and deliver the
"your issue is fixed" message to every waiting ticket.

This needs the member's connected Linear, scoped to their workspace access. If Linear isn't
connected, degrade by drafting the release notes from a pasted issue list — do not stop.

1. Pull the completed cycle in Linear and its issues in a done state. Exclude non-shipped states
   (canceled, duplicate). Never treat "in review" as shipped.
2. For each shipped issue, read it (and its comments where the user-visible effect is unclear)
   and translate to a client-safe line: what the user experienced → what is now fixed, in plain
   language. Strip internal jargon, code details, blame, and anything security-sensitive (a fixed
   vulnerability is "a security improvement", never with exploit detail).
3. Assemble the notes: Fixed / Improved / Known issues sections, dated. Show me the draft for
   review — nothing external moves before you approve the wording.
4. Map issues to waiting tickets: search tickets referencing each issue id or tracked as waiting
   on it. Present the ticket list per issue for confirmation — this is the blast radius; a
   wrong-ticket fix notice tells a client their unfixed problem is solved.
5. On confirmation, for each affected ticket: leave a note with the relevant fix notice only
   (plain text, no markdown — PSA-safe; not the whole release notes), and propose the "fix shipped
   — verify with client" status where the member wants it. Ticket notes are plain text; ask
   whether the note is internal or client-visible, don't assume.
6. Report: notes published (where the member chose to put them), tickets noted, tickets skipped
   and why.
```
