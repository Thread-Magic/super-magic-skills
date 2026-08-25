---
name: Wire Fraud Verification Protocol
description: Callback verification for any payment change request: banking updates, new wire instructions, or payroll redirects — verify out-of-band, no exceptions.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# Wire Fraud Verification Protocol

**When to use:** Any inbound request to change or add banking details, wire instructions, or a payment destination (vendor, client, or internal); a payroll direct-deposit change; real-estate / title / closing fund-transfer instructions; or as the verification step invoked by vendor-fraud-bec-alert or business-email-compromise-recovery.

**Run it:** on one ticket (a request to change or add payment details).

## Prompt

```
Apply one rule without exception: a request to change where money goes is verified by voice,
to a number you already had, before it takes effect. This is the reusable standard other
skills call for the money side. It governs verification of payment-detail changes; it is NOT
investment or financial advice, and the decision to release funds stays with the client. Work
it in order:

1. Treat every payment-change request as unverified until callback clears it — regardless of
   how legitimate the email thread looks, and with no exception for urgency, seniority or a
   convincing thread. Compromised real mailboxes produce genuine-looking threads where only
   the banking details changed.
2. Freeze the change: no payment goes out and no banking record is updated on the strength of
   the request alone. Hold it until verification completes.
3. Get the number from a trusted source, never the request: use a phone number from prior
   invoices, the signed contract, or the client/vendor record on file — NEVER a number,
   email, or link in the request message itself. The attacker wrote those.
4. Call and verify with a known person: confirm the change by voice with a known contact at
   the counterparty. Read the requested details to them for confirmation; do not accept new
   details supplied only in the message. No number on file → reach the counterparty through a
   previously known contact or their publicly listed main line and ask for the known person.
5. Never move payment details across email: do not email banking/wire details to confirm,
   compare, or "double-check" — not to the client, not to the vendor. Verification is
   voice-to-a-known-number, full stop, and the guidance you give the client says the same.
6. Record the verification: who called whom, at which number, sourced from where, when, and
   the outcome (confirmed / denied / unreachable). Unreachable is not verified — the change
   stays frozen until a known contact confirms by voice.
7. If verification fails or the request proves fraudulent, branch to vendor-fraud-bec-alert
   (and business-email-compromise-recovery if the client's own mailbox is the source), and if
   money already moved, run the money-moved path — bank recall attempt first, fraud report
   per jurisdiction.

Write defensively: "we are verifying a banking-change request before processing", never an
accusation that the counterparty was breached ahead of evidence. Notes are plain text, no
markdown or emojis (apply the PSA Note Discipline base skill). When in doubt, hold the
payment.
```
