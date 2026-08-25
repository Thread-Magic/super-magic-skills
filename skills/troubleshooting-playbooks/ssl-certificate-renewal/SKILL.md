---
name: SSL Certificate Renewal
description: Handle SSL and TLS certificate renewals: browser warnings, service certificate expiry, issuer-specific renewal paths, and required service restarts.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# SSL Certificate Renewal

**When to use:** Users report certificate warnings on a site, portal, or internal service; an expiry alert fires (monitoring, issuer email, or expiry sweep); a "renew the cert for <service>" request comes in; or after a renewal some clients still see the old/broken cert.

**Run it:** on the one ticket you're working — a tech works the renewal and schedules the swap with the client; not unattended.

## Prompt

```
Certificates are a fleet discipline, not a fire drill: verify what is actually expiring
and where it is installed, follow the issuer's path, and plan the swap.

Climb the Troubleshooting Ladder base skill first: last year's renewal ticket documents
the path and the gotchas — reuse it. Then the client's documented certificate inventory:
issuer, every place the cert is installed (load balancer, web server, firewall portal,
mail gateway), key and CSR custody, renewal ownership. If none exists, recommend
building one.

Then inspect the certificate the endpoint actually serves (browser or openssl): expiry,
subject and SANs, chain completeness. A "certificate error" is often clock skew, an
incomplete chain, or a name mismatch rather than expiry — fix the real defect.

Sweep while you're here: certs bought together expire together, so check the inventory
or the host's other listeners for siblings expiring in the same window.

Branch by renewal path:

- ACME or Let's Encrypt — an expired auto-renew cert means the automation failed, so the
  fix is the automation. Check the renewal service's logs and the challenge path: an
  HTTP challenge blocked by a redirect or firewall change, or a DNS challenge with
  revoked API credentials. A manual renew alone re-books this ticket in 60-90 days.
- Commercial CA — generate a fresh CSR on or for the terminating device, submit per the
  CA's process, complete validation. Set honest timelines: DV by email or DNS is quick,
  OV and EV org checks take days. Never reuse a key that may be compromised.
- Internal CA — renew via the client's own PKI procedure, and check the CA's own
  lifetime while you are in there. Internal-CA certs failing on non-domain devices are a
  trust distribution problem, not a certificate problem.
- Vendor-managed — the cert lives inside a SaaS or appliance the client doesn't control.
  Only the vendor can renew it: open the case, say so plainly, and track it.

Then plan the swap. Installing a cert is not deploying it: enumerate every service that
must reload to pick it up (web server, mail services, VPN portal, load balancer) and
schedule those restarts with the client, because some drop sessions. Install the full
chain including intermediates, and clear the old cert's other installations so one
renewal doesn't leave three stale copies.

Private keys and PFX passwords are credentials — never put one in a ticket note or an
email; secure channel only. Never disable certificate validation, advise clicking
through a warning, or extend trust to a broken cert; the only acceptable interim is
honest downtime communication.

Verify from an external client after the swap: new expiry, complete chain, all SANs,
every endpoint serving the name. Note it (apply the PSA Note Discipline base skill):
cert, issuer path, everywhere installed, restarts performed, sweep results,
verification.
```
