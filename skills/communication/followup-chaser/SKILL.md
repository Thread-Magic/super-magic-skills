---
name: Follow-up Chaser
description: Draft a polite, escalating follow-up when a client hasn't replied on a ticket — first nudge, second nudge, or final pre-closure attempt, tone matched to the attempt number.
category: Communication
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Follow-up Chaser

**When to use:** "The client hasn't responded — draft a follow-up" / "second follow-up on this ticket" / working a stale-ticket queue where each waiting-on-client ticket needs its next chase.

**Run it:** on one ticket · across a waiting-on-client queue · or as a Flow (triggered on a ticket waiting on the client).

## Prompt

```
Draft the next follow-up for a ticket waiting on the client, with tone matched to how many
attempts have already been made. If I point you at a queue, do this for each waiting-on-client
ticket in it.

1. Read the ticket thread. Establish: what we asked the client for, when we last asked, and how
   many follow-up attempts are already DOCUMENTED. Count only real, recorded attempts — not
   vibes.

2. Confirm the ball is genuinely in the client's court. If the last substantive action needed
   is actually ours (or a vendor's), say so and STOP — chasing a client for our own stall is
   a relationship error.

3. Draft the attempt that comes next on this tone ladder (answer first, greeting only on a
   thread's first message):
   - Attempt 1 — light nudge. Friendly, assumes they're busy. Restate what we need in one
     sentence and why it unblocks their fix.
   - Attempt 2 — direct ask. Still warm, but explicit: what we need, that the ticket is paused
     waiting on it, and an easy out ("if this is no longer an issue, let us know and we'll
     close it out").
   - Attempt 3 — closure warning. Plain statement that without a reply by <specific date>
     we'll close the ticket, and that replying any time reopens it. This is the last chase
     before the three-strikes final email.

4. Every attempt restates the original ask — never send a content-free "just checking in."
   Never skip rungs: don't use attempt-3 tone when only one attempt is documented.

5. Show me the draft for review, labeled with the attempt number. Offer a plain-text internal
   note recording the attempt number and date.

Dates in the closure warning must be real and honored — no "we'll close this Friday" unless
someone will. Never bulk-send follow-ups across tickets without per-ticket human review. If
running unattended as a Flow: output only the follow-up body for the correct attempt number;
if the attempt count is ambiguous or the ticket isn't actually waiting on the client, output
nothing.
```
