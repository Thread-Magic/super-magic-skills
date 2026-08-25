---
name: Phishing Triage
description: Triage a reported phishing email without touching the payload: check blast radius, contain if malicious, and reply to the reporter with a verdict.
category: Security
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Phishing Triage

**When to use:** "Is this a phishing email?" / a user forwarded something suspicious; a phishing-report ticket (report button, mailbox plugin, or manual forward) lands on the security board; or a tech wants a second opinion on a suspect message before releasing or deleting it.

**Run it:** on one ticket (a reported suspicious email).

## Prompt

```
Take a reported suspicious email from "is this phishing?" to a documented verdict:
indicators captured safely, simulation traffic filtered out, everyone else who received it
identified, containment advised where needed, and the reporter answered. Work it in order:

1. Capture the indicators from the ticket as text only: sender address and display name,
   reply-to, subject, send time, every link target exactly as written, and attachment names
   and types. Never open, click, fetch or render a link or attachment from the message — not
   even to "check what it is."
2. Simulation branch: compare the sender and link domains against the client's documented
   phishing-simulation vendor domains in the knowledge base. On an exact match to a
   documented simulator domain, classify as simulation, close internally with a plain-text
   note naming the matched domain, and do NOT reply to the client — a reply skews their
   simulation-program metrics. Stop here. A partial domain match is not a match; never close
   a real phish as a simulation.
3. Assess indicators: lookalike or cousin domain, urgency and payment lures,
   credential-harvest link (display text vs actual target mismatch), unexpected attachment
   types, thread hijacking of a real prior conversation. If full headers were pasted, hand
   the deep parse to email-header-analysis and fold its verdict in.
4. Blast-radius check: search the client's boards and recent tickets for the same sender or
   subject. Establish who else received the message and — critically — whether anyone
   clicked, replied, entered credentials, or opened an attachment. Never state "no one else
   received this" off a capped search; report "no other reports in the last N tickets
   searched" (apply the Sweep Honesty base skill).
5. If anyone interacted with a message you judge malicious, escalate immediately and start
   compromised-account-containment for the affected users. Containment outranks finishing the
   write-up: contain fast, investigate second.
6. Deliver the verdict:
   - Malicious → advise quarantine/removal from all recipient mailboxes, sender/domain block
     at the gateway, and a credential reset for anyone who clicked.
   - Suspicious but unconfirmed → say exactly that, with what would confirm it.
   - Legitimate → explain the signals that clear it, so the reporter learns.
7. Reply to the reporter — draft it for a human to review and send — and thank them;
   reporting is the behavior you want repeated. Log the verdict, the evidence, and the
   reasoning behind the call as an internal note, then classify and set status per
   soc-classification-tree.

Write defensively throughout (defensive-writing-standard): a reported message is a "reported
message", not a "breach" or a "hack", and no impact claim goes in writing ahead of confirmed
facts. Document why the verdict was reached, not only what was done.
```
