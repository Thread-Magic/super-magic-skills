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
A registrar renewal notice is both a real deadline and one of the oldest invoice scams
going. Treat it as unverified. Never click a link or open an attachment in it.

1. Verify the sender before treating the deadline as real: does the sender domain match the
   actual registrar of record character-for-character? A lookalike is a mismatch. Scam
   signals: a "registry" or "domain service" the client has no relationship with, listing
   upsells dressed as renewals, urgency plus a payment link, prices far above market, PDF
   invoices from generic mailboxes. Failed verification plus a payment or banking element:
   branch to vendor-fraud-bec-alert, but keep going — the domain may still genuinely be
   expiring.
2. Confirm the real expiry independently, never from the notice: read the domain's registrar,
   expiry and name servers in Liongard, dating the dataprint (Inspector Read Discipline base
   skill), or fall back to a passive WHOIS/RDAP lookup. If the two disagree the independent
   source wins.
3. Identify the registrant owner from the client and contact records, documentation and prior
   renewal tickets: MSP-managed (the desk renews), client-managed (their finance or admin
   renews) or third-party-managed (web agency, previous IT). The desk must not pay for a
   domain it does not manage.
4. Route with a timeline. Set priority and board, and leave a plain-text internal note giving
   the sender verdict, the confirmed expiry with source and as-of date, the registrar of
   record, the owning party and the recommended action with its deadline:
   - Expired or within days → urgent, incident-adjacent: an expired domain takes down mail
     and web.
   - Weeks out → normal task to the owning party with the confirmed date.
   - Auto-renew confirmed at the real registrar → informational; note the evidence and close
     per desk policy.
   - Scam notice, no real expiry → fraud path; warn the client not to pay.
   Never record a renewal as done — you recommend, the owner acts.

As a Flow: your entire reply is the note, plain text, verdict line first — VERIFIED RENEWAL
(expires <date> per <source>), SCAM-PATTERN NOTICE (routed to fraud path) or UNVERIFIED
(human review required) — then the evidence. The only writes are priority/board routing and
that note; never close the ticket, send anything outbound, or touch a payment or approval
step. An unconfirmable expiry is UNVERIFIED — stop there.

Never pay, approve or forward a renewal invoice that hasn't passed sender verification; even
then, payment is the owning party's action unless the domain is explicitly MSP-managed with
an established process. A scam notice and a real approaching expiry can both be true —
resolve both. Client-facing wording follows the defensive-writing-standard skill — factual,
non-accusatory. If nothing independent confirms the expiry, say so and route to a human.
```
