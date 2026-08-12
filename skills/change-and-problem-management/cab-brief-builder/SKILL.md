---
name: CAB Brief Builder
description: Build the weekly change-board pack — pending changes ranked by risk, collision flags, and last week's change outcomes — so the CAB meeting is 20 minutes of decisions instead of an hour of reading tickets aloud.
category: Change & Problem Management
tools: [search_tickets, search_knowledge_base, add_ticket_note, list_boards, list_ticket_statuses]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# CAB Brief Builder

**When to use:** "Build the CAB pack for Thursday" / "what's on the change board this week?" / a recurring pre-meeting prep run the day before the change review / a lead wants a one-off snapshot of pending change risk across clients.

**Run it:** on one change · or across all pending changes on the board.

## Prompt

```
Assemble everything the change advisory board needs into one skimmable pack: what's
waiting for a decision, what's riskiest, what collides, and how last week's approvals
actually turned out. The outcomes section is what keeps a CAB honest.

1. Establish the review window (default: changes pending decision now, plus changes
   executed since the last CAB — ask for the desk's cadence if unknown).

2. PENDING CHANGES: search the change board for approval-pending statuses.
   For each, pull the one-line what/scope/window, the risk classification and scores
   (from change-risk-assessment — if a change reaches the pack unclassified, list it
   under "not ready: unassessed" rather than guessing a rank), and the prerequisites-gate
   status (incomplete requests are listed as "not ready" with the gap, not queued for
   decision).

3. RISK RANKING: order the ready changes by risk — HIGH blast radius first, then LOW
   rollback confidence as tiebreaker. State the ordering rule in the pack.

4. COLLISION FLAGS: cross-check proposed windows against each other and against
   already-scheduled changes (same systems, same clients, shared infrastructure, freeze
   windows — reuse the checks from change-calendar-management). Flag each collision inline
   on both changes involved.

5. LAST WEEK'S OUTCOMES: for changes executed since the last CAB, report per change:
   implemented as approved / implemented with deviation / rolled back / not attempted —
   based on ticket evidence; a bare "done" is UNVERIFIED, not success. Include the
   emergency changes that bypassed the board (from emergency-change-handling) with their
   retro-documentation status.

6. Compose the pack, ~1 page, in fixed order: (a) decision queue with risk rank and
   one-line asks, (b) not-ready list with reasons, (c) collision flags, (d) last week's
   outcomes with an honest success/rollback/unverified count, (e) recurring themes worth
   a policy tweak.

7. Deliver in chat for the organizer; on request post a plain-text copy as a note on the
   CAB/agenda ticket.

Guardrails: the pack informs decisions; it makes none — no change is marked approved
because it appeared in a brief. Never promote an unassessed or prerequisites-incomplete
change into the decision queue to make the pack look fuller — "not ready" is a legitimate
section. Outcome reporting uses evidence standards, not optimism: unverified completions
are reported as unverified, rollbacks are never euphemized into "partial success."
Aggregate honestly under result caps — if a board search may be capped, state the pack
may be incomplete. Sanitized for the room: name systems and clients only as the desk's
tickets do; no credentials or personal data ride along.
```
