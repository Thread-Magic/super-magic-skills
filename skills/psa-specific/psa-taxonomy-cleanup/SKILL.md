---
name: PSA Taxonomy Cleanup
description: Rationalize PSA ticket type/subtype/category sprawl: census real usage from tickets, propose merges and retirements, enforce migration discipline first.
category: PSA-Specific
tools: [search_tickets, list_boards, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# PSA Taxonomy Cleanup

**When to use:** "Our ticket types are a mess — help me clean them up", reporting by type/category is unreliable because values overlap or duplicate, or before a reporting project / new-board rollout that depends on a coherent taxonomy.

**Run it:** across all tickets on the board(s) in scope (run manually as an on-demand rationalization sweep).

## Prompt

```
You are running a manual, on-demand taxonomy rationalization sweep on a PSA desk (ConnectWise,
Autotask, HaloPSA). Type, subtype, category and item lists sprawl over time — near-duplicates
("Email" vs "E-mail" vs "O365 Email"), one-off values used twice ever, overlapping buckets that
make reporting meaningless. Census how the taxonomy is actually used, propose merges and
retirements grounded in that evidence, and enforce migration discipline so no historical ticket
is orphaned. This skill proposes; it changes nothing.

1. Confirm scope: which boards, which dimensions (type, subtype, category, item), and the
   lookback window. Taxonomies are often per-board, especially on ConnectWise — never merge
   across boards without confirming the values mean the same thing.

2. Usage census. Pull tickets over the window, one search per value or per board so result
   caps land per-slice rather than globally, and tally how many tickets carry each value. The
   census, not intuition, is the evidence base. Flag any count that may have hit a cap as
   "at least N" (apply the Sweep Honesty skill): a low count may be a capped search, not a
   rare value, so split searches before recommending a retirement.

3. Classify each value — high-use (keep), duplicate or near-duplicate (merge candidate, name
   the survivor), low or zero use (retire candidate), overlapping (an ambiguous bucket needing
   a definition, not just a merge). Group merge candidates under their survivor.

4. Propose, never execute: the target taxonomy, each merge (from → into) and each retirement
   with its ticket count, and a one-line rationale per change.

5. Migration discipline. Taxonomy changes are destructive and rewrite historical reporting. For
   every merge or retirement, spell out what happens to the tickets carrying the old value:
   remapped to the survivor, or explicitly retained read-only — never left pointing at a
   deleted value. State the order — remap existing tickets first, retire the value second — so
   nothing is orphaned. The remap is PSA-side work — the PSA is master of the taxonomy and
   Thread mirrors the result; never clean up Thread-side values independently. Check
   dependencies first: a value referenced by a Flow condition, a saved View, an agreement
   mapping or a standing report breaks silently if it changes.

6. Output a plain-text cleanup plan: the census table (value, count, classification), the
   target taxonomy, the merge and retire list with counts and rationale, the migration order,
   and a review-before-enacting list of every dependency touched. End with what a human must
   do in the PSA and in what sequence.

Keep the target taxonomy minimal and non-overlapping, and give each survivor a one-line
definition so the sprawl doesn't regrow. Anything destined for a PSA note is plain text — no
markdown or emojis (apply the PSA Note Discipline skill).
```
