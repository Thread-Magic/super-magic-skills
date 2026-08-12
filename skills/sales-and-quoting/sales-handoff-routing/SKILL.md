---
name: Sales Handoff Routing
description: Move a service ticket that turns out to be a sales conversation, a purchase, renewal, expansion, or pricing question, to the sales board and account owner.
category: Sales & Quoting
tools: [search_tickets, update_ticket, add_ticket_note, list_boards, search_members]
connectors: [Zapier: Microsoft Outlook]
scope: single
flow: no
role: [Sales & Business Development]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Sales Handoff Routing

**When to use:** "This 'support' ticket is actually asking to buy licenses — route it"; "client asked about renewing/upgrading in the middle of a ticket — hand off to sales"; or "move this to the sales board and loop in the account owner."

**Run it:** on the ticket that's really a sales conversation — run it manually (not a Flow; board moves and owner emails need a human confirm).

## Prompt

```
You are recognizing the ticket that is really a sales conversation, moving it where sales
works, putting the account owner on it, and handing over a summary so the client never has
to repeat themselves.

1. Read the full thread and confirm the sales nature: an explicit
   purchase/renewal/expansion/pricing request, not a support issue with a purchase
   side-mention. Mixed tickets: if a live support issue remains, keep this ticket for
   support and flag the sales portion separately (or split) — never strand an unresolved
   technical problem on a sales board.

2. Identify the destination: the sales/opportunities board, and the account owner (from the
   desk's account-assignment convention or the requester). If either is ambiguous, ask — a
   misrouted sales lead dies quietly.

3. Write the handoff summary as a plain-text internal note: who is asking (contact + role),
   what they want (quote their actual words), context from the thread (environment facts,
   quantities, urgency/renewal dates mentioned), current commitments already made to the
   client in the thread (verbatim — sales must know what support already said), and
   suggested next step.

4. With the requester's confirmation, move the ticket to the sales board, assign the account
   owner, and set the desk's sales-intake status if one exists.

5. Draft the heads-up email to the account owner (as a draft in Outlook if connected, else
   as text in chat): two paragraphs — the ask and the context, reference to the ticket, any
   time sensitivity. Draft only; the requester sends it.

6. Confirm back: what moved where, who owns it, and what (if anything) was said to the
   client. If the client is waiting on an acknowledgment, remind the requester that someone
   should tell the client the right person will follow up — this skill does not message the
   client.

Guardrails: confidence gate — reroute only when the sales intent is explicit in the client's
own words; a support issue with a hint of interest stays in support (flag it via Tickets to
Opportunities instead), and an ambiguous or mixed ticket gets no move at all. Never promise
the client pricing, timelines, or that "sales will call today" — no client-facing writes at
all. Never state what the current agreement covers as fact without agreement evidence — put
the question in the handoff summary. Preserve the trail: board moves and assignment happen
only after requester confirmation; the summary note goes on BEFORE the move so it travels
with the ticket. No sales board configured → assign the account owner and label per
convention; no Outlook connector → email draft delivered as text.
```
