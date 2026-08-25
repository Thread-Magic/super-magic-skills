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
A freeze window is a client saying "nothing changes during this period unless we
personally accept the risk". Keep those windows recorded where intake can find them,
enforce them when changes are proposed, and run the exception path when something
genuinely cannot wait.

RECORDING A FREEZE
1. Capture it as structured facts: client, explicit start and end dates (resolve "tax
   season" to dates with the client), what is frozen (all changes vs. specific systems),
   what is exempt (typically security-critical patches and break-fix — get this stated,
   not assumed), the client-side authority who can grant exceptions, and who requested it.
2. Store it where the desk's calendar checks read from — the client's KB or wiki record —
   and confirm it is findable there by the client's name. A freeze nobody can find
   protects nobody.
3. Freezes expire: every record carries its end date, open-ended ones a review date
   instead. Flag freezes past their end date for confirmation-or-removal rather than
   deleting them unilaterally.

ENFORCEMENT (at intake / scheduling)
4. Match the affected clients of a proposed change window against active freeze records.
   Overlap -> the change is blocked from scheduling: leave a note citing the freeze
   (client, dates, scope, source record) and send the change back to the requester.
5. Distinguish frozen from exempt: where the change matches the freeze's stated exemptions
   (a critical security patch, say), route it onward as normal — citing the exemption
   clause, never inferring one.

EXCEPTION PATH
6. An exception requires all three: a written business case for why it cannot wait until
   the freeze ends, the risk assessment (change-risk-assessment) attached, and explicit
   approval from the client-side authority named in the freeze record. Route it for
   approval through the system where that exists, otherwise record the client's written
   approval verbatim in a note. Client silence, or approval from anyone other than the
   named authority, is not an exception.
7. Record granted exceptions on both the change ticket and the freeze record's history — a
   freeze that leaks exceptions weekly is really a calendar problem, and that pattern
   should be visible.

Guardrails: the default answer during a freeze is no. You never grant an exception — you
assemble the case and route it to the named human authority. An emergency change is not an
automatic freeze exception: break-glass work during a freeze still notifies the client's
named authority immediately, because the freeze is their risk posture, not the MSP's. If
freeze records may be incomplete or stale (no review in over 6 months), say so when
clearing a window rather than asserting "no freeze exists". Notes are plain text, no
markdown or emojis (apply the PSA Note Discipline base skill), and a freeze citation names
the source record so the block is verifiable.
```
