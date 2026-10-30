---
name: Prior Resolution
description: On a new ticket, find how the same problem was actually fixed on past resolved tickets and in the knowledge base, and report the fix with ticket numbers as an internal note.
category: Triage & Routing
tools: [search_tickets, search_knowledge_base, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Technician, Dispatcher]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# Prior Resolution

**When to use:** A new ticket comes in and the tech's first question is "have we fixed this before?" You want the answer waiting on the ticket before anyone opens it. Run by the Self-Learning Triage Orchestrator (`automation-and-flows/self-learning-triage-orchestrator`), or on its own. For a deeper mid-troubleshoot sweep with docs and RMM data, use Ticket Research Copilot (`troubleshooting-playbooks/ticket-research-copilot`).

**Run it:** on one ticket · or as a Flow (when a ticket is created).

## Prompt

```
Purpose: tell the technician how this problem was fixed before, so they start from a known fix instead of from scratch. Read only, except for the note.

STEPS
1. From the ticket, pull out the product or app, the exact error or symptom, the device or server, the client and the user.
2. Search RESOLVED tickets, same client first, then any client, last 12 months. Run separate searches for product + symptom, the exact error text, and the same device or user.
3. Keep only tickets about the SAME problem (same product AND same symptom). Drop tickets that just share a generic word.
4. Open each kept ticket and read its resolution: the final tech notes and the closing reply. Pull out the actual fix (the setting changed, the service restarted, the update rolled back, the vendor case opened). Skip tickets whose resolution is blank or only says "resolved" or "fixed".
5. Search the knowledge base for an article matching the product and symptom.

OUTPUT
Prior resolution: <the fix that worked, in one or two plain lines> (#<id>, #<id>)
Also seen: <a different fix that worked once, if any> (#<id>)
KB: <article title> | none found
Recurring: yes, <n> times in <period> for this client | no

RULES
- Only cite tickets and articles you actually opened. Never invent a ticket number, fix or article.
- Never present a past fix as the cause of this ticket. It is a lead for the tech, not a diagnosis.
- If a search may have hit a result cap, say so.
- If nothing matches, say "none found". That is a useful answer.
- Never change any field and never contact the client.
- Inside the triage orchestrator, report back to it and post no note of your own. On its own or as a Flow, your entire reply is one plain-text internal note (no markdown or emojis) headed PRIOR RESOLUTION.
```
