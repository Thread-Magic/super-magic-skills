---
name: Outage Notification
description: Draft a major-incident or mass-outage client notice — known impact, what we're doing, when the next update comes — without speculating on cause.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Retention & Growth (CSAT/Expansion)]
---

# Outage Notification

**When to use:** "Draft an outage notification for <service> being down" / "notify all affected clients about this incident" — a major incident ticket needs its first client-facing notice or an interim update.

**Run it:** on one incident ticket.

## Prompt

```
Draft the message clients get during an active outage: calm, factual, and specific about the
one thing that stops them flooding the desk — when they'll hear from you next.

1. Gather the confirmed facts from the incident ticket(s): what service/system is affected,
   since when, who/what is impacted, and what the team is actively doing. Confirmed means stated
   in the record — not inferred.

2. Draft in this order:
   - Known impact: what's affected and what still works, in the client's terms ("email
     delivery is delayed" not "the SMTP relay is degraded").
   - What we're doing: the active response, one or two sentences ("our team is engaged and
     working with the vendor").
   - Next update time: a specific commitment — "we will send the next update by <time>, or
     sooner if the situation changes." This line is mandatory.
   - What the client should do meanwhile, if anything (usually: nothing, no need to open a
     ticket).

3. Keep it short — during an outage, clients read the first three lines. For interim updates,
   lead with what changed since the last notice; for the all-clear, state restoration, confirm
   stability, and note a post-incident summary will follow if one is planned.

4. Show me the draft for review, labeled "OUTAGE NOTICE DRAFT." Mass distribution is a human
   action — provide the text, never the send.

Never speculate on cause: no "likely a cyber attack," no "appears to be <vendor>'s fault," no
unconfirmed root cause. "We are investigating the cause" is the only pre-confirmation phrasing.
Never use "breach," "hacked," or "compromised" unless a confirmed security incident is formally
declared (then the security team's language governs). The next-update time is a real commitment
— pick one the team will keep, and err generous. Never name other affected clients or reveal
the blast radius across your client base.
```
