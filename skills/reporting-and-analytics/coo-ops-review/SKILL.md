---
name: COO Ops Review
description: An ops leader asks what the team is doing well and not so well — an honest, evidence-backed operations review of the service desk.
category: Reporting & Analytics
tools: [search_tickets, search_members, search_clients, list_boards]
connectors: []
scope: global
flow: no
role: [MSP Owner / Leadership]
outcome: [Fewer Escalations & Less Noise, Retention & Growth (CSAT/Expansion)]
---

# COO Ops Review

**When to use:** "What is the team doing well and not so well?", a COO or ops director's monthly/quarterly desk review, or "give me an honest assessment of the operation — strengths and weaknesses."

**Run it:** across all tickets in the period — manually on demand (an ops review has no ticket event for a Flow to trigger on).

## Prompt

```
An honest two-column review of the service desk for an operations leader: what the team
is genuinely doing well, what it is not, and the evidence behind every claim — more
operational than the CEO brief, more balanced than a problem list. Leadership eyes only.

1. Confirm the period (default: last 30-60 days) and run the evidence sweep with split
   searches per signal per board (intake, closures, aging, unassigned, sentiment,
   reopens, escalations); exclude junk/NOC boards and auto-closed statuses; track caps
   and disclose them rather than presenting a partial sweep as complete.

2. Build DOING WELL — 3-5 findings, each with its evidence: responsiveness holding
   under rising intake, strong sentiment on a hard client, aging tail shrinking,
   escalations landing cleanly. Real findings only; if a category is merely fine, it
   does not make the list.

3. Build NOT SO WELL — 3-5 findings with equal evidentiary standard: waiting-on-client
   tickets going stale without follow-up, reopen rate creeping on one board, unassigned
   urgent items pooling overnight, chronic issues without RCA.

4. For each weakness: the operational cause as read from the data (process, coverage,
   tooling, skills) — stated as a hypothesis where the data can't prove it — and one
   concrete corrective.

5. Every claim, positive or negative, cites its evidence pattern; praise without
   evidence is filler, criticism without evidence is slander — cut both. AGGREGATE
   rather than enumerate; a specific ticket or client appears only as the single best
   illustration of a systemic point. Weaknesses belong to processes and structures in
   this review — individual coaching goes through the manager's 1:1 channel. NEVER use
   volume alone as a good-or-bad signal (rising intake can mean growth; falling
   closures can mean harder work). Be genuinely balanced: forcing 5 weaknesses out of a
   healthy period is as dishonest as hiding them in a rough one.

6. Close with the balance judgment (is the operation net-improving or net-degrading,
   and the single trend that decides it), then a methodology note (period, searches,
   exclusions, caps).
```
