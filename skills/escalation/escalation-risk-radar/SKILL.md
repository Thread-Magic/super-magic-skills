---
name: Escalation Risk Radar
description: Scan open tickets for the early signs of a blow-up — negative sentiment, an SLA deadline closing in, and threads that have gone quiet — score and rank them, so a senior tech can step in before a client escalates.
category: Escalation
tools: [search_tickets, search_clients, add_ticket_note, update_ticket]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager, Dispatcher]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Escalation Risk Radar

**When to use:** A lead wants to get ahead of escalations — "which open tickets are about to blow up?", a mid-shift pulse on a busy queue, or a CSM checking a specific client's open work before a call.

**Run it:** across all open tickets · or scoped to one client, board, or assignee.

## Prompt

```
Scan open tickets for the early warning signs of an escalation, score each risky one, and hand
back a ranked list so a senior tech can intervene before a client blows up.

1. Set scope: all open tickets, or narrowed to a client, board, or assignee if I say so. If I scope
   to a client, resolve that client first, then search their open tickets. Search per board when
   scanning widely, and say so if a search may have capped — never imply full coverage when results
   were limited.

2. For each open ticket, read the latest activity and flag these risk signals:
   - Negative sentiment: the client sounds frustrated, angry, or is threatening to leave.
   - Stalled: no update in 3+ days (rising risk the longer it's been silent).
   - SLA pressure: the respond or resolve deadline is close (within a few hours) or already breached.
   Judge sentiment and staleness from the actual messages and timestamps, not the title.

3. Score each flagged ticket so the worst rise to the top. Weight the signals roughly:
   - Very negative sentiment: high. Negative sentiment: medium.
   - SLA breached or breaching within a few hours: high.
   - Stalled 5+ days: medium. Stalled 3-5 days: low.
   Signals stack — a stalled, breaching, angry ticket should score far above a merely quiet one.

4. Rank the flagged tickets highest-risk first and group into tiers: Critical, High, and Watch.
   For each, show the ticket number, client, assignee, which signals fired, the score/tier, and how
   long since the last update.

5. For each Critical ticket, recommend one concrete next step — reassign to a senior tech, post a
   client update now, or push on the SLA — and offer to leave a plain-text internal note flagging
   it for follow-up. Only write notes or reassign on my go-ahead; this is a read-and-report sweep by
   default. Notes bound for the PSA are plain text — no markdown, no emojis.

Report only what the data supports — don't inflate a quiet ticket into a crisis, and don't invent
sentiment the messages don't show. If nothing is at risk, say so plainly.
```
