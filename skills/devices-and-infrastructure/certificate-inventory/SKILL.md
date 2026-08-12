---
name: Certificate Inventory
description: Build an expiry calendar of every certificate a client depends on — public web, RDS, LOB, internal CA, device certs — with owner and renewal steps.
category: Devices & Infrastructure
tools: [search_itglue, search_hudu, liongard_launchpoint, liongard_metric, liongard_timeline, liongard_query, search_tickets, search_knowledge_base, add_ticket_note, create_ticket, schedule_ticket]
connectors: [Liongard, IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Certificate Inventory

**When to use:** "What certificates does <client> have and when do they expire?" — or an expired cert just caused an outage and leadership asks "what else is out there?"

**Run it:** across a client's whole certificate estate, on demand (not a Flow — this is a planning sweep, not a per-ticket event).

## Prompt

```
Assemble the per-client certificate register — what exists, where it lives, when it expires, who renews it and how — and turn expiry dates into scheduled work instead of outages.

1. Harvest documented certs: search the documentation (IT Glue / Hudu) for certificate, SSL/TLS, and CA docs. Per cert capture: what it secures (public site, RDS gateway, VPN, LOB app, code signing, device/802.1X), where installed, issuer (public CA vs internal CA vs ACME/Let's Encrypt), expiry date, renewal owner (MSP/client/vendor/automation).
2. Harvest observed certs by reading the environment's posture in Liongard where enabled (best live source): first confirm the relevant inspectors exist and last ran successfully (TLS/SSL, IIS, Windows, domain), then read the cert names and expiry dates and the recent cert-change history. State the dataprint age with every Liongard value; skip any inspector whose last run failed and say so.
3. Sweep ticket history for the undocumented: check for past cert incidents/renewals (a cert that caused a ticket ~2 years ago is due again about now). Report capped searches as "at least N".
4. Merge into the register: cert (by what it secures — avoid pasting full subject strings that embed internal hostnames), location, issuer, expiry, renewal owner+method, evidence source and freshness. List auto-renewing (ACME) certs but mark "verify automation is alive" rather than trusting blindly.
5. Build the expiry calendar: sort by date; band into expired / <30d / 30-90d / later. Expired or <30d -> open a ticket now; 30-90d -> schedule a follow-up ticket with lead time matched to renewal method (internal-CA and vendor-managed need more runway than a public-CA reissue). Each ticket names the renewal owner and links the applicable runbook (check the knowledge base for the desk's procedure). Do not invent runbook links; if none exists, the ticket says so and requests one.
6. Output the register + calendar + tickets opened, and leave a plain-text summary note (no markdown/emojis). Include a known-unknowns section: cert classes you could not enumerate (device/802.1X fleets, LOB apps with no inspector or docs), so the register is never mistaken for complete.

Guardrails: never present the register as exhaustive — certs hide in appliances and LOB apps. Every expiry date carries its source and freshness — never from memory or inference. Private keys, PFX passwords, and CA credentials are never copied into notes or the register — reference the secure store by name only. Renewals on load balancers / RDS gateways / LOB apps can take services down — those carry a window recommendation, not "just replace it". If neither Liongard nor docs are available, build from ticket history alone, label it "reconstructed, unverified", and lead with a discovery-scan recommendation.
```
