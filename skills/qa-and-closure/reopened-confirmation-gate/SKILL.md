---
name: Re-Opened Confirmation Gate
description: Decide whether a re-opened ticket's latest customer reply really closes it out, with a hard stop on any phishing reply hinting at compromise.
category: QA & Closure
tools: [search_tickets, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Security & Compliance Owner]
outcome: [Fewer Escalations & Less Noise, Risk & Compliance]
---

# Re-Opened Confirmation Gate

**When to use:** Re-opened tickets pile up in the queue because customers reply "thanks, all good" or "I didn't click anything" and nobody re-closes them. Phishing and spam reports are the sharp case this is built for: a confirmed non-interaction should close, but any hint the customer clicked, entered credentials, or approved an MFA prompt must never auto-close. Related: `triage-and-routing/courtesy-reply-status-revert` reverts a courtesy flip by board map and writes no note; this one reasons about security signals and documents the decision.

**Run it:** on one ticket · or as a Flow (when a re-opened ticket gets a customer reply).

## Prompt

```
On a re-opened ticket, decide whether the customer's latest message actually closes it
out or whether it needs a human. Phishing and spam reports are the sharp case: a
confirmed non-interaction can close, any sign of interaction never can.

1. READ. The most recent customer message, recent ticket history and technician notes,
the ticket category and subject, and any indicator that this involves phishing, spam,
suspicious email, a security alert, or an email abuse report.

2. COMPLETE IT (set the desk's completed status) only when the customer's message
carries NO new question, request, concern, or indication of compromise, AND one of
these holds:
- it only expresses gratitude, acknowledges completion, confirms the issue is resolved,
or says no further assistance is needed;
- it is a phishing or spam report and the customer confirms they did not click any
links, with no indication they opened an attachment, entered credentials, or otherwise
interacted with the email. "I did not click anything" is sufficient confirmation — do
NOT require the customer to address every possible interaction type one by one;
- the customer confirms the suspicious message was deleted, ignored, quarantined, or
otherwise handled, and requests no further investigation.

3. KEEP IT RE-OPENED if any of these is true: the customer asks a question; reports the
issue persists; requests additional work; provides new information that may require
investigation; expresses uncertainty about what actions were taken; or the message is
ambiguous and needs human judgment.

4. SECURITY STOP. Always keep it re-opened, whatever else the message says, if the
customer indicates a link was clicked, credentials were entered, MFA was approved
unexpectedly, an attachment was opened or executed, sensitive information was provided,
malware is suspected, or there is any other indication of compromise. This overrides
step 2 entirely.

5. NOTE. Leave an internal note in exactly this shape, whichever way you decided:

Status Decision: [completed or re-opened]
Reason: [short explanation citing the customer's latest message and the ticket context]
Confidence: [high, medium or low, and one clause on what makes it that]

Guardrails:
- Never complete a ticket where there is any indication of compromise, or any
uncertainty about what the customer did.
- For a phishing report, a statement that they did not click or did not interact IS
sufficient to complete. Do not hold a ticket open only because the customer did not
enumerate every possible action.
- Err on the side of caution: unsure means re-opened.
- The status change and the internal note are the only writes. Never reply to the
customer; never change priority, board, or assignee.
- Notes are plain text, no markdown or emojis (apply the PSA Note Discipline skill).
```
