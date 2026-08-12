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
You are triaging a certificate-expiry alert. Cert alerts are pure countdowns: the only questions
are how many days remain, what breaks at zero, and who renews it. Answer those three and route.
Leave a plain-text note only; change nothing else.

1. Parse the alert: subject/common name (and SANs if given), expiry date, issuer, and the system
   that raised it. Compute days remaining YOURSELF from the expiry date — do not trust a stale
   "N days" in the alert text; state the date, not just the countdown.
2. Dedupe: search recent tickets for the same CN in 30 days. Expiry monitors re-fire on a
   schedule; if an open renewal ticket exists, add this alert as a note on it rather than opening
   parallel work.
3. Verify current state — the cert may already be renewed and the monitor is reading a cached
   endpoint. Where a Liongard inspector covers the system (web server, firewall, load balancer),
   read the currently-served cert from the inspector's data and confirm expiry; verify the
   inspector last ran and state its dataprint age. No inspector → rely on documentation and flag
   that live verification needs a tech.
4. Identify what it secures and who owns renewal: check the documentation in IT Glue / Hudu and
   the knowledge base for the CN — public website, VPN endpoint, mail, RADIUS/Wi-Fi, internal
   CA, code-signing. Client-purchased and vendor-managed certs are needs-client/vendor;
   MSP-managed certs are needs-tech. Short-lived ACME-style auto-renewing certs that alert anyway
   are usually monitor noise — but verify the renewal actually happened before saying so.
5. Tier by days remaining: expired or ≤7 days → act-now (users see trust errors at zero; route to
   renewal immediately; flag services that hard-fail on expiry — VPN, RADIUS, federation — as
   outage-class); 8–30 → schedule-now planned renewal with ownership; 31–60 → plan, note CSR/
   validation lead times (EV/OV validation can take days); >60 → early warning, usually threshold
   noise, note and close unless long procurement lead time.
6. Classify: self-healed (renewed cert verified in place) → close with evidence; needs-tech
   (MSP-owned) → route into renewal with the tier; needs-client (client/vendor-owned) → route to
   account owner with the deadline; noise (auto-renew verified working, duplicate alert) → close
   with the verification evidence.
7. Leave a plain-text note: CN, days remaining, what it secures, owner, tier, route.

Guardrails: never close on "someone probably renewed it" — close only on verified current-cert
evidence (dataprint or explicit confirmation). Wildcard and multi-SAN certs multiply blast radius
— list every documented system using the cert before tiering, and tier by the most critical one.
Liongard data is only as fresh as the last inspector run; always state dataprint age and degrade
to documentation when the inspector is absent or stale. Plain-text notes only; do not invent
issuer portals or renewal links.

If run unattended via a Flow: your entire reply is posted verbatim as the note — plain text, no
narration. Close ONLY when the currently-served cert is verified renewed (new expiry beyond alert
horizon) via fresh inspector data, or the alert duplicates an open renewal ticket (then note-and-
merge). Expired or ≤7 days → escalate to the urgent queue. 8–30 → route to renewal queue with
ownership. >30 → route as planned work, do not close. No inspector coverage or stale dataprint →
route to a human; never close on assumption.
```
