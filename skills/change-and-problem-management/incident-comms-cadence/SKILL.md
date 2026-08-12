---
name: Incident Comms Cadence
description: Draft internal and client updates on a fixed clock during a major incident from ticket evidence, tracking the next-due time so the cadence never lapses.
category: Change & Problem Management
tools: [search_tickets, add_ticket_note, search_contacts, search_clients]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Faster Resolution & Response]
---

# Incident Comms Cadence

**When to use:** a major incident was declared and updates need drafting on schedule / "draft the next client update / what do we tell them at the top of the hour?" / the comms lead wants a check on whether we're current and when the next update is due / post-incident reconstruction of what was communicated when.

**Run it:** on one incident.

## Prompt

```
Run the update clock set at declaration: who gets updated, at what interval, saying what.
Treat a missed update as an incident-response failure in its own right — in a major, silence
is read as bad news.

1. Load the cadence from the master incident ticket: intervals (default internal 30 min /
   client 60 min; a client's contractual terms override when stricter), audiences, and the
   comms lead who approves sends.

2. WHO SAYS WHAT — two different artifacts, never one message dual-purposed:
   - Internal update (plain-text note on the master ticket, for the response team):
     technical state, workstream progress, hypotheses including uncertain ones, resource
     needs. Candid.
   - Client update (drafted for the comms lead): impact in the client's terms, what's
     being done stated plainly, next update time, and an ETA ONLY if the IC has committed
     one. Follows the outage-notification framing; anything security-flavored follows the
     defensive-writing standard — no "breach," no cause speculation.

3. Draft each update strictly from ticket evidence since the last update. The no-progress
   update is legitimate and has a fixed shape: "still working, here's what we've ruled out,
   next update at <time>." Never invent progress to make an update feel worthwhile.

4. Every client update states when the next one comes — and that promise becomes the new
   deadline. An update that goes out late is still sent, with the honest timestamp; the
   lapse is noted internally, not papered over.

5. Route client-facing drafts to the comms lead for approval and send; confirm the audience
   list against the client's documented incident contacts — updates to
   the wrong contact list are a common majors failure. Record each sent update (time,
   audience, gist) in a note so the comms trail is reconstructable.

6. On stand-down: draft the closure notice (service restored, monitoring continues, RFO to
   follow — see rfo-letter) and record cadence end.

CADENCE CHECK: read the master ticket's comms notes, compute last-sent vs. interval for
each audience, and report: current / due in N minutes / OVERDUE by N minutes, with the next
drafts ready.

Guardrails: the agent drafts and tracks; the comms lead (a human) approves and sends
anything client-facing — no unattended client sends during a major. Never state a cause to
clients before the IC confirms it — early cause statements are almost always wrong and live
forever in inboxes. Never promise an ETA the IC hasn't committed to; "next update at <time>"
is the only promise the drafter may originate. One clock, one owner: if the comms-lead role
is unassigned or ambiguous, flag it to the IC immediately. Internal candor, external
discipline: hypotheses stay internal until confirmed.
```
