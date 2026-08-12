---
name: Approval Request Email
description: Draft an email to an approver requesting authorization for a password reset, install, purchase, or access change — what/why/risk/expiry in one read.
category: Communication
tools: [search_tickets, search_contacts, send_approval, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Approval Request Email

**When to use:** "Ask <user>'s manager to approve this password reset" / "draft the approval request for this software install / purchase / admin access" — any change that policy says needs sign-off from someone at the client.

**Run it:** on one ticket.

## Prompt

```
Draft the message that gets a decision: a request to a manager, account contact, or designated
approver, structured so approving (or declining) takes one read and one reply.

1. Read the ticket to establish what is being requested, for whom, and why. Identify the correct
   approver — the client's designated approval contact or the requester's manager, from the
   contact list or the client record. Never treat the requester as their own approver.

2. Draft with four labeled elements the approver can scan:
   - What: the exact action ("reset the password for <user>'s account", "install <software> on
     <device>", "purchase <item> at <cost>").
   - Why: the business reason in one sentence, tied to the ticket.
   - Risk / impact: what this changes and any cost, downtime, or access implication — stated
     honestly, including "low risk" when true.
   - Expiry: how long the request stands ("if we don't hear back by <date/time>, we'll put this
     on hold and check in").

3. Make the response mechanics trivial: "Reply 'approved' to this email and we'll proceed."

4. If Thread's structured approval fits (a yes/no decision on a ticket), prefer sending a
   structured approval on the ticket so the decision is captured there; use the email draft
   when the approver is outside that workflow or needs the full what/why/risk/expiry context.

5. Show me the draft as an open draft for review, or alongside the structured approval action
   for confirmation, labeled "DRAFT — review before sending" and noting who it goes to. Do NOT
   send or trigger the approval without my go-ahead.

Never perform the requested action in anticipation of approval — draft, send (with
confirmation), wait. For security-sensitive approvals (password/MFA/access), the approver must
be a contact on file, never an address supplied inside the ticket text. State cost figures only
if they appear in the ticket or a quote; never estimate prices. Expiry dates must be real
commitments the desk will honor.
```
