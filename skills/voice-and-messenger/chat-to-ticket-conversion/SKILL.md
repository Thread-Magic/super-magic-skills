---
name: Chat-to-Ticket Conversion
description: Capture a live Messenger chat's context into a real ticket with title, description, contact, priority, and steps tried — no repeating for the user.
category: Voice & Messenger
tools: [search_tickets, update_ticket, create_ticket, assign_contact, add_ticket_note, log_time_entry, list_ticket_priorities]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Chat-to-Ticket Conversion

**When to use:** "This chat is a real issue — make it a proper ticket" / a Messenger conversation reveals a problem needing escalation, scheduling, or another team / the chat's quick fix failed and the issue needs to persist past the session / end-of-chat hygiene before handing to the queue.

**Run it:** on the live chat/ticket · or as a Flow that fires when a Messenger chat ticket is created or updated, to structure it for handoff.

## Prompt

```
The moment a chat stops being a quick question and becomes real work, everything said so far
must become ticket structure — issue, environment details, steps already tried — so the next
tech starts where the chat left off, not from zero.

1. Read the entire chat thread. In Thread, a Messenger chat typically already lives on a
   ticket — the job is usually STRUCTURING that ticket, not creating a second one. Open a
   separate ticket only when the chat contains a genuinely distinct second issue or desk
   process requires a different board.

2. Extract from the chat, quoting the user where load-bearing:
   a. The issue as the user described it, plus error messages, device/app names, and when it
      started.
   b. Environment facts surfaced mid-chat (OS, location, "it works on my laptop but not the
      desktop").
   c. STEPS ALREADY TRIED — both what the tech suggested and what the user did, with
      outcomes; this is the part whose loss forces the user to repeat themselves.
   d. Any commitments made in chat ("we'll schedule a tech", "I'll follow up tomorrow") and
      stated urgency/deadlines.

3. Structure the ticket: a searchable title ("<symptom> — <system>", not "chat with
   <user>"), the extracted summary as description, the priority set from stated impact, and
   the correct contact attached if the chat identified someone other than the current record.

4. Leave the structured summary as a plain-text note: issue, environment, steps tried with
   outcomes, current state, next action + owner, commitments. This note is the handoff
   artifact.

5. Offer to log the chat time — chat work is the most under-logged time on most desks.

6. Tell the user in-thread before the chat ends (per Live Chat Etiquette): ticket number,
   what happens next, and that they won't need to re-explain.

7. Output: ticket number, the structured summary, and anything the chat left unresolved or
   ambiguous.

Guardrails: the no-repeat guarantee is the point — if a detail was said in chat, it must be
findable on the ticket; when summarizing, prefer including a marginal detail over dropping
it. Quote, don't diagnose: the description records what the user reported; hypotheses go in
the internal note, clearly labeled. Never mark steps as "tried" unless the chat shows they
were completed. Chats capture credentials disturbingly often; never copy passwords/MFA codes
into fields or notes — "credential shared in chat, advised rotation" is the correct trace.
Duplicate check before opening any new ticket: if an open ticket already covers this issue for
this user, structure and cross-reference instead. Plain-text notes for PSA-synced tickets;
keep the user-facing wrap-up in the chat's language.
```
