---
name: SOC Client Email Pack
description: Pick the right client-outreach template for a security event (leaked credentials, BEC, inbox rule, lookalike domain) and draft with verified facts only.
category: Security
tools: [search_tickets, search_contacts, view_openDraft, send_client_email]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Retention & Growth (CSAT/Expansion)]
---

# SOC Client Email Pack

**When to use:** A security runbook reached the "notify the client" step; "draft the client email for this security ticket"; or a tech wants the right first message for a leaked-credential / BEC / inbox-rule / lookalike-domain event.

**Run it:** on one ticket (the first client outreach for a security event).

## Prompt

```
Provide the first-outreach template for the most common client-facing security events. Every
template shares one skeleton — what we detected, what we've done, what we need from you, what
happens next — filled only with verified facts and worded to the defensive-writing-standard.
Draft only; a human reviews and sends every security notification. Work it in order:

1. Identify the threat type and pull the verified facts from the ticket: what was detected,
   when (timestamps), what has already been done, and what the client must do. Anything not
   yet verified does not go in the email.
2. Select the template skeleton by threat type:
   - Leaked credentials: which account, exposure source and date, that this is a third-party
     exposure and not a breach of their systems, rotation-everywhere and MFA-verification
     asks. Never include the credential value itself.
   - Vendor fraud / BEC: the fraudulent request received, freeze guidance for pending
     payments to the affected vendor, the callback-verification instruction (verify by phone
     using a number on file — never contact details from the suspicious message), and the
     rule to state outright: banking or wire details are never confirmed or changed by email.
   - Malicious inbox rule: what the rule did in plain terms, that it was removed and the
     account secured, what the user should watch for, timestamps.
   - Lookalike domain: the suspect domain spelled out defensively (spaced or bracketed so it
     isn't a live link), what it could be used for, the verify-sender-addresses and
     callback-for-payment-changes guidance.
3. Every template closes with all four skeleton sections plus: when the next update will
   come, and how the client can verify this message genuinely came from the service desk.
4. Apply the house voice (the email baseline standard) and the defensive-writing-standard
   vocabulary: first outreach never says "breach" or "hacked"; unconfirmed items are "under
   investigation."
5. Anything unknown stays a visibly marked placeholder — <exposure date>, <affected account>
   — and is flagged to the technician; never fill a gap with a plausible guess.
6. Present as a draft for a human to review and send. Where in-app draft tools are
   unavailable, output the complete email text for the technician to copy — a human sends
   either way.

Never put a leaked credential value or hash, a live malicious link, or another client's
details in any email. No fabricated facts, timestamps or reassurances: placeholders stay
visible until a human resolves them. Disclosure scope and timing follow the client's incident
policy and management direction.
```
