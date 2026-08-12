---
name: Automation Completion Auto-Close
description: When note evidence shows an intent or external automation finished the work, verify and auto-close the ticket — abort if any human message arrives after.
category: Automation & Flows
tools: [search_tickets, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Automation Completion Auto-Close

**When to use:** An intent or automation resolves a request end-to-end (password reset, provisioning step) and the ticket lingers open; "close the ones the automation already finished"; a flow should sweep automation-handled tickets closed once the completion note lands. Fires on the NOTE-ADDED event (the completion note landing) — not a timer or "N minutes after".

**Run it:** on one ticket · or as a Flow (triggered when a completion note is added).

## Prompt

```
Close tickets an automation genuinely finished — but only after confirming from note
evidence that it completed, and only if no human has said anything since. When in doubt,
leave the ticket open; a false close is worse than a lingering open ticket.

Your entire reply is the audit note, verbatim: either `AUTO-CLOSED. Automation: <name>.
Evidence: <note ref>. No human message after completion.` or `NO ACTION. Reason: <no
completion note | human message after completion | status missing>.`

1. Re-read the ticket and its full thread, newest-first.

2. Find explicit completion evidence: a success message from the intent/automation, a
   "completed / done / provisioned" system note tied to THIS ticket's request — not a
   "started" or "queued" note, and not a client asking for the thing. No unambiguous
   completion note -> stop. Never fabricate completion or infer "it probably worked" from
   silence.

3. Abort on any human message after completion. If a technician or client posted anything
   (question, correction, new request) after the completion note, the ticket is live again
   -> do nothing. This abort is absolute.

4. Confirm the target closed/resolved status exists (respect the desk's closed-status
   taxonomy). Status missing on tenant -> no action.

5. Close the ticket by moving it to the resolved/closed status and leave a plain-text audit
   note: which automation completed, the note it was evidenced by, and that no human message
   followed.

Status change and the audit note are the only writes — no reply to the client, no re-
categorization. At most one close per ticket. Notes are plain text (PSA compatibility).
```
