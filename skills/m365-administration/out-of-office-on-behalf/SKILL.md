---
name: Out-of-Office on Behalf
description: Set automatic replies on an absent user's mailbox by request: manager or HR authorization verified, message kept minimal, and an end date set.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Out-of-Office on Behalf

**When to use:** A ticket asks to turn on out-of-office for a user who is out sick / on emergency leave, set an auto-reply on a departed employee's mailbox, or change/extend/remove a user's existing auto-reply while they're away — anything where the requester doesn't own the mailbox and the OOO speaks AS the user to everyone who emails them. NOT for a user asking about their own OOO — that's a how-to, answer it directly.

**Run it:** on one mailbox — you verify authorization and draft the content, a technician drives the module (not a Flow: it needs a human at the console).

## Prompt

```
You set an auto-reply on a mailbox the requester does not own, so the authorization question
comes BEFORE the content question. You prepare and verify; the tech drives the module.
Never invent data.

1. Authorization first. Read the ticket and establish one of these, on record:
   - The absent user asked themselves, by email or message; or
   - Their manager or HR requested it — confirm the reporting relationship where
     documented, otherwise send an approval request to the client's authorized contact; or
   - It is a departed employee and offboarding policy covers it (employee-offboarding owns
     the wider process; this skill executes the reply).
   A peer or "the team" asking is not sufficient — escalate to the manager. Without that
   authorization on record, do nothing.

2. Content discipline. Draft the message and have the authorizer approve the exact text:
   - No reason for absence. "Out of the office" — never "on medical leave", "having
     surgery", "on maternity leave", or anything personal. Even sympathetic details are the
     user's to disclose, not the desk's.
   - No return date unless the authorizer confirms one is safe to share; "until further
     notice" is fine.
   - Name an alternate contact ONLY with that person's agreement on record — you are signing
     them up for the absent user's inbox load.
   - Internal and external replies are separate messages. Keep the external one minimal: it
     leaks org structure to strangers and confirms a live address to spammers. Check the
     mailbox's external-reply setting.

3. Capture any existing auto-reply configuration before overwriting it — that text is the
   rollback, and it may be the user's own wording. Then prepare execution for the tech
   (verify against current module versions):
   Set-MailboxAutoReplyConfiguration -Identity <user> -AutoReplyState Scheduled -StartTime
   <t1> -EndTime <t2> -InternalMessage "<text>" -ExternalMessage "<text>"
   Prefer Scheduled with an end date over Enabled, which runs until someone remembers. Where
   there is no known return date, set a review date in the ticket and calendar the follow-up
   — no immortal auto-replies.

4. If mail must be WORKED during the absence, an auto-reply does not do that — that is a
   delegation conversation with its own consent rules (shared-mailbox-delegation). Offer
   it, don't bundle it.

5. Verify with evidence: send a test message and confirm the approved text arrives. Exchange
   sends one auto-reply per sender per session, so test from a fresh sender or toggle the
   state.

6. Leave a plain-text note (PSA Note Discipline base skill): mailbox, who authorized by name
   and role, the exact internal and external text set, start and end times, the alternate
   contact's consent reference, the date, and rollback (-AutoReplyState Disabled, plus the
   prior configuration you captured). Log time.
```
