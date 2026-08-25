---
name: Workaround Documentation
description: Document a workaround in the standard format (steps, hold time, cost, expiry review) and label the ticket workaround-only so nobody mistakes it for a fix.
category: Change & Problem Management
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Workaround Documentation

**When to use:** a tech found a workaround mid-incident and it needs capturing before it evaporates ("write up what I just did") / a problem record moving to KNOWN ERROR needs its workaround documented / "what's the workaround for <known issue>?" / a workaround review sweep.

**Run it:** on one workaround · or as a workaround-review sweep.

## Prompt

```
A workaround is a controlled loss: service limps on while the real fix waits.
Undocumented, it gets reinvented every incident, applied after the fix ships, or quietly
becomes the permanent answer nobody chose. Write it down, in a standard shape.

1. Extract the workaround from the source ticket(s) — what the tech actually did, from the
   notes, not an idealized version. Where the notes are thin, ask the tech now, while they
   still remember.

2. Document it in the standard format:
   - Applies to: the symptom or known error this works around, linked to the problem
     record or KEDB entry. A workaround with no problem record raises the question: open
     one?
   - Steps: numbered, executable by a tech who wasn't there, including how to confirm it
     worked.
   - Hold time: how long relief lasts (until next reboot / next sync / indefinitely),
     evidence-based from the tickets and marked "estimated" where it is.
   - Cost: what is degraded while it is active (features off, manual effort per day, risk
     carried) — the number the fix-vs-accept decision needs.
   - Undo: how to remove it cleanly when the fix ships.
   - Expiry review date: every workaround gets one (default 60 days). A workaround is a
     lease, not a deed.

3. Store it where the desk retrieves knowledge (a KB draft, and/or the KEDB entry's
   workaround section) and leave a pointer note on the source ticket (apply the PSA Note
   Discipline base skill — plain text, no markdown or emojis).

4. LABEL THE TICKETS: on every incident resolved by this workaround, the closing note says
   "resolved via WORKAROUND-ONLY — permanent fix tracked in <problem record>", never a
   bare "resolved" — that keeps them distinguishable from real fixes in QA, recurrence
   analysis and client reporting. Set the workaround-only status or type field where the
   desk has one.

5. On retrieval for a live incident: quote the documented steps with the document's date
   and hold-time caveats. Cite only documents that exist — never fabricate a link, a KB
   reference, or a remembered-sounding procedure.

6. Review sweep: list workarounds past their expiry review date with days overdue, the
   incident count still applying them, and a recommendation each — extend (fix pending),
   retire (fix shipped: coordinate KEDB retirement), or escalate (a "temporary" workaround
   has become permanent with no accepted-risk decision).

Guardrails: a workaround note never claims the underlying problem is resolved — the
workaround-only label is non-negotiable on every ticket it closes. Document what was
actually done, verified against the ticket record; do not "improve" the procedure
speculatively. "No documented workaround exists" is the correct answer when it is true.
Workarounds with security implications (disabled controls, relaxed policies) get flagged
to the lead at documentation time, not just at review.
```
