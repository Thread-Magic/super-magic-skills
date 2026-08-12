---
name: Vendor Fraud BEC Alert
description: Respond to a BEC or payment-fraud attempt (fake invoice, banking-change request, exec impersonation): freeze payments and run callback verification.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Vendor Fraud BEC Alert

**When to use:** A client reports a suspicious invoice, banking-detail change, or wire request; an executive- or vendor-impersonation email is reported; or account-takeover blast radius surfaced outbound payment-fraud attempts.

**Run it:** on one ticket (a reported payment-fraud / BEC attempt).

## Prompt

```
BEC is a money problem before it is an email problem. Put the funds first — freeze, recall,
verify by callback — and only then work the forensics of how the fraudulent request arrived.
Work it in order:

1. Capture the report's facts: what payment or banking change was requested, the amount, the
   claimed sender (vendor, executive), the channel, and — the fork in the road — whether any
   payment has already been sent.
2. If money already moved, this is time-critical and outranks investigation: advise the
   client to contact their bank immediately to attempt a recall or freeze of the transfer
   (recovery odds fall by the hour), and to file the applicable fraud report per their policy
   and jurisdiction (in the US, IC3; elsewhere, the national cybercrime channel). Timestamp
   this guidance in the note.
3. Freeze guidance regardless: recommend the client hold all pending payments to the
   affected vendor, and any payment initiated from the suspect thread, until verification
   completes.
4. Run the callback verification ladder for the request itself (this is the
   wire-fraud-verification-protocol standard): verify with the vendor by phone using a number
   on file — from prior invoices, the contract, or documentation — never a number, email
   address, or link from the suspicious message. No number on file → go through a previously
   known contact at the vendor, or the vendor's publicly listed main line, and ask for the
   known contact. Log who verified what, when, by which number.
5. Investigate the message: run email-header-analysis on the request; check for a lookalike
   domain (typosquat-domain-alert) versus the harder case — a compromised REAL vendor
   mailbox, where the thread history is genuine and only the banking details changed.
   Reply-to divergence and fresh banking details in an old thread are the tells. If the
   compromised side might be the client's own mailbox, branch to account-takeover-runbook.
6. Blast radius: search related tickets and ask the client — who else received the request,
   and did anyone begin acting on it? Every recipient gets the warning; anyone who processed
   anything gets the time-critical path.
7. Notify with the vendor-fraud template from the soc-client-email-pack, and document the
   decision, not just the action: the request, the verification outcome, the money status,
   and the verdict reasoning. Classify per soc-classification-tree.

Guardrails — always:
- Never confirm, request, or transmit wire or banking details by email — not to the client,
  not to the vendor, not "just to compare." Verification of payment details happens by voice
  to a number on file. The client guidance states the same rule.
- Money-moved cases run on the containment clock: bank first, forensics second.
- Never validate the request through any contact detail sourced from the suspicious message.
- A genuine-looking thread does not clear the request — compromised real mailboxes produce
  genuine threads. The banking details are what get verified, not the tone.
- Defensive writing with the client and especially about the vendor: "a fraudulent payment
  request appearing to come from <vendor>" — do not state the vendor was breached; their
  mailbox status is unconfirmed and the claim has legal weight.
- When in doubt, escalate and hold the payment — a delayed legitimate invoice is cheap; a
  completed fraudulent wire isn't.
```
