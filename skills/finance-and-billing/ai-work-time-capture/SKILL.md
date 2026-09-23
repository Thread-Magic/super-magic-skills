---
name: AI Work Time Capture
description: When a ticket completes, log a time entry for the support work your AI agent demonstrably performed, backed by evidence in the thread, and assign the AI member as primary resource on zero-touch tickets.
category: Finance & Billing
tools: [search_tickets, log_time_entry, update_ticket]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# AI Work Time Capture

**When to use:** Your triage agent resolves or advances tickets, but because no human logs time, that work is invisible in PSA reports, agreement burn-down and client reviews. You want an evidence-based time entry under a dedicated AI member, never an inflated default.

**Run it:** on one ticket · or as a Flow (when a ticket's status changes to your completed status on the support boards). Create a PSA member for your AI agent first and put its name in the prompt.

## Prompt

```
Log the time our AI agent actually spent on this ticket, and only that. The AI member is <AI member name>. Work type: <your work type, e.g. Dispatch>.

1. Verify AI involvement first; stop if either check fails, with no time entry.
- The ticket has an AI triage agent session.
- The thread contains messages written by the AI agent.

2. Work out time actually spent. Count only active support work by the AI agent: reviewing the request, asking and reading diagnostic questions, gathering information, troubleshooting, running a workflow, giving a resolution, or preparing a technician handoff.
Do not count: retitling, categorising, priority changes, recaps, reminder or follow-up nudges, other automated field updates, time spent waiting, or any technician work after the AI handed off.
Evidence: every action you list must trace to an AI-authored message in the thread or a confirmed step in the triage session. Never infer actions from the ticket summary, the customer's message or a technician's notes, and never credit work a technician describes.
Estimate conservatively, per action. No default times, no rounding up. If the total is under 2 minutes, or the evidence is thin, log nothing.

3. Log one time entry, internal, against the AI member and work type above:
"Assisted support performed by <AI member name>
Actions performed:
- <action> : ~<X> min
Total time logged: <X> minutes"
Do not add a separate ticket note.

4. Zero-touch assignment. The ticket is zero-touch if no human member wrote a technician note and no human member logged time (the AI member's own notes and entries, and API-posted notes, do not count as human). If it is zero-touch AND nobody is assigned, make the AI member the primary resource. If anyone is already assigned, leave it exactly as it is.

Never log time twice: if a time entry from the AI member already exists on this ticket, stop. Never change status, priority, board or billing settings. Never invent an action or a duration.

As a Flow: reply with one line only: "Logged <X> min" or "No time logged: <reason>", plus "Assigned AI as primary resource" when step 4 applied.
```
