---
name: Certificate Expiry Alert
description: Triage a certificate expiry alert — tier urgency by days remaining, identify what the cert secures and who owns renewal, and route into renewal work.
category: Alert Runbooks
tools: [search_tickets, liongard_metric, liongard_timeline, liongard_launchpoint, search_itglue, search_hudu, search_knowledge_base, add_ticket_note, update_ticket]
connectors: [Liongard, IT Glue, Hudu]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# Certificate Expiry Alert

**When to use:** A "certificate expires in N days" or "certificate expired" alert lands; or a tech asks "what is this cert alert about and who owns it?"

**Run it:** on the alert ticket · or as a Flow that fires on the cert-expiry alert ticket event.

## Prompt

```
Triage a certificate-expiry alert. Cert alerts are pure countdowns: how many days remain, what
breaks at zero, and who renews it.

1. Parse the alert: common name and SANs, expiry date, issuer, raising system. Compute days
   remaining YOURSELF from the expiry date — the alert's "N days" may be stale — and state the
   date, not just the countdown.

2. Search recent tickets for the same CN, 30 days. Expiry monitors re-fire, so if an open renewal
   ticket exists, note this alert there instead of opening parallel work.

3. Verify current state — the cert may already be renewed, with the monitor reading a cached
   endpoint. Where a Liongard inspector covers the system, read the served cert and confirm
   expiry, checking the inspector ran and giving the dataprint age. Without one, rely on
   documentation and flag that live verification needs a tech.

4. Identify what it secures and who renews it, from IT Glue or Hudu and the knowledge base:
   public website, VPN, mail, RADIUS or Wi-Fi, internal CA, code-signing. ACME-style
   auto-renewing certs that alert anyway are usually monitor noise — verify the renewal happened
   before saying so.

5. Tier by days remaining. Expired or 7 or fewer: act-now — users see trust errors at zero, so
   route to renewal now and flag services that hard-fail on expiry (VPN, RADIUS, federation) as
   outage-class. 8 to 30: planned renewal now, with ownership. 31 to 60: plan it, noting CSR and
   validation lead times — EV and OV validation can take days. Over 60: early warning, usually
   threshold noise; note and close unless procurement is slow.

6. Classify by ownership and note it — plain text, no markdown or emojis (PSA Note Discipline
   base skill): CN, days remaining, what it secures, owner, tier, route. Renewed cert verified in
   place: close with the evidence. MSP-owned: into renewal at its tier. Client or vendor owned:
   account owner, with the deadline. Auto-renew verified working, or a duplicate: close with the
   verification.

Never close on "someone probably renewed it" — only verified current-cert evidence closes this.
Wildcard and multi-SAN certs multiply blast radius: list every documented system using the cert,
and tier by the most critical. Inspector data is only as fresh as the last run: give the
dataprint age, and fall back to documentation when it is absent or stale (Connector Degradation
base skill). Don't invent issuer portals or renewal links.

As a Flow: your entire reply is the note. Close ONLY when the served cert is verified renewed (a
new expiry beyond the alert horizon, in fresh inspector data), or the alert duplicates an open
renewal ticket — then note and merge. Expired or 7 days or fewer: urgent queue. 8 to 30: renewal
queue with ownership. Over 30: planned work, do not close. No inspector coverage or a stale
dataprint: route to a human, never close.
```
