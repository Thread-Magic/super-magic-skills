---
name: Live Chat Etiquette
description: House rules for working a live Messenger chat — response cadence, holding messages, handoff phrasing, and ending the chat cleanly for the desk playbook.
category: Voice & Messenger
tools: [search_tickets, search_knowledge_base, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Live Chat Etiquette

**When to use:** "Draft my next reply in this Messenger chat" / "write a holding message — I need 10 minutes" / "how do I hand this chat to <team> without making the user re-explain?" / "write our chat etiquette playbook for new techs."

**Run it:** on the live chat you're working — run it manually as you draft (not a Flow; it assists a person mid-conversation).

## Prompt

```
Chat is a different contract than email: the client is sitting there watching the typing
indicator. Draft chat messages and coach chat conduct against the cadence, holding, handoff,
and closing rules that keep live conversations from going quiet or going wrong.

1. Read the live thread (or the pasted chat) — cadence rules depend on how long the client
   has already been waiting and what was last promised.

2. Apply the cadence contract:
   - Acknowledge within the desk's first-touch window even without an answer — "looking at
     this now" beats a perfect reply five minutes later.
   - Never go silent longer than the interval you last set. Every quiet stretch needs a
     holding message BEFORE it starts, with a duration: "I need about 10 minutes to check the
     server — I'll message you by 2:15."
   - When a promised check-in time arrives and you're not done, check in anyway with the new
     estimate. Re-promising is fine; ghosting is not.

3. Draft in chat register: short lines, one question at a time, no email formalities
   ("Dear...", signature blocks), no walls of text — split anything long into sequential
   messages. Mirror the client's formality; stay on the professional side of it.

4. Holding messages state three things: what you're doing, how long, and what they can do
   meanwhile (nothing is a valid answer — "no action needed on your side").

5. Handoffs: never make the user repeat themselves. Before transferring, post the one-line
   context summary INTO the thread ("Handing you to <team>: they'll see that your VPN drops
   every ~10 min since Monday's update"). The receiving tech opens with confirmation of that
   context, not "how can I help?". If the handoff means a wait, say how long and offer the
   async fallback.

6. Ending cleanly: confirm the outcome in one line, state what happens next (ticket number,
   follow-up time, or "this is resolved — reopen by replying here"), and let the client close
   last where practice allows. A chat that became real work exits through Chat-to-Ticket
   Conversion, and the client is told the ticket number before the chat ends.

7. For playbook requests: assemble the rules above into a desk-specific one-pager, pulling
   existing standards from the knowledge base so the output extends rather than contradicts
   current policy.

Guardrails: never promise a response interval the desk can't keep — a cadence rule broken
daily trains clients to distrust the channel. No troubleshooting steps with destructive
potential over chat without the same confirmation you'd require by email — speed is not
consent. Chat is still the record: everything lands on the ticket thread; no "off the record"
guidance. Don't simulate typing-status or presence claims you can't see; base cadence
judgments on message timestamps only. If the in-app draft view isn't available (running from
outside the app), output the drafted message text for the member to paste. Avoid idioms; many
desks run chats in the client's language — draft in the thread's language.
```
