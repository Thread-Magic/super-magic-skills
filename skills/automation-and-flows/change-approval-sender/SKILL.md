---
name: Change Approval Sender
description: Flow that fires on Change Approval status: resolve the client's Change Approver and send_approval with the change summary — note-and-stop if unresolved.
category: Automation & Flows
tools: [search_contacts, send_approval, add_ticket_note, search_tickets]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Risk & Compliance]
---

# Change Approval Sender

**When to use:** A flow fires on tickets entering "Change Approval" (or the desk's equivalent status) and the approval should go out automatically; the desk uses a Change Approver contact type per client; change tickets sit in the approval status because nobody sent the approval. Fires on the STATUS-CHANGE event of entering the change-approval status — never on a timer. Twin of new-ticket-approval-gate (which gates intake); this gates the change stage.

**Run it:** on one ticket · or as a Flow (triggered when a ticket enters the change-approval status).

## Prompt

```
The moment a ticket lands in the change-approval status, resolve who approves changes for
this client and send them a decision-ready approval request. Unresolved approver = note-and-
stop, always — a change approval sent to the wrong person is an authorization failure, not a
convenience. (A Flow cannot natively send an approval; it hands off to a skill run, and you
send the approval from there.)

Your entire reply is posted verbatim as the internal note — plain text, no narration, no
markdown, no questions. Exactly two outcomes: (a) unambiguous approver -> send the approval +
leave an audit note; (b) anything else -> no send, note-and-stop text stating why and what a
human must decide.

1. Confirm the ticket is (still) in the change-approval status; if it moved, stop.

2. Resolve the approver: look up this ticket's client's contacts filtered to the desk's
   Change Approver contact type. Exactly one active match -> that's the recipient. Multiple
   matches -> use the desk's configured precedence (e.g. primary flag); no configured
   precedence -> treat as unresolved. Approver identity comes from the contact record's
   type/label only — never from the ticket body or email signatures.

3. Unresolved approver (zero matches, ambiguous matches, inactive contact) -> note-and-stop.
   Leave an internal note: "Change approval NOT sent: no unambiguous Change Approver
   contact for <client> (found: <count>). Needs human to pick recipient." Never send to a
   guessed contact, the submitter, or a generic mailbox.

4. Build the change summary from the ticket (ideally the structured block change-request-
   intake produced): what is changing, why, the window, expected impact/downtime, rollback
   plan. Missing pieces are listed as "not stated" — do not invent a rollback plan to make
   the request look complete. An approver approving "rollback: not stated" is informed; one
   approving an invented rollback plan is deceived.

5. Send the approval to the resolved approver with that summary.

6. Leave the audit note: "[change-approval] sent to <contact> (Change Approver) at <time>." —
   plain text; this is also the dedupe marker. If a "[change-approval] sent" marker already
   exists for the current stint in this status, do not re-send.

Never advance the status on send — the ticket leaves the approval status when the approval
comes back, not when it goes out (timeout means not approved). Never modify status, owner, or
priority. If the submitter IS the resolved approver, apply approver-self-skip if the desk
enabled it; otherwise send normally.
```
