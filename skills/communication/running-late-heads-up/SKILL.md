---
name: Running Late Heads-Up
description: When a technician says they are running behind, find their next firm appointment and send that client a short heads-up note with the delay, in one step.
category: Communication
tools: [list_schedule_entries, search_tickets, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Retention & Growth (CSAT/Expansion), Faster Resolution & Response]
---

# Running Late Heads-Up

**When to use:** You are in the field or stuck on a call and about to miss your next appointment. You type "running 20 late" and want the client told before they start wondering, without opening the schedule, finding the ticket and writing the note yourself.

**Run it:** on one ticket, by hand (it starts from you, not from a ticket event). Save it under a short name so it is one word to run from your phone.

## Prompt

```
I am running late. Tell my next client.

1. Take the delay in minutes from my message. If I did not give one, ask: "How many minutes behind are you?"

2. Find my schedule from now through the end of today. Pick the soonest firm appointment that has not been marked done. If there is none today, say so and stop. If two start within 15 minutes of each other, ask me which one.

3. Open that appointment's ticket and get the contact's first name.

4. Show me what you are about to send, then add a client-visible note on that ticket:
"Hi <first name>, just a heads up: I am running about <minutes> minutes behind and will be with you shortly. Sorry for the delay, and thanks for your patience!
<my name>"
No first name on file: start with "Hi there,".

5. Do not email it separately unless I ask, and do not move or change the appointment.

6. Confirm: the ticket number, the contact, and the appointment time you warned them about.

If my delay pushes past the end of the appointment window, say so and suggest I reschedule instead. Never invent a client, ticket or time.
```
