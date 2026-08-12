---
name: Expectation-Setting Acknowledgment
description: Draft the first-touch acknowledgment on a new ticket — what we understood, how seriously we're treating it, next steps, and when the client hears back.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Retention & Growth (CSAT/Expansion)]
---

# Expectation-Setting Acknowledgment

**When to use:** "Acknowledge this new ticket for the client" — a fresh ticket needs a first response that's more than an auto-reply and proves the request was actually read.

**Run it:** on one ticket · or as a Flow (triggered when a ticket is created).

## Prompt

```
Draft the first human message on a ticket: proves the request was read, sets the working
expectation, and buys the desk room to work without the client chasing.

1. Read the client's full request. The acknowledgment must demonstrate comprehension — a
   generic "we received your request" is what the auto-responder already sent.

2. Draft with four beats:
   - What we understood: a one-sentence restatement of their issue in their terms ("you're
     unable to open shared files since this morning, and it's affecting your whole team"). This
     beat builds trust — get it right.
   - How we're treating it: the working severity in client terms ("we're treating this as a
     priority") — reflecting the ticket's ACTUAL priority, never overstating urgency to please.
   - What happens next: the immediate next step and who's on it ("a technician is picking this
     up to <first action>").
   - When you'll hear from us: a specific UPDATE commitment ("you'll have an update from us by
     <time>") that fits the desk's real response norms — the line that stops the "any update?"
     email.

3. If anything in the request is ambiguous and blocks work, fold the clarifying question into
   the acknowledgment — one email, not two. If the request is too vague to restate, lead with
   the clarifying question instead of a guessed summary.

4. Keep it to one short paragraph plus the update-time line.

5. Show me the draft for review, labeled "DRAFT."

Never promise a RESOLUTION time at first touch — commit to an update time only. "Fixed by
Friday" at intake is a guess wearing a promise's clothes. Severity language must match the
ticket's real priority; if the client's expectation and the assigned priority clash, flag it to
me rather than papering over it. The update-time commitment must be one the desk will keep —
align with SLA/board norms, and ask me if unsure. If running unattended as a Flow: output only
the acknowledgment body; derive the update-time from the board's configured expectation only,
and if none is available end with "we'll follow up shortly" rather than inventing a deadline;
if the request text is empty or auto-generated noise, output nothing.
```
