---
name: Litigation Hold
description: Place or manage a legal hold on a user's mailbox and data — scope confirmed by an authorized requester, no user notification unless counsel approves. Use when a ticket asks for a litigation hold, legal hold, or data preservation for a legal matter.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Litigation Hold

**When to use:** "Place a litigation hold on <user>'s mailbox" / "legal needs everything preserved for <user>" / an offboarding for a user who may be under an existing hold / "can we release the hold on <user>?"

**Run it:** on one ticket — authorization- and scope-gated, so a human confirms with the legal requester.

## Prompt

```
Set up (or release) this legal hold correctly and quietly: scope confirmed with the
authorized requester, preservation verified before anything else touches the account,
and nobody tipped off without counsel's say-so.

PLACING A HOLD:
1. Verify the requester is authorized for legal holds at this client: legal counsel,
   an officer, or the client's documented legal/HR contact (knowledge base / IT Glue
   documentation). A manager or the user's colleague is NOT authorized. If
   authorization is unclear, confirm through a contact on file before proceeding —
   don't skip this for speed.

2. Confirm scope in writing with the requester: which custodians (users), which data
   (mailbox, archive, OneDrive/files, Teams/chat), hold duration or "until released,"
   and the matter reference if one exists. Do not guess scope — an under-scoped hold
   is a spoliation risk.

3. Confirm the notification rule explicitly: by default do NOT notify the user or their
   manager that a hold exists. Only notify if counsel approves in writing. Route all
   status questions back to the requester.

4. Verify licensing supports the hold (holds typically require specific plan levels);
   if not, present options to the authorized requester before any license change — and
   note the cost per License Lifecycle practice.

5. Place the hold, then verify it is active and covers the confirmed scope before
   reporting done. If the user is being offboarded, the hold and data preservation take
   precedence: coordinate with Employee Offboarding so no step (license removal, mailbox
   conversion, account deletion) destroys held data.

6. Post a plain-text note visible only per the client's confidentiality practice:
   requester, scope, activation date, verification result, and the no-notification
   status. Confirm to the requester and log time.

RELEASING A HOLD: release only on written instruction from the same class of
authorized requester, verified as above. Confirm no other matter still requires the
hold, release, verify, and note it.

Guardrails: scope and activation only on confirmation from an authorized requester,
never on a verbal or unverified request. Never notify the user, their manager, or
anyone outside the request chain unless counsel approves in writing. Never let an
offboarding, license change, or cleanup delete data under hold. Do not speculate in
the ticket about the legal matter itself — the note records actions, not theories. When
in doubt at any step, pause and ask the authorized requester; a delayed hold beats a
wrong one, but flag urgency so it's decided fast.
```
