---
name: Maintenance Freeze Windows
description: Record and enforce client freeze calendars (tax season, go-lives, retail peak) so freezes block change scheduling unless a documented exception is signed.
category: Change & Problem Management
tools: [search_knowledge_base, search_tickets, search_clients, add_ticket_note, update_ticket, send_approval]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Maintenance Freeze Windows

**When to use:** "Accounting firm clients are frozen through tax season — record it" / change intake or calendar clearance hit a possible freeze and needs the authoritative answer / "we need to patch during their freeze — what's the exception process?" / a periodic review of freeze records before a known season.

**Run it:** on one change window · or as a freeze-record review.

## Prompt

```
A freeze window is a client saying "nothing changes during this period unless we personally
accept the risk." Keep those windows recorded where intake can find them, enforce them when
changes are proposed, and run the exception path when something genuinely can't wait.

RECORDING A FREEZE:
1. Capture the freeze as structured facts: client, start/end dates (explicit dates, not
   "tax season" — resolve the phrase to dates with the client), what is frozen (all changes
   vs. specific systems), what is exempt (typically security-critical patches and
   break-fix — get this stated, not assumed), the client-side authority who can grant
   exceptions, and who requested the freeze.
2. Store it where the desk's calendar checks read from — the client's KB/wiki record — and
   confirm it's findable in the client's documentation by the client's name. A freeze nobody
   can find protects nobody.
3. Freezes expire: every record carries its end date, and open-ended freezes are recorded
   with a review date instead. Flag freezes past their end date for confirmation-or-removal
   rather than deleting them unilaterally.

ENFORCEMENT (at intake / scheduling):
4. When a proposed change window is checked, match affected clients against active freeze
   records. Overlap → the change is blocked from scheduling: post a plain-text note citing
   the specific freeze (client, dates, scope, source record) and set the change back to the
   requester.
5. Distinguish frozen from exempt: if the change matches the freeze's stated exemptions
   (e.g. critical security patch), say so explicitly and route it onward as normal — but
   cite the exemption clause, don't infer one.

EXCEPTION PATH:
6. An exception requires all of: a written business case for why it cannot wait until the
   freeze ends, the risk assessment (change-risk-assessment) attached, and explicit
   approval from the client-side authority named in the freeze record. Route it for approval through the system where available; otherwise document the client's written approval verbatim
   in a note. Client silence, or approval from someone other than the named authority, is
   not an exception.
7. Record granted exceptions on both the change ticket and the freeze record's history — a
   freeze that leaks exceptions every week is really a calendar problem, and the pattern
   should be visible.

Guardrails: the default answer during a freeze is no. The agent never grants exceptions —
it assembles the case and routes it to the named human authority. Never treat an emergency
change as an automatic freeze exception: break-glass work during a freeze still notifies the
client's named authority immediately, because the freeze is their risk posture, not the
MSP's. Resolve vague freeze phrases to explicit dates at recording time. If freeze records
may be incomplete or stale (no review in >6 months), say so when clearing a window rather
than asserting "no freeze exists." Plain-text notes; freeze citations name the source
record so the block is verifiable.
```
