---
name: Triage Agent Tuning
description: Tune Triage Agent custom rules from observed misses — wrong boards, wrong priorities, tickets it should have left alone — plus bypass-word usage analysis.
category: Automation & Flows
tools: [search_tickets, list_boards, list_ticket_priorities, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, Dispatcher]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Triage Agent Tuning

**When to use:** "The triage agent keeps putting <vendor> alerts on the wrong board" / "techs are bypassing triage constantly — figure out why" / a monthly review of triage accuracy after rule or board changes.

**Run it:** across all tickets in the window — manually on demand (rule tuning has no ticket event for a Flow to trigger on).

## Prompt

```
Turn a pile of "the triage agent got this wrong" examples into a small set of precise
custom-rule edits, backed by evidence of how often each miss actually occurs. Triage Agent
rules live in settings with no API write — this skill PRODUCES rule text; the admin applies
it. Never claim a rule has been applied.

1. Collect the misses. Start from examples the member supplies; then widen the search
   for the same pattern (same sender, subject shape, or client) over the
   last 30 days to measure recurrence. Split searches per board/signal; report capped
   counts as "at least N".

2. Classify each miss: wrong board, wrong priority, wrong type/classification, acted when
   it should have skipped, or skipped when it should have acted.

3. Bypass-word analysis: search recent tickets/notes for the tenant's bypass word. High
   usage concentrated on one board or ticket shape marks exactly where a rule is missing or
   wrong; broad scattered usage suggests a trust problem rather than a rule problem. Report
   frequency, where it clusters, and the apparent reason.

4. Draft custom-rule text for each confirmed pattern. Rules should be few, specific, and
   testable: name the observable signal (sender domain, subject pattern, keyword) and the
   exact outcome (board, priority — using the desk's real board and priority values). Prefer
   one rule that covers a pattern over five that cover instances. Every proposed rule needs
   evidence of recurrence — do not write rules from a single anecdote.

5. For each proposed rule show: the evidence (ticket count), the rule text, 1–2 recent
   tickets it would have handled correctly, and any ticket it might now handle INCORRECTLY.
   Always run this over-matching check — a rule that fixes 10 misses but breaks 50 correct
   routings is a regression.

6. Output the rule set for the admin to paste into the Triage Agent settings, ordered by
   impact. Keep the total set small and recommend deleting stale rules whose pattern no
   longer appears. Recommend re-running this review two weeks after applying.
```
