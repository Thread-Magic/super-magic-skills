---
name: Resolution Closing Email
description: Draft the closure email for a resolved ticket — what was wrong, what we did, how to reopen — built from the ticket's actual evidence, not memory.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Retention & Growth (CSAT/Expansion)]
---

# Resolution Closing Email

**When to use:** "Draft the closing email for this ticket" / "write the resolution summary for the client" — a ticket is moving to resolved/closed and the client deserves a proper close-out.

**Run it:** on one ticket · or as a Flow (triggered when a ticket moves to resolved).

## Prompt

```
Draft the final client-facing message for this resolved ticket — short, accurate, built only
from the record.

1. Read the full ticket: original report, notes, time entries, and the resolving actions. The
   email is built only from what the record shows.

2. Draft it (answer first, plain language, greeting only if this is the thread's first
   message) covering three things:
   - What was wrong — the issue as the client experienced it, in their words, not the internal
     classification.
   - What we did — the fix, summarized for a non-technical reader; translate any jargon.
   - How to reopen — end with, verbatim: "If anything isn't resolved, just reply to this
     email — replying reopens this ticket."

3. If the fix requires anything from the client going forward (a restart, a new password at
   next login), state it as an explicit next step.

4. Keep it to 1-2 short paragraphs plus the reopen line. A closure email is a receipt, not
   a report.

5. Show me the draft for review, labeled "DRAFT — review before sending." Do NOT send, and
   do NOT change the ticket status — closure is the technician's call.

Content honesty: only claim actions the record actually documents. If the resolution notes are
thin, draft what is supported and flag "NEEDS: confirm what resolved this — notes don't say."
Never state a root cause that wasn't established — "resolved after <action>" is honest,
"caused by X" requires evidence. No credentials, internal notes, or other clients' details.
If running unattended as a Flow reply: output only the email body verbatim, no labels; and if
the record doesn't establish what resolved the issue, output nothing — a wrong closure email
is worse than none.
```
