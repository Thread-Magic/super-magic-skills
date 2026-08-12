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
You set an auto-reply on a mailbox the requester doesn't own — with the authorization question answered BEFORE the content question. You prepare and verify; the tech drives the module. Never invent data.

1. Authorization first. The requester is not the mailbox owner, so verify (read the ticket for context):
   - The absent user themselves asked (email/message on record), OR
   - Their manager or HR requested it (look up the contact to confirm the reporting relationship where documented; otherwise get the client's authorized contact to confirm via an approval request), OR
   - It's a departed employee and offboarding policy covers it (employee-offboarding owns the wider process; this skill executes the reply).
   A peer or "the team" asking is not sufficient — escalate to the manager.

2. Content discipline — draft the message and get the authorizer to approve the exact text. Rules:
   - No reason for absence. "Out of the office" — never "on medical leave," "having surgery," "on maternity leave," or anything personal. Even sympathetic details are the user's to disclose, not the desk's.
   - No return date unless the authorizer confirms one is safe to share; "until further notice" is fine.
   - Alternate contact named ONLY with that person's agreement on record — you are signing someone up for the absent user's inbox load.
   - Internal and external replies are separate messages: external stays terser (external replies also leak org structure to strangers and confirm live addresses to spammers — keep the external one minimal, and confirm the tenant/mailbox external-reply setting is appropriate).

3. Prepare execution for the tech (PowerShell labeled: verify against current module versions): `Set-MailboxAutoReplyConfiguration -Identity <user> -AutoReplyState Scheduled -StartTime <t1> -EndTime <t2> -InternalMessage "<text>" -ExternalMessage "<text>"` — prefer `Scheduled` with an end date over `Enabled` (which runs until someone remembers). For no-known-return cases, set a review date in the ticket instead and calendar the follow-up.

4. Consider the pairing: if mail must be WORKED during the absence, an OOO alone doesn't do that — that's a delegation conversation (shared-mailbox-delegation) with its own consent rules. Offer it; don't bundle it.

5. Verify via evidence: send a test message and confirm the auto-reply arrives with the approved text (note: Exchange sends one auto-reply per sender per OOO session — test from a fresh sender or toggle state).

6. Document what/why/when/rollback — leave a plain-text note: mailbox, who authorized (name and role), exact message text set (internal and external), start/end times, alternate contact's consent reference, date set, and rollback (`-AutoReplyState Disabled`; prior configuration captured before change if one existed). Log time.

Guardrails: No OOO on another person's mailbox without manager/HR/owner authorization on record — when in doubt, do nothing and escalate. Never state or imply the reason for absence in the message. Alternate contacts are named only with their documented agreement. Always an end date or a calendared review — no immortal auto-replies. Capture any existing auto-reply configuration before overwriting it; that text is the rollback and may be the user's own wording.
```
