---
name: First Contact Resolution Report
description: Report the desk's FCR rate, the share of tickets resolved by first assignee with no handoffs, with the definition stated to prevent later disputes.
category: Reporting & Analytics
tools: [search_tickets, search_members, list_boards, list_ticket_statuses]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Faster Resolution & Response]
---

# First Contact Resolution Report

**When to use:** "What's our FCR rate?" / "how often do we fix things on the first touch?", benchmarking the desk before/after a triage or automation change, or the inverse: "why do our tickets bounce between people so much?"

**Run it:** across all resolved tickets in the period — manually on demand (a rate report has no ticket event for a Flow to trigger on).

## Prompt

```
Measure first-contact resolution for the desk (or a board, team, or tech) over a
period, using ONE explicit definition printed in the output: a ticket counts as FCR
when it was resolved directly by its first assignee with no intermediate handoffs — no
reassignment, no board bounce, no escalation. FCR debates are almost always definition
debates; this skill ends them by shipping the definition with the number.

1. Confirm the period (default: last full month) and scope — the whole desk, a single
   board, a team, or one tech (look up the tech by name if needed).

2. State the definition up front and get agreement if the requester implies a different
   one (some desks count "resolved within one business day" as FCR — a different
   metric; offer to run both, labeled separately).

3. Run split searches per board: tickets resolved in the period, then identify the
   non-FCR set — tickets showing reassignment, board moves, or escalation between first
   assignment and resolution. Use the strongest signals the data exposes; where
   handoffs are only partially visible, say which signal you used and what it can miss.

4. Compute FCR = (resolved with no handoffs) / (all resolved), overall and broken down
   by board and category where volume permits. Exclude auto-closed/no-touch tickets
   from both numerator and denominator — automation resolutions are a different (good)
   story and inflate FCR if mixed in.

5. ANTI-PATTERN CHECK — a suspiciously high FCR can mean techs avoid escalating when
   they should; scan the non-FCR set's reopen rate vs the FCR set's. If FCR tickets
   reopen more, flag it: speed is being bought with quality.

6. Output: the definition verbatim (always — a bare percentage is not a deliverable),
   the headline rate with prior-period comparison if available, the breakdown table,
   the top three handoff patterns (which category bounces, and to whom, as patterns not
   blame), and a methodology note (period, scope, handoff-detection signals,
   exclusions, searches, caps). Per-tech FCR is role-sensitive: escalation-tier
   engineers structurally cannot have high FCR because they receive the handoffs —
   benchmark role-aware and never rank techs on this number alone. AGGREGATE, not
   enumerate. Never present capped searches as exact totals. If handoff history is not
   reliably visible, downgrade honestly: report a bounded estimate ("between X% and Y%
   depending on treatment of Z") instead of a false-precision single number.
```
