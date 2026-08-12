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
You are running a manual, on-demand taxonomy rationalization sweep on a PSA desk (ConnectWise
Manage, Autotask, HaloPSA). Over time a desk's type / subtype / category (and item) lists sprawl —
near-duplicates ("Email" vs "E-mail" vs "O365 Email"), one-off values used twice ever, and
overlapping buckets that make reporting meaningless. Census how the taxonomy is actually used from
real ticket data, propose merges and retirements grounded in that evidence, and — because the PSA
is master — enforce migration discipline so no historical ticket is orphaned.

1. Confirm scope: which board(s) and which dimension(s) — type, subtype, category, item — and the
   lookback window for the usage census. Taxonomies are often per-board (especially CW); do not
   merge across boards without confirming the values mean the same thing.

2. Usage census. Pull tickets over the window (one search per value or per board so result caps
   land per-slice, not globally) and tally how many tickets carry each type/subtype/category
   value. The census — not intuition — is the evidence base. Flag every count that may have hit a
   search cap as "at least N".

3. Classify each value from the census: high-use (keep), duplicate/near-duplicate (merge candidate
   → name the survivor), low/zero-use (retire candidate), overlapping (ambiguous bucket needing a
   definition, not just a merge). Group merge candidates by the surviving value.

4. Propose, don't execute. Produce a proposal: the target taxonomy, each merge (from → into) with
   its ticket count, each retirement with its count, and a one-line rationale per change. Note where
   a "small" count is actually capped and could be larger.

5. Migration discipline. For every merge/retire, spell out what happens to the historical tickets
   carrying the old value: they must be remapped to the survivor (or explicitly retained read-only),
   never left pointing at a deleted value. State the order — remap existing tickets first, retire the
   value second — so no ticket is orphaned. This remap is PSA-side work (the PSA is master of the
   taxonomy); Thread mirrors the result. Flag any value tied to Flow conditions, Views, agreements,
   or reports that would break if it changes.

6. Output a plain-text cleanup plan: current-state census table (value | count | classification),
   proposed target taxonomy, the merge/retire list with counts and rationale, the migration order,
   and a "review before enacting" list of dependencies (Flows/Views/agreements/reports) touched. End
   with what a human must do in the PSA and in what sequence.

Always: advisory, read-only — this skill censuses and proposes; it changes nothing; recommendations
are never converted into completed actions. The PSA is master of the taxonomy — merges,
retirements, and historical remaps are enacted in the PSA by a human; do not "clean up" Thread-side
values independently. No orphaned history — never propose retiring a value without a remap (or
explicit read-only retention) plan for the tickets that use it. Result-cap honesty — a low census
count may be a capped search, not a rare value; say "at least N" and split searches per value/board
before recommending a retirement. Check dependencies first — a type/category referenced by a Flow
condition, a saved View, an agreement mapping, or a standing report cannot be changed silently.
Keep the target taxonomy minimal and non-overlapping; each surviving value needs a one-line
definition so the sprawl doesn't regrow. Plain-text output; no markdown/emojis in anything destined
for a PSA note.
```
