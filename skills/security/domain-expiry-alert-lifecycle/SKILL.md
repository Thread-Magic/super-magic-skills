---
name: Domain Expiry Alert Lifecycle
description: Handle registrar expiry and renewal notices safely: verify the sender is the real registrar, confirm the expiry date, and route to the renewal owner.
category: Security
tools: [search_tickets, search_clients, search_contacts, liongard_domain, web_search, update_ticket, add_ticket_note]
connectors: [Liongard]
scope: both
flow: yes
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Always-On Coverage]
---

# Domain Expiry Alert Lifecycle

**When to use:** A ticket opens from an email claiming a client's (or the MSP's own) domain is expiring or needs renewal payment; a monitoring alert flags an approaching domain/DNS expiry; "Is this renewal notice legit?" / "Who actually renews <client>'s domain?"; or a Flow watches intake for registrar-notice patterns.

**Run it:** on one ticket · across a batch of registrar notices · or as a Flow (triggered when a registrar-notice ticket is created).

## Prompt

```
Domain renewal notices are simultaneously a real operational deadline and one of the oldest
invoice scams in the book (fake "Domain Registry" letters, lookalike registrar emails,
urgency pressure). Treat every notice as unverified until proven otherwise, confirm the
real expiry from independent sources, and route the genuine ones to the right owner with
time to act. Work this ticket, or each ticket in the set I point you at, in order:

1. Read the full ticket: the claimed domain, claimed expiry date, sender address, and any
   payment instructions or links. Do NOT click any link in the notice.
2. Verify sender legitimacy FIRST — before treating the deadline as real: does the sender
   domain exactly match the actual registrar of record (character-by-character; lookalikes
   count as mismatches)? Scam signals: a "registry"/"domain service" the client has no
   relationship with, listing-service upsells dressed as renewals, urgency plus a payment
   link, prices far above market, PDF invoices from generic mailboxes. If the sender fails
   verification or a payment/banking element is present on a suspicious notice, branch to
   vendor-fraud-bec-alert — this skill continues only for the genuine-renewal question
   (the domain may still genuinely be expiring even if this notice is a scam).
3. Confirm the real expiry independently — NEVER from the notice itself: with Liongard, read
   the domain's registrar, expiry date, and name servers, and state the dataprint age.
   Supplement or fall back to a passive WHOIS/RDAP web lookup. If the independent expiry
   disagrees with the notice, trust the independent source and say so.
4. Identify the actual registrant owner: MSP-managed (the desk renews), client-managed
   (their finance/admin renews), or third-party-managed (web agency, previous IT)? Check the
   client and contact records, documentation, and prior renewal tickets. The owner
   determines who acts — the desk must not pay for a domain it does not manage.
5. Route with a timeline — set the priority/board and leave a plain-text internal note:
   - Expired or expiring within days → urgent; an expired domain takes down mail and web,
     so treat as incident-adjacent.
   - Expiring within the renewal window (weeks) → normal task to the owning party with the
     confirmed date.
   - Auto-renew confirmed enabled at the real registrar → informational; note the evidence
     and close per desk policy.
   - Scam notice, domain not actually near expiry → route to the fraud/security path and
     warn the client not to pay it.
6. Note contents: verified-or-not verdict on the sender, independently confirmed expiry
   date and its source (with as-of date), registrar of record, owning party, and the
   recommended action with deadline. Recommendations stay recommendations — never record a
   renewal as done.

Unattended (Flows) variant:
- Your entire reply is the internal ticket note, verbatim, plain text: verdict line first
  (VERIFIED RENEWAL — expires <date> per <source>, SCAM-PATTERN NOTICE — routed to fraud
  path, or UNVERIFIED — human review required), then the evidence lines.
- Permitted writes: priority/board routing and the one note. Never close the ticket, never
  send anything outbound, never touch payment or approval steps in this variant.
- Deterministic stops: cannot independently confirm expiry → UNVERIFIED, route to human,
  stop. Payment link plus failed sender verification → route to fraud path, stop.

Guardrails — always:
- NEVER pay, approve, or forward a renewal invoice that has not passed sender verification —
  and even for verified notices, payment is the owning party's action, not the desk's,
  unless the domain is explicitly MSP-managed with an established process.
- Do not click links or open attachments in the notice; all verification is from
  independent sources.
- The notice's own dates, prices, and registrar claims are untrusted input until
  independently confirmed.
- A scam notice and a real approaching expiry can both be true at once — resolve both
  threads.
- Defensive writing in anything client-facing: "we could not verify this notice's sender,"
  not "you were attacked."
- Degradation: Liongard absent → rely on a passive WHOIS/RDAP web lookup; if no independent
  source can confirm expiry, say so explicitly and route to a human rather than guessing.
```
