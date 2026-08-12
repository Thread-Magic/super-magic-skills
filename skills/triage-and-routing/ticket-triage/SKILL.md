---
name: Ticket Triage
description: Classify a new or unassigned ticket, gauge severity, catch duplicates, and route it to the right board, status, and priority.
category: Triage & Routing
tools: [search_tickets, list_boards, list_ticket_statuses, list_ticket_priorities, search_clients, update_ticket]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Ticket Triage

**When to use:** A new or unassigned ticket needs classifying and routing — a first pass before dispatch, or a morning sweep of the unassigned intake board.

**Run it:** on one ticket · across all new/unassigned tickets on a board · or as a Flow that triages every ticket the moment it's created.

## Prompt

```
Triage this ticket — or, if I point you at a board or filter, each new or unassigned ticket
in that set. Read the full history first, including the first message and every reply; don't
judge from the subject alone (titles are often stale or auto-generated). For each ticket:

- Classify the issue from the body of the request (access, hardware, software, network,
  email, security, etc.) — not from keywords in the subject.
- Gauge severity: anything security-related (compromise, phishing, malware, unexpected MFA or
  login activity) or affecting multiple users or a whole site is high priority by default.
  A calm tone doesn't lower it — only the requester explicitly de-escalating, confirmed with
  the tech, does.
- Check for a duplicate of an existing open ticket using strong signals (same alert ID,
  device, monitoring reference, or same contact + same specific error in a recent window),
  never wording alone. Note suspected duplicates with their ticket numbers.
- Set the right board, status, and priority, and leave a one-line internal note on what you
  changed and why. If the board/status/priority names are unclear for this client, look them
  up rather than guessing.

Show me your recommendation first and apply it once I confirm. Running in a Flow, apply it
directly and note what you set. When you're not confident where a ticket belongs, say so and
leave it for a human rather than guessing. Never invent ticket numbers, clients, or categories.
```
