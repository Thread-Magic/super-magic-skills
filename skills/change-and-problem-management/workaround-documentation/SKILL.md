---
name: Workaround Documentation
description: A workaround living in one tech's head is a liability — document it in the standard format (steps, hold time, cost, expiry review), label the ticket "workaround-only," and make sure nobody mistakes it for a fix.
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
A workaround is a controlled loss: service limps on while the real fix waits. Undocumented,
it's a trap — reinvented per incident, applied after the fix ships, or silently becoming
the permanent answer nobody chose. Write workarounds down in a standard shape and keep them
honestly labeled as what they are.

1. Extract the workaround from the source ticket(s): what the tech actually did, from the
   notes — not an idealized version. Where the notes are thin, ask the tech now, while they
   still remember; that's the moment this skill exists for.

2. Document in the standard format:
   - Applies to: the symptom/known error this works around, linked to the problem record
     or KEDB entry if one exists. A workaround with no problem record triggers the
     question: should one be opened?
   - Steps: numbered, executable by a tech who wasn't there. Include how to confirm it
     worked.
   - Hold time: how long relief lasts (until next reboot / next sync cycle / indefinitely)
     — evidence-based from the tickets, marked "estimated" where it is.
   - Cost: what's degraded while the workaround is active (features off, manual effort per
     day, risk carried) — the number the fix-vs-accept decision needs.
   - Undo: how to remove the workaround cleanly when the fix ships.
   - Expiry review date: every workaround gets one (default 60 days). A workaround is a
     lease, not a deed.

3. Store where the desk retrieves knowledge (KB draft via the desk's pipeline, and/or the
   KEDB entry's workaround section) and post a plain-text pointer note on the source ticket.

4. LABEL THE TICKETS: on every incident resolved by this workaround, the closing note
   states "resolved via WORKAROUND-ONLY — permanent fix tracked in <problem record>" —
   never a bare "resolved." This keeps workaround-resolutions distinguishable from real
   fixes in QA, recurrence analysis, and client reporting. Where the desk has a
   workaround-only status/type field, set it.

5. On retrieval for a live incident: quote the documented steps with the document's date
   and hold-time caveats; cite only documents that exist — never fabricate a link, a KB
   reference, or a remembered-sounding procedure.

6. Review sweep: list workarounds past their expiry review date with days overdue, incident
   count still applying them, and a recommendation each — extend (fix still pending),
   retire (fix shipped — coordinate KEDB retirement), or escalate (the "temporary"
   workaround has quietly become permanent without an accepted-risk decision).

Guardrails: a workaround note never claims resolution of the underlying problem — the
workaround-only label is non-negotiable on every ticket it closes. Document what was
actually done, verified against the ticket record; do not "improve" the procedure
speculatively. Every workaround carries its cost and its expiry review date. Never fabricate
references, links, or steps on retrieval; "no documented workaround exists" is the correct
answer when true. Workarounds with security implications (disabled controls, relaxed
policies) get flagged to the lead at documentation time, not just at review.
```
