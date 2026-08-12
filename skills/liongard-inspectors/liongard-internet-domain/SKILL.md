---
name: Liongard Internet Domain & TLS Read
description: Answer domain, DNS, and certificate questions from Liongard's Internet Domain/DNS and TLS/SSL inspectors — registrar and expiry, DNS record changes, mail-auth records, and cert-expiry sweeps across one client or all of them.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_domain, liongard_metric, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: both
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Internet Domain & TLS Read

**When to use:** "When does <client>'s domain expire / where is it registered?", "did their DNS change?" (MX/SPF/DKIM/DMARC/NS context on a mail or outage ticket), "which certificates expire in the next 30/60/90 days?" per client or across all clients, or a pre-QBR domain-hygiene check.

**Run it:** on one client's domains · or as a cert-expiry sweep across every client.

## Prompt

```
Answer a domain / DNS / certificate question for CLIENT_NAME (or across all clients) from the Liongard Internet Domain/DNS and TLS/SSL inspectors. Read-only.

1. Find the Internet Domain/DNS and TLS/SSL inspectors and confirm they ran recently; date the data. These are external reads (no on-prem agent) and exist per monitored domain — enumerate which of the client's domains are actually watched and say so; the unwatched second domain is a standing blind spot. The reconciled domain inventory gives the cross-client view.
2. Read the values from the latest dataprint, verifying every field angle against the live dataprint:
   - Registration → registrar, creation/expiry dates, registrant org, name servers, registrar-lock status. Expiry within 60 days or an unlocked domain is a flagged finding with a recommended ticket. Do expiry math against today's date and show it ("expires <date>, N days out").
   - DNS state and changes → current MX, SPF, DKIM selectors, DMARC policy, NS records; check what changed and when. On a mail-flow ticket this is answered first. Unexpected NS or registrar changes are hijack-shaped and escalate — a hijack looks exactly like an unannounced migration.
   - Cert sweep (single client) → certs by expiry date, issuer, and covered names.
   - Cert sweep (all clients) → certs expiring within N days across every TLS/SSL inspector, grouped by client, worst-first. Offer to open a ticket per expiring cert on the right client with expiry date and covered names — one ticket each, only on confirmation, deduplicated against open tickets first.
   - Open-ended → ask in plain language ("which domains have no DMARC record?"), verified before reporting.
3. External-read caveat: these inspectors see public DNS and presented certs only — internal-only certs and split-horizon DNS are invisible; never claim full cert coverage from this sweep alone. Output: answer, evidence rows, data as-of timestamps, monitored-vs-unmonitored scope statement. Notes are plain-text only. Degradation: inspectors absent → public WHOIS/DNS is NOT a substitute (no instrumentation, no history) — recommend adding the inspectors and answer only what tickets/documentation attest.
```
