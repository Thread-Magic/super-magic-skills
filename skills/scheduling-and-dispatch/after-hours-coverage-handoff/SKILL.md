---
name: After-Hours Coverage Handoff
description: Build the end-of-business handoff to on-call or after-hours coverage — open urgent work, expected client callbacks, and site notes the night crew needs.
category: Scheduling & Dispatch
tools: [search_tickets, search_members, list_ticket_priorities, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Always-On Coverage]
---

# After-Hours Coverage Handoff

**When to use:** "Build the handoff for tonight's on-call" / "end-of-day handoff"; a lead closing the desk wants what the overnight NOC or answering-service escalation path needs; or a day tech going offline mid-incident needs to hand a hot ticket to coverage.

**Run it:** across the desk's open urgent tickets at end of business — a manual handoff sweep, not a Flow.

## Prompt

```
You are building a clean shift boundary: everything the on-call tech or after-hours desk
must know, in one brief — so nothing urgent depends on the day shift's memory.

1. Establish the boundary: end-of-business time in the desk's timezone, and who is
   receiving (look up the on-call tech, or the after-hours team). If the on-call target
   isn't stated and no rotation is on record, ask — never guess who is on call.

2. Open urgent work. Search for open Critical/High tickets (one search per board —
   result caps apply): current state, last action taken, next expected step, whether the
   client is waiting on us. Anything actively being worked at the boundary gets a per-ticket
   mini-brief.

3. Expected callbacks. Tickets where a client or vendor said they'd call back tonight,
   scheduled after-hours work (maintenance windows, patch nights), and any promise the day
   shift made with a tonight deadline.

4. Site notes. Per client involved above: access constraints, named-contact-only rules,
   alarm/escort requirements, VIP handling, standing warnings on record. Only what is
   documented or stated — no invented site lore.

5. Compose the brief in three sections in that order, each item with ticket number, client,
   one-line state, and the "if X happens, do Y" instruction where the day shift knows it.

6. Post the brief where the desk's handoff lives: as plain-text notes on the affected
   tickets (each ticket gets its own relevant slice, not the whole brief), and output the
   full brief for the lead to deliver to the on-call channel.

7. Flag gaps explicitly: "Ticket <n> has no next-step documented — day owner should brief
   verbally before leaving."

Guardrails: never guess the on-call recipient; a handoff sent to the wrong person is worse
than none. No fabrication: next steps and site notes come from the ticket record or the
lead's own statements — unknown → say "unknown". Per-ticket notes carry only that ticket's
slice; don't leak other clients' details (plain text, PSA-safe). Include credentials by
reference only ("credentials in the documentation system under <client>") — never paste
secrets. Result-cap honesty: if the urgent-work sweep may have capped, say the list may be
incomplete and name the boards checked. This hands off; it does not reassign tickets to the
on-call tech unless the desk's process says to — ask first.
```
