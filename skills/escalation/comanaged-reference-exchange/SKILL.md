---
name: Co-Managed Reference Exchange
description: Keep ticket references straight across a co-managed IT boundary — recognize the other side's ticket-number format, preserve foreign references in every summary, draft the reference-exchange reply, and audit both-ways linkage before close.
category: Escalation
tools: [search_tickets, add_ticket_note, update_ticket, search_contacts]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Co-Managed Reference Exchange

**When to use:** A ticket arrives from a co-managed client's internal IT desk carrying their ticket reference; "draft the reply to their helpdesk with our ticket number"; before closing a co-managed ticket ("check we exchanged references both ways"); or summarizing/handing off any co-managed ticket.

**Run it:** on one ticket.

## Prompt

```
In co-managed IT every issue lives twice — once in our PSA, once in the client's
internal system. Treat the other side's ticket number as first-class data so neither
desk ever asks "which ticket is this again?"

1. Recognize the foreign reference. Scan subject and body for the client's
   ticket-number format — common shapes: INC0012345 / REQ-prefixed (ServiceNow-style),
   <PREFIX>-1234 (Jira-style), #12345, "Case 00123456". If the tenant's KB documents each
   co-managed client's format, match against that; otherwise infer from the pattern and
   say which pattern you matched.

2. Preserve it: record the foreign reference in a plain-text note in a fixed, searchable
   form — `External ref (<client> helpdesk): <REF>` — and, where the tenant uses a custom
   field for it, set that field. From here on, EVERY summary, handoff card, escalation
   note, and status update must carry both references (ours and theirs).

3. Draft — never auto-send — the reference-exchange reply to the client's helpdesk:
   acknowledge receipt, quote THEIR reference back to them, give them OUR ticket number
   for their records, and state current status and next step. Match their formality;
   plain text. Show the draft to the technician for sending.

4. During the ticket's life, when relaying updates in either direction, translate
   references correctly: their number when writing to them, ours internally, both in
   summaries. Never swap or conflate the two.

5. Both-ways audit before close: confirm (a) their reference is recorded on our ticket,
   and (b) the thread shows our reference was actually communicated to their desk — not
   just drafted. If either leg is missing, flag it and draft the missing communication
   before the ticket closes.

6. If multiple foreign references appear on one thread (their desk split or re-filed),
   record all of them with dates and note which is current.

7. End with: both references side by side, exchange status (both-ways complete / missing
   leg + the drafted fix), and where the foreign reference is stored.

Guardrails: never auto-send the exchange reply — the technician sends it; drafts are
clearly labeled drafts. Never invent, "correct," or reformat the other side's ticket
number; quote it exactly as received. If two candidate references appear, ask rather
than pick. A co-managed ticket should not close with a one-legged exchange — surface it,
but the close decision stays with the technician. Reference-format inference is stated as
inference, never as confirmed knowledge of the client's system. All notes plain text;
keep the foreign reference in the fixed searchable form.
```
