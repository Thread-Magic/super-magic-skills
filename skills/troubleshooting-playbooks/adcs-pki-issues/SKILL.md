---
name: AD CS / Internal PKI Issues
description: Troubleshoot AD CS internal PKI issues — enrollment and template failures, CRL revocation-check errors, and certificate expiry cascades before reissuing.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# AD CS / Internal PKI Issues

**When to use:** Auto-enrollment or manual enrollment fails, or a template won't offer or issue; "certificate revoked" / revocation-check failures or apps rejecting internally-issued certs; a CA certificate or widely-used issued cert is expiring/expired and things are breaking; or downstream services (NPS/802.1X, VPN, IIS, LDAPS) failing in ways that trace to certificates.

**Run it:** on the one ticket you're working — a hands-on diagnosis a tech drives with CA-admin access, not something to run unattended.

## Prompt

```
You are diagnosing an internal PKI (AD CS) problem. Failures cascade: a stale CRL or a CA
nearing expiry breaks auth, VPN, Wi-Fi and web services at once, and reissuing a certificate
without fixing the chain or CRL just moves the failure.

Climb the Troubleshooting Ladder base skill first: this client's past PKI tickets (a broad
multi-service failure starting on a date is usually a CRL that stopped publishing or a CA
cert that lapsed), then their documentation for the CA design: root versus issuing CAs, CA
certificate expiries, the CDP and AIA publication points, the CRL interval and overlap, and
which templates matter.

Evidence: for enrollment, the client error and the CA's Failed Requests disposition; for
revocation, whether clients can actually fetch the CRL from the published CDP URLs; plus the
CA's certificate validity and CRL freshness.

1. Enrollment or template failure — auto-enrollment silently fails or a template is missing.
   Check template permissions (Enroll and Autoenroll for the right security group is the
   usual gap), the template's version, and whether the CA is configured to issue it. A
   version-bumped template may need re-adding on the CA. Grant the minimum to the intended
   group, not broad enroll rights.

2. CRL or revocation breakage — the CRL is stale (the CA stopped publishing: check the
   service and schedule), expired (interval and overlap too short, a publish missed), or
   unreachable (the CDP URL points where clients can't reach — DNS, the web server hosting
   it, or an HTTP CDP never published). Republish from the CA and confirm clients can fetch
   it. A CA offline past its CRL validity breaks everything that checks revocation — urgent.
   Never fix a revocation failure by disabling revocation checking on clients; make the CRL
   fresh and reachable.

3. Expiry cascade — a CA certificate or mass-issued certificate at or near expiry. Renewing
   a CA certificate, especially with a new key, is a planned change: the renewed CA
   certificates and CRLs must reach every client. Escalate to the PKI owner and plan it;
   never renew reactively under pressure. Breaking the chain or losing a root's private key
   is catastrophic.

4. Downstream service on certificates — NPS/802.1X, VPN, LDAPS or IIS. The server
   certificate expired, or was renewed and never re-bound, or clients can't validate the
   chain. Fix at the certificate and chain layer.

Private keys and CA backups are highly sensitive: never export or handle keys, never put
secrets in notes. Don't invent command syntax or error dispositions; check Microsoft's docs
and cite.

Verify the specific artifact: a test enrollment issues, the chain validates against a fresh
reachable CRL, the downstream service authenticates. Then note it (apply the PSA Note
Discipline base skill): topology, the error, CRL and expiry state, branch, action, and
verification.
```
