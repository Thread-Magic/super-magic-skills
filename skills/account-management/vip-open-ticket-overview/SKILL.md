---
name: VIP Open Ticket Overview
description: Produce a one-page status of every open ticket for a client's named executives, including tickets an assistant filed on their behalf, flagged critical, watch or on track.
category: Account Management
tools: [search_tickets, search_contacts]
connectors: []
scope: global
flow: no
role: [CSM / Account Manager, Service & Ops Manager]
outcome: [Retention & Growth (CSAT/Expansion), Faster Resolution & Response]
---

# VIP Open Ticket Overview

**When to use:** A client's leadership team is the relationship. Before a check-in, or every morning for a high-touch client, you want to see every open ticket for their executives in one view, including the ones an assistant filed under their own name, so nothing an executive is waiting on goes stale.

**Run it:** across one client's VIP contacts, on demand (a daily review has no ticket event, so it is not a Flow). For bumping VIP priority at intake, use `triage-and-routing/vip-priority-handling`.

## Prompt

```
Give me a status overview of open tickets for this client's VIPs. Read-only: change nothing.

Client: <client name>. VIPs: <names>, or "every contact flagged VIP at this client".

1. Resolve the client and each VIP to a contact. Report any VIP you cannot find instead of guessing.

2. For each VIP, find open tickets where they are the contact.

3. Proxy-filed tickets: assistants often submit for an executive under their own name. For each VIP also search this client's open tickets for the VIP's first and last name. Add new matches, marked "proxy". Remove duplicates.

4. Leave out pure monitoring and security alert tickets (agent alerts, alert boards); they are not the executive's request.

5. Read the detail of each remaining ticket and flag it:
- CRITICAL: negative sentiment, past its response or resolution target, unassigned, or top priority.
- WATCH: no update in more than one business day (weekends do not count: last updated Friday flags only if still untouched at the end of Monday).
- ON TRACK: assigned, within target, updated within one business day.

6. Output:
VIP overview - <client> - <date>
Totals: <open> open | <n> critical | <n> watch | <n> on track | <n> proxy-filed
Per VIP: each ticket as "<flag> #<number> <title> | priority | assignee | last updated | sentiment", or "No open tickets".
Needs action today: the critical and watch tickets, each with one suggested next step.

If a search may have capped, say the totals are a minimum. Never invent tickets, dates or sentiment.
```
