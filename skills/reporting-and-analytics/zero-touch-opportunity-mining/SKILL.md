---
name: Zero-Touch Opportunity Mining
description: Someone asks where the biggest opportunities are to increase zero-touch resolution, or which ticket patterns should become intents or flows.
category: Reporting & Analytics
tools: [search_tickets, list_intents, list_flows, list_boards]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Zero-Touch Opportunity Mining

**When to use:** "Where are our biggest zero-touch opportunities?", "analyze previous tickets and suggest intents based on common trends," or "what should we automate next to lift our zero-touch rate?"

**Run it:** across all resolved tickets in the period — manually on demand (an opportunity scan has no ticket event for a Flow to trigger on).

## Prompt

```
Mine recent tickets for the patterns most worth automating: candidates for intents and
flows, ranked by volume x automatability, with the existing automation inventory
checked so you don't propose what already exists. This skill RECOMMENDS — it never
creates or modifies intents/flows.

1. Confirm the period (default: last 60-90 days) and pull the resolved-ticket
   population with split searches per board; disclose caps (volume figures from capped
   searches are floors, not totals).

2. Cluster into repeatable request/issue patterns (password resets, new-user requests,
   distribution-list changes, printer mapping, common alert classes, status inquiries).

3. Check the existing inventory — list the current intents and flows and mark clusters
   already covered, partially covered, or uncovered. (Reading that inventory is
   admin-only and may be hidden for this member — if unavailable, degrade to
   recommendations-only and say so.)

4. Score each uncovered/partial cluster:
   - Volume — tickets per month in the cluster.
   - Automatability — how deterministic the resolution is: fixed steps, low judgment,
     verifiable inputs, no human approval legally required. Score high/medium/low with
     a one-line justification.
   Rank by volume x automatability.

5. For the top 5, give: the pattern, monthly volume, estimated tech-time it consumes,
   the proposed mechanism (intent with variations, flow trigger, self-service KB
   deflection, or an upstream fix that removes the tickets entirely), and ONE
   representative ticket. Sometimes the best "automation" is elimination — if a cluster
   traces to a fixable root cause (bad monitor threshold, missing license), recommend
   the fix over an intent. Identity-sensitive patterns (password/MFA resets) must carry
   a note that any automation needs a verification step; never propose fully unattended
   credential handling. Exclude junk/NOC boards unless alert handling is the stated
   target.

6. Present as recommendations. Offer to draft an intent or flow for the #1 candidate
   ONLY if the requester is an admin and asks — creation is a separate, confirmed step.
```
