---
name: Zapier Outlook Client Email
description: Send or draft email from shared mailboxes via Outlook and pull a requester's recent emails into ticket context for support conversations.
category: Connectors
tools: [search_tickets, search_contacts, add_ticket_note]
connectors: [Zapier: Microsoft Outlook]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Faster Resolution & Response]
---

# Zapier Outlook Client Email

**When to use:** "Email <user> from the support mailbox that their account is unlocked," "draft the renewal email from billing@ — I'll review," or "pull up what <user> emailed us this week."

**Run it:** on one ticket.

## Prompt

```
Work the desk's real mailboxes: send or draft from shared addresses (support@, billing@) through
Outlook, and pull a requester's recent correspondence into the ticket picture.

This runs only if the member has connected Zapier, and the connected Microsoft account must have
rights to the shared mailbox — a send that silently comes from the member's personal address is a
real failure mode, so verify the From on first use. If Zapier is absent, degrade to drafting the
email text in chat — do not stop. Each Zapier call = 2 Zapier tasks.

Sending / drafting:
1. Resolve the recipient from the contact record — never from an address typed loose in a note or
   guessed from a name pattern.
2. Draft in the desk's client-email register: plain professional language, correct salutation,
   ticket reference, clear next step. Localize when the desk serves non-English clients.
3. Choose Draft vs Send: anything sensitive, billing-related, legal-adjacent, or first-of-its-kind
   goes to a draft in the shared mailbox for human review. Routine confirmations may send after I
   confirm recipient + body. When in doubt, draft — a draft is free to fix; a sent email is not. No
   credentials or secure links in bodies; use the desk's secure delivery method.
4. Show me recipient, sending mailbox, subject, and body, wait for confirmation, then execute.
5. Leave a note (plain text): what was sent/drafted, from which mailbox, to whom.

Pulling context:
6. Search the mailbox for the requester's recent emails, scoped to their address and a stated window
   (default 14 days). Summarize what's relevant to the ticket — dates, asks, attachments mentioned —
   and state only what the emails actually say, noting when the window or result cap limits the
   picture. Quote only as needed; don't dump full bodies into the ticket. Offer to note the summary
   onto the ticket.
```
