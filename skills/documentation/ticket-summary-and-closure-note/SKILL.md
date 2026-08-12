---
name: Ticket Summary & Closure Note
description: Produce a clean ticket summary as a resolution note, closure note, or templated P1/P2 handoff — in the requested format and point of view.
category: Documentation
tools: [search_tickets, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Ticket Summary & Closure Note

**When to use:** "Write a closure note for this ticket" / "give me a resolution note in our standard format" / "summarize this in first person for my PSA note" — or a P1/P2 being handed to another tech or after-hours team that needs a structured handoff.

**Run it:** on one ticket.

## Prompt

```
Summarize a ticket thread into the exact note the situation calls for.

1. Read the full thread: replies, internal notes, time entries. Establish problem ->
   actions taken -> outcome -> anything outstanding.

2. Pick the format the request calls for:
   - Resolution / closure note — Problem, Actions Taken, Outcome, and (only if work
     remains) one clear Next Step with owner and deadline.
   - P1/P2 handoff summary — fixed template: Current Status; Impact (who/what is
     down); Timeline of key events with timestamps; Actions Taken So Far; What Has
     Been Ruled Out; Next Action + Owner; Client Communication State (who was told
     what, when).
   - Plain recap — short prose for a client-visible closure message.

3. Apply the requested point of view: default third person, or first-person
   technician POV ("I reset the profile and verified login") when asked — write as
   the assigned technician, not as an AI. First-person changes voice only; never add
   work the technician did not record.

4. If the note will sync to a PSA, use PLAIN TEXT only: no markdown, no emojis, no
   smart quotes, no em-dashes. Follow the requested format precisely, including "no
   bullet points" or word limits when specified.

5. In handoff summaries, separate fact from hypothesis explicitly ("Confirmed:" vs
   "Suspected:"). Do not invent detail the thread does not support — no fabricated
   confirmations, timestamps, or root causes. If the outcome is unclear, say
   "outcome not confirmed in thread" rather than asserting resolution. Never include
   credentials or one-time codes found in the thread in any summary.

6. Output the note in chat for review. Only post it as a ticket note when explicitly
   asked, and post handoff/QA summaries as INTERNAL notes unless told otherwise.
```
