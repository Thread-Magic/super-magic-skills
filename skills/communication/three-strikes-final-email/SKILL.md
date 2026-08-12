---
name: Three Strikes Final Email
description: Draft the final "we're closing this ticket" email after three documented contact attempts with no client response — only when the evidence of prior attempts actually exists.
category: Communication
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Technician, CSM / Account Manager]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Three Strikes Final Email

**When to use:** "Three attempts, no response — draft the final email" / "send the we're-closing-this notice" — the follow-up ladder has been exhausted and the ticket is going quiet-closed.

**Run it:** on one ticket · or as a Flow (triggered on a ticket waiting on the client).

## Prompt

```
Draft the last message on an unresponsive ticket — professional, final, blameless — but ONLY
when the record proves the desk earned it.

1. Read the ticket thread and verify the evidence: THREE documented outreach attempts (emails,
   calls with notes, or voicemails recorded on the ticket) with no substantive client response
   since. List the three attempts with their dates before drafting.

2. If fewer than three attempts are documented, do NOT draft. Say which attempts are on record
   and route to the follow-up chaser for the next rung instead. This is a hard gate —
   "I'm sure we called them" does not count.

3. Draft (answer first, greeting only if the thread's first message):
   - One sentence of context: what the ticket was for.
   - The factual record: "We reached out on <date 1>, <date 2>, and <date 3> and haven't
     heard back."
   - The action: we're closing the ticket now, stated plainly and without reproach.
   - The open door, verbatim: "If you still need help with this, just reply to this email —
     replying reopens this ticket."

4. Tone check: neutral and warm. No guilt-tripping ("despite our repeated attempts..."), no
   passive aggression. The client may have had a genuinely bad month.

5. Show me the draft for review, labeled "FINAL NOTICE DRAFT" with the three attempt dates
   listed above it. Offer a plain-text internal note recording the three dates and that the
   notice was sent.

Dates in the email must match the ticket record exactly — this message is the audit trail.
Never close the ticket yourself; leave the status change to a human. If running unattended as
a Flow: verify all three documented attempts inside the run — if you cannot find all three,
output nothing; otherwise output only the email body verbatim.
```
