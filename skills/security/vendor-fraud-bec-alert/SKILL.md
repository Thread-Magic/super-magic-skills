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
verify by callback — then work the forensics. In order:

1. Capture the facts: what payment or banking change was requested, the amount, the claimed
   sender (vendor, executive), the channel, and — the fork in the road — whether any payment
   has already been sent.
2. If money already moved, this outranks investigation: advise the client to contact their
   bank immediately to attempt a recall or freeze of the transfer (recovery odds fall by the
   hour), and to file the applicable fraud report for their policy and jurisdiction — in the
   US, IC3; elsewhere, the national cybercrime channel. Timestamp that guidance in the note.
3. Freeze regardless: have the client hold all pending payments to the affected vendor, and
   any payment initiated from the suspect thread, until verification completes.
4. Run the callback verification ladder — the wire-fraud-verification-protocol standard:
   verify with the vendor by phone on a number already on file, from prior invoices, the
   contract or documentation — never a number, email address or link from the suspicious
   message. No number on file → reach a previously known contact at the vendor, or the
   vendor's publicly listed main line, and ask for that contact. Log who verified what, when,
   on which number.
5. Investigate the message: run email-header-analysis, and check for a lookalike domain (typosquat-domain-alert) versus the harder case — a compromised REAL
   vendor mailbox, where the thread history is genuine and only the banking details changed.
   Reply-to divergence and fresh banking details in an old thread are the tells. A
   genuine-looking thread never clears the request — verify the details, not the tone. If the
   compromised side might be the client's own mailbox, branch to account-takeover-runbook.
6. Blast radius: search related tickets and ask the client who else received the request and
   whether anyone began acting on it. Every recipient gets the warning; anyone who processed
   anything takes the step 2 path.
7. Notify with the vendor-fraud template from the soc-client-email-pack, and document the
   decision, not just the action: the request, the verification outcome, the money status,
   and the reasoning behind the verdict. Classify per soc-classification-tree.

Never confirm, request or transmit wire or banking details by email — not to the client, not
to the vendor, not "just to compare." Payment details are verified by voice to a number on
file, and the client guidance states the same rule. Write defensively about the vendor
(defensive-writing-standard): "a fraudulent payment request appearing to come from <vendor>",
never that the vendor was breached — their mailbox status is unconfirmed and the claim
carries legal weight. When in doubt, escalate and hold the payment.
```
