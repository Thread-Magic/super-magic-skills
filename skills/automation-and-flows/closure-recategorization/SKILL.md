---
name: Closure Recategorization
description: When a ticket enters a resolution status, re-read the whole thread and correct its type/subtype/item and category to match what the work actually was — using only values valid on that board. Answers the "fix the classification at close so reporting is right" workflow.
category: Automation & Flows
tools: [search_tickets, list_boards, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, Dispatcher]
outcome: [Time & Cost Savings (Capacity)]
---

# Closure Recategorization

**When to use:** A ticket just entered a resolution/closed-family status and its intake classification looks wrong; "fix the categorization on resolved tickets before they sync out for reporting"; a flow on close should re-classify from the full thread. Fires on the EVENT of entering a resolution status — never on a timer or "N hours after close".

**Run it:** on one ticket · or as a Flow (triggered when a ticket enters a resolution/closed status).

## Prompt

```
Tickets are classified at intake from a one-line request and rarely revisited; by close, the
thread reveals what it really was. Re-read the resolved thread and correct type/subtype/item
and category so closed-ticket reporting reflects reality — using only classification values
that exist on the board.

Your entire reply is the audit note, posted verbatim, plain text (no narration): either
`RECLASSIFIED. Was: <old>. Now: <new>. Evidence: <one line>.` or `CLASSIFICATION UNCHANGED.
<one line>.`

1. Re-read the ticket and its ENTIRE thread — the resolution, the
   work notes, the final client-visible reply. Classify from what was actually done, not the
   opening summary.

2. Establish the valid value set for this board. Thread does not expose PSA setup tables
   directly, so derive it in order of preference: the desk's documented taxonomy sheet;
   values observed on recently closed tickets on the SAME board; or ask
   the reviewer. Never use a value you have not seen on this board (confirm the board
   context first). Respect pairwise validity — an Item must have been seen with its
   Subtype.

3. Compare the current classification to the evidence-based one. If they already agree, do
   nothing (CLASSIFICATION UNCHANGED).

4. If they differ, correct the type/subtype/item and category, using only
   board-valid values. NEVER invent a value — PSAs reject or silently drop unknown values on
   sync. Do not default to a catch-all ("General / Other") to look tidy; if no observed
   value fits, leave it unchanged and flag the gap in the note. If the thread is too thin to
   reclassify with confidence, leave it unchanged.

5. Leave the plain-text audit note: old classification, new
   classification, one-line evidence ("resolution shows this was a mailbox permissions fix,
   not a hardware issue").

Classification and the audit note are the only writes — never reopen, re-close, or change
status/owner/priority. One reclassification per closure event. If classification drives
agreement or billing routing on this desk, say so in the note and get confirmation in
attended mode. Notes are plain text — no markdown or emojis (PSA compatibility).
```
