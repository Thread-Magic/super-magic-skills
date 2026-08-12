---
name: Silent Ticket Detector
description: Find tickets where the client replied but no technician responded within threshold — surface each with wait time, @mention the tech, and draft a reply.
category: QA & Closure
tools: [search_tickets, search_members, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Silent Ticket Detector

**When to use:** "Any tickets where the client is waiting on us?" / "who's been left on read?" — a dispatcher's mid-day sweep, a lead measuring response discipline, or embedded in a Flow on a timer or customer-responded status.

**Run it:** on one ticket · across all open tickets · or as a Flow (when a ticket flips to a customer-responded status).

## Prompt

```
The inverse of the stale-ticket problem: the client did their part and the desk went quiet.
Detect inbound messages sitting unanswered past the threshold, nudge the owner, and offer to
draft the overdue reply.

1. Confirm the silence threshold: the desk's response-time promise per priority where stated,
   otherwise a default of 4 business hours.

2. Find candidates: open tickets whose most recent client-visible message is inbound (from the
   client) and older than the threshold, with no outbound client-visible reply after it. Include
   tickets flipped to a customer-responded status that nobody picked up. Split searches per board;
   disclose result caps — the silent ticket you miss is the one that churns the client.

3. Filter false positives by reading each thread: an inbound "thanks, that fixed it" is a closure
   signal, not an unanswered question; an inbound message answered by phone counts as answered
   only if a note documents the call. Automated inbound (alerts, bounce-backs) is out of scope.

4. Rank by client wait time, weighted by priority and visible frustration in the message.

5. For each silent ticket, leave an internal plain-text note @mentioning the assigned tech —
   look them up to resolve the mention — with: hours the client has been waiting, one-line gist of
   what the client asked, and "reply needed." If unassigned, flag for dispatch instead of
   mentioning nobody. @mention notes state facts, never blame language.

6. Offer to draft the response for any ticket the user picks: a short client-facing reply
   addressing the client's actual last message (acknowledge, answer or honest ETA, next step).
   Present the draft; the user sends or posts it — never auto-send client-facing replies in
   attended mode.

7. Output: ranked table (ticket, client, assigned tech, hours silent, gist of the pending
   question), notes posted, drafts offered.

If evidence of an off-thread response may exist (e.g. a schedule entry created right after the
inbound), flag as PROBABLY HANDLED, UNDOCUMENTED rather than silent — and suggest documenting it.

Running as a Flow: the trigger is a timer sweep, or customer-responded status older than the
threshold. Your entire reply is the internal note posted verbatim: "@<assigned tech> - client
reply from <date/time> has waited <N> business hours. Pending: <one-line gist>. Reply needed."
Plain text, no markdown, nothing else. Never post client-facing content unattended — the nudge is
internal only; drafting the client reply is attended work. Post only when the last client-visible
message is inbound, older than threshold, with no outbound reply after it and no documenting note.
If any doubt (possible phone handling, automated sender, ambiguous thread), do nothing and stop.
Don't re-post if an identical nudge for the same inbound message already exists.
```
