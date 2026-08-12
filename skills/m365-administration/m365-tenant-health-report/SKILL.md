---
name: M365 Tenant Health Report
description: Produce an advisory digest of a client tenant's Microsoft 365 Service Health incidents and Message Center posts — what's degraded now and what change is coming — as a plain-language brief, not an action. Use when someone asks "is anything wrong with <client>'s M365," "what Microsoft changes are coming," or wants a periodic tenant health/roadmap digest.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: global
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Always-On Coverage]
---

# M365 Tenant Health Report

**When to use:** Someone asks "is anything wrong with <client>'s Microsoft 365 right now," "what Microsoft 365 changes are coming that affect us," wants a recurring (weekly/monthly) tenant health + roadmap digest, or needs a wave of client tickets correlated with a known Microsoft incident. This is a MANUAL digest — Flows are event-triggered with no schedule, so there is no unattended/scheduled variant; run it on demand or from an external scheduler. This is advisory — it reads and reports; it never changes the tenant.

**Run it:** as an on-demand digest across the whole tenant — you read and report only; it never changes tenant configuration (not a Flow: no schedule trigger).

## Prompt

```
You are producing an advisory Microsoft 365 tenant health digest. This skill reads and reports; it never changes tenant configuration. Anything actionable becomes its own ticket/skill. No fabrication — do not invent incident IDs, ETAs, deadlines, or links; if the source doesn't say, report it as unknown/not available.

1. Gather two feeds for the specific tenant (via the admin center Service Health dashboard and Message Center, or a connected source; pull documented client context from the client's documentation — connector-gated, skip gracefully if neither is connected — the knowledge base, and prior tickets): active/recent Service Health incidents and advisories (with affected workload and status), and Message Center posts (planned changes, new features, and — most importantly — deprecations/required actions with their deadlines).

2. Service Health section: list current incidents/advisories by workload (Exchange, Teams, SharePoint, Identity, etc.), each with a one-line plain-language impact and Microsoft's current status/ETA. Separate "active, affecting users now" from "recently resolved." Do not restate Microsoft's text verbatim at length — summarize the impact.

3. Message Center section: surface the posts that need attention, prioritized — anything with a required admin action and a deadline first (these are the ones that bite: a deprecation the client must act on), then major changes, then informational. For each, note the workload, what changes, and the date.

4. Correlate with the client's tickets. Read open/recent tickets for symptoms that match an active incident — if a live Microsoft incident explains a cluster of tickets, say so; that saves the desk chasing a phantom local fault.

5. Recommend, don't act. Where a Message Center item needs preparation (a config change before a deprecation, a comms to users about a feature change), state it as a recommended follow-up with the deadline — do NOT perform any tenant change from this skill. The zero-assumption rule applies: this brief lists what to do, it does not do it. Anything actionable becomes its own ticket/skill.

6. Output a plain-text digest (leave a note where a tracking ticket exists): date/window and tenant, Service Health (active then resolved), Message Center (required-action-with-deadline first), any ticket correlations, and a short "recommended follow-ups" list with owners/dates left for the human to assign. State the data as point-in-time (Service Health and Message Center move) — timestamp the digest. No fabricated incident IDs, dates, or links — if a detail isn't in the source, say it's not available. Summarize Microsoft's wording, don't reproduce it at length; plain-text note for PSA compatibility. Log time.

When in doubt, do nothing to the tenant and route the actionable item to the owning skill/ticket.
```
