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

1. Capture the indicators from the ticket without interacting with them: sender address and
   display name, reply-to, subject, send time, every link target exactly as written, and
   attachment names and types. Never open links or attachments, and never fetch a URL from
   the message to "check what it is."
2. Simulation branch: compare the sender and link domains against the client's documented
   phishing-simulation platform domains (check the knowledge base for the client's
   simulation vendor record). If it matches a known simulator → classify as simulation,
   close internally with a plain-text note naming the matched domain, and do NOT reply to
   the client — a reply skews their simulation-program metrics. Stop here.
3. Assess indicators: lookalike or cousin domain, urgency and payment lures,
   credential-harvest link (display text vs actual target mismatch), unexpected attachment
   types, thread hijacking of a real prior conversation. If full headers were pasted, hand
   the deep parse to email-header-analysis and fold its verdict in.
4. Blast-radius check: search for the same sender or subject across the client's boards and
   recent tickets. Determine who else received the message and — critically — whether anyone
   clicked, replied, entered credentials, or opened an attachment.
5. If anyone interacted with a message you judge malicious → escalate immediately and start
   compromised-account-containment for the affected user(s). Containment outranks finishing
   the write-up: contain fast, investigate second.
6. Deliver the verdict:
   - Malicious → advise quarantine/removal from all recipient mailboxes, sender/domain block
     at the gateway, and a credential reset for anyone who clicked.
   - Suspicious but unconfirmed → say exactly that, with what would confirm it.
   - Legitimate → explain the signals that clear it, so the reporter learns.
7. Reply to the reporter (draft it for a human to review and send) with the verdict using
   the defensive-writing-standard vocabulary (a suspicious email is a "reported message,"
   not a "breach"). Log the verdict, the evidence, and the decision reasoning as an internal
   note; classify and set status per soc-classification-tree. Thank the reporter — reporting
   is the behavior you want repeated.

Guardrails — always:
- Never open, click, fetch, or render links or attachments from the reported message.
  Capture indicators as text only.
- Check simulation status both ways: never raise a real incident for a simulation, and never
  close a real phish as a simulation on a partial domain match — require an exact documented
  simulator domain. Never reply to the client on a confirmed simulation; close internally
  only.
- Clicked or replied means escalate immediately — a false escalation is cheap, a missed
  compromise isn't.
- Never state "no one else received this" from a capped search; report "no other reports
  found in the last N tickets searched."
- Document the decision, not just the action: the note must say why the verdict was reached.
- Defensive writing throughout: no "breach," no "hacked," no impact claims before facts are
  confirmed.
```
