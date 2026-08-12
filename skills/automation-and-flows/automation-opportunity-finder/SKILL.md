---
name: Automation Opportunity Finder
description: Mine recent tickets for repetitive manual work, estimate hours burned per pattern, and route each finding to a flow, intent, RMM policy, or training fix.
category: Automation & Flows
tools: [search_tickets, list_boards, list_flows, list_intents]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity)]
---

# Automation Opportunity Finder

**When to use:** "Analyze last quarter's tickets and tell me what to automate" / "we want to raise zero-touch resolution — where's the low-hanging fruit?" / an exec asks for an automation ROI story with numbers behind it.

**Run it:** across all tickets in the window — manually on demand (a read-only analysis has no ticket event for a Flow to trigger on).

## Prompt

```
A wider net than Intent Mining: find ALL repetitive manual work in the ticket stream — not
just deflectable requests — estimate the hours it consumes, and route each pattern to the
mechanism that kills it. Read-only analysis; never create flows or intents here — hand off
to the builder skills, each with its own confirmation gate.

1. Confirm the window (default 90 days) and boards. Search tickets per
   board and per recurrence signal (same title shape, same alert source, same request
   type) — split searches; label capped counts as "at least N".

2. Cluster into recurring patterns. For each, capture: occurrences in window, whether
   resolution steps are identical each time, and who does the work.

3. Estimate time savings per pattern: occurrences x average handle time. Take handle time
   from time entries where they exist; otherwise use a stated assumption (e.g. "assuming
   15 min each") and label it as an assumption IN THE SAME SENTENCE as the number, never as
   measured fact.

4. Route each pattern to its correct mechanism:
   - Predictable end-user request with a scriptable answer -> intent (hand to Intent Builder).
   - Internal choreography on ticket events (statuses, assignments, notes, notifications)
     -> flow (hand to Flow Builder).
   - Same technical fix on endpoints (disk cleanup, service restart, patching) -> RMM
     script/policy — note the tech executes this in the RMM; Super Magic can deep-link a
     device but cannot run scripts.
   - Alert noise with no action ever taken -> monitoring tuning (fix the sensor).
   - Same how-do-I question or repeated tech mistakes -> training or KB article.
   Do NOT recommend automating judgment-heavy or safety-relevant work (security response,
   offboarding approvals) end-to-end; route those to "assisted", not "zero-touch".

5. Check the existing intents and flows; anything already covered moves to an "already
   automated — verify it's working" list instead of the build list.

6. Output a ranked table: pattern, occurrences (with cap caveats), estimated hours/month
   (with assumptions), routed mechanism, one-line next step. Rank by estimated hours saved
   x ease of implementation. Sanitize examples: <client>, <vendor>, <device> placeholders.
```
