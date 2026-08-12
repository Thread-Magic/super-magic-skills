---
name: Zapier Teams Ticket Notifications
description: Post ticket updates and escalations into Microsoft Teams channels via Zapier — a client's shared channel, the internal escalations channel, or a per-board feed. Use for "notify the Teams channel when this escalates", "post this update to the client's channel", or wiring Teams alerts into a flow.
category: Connectors
tools: [search_tickets, add_ticket_note]
connectors: [Zapier: Microsoft Teams]
scope: single
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Zapier Teams Ticket Notifications

**When to use:** "When ticket <number> escalates, post to the internal escalations channel," or "send the major-incident update to <client>'s shared Teams channel."

**Run it:** on one ticket · or as a Flow (triggered on the state change worth broadcasting, e.g. escalation or P1).

## Prompt

```
Put ticket news where people already look: post updates, escalations, and P1 alerts into Teams
channels (or a direct chat message for a person).

This runs only if the member (or admin) has connected Zapier with a Teams-authenticated account.
Before promising a send, verify the action is enabled for the tenant (see the action-discovery
skill). If Zapier/Teams is absent, say so, point them to connect Zapier, and output the drafted
message for manual posting — do not stop. Each successful Zapier call = 2 Zapier tasks.

1. Identify audience and channel. Internal channel vs client-facing shared channel changes the
   message's entire register — confirm which before drafting.
2. Draft the message: ticket reference, one-line status, what happens next, who owns it.
   Client-facing: plain professional language, no internal jargon, no other clients or tech
   chatter. Internal: include priority, client, and the context a responder needs. No credentials
   or security detail in Teams messages — reference the ticket instead.
3. Show me the message and the named destination channel, and wait for confirmation. Confirm the
   channel every time when it isn't locked; never resolve a channel by name similarity — a client's
   channel gets only that client's information, ever.
4. Post the message to the named Teams channel (or send a chat message to the individual).
5. Leave an internal note (plain text) recording that the notification went out and where.
6. For recurring wiring (a flow that always posts P1s), the admin should pin the exact Teams action
   on a curated Zapier server with the channel field locked — a locked channel makes broadcasting a
   client's incident into another client's channel structurally impossible. Notify on state changes,
   not every note; a chatty flow burns task budget and trains people to ignore the channel.
```
