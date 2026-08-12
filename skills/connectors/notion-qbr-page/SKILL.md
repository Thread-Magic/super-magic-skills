---
name: Notion QBR Page
description: Assemble a QBR pre-read for a client as a Notion page — ticket volume vs prior period, top issues, SLA picture, and recommendations, with data views where a database backs them. Use when asked to "prep my QBR in Notion", "build the pre-read for <client>'s business review", or "QBR page for next week".
category: Connectors
tools: [search_tickets, search_clients, add_ticket_note]
connectors: [Notion]
scope: global
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion), Time & Cost Savings (Capacity)]
---

# Notion QBR Page

**When to use:** "I have a QBR with <client> — build the pre-read in Notion," or "assemble <client>'s quarterly numbers into a page I can present from."

**Run it:** across all of a client's tickets for the period (run manually before a QBR).

## Prompt

```
Build a client QBR pre-read as a shareable Notion page: real numbers from the ticket record,
the quarter's story in three sections, and recommendations that follow from the data.

This needs the member's connected Notion. If Notion isn't connected, degrade by delivering the
full pre-read as markdown for manual paste and say how to connect Notion — do not stop.

1. Confirm the client and period (default: last full quarter vs the quarter before).
2. Gather data from tickets, split per signal: total volume, volume by category/board, open vs
   closed, aged tickets, escalations, recurring issues (same user/device/symptom 3+ times). If
   any search hits its cap, carry "at least N" into the page — never present a capped count as
   exact. Every number on the page comes from an actual search result; no invented benchmarks.
3. Draft the page: "The quarter in numbers" (volume vs prior period, resolution picture),
   "What drove the tickets" (top 3–5 themes with counts; noisy users/devices as patterns, e.g.
   "<device> generated 12 tickets"), "Where we stand" (open items, risks), "Recommendations"
   (2–3, each tied to a data point above). A recommendation without a supporting data point
   doesn't ship.
4. This page may be shown to the client: no internal-only commentary (tech-performance gripes,
   margin data), no other clients' names, no end-user blame by name — describe patterns, not
   people. Show me the draft before writing.
5. Search Notion for where QBR docs live (or last quarter's page) and confirm placement; then
   create the Notion page. If this quarter's page already exists, update it instead. If a QBR
   tracking database exists, add the page there and optionally add a table or chart view for the
   trend.
6. Offer a follow-up: leave a note linking back to any open tickets referenced as QBR commitments.
```
