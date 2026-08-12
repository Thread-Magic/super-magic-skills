---
name: Zapier Slack Escalation Ping
description: Ping the right engineer in Slack — DM or channel — with a one-line brief and ticket link when a ticket needs eyes now, with anti-nag dedupe.
category: Connectors
tools: [search_tickets, search_members, add_ticket_note]
connectors: [Zapier: Slack]
scope: single
flow: no
role: [Technician, Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Zapier Slack Escalation Ping

**When to use:** "Ping <member> — ticket <number> needs a senior look before the SLA blows," or "drop this in the escalations channel with the link."

**Run it:** on one ticket.

## Prompt

```
The fastest honest interrupt: one Slack message — a DM, or a message to the desk's escalation
channel — carrying exactly what the recipient needs to decide in five seconds — what, how urgent,
which ticket — with a dedupe discipline so Slack doesn't become the boy who cried breach.

This runs only if the member has connected Zapier with Slack. If it's absent, degrade by outputting
the composed one-liner for the member to send, and still note the escalation attempt on the ticket
— do not stop. Each Zapier call = 2 Zapier tasks (one ping = one call; the dedupe check is a ticket
read, not a Slack search).

1. Resolve the recipient deliberately: the ticket owner, the designated escalation contact, or
   whoever the member names — via the tenant's escalation policy. For on-call rotation, PagerDuty
   owns the truth; don't guess who's on call from Slack presence.
2. Anti-nag dedupe: check the ticket's notes for a prior escalation ping about the same condition.
   Already pinged and nothing material has changed → do not ping again; report that a ping is
   outstanding and since when. Re-ping only when the member explicitly asks or the situation has
   genuinely escalated (new severity, new deadline) — and say what changed.
3. Compose the one-liner: severity/urgency, one-sentence issue, client-safe identifier, ticket
   number and link, and the specific ask ("needs owner in 30 min", "approve the change"). One
   message, no essay — the ticket holds the detail. The ask must be decidable from the message
   alone. Never inflate severity to get attention; no client personal data or credentials.
4. Show me recipient + message, wait for confirmation, then send it in Slack. DM for a named
   individual; the escalation channel when the ask is "someone claim this".
5. Leave a note (plain text): who was pinged, where, when, and the ask — this note is what the
   dedupe step reads next time. If the ping demands a response and none arrives in the stated
   window, surface that to the member — not a license to auto-ping hourly.
```
