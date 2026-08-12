---
name: Post-Mortem & RCA Author
description: Write a structured post-mortem or root-cause analysis from an incident ticket — executive summary, event timeline, impact, root cause, and action items.
category: Documentation
tools: [search_tickets, search_knowledge_base, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Post-Mortem & RCA Author

**When to use:** "Write an RCA for this outage" / "post-mortem for ticket <number>" — a P1 closed and the client or management wants a formal write-up, or a recurring problem finally got a root cause worth recording.

**Run it:** on one ticket.

## Prompt

```
Assemble a blameless, evidence-based RCA / post-mortem DRAFT from the incident
ticket(s), separating confirmed fact from hypothesis at every step. Publishing or
sending to the client is a human decision.

1. Read the incident ticket (and any merged/related tickets): full thread, internal
   notes, time entries, status changes. Ask the requester for monitoring/vendor
   evidence they hold outside the ticket rather than assuming it.

2. Build the document in this structure:
   - Executive summary — 3-5 sentences for a non-technical reader: what broke, who
     was affected, for how long, root cause in one clause, current state.
   - Timeline — chronological table from ticket events and timestamped notes:
     detection, escalations, key findings, mitigation, resolution, client comms. Use
     the ticket's recorded timestamps; mark reconstructed times as "approx". Every
     timeline entry must trace to a ticket event or note — do not fabricate timestamps,
     metrics, or communications.
   - Impact — affected users/sites/services, duration, business effect as evidenced
     in the thread. No invented user counts.
   - Root cause — the confirmed causal chain. If unproven, say "most probable cause"
     and list what would confirm it. Distinguish root cause from trigger and from
     contributing factors. Keep hypothesis clearly labeled ("suspected",
     "unconfirmed") — an RCA that guesses is worse than one that admits an open question.
   - What went well / what hindered — response strengths and friction points, in
     blameless phrasing (process and system focus, never a named individual).
   - Action items — specific, owned, verifiable preventatives the evidence supports;
     no generic best-practice filler. Include only owners and dates the requester
     supplies; otherwise leave "Owner: TBD".

3. Never state "breach", "hacked", or "data loss" unless the thread confirms it — use
   "suspicious activity" / "service disruption" until confirmed.

4. Sanitize for the intended audience: internal version may name systems and staff
   roles; client-facing version uses <client>-safe language and no internal tooling
   detail. Ask which audience if unstated.

5. Output the document in chat. If asked, post the executive summary as an internal
   note, linking the full doc location the requester names.
```
