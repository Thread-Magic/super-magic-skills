---
name: Client Reply
description: Draft an external client reply in your house voice and format — resolution updates, status notes, closing messages, or any client-facing email on a ticket.
category: Communication
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Client Reply

**When to use:** "Draft a reply to the client on this ticket" / "tell <user> their account is unlocked" / "let them know we're still working with the vendor" — any client-facing email where tone, format, and accuracy matter.

**Run it:** on one ticket.

## Prompt

```
Draft a client-facing reply for this ticket, on-brand and ready for a human to send.

1. Read the FULL ticket thread first — every prior message, note, and status change. Never draft
   from the latest message alone.

2. Draft the reply leading with the answer or current state, then the supporting detail.
   Apply our house voice:
   - Greet the client by first name on the FIRST message of a thread only; skip the greeting
     on later replies in the same thread.
   - No filler openers ("I hope this email finds you well", "Just reaching out"). Start with
     substance.
   - No technical jargon unless the client used the term first; gloss any unavoidable term.
   - 1-2 short paragraphs. If it needs more, it probably needs a call.
   - Answer first, then detail; who does what next and by when.

3. If the member has a preferred/banned word list configured, apply it: replace banned words
   with their substitutes, prefer listed alternatives.

4. If this is a close-out reply, end the body with: "If anything isn't resolved, just reply
   to this email — replying reopens this ticket."

5. Signature: if the workspace applies a managed signature automatically, end after the last
   body sentence — do NOT add a sign-off that would double up. Only add one when no managed
   signature exists.

6. Show me the reply as an open draft for review, labeled "DRAFT — review before sending."
   Do NOT send.

Content honesty: never invent details — no made-up timestamps, steps taken, ticket numbers,
links, or promises. If the thread doesn't establish a fact, leave it out or mark it
<confirm with tech>. Never expose internal notes, credentials, pricing, or other clients'
details. Keep it a draft until a human approves it — never send autonomously. If the thread
is in another language, draft in that language. Offer a plain-text internal note only if the
member wants a record.
```
