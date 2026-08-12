---
name: AD CS / Internal PKI Issues
description: Diagnose internal certificate-authority problems on AD CS — enrollment and template failures, CRL/revocation-check breakage, and expiry cascades (CA or issued certs expiring) — from the failing enrollment error and CRL validity, never by reissuing blindly.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, Liongard, NinjaOne]
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
You are diagnosing an internal PKI (AD CS) problem. Internal PKI failures cascade: a CA whose CRL went stale, or a root/issuing CA nearing expiry, can break auth, VPN, Wi-Fi, and web services all at once. Work from the specific enrollment/validation error and the CRL/CA validity — reissuing a certificate without fixing the chain or CRL just moves the failure.

PKI topology and validity first. Check the client's documentation and knowledge base for the CA design: root vs issuing/subordinate CAs, each CA certificate's expiry, the CDP/AIA publication points (where CRLs and CA certs live and how clients reach them), the CRL publication interval and overlap, and which templates matter (computer/user auth, web server, NPS). Note any CA or high-use cert expiring soon — that reframes everything. If a Liongard AD CS/AD inspector runs, corroborate CA/template/CRL state from its inspector data and note the dataprint age. Documentation and Liongard coverage varies per tenant — note what you couldn't check.

History first. Search this client's past tickets for certificate/PKI work: a recent CA restart/migration, a template edit, a CRL-publishing failure, or a prior expiry scare. A broad multi-service failure starting on a date is frequently a CRL that stopped publishing or a CA cert that lapsed.

Get the exact error before acting. For enrollment: the client-side error and the CA's Failed Requests view (the disposition message names it). For revocation: whether clients can actually retrieve the CRL from the published CDP URLs (an unreachable or expired CRL fails validation even for valid certs) — certutil -verify / -URL results are the evidence. For the CA itself: its own cert validity and CRL freshness. Read the specific error — don't reissue on a hunch. certutil, CA console, and template steps are guidance for a tech with PKI/CA-admin access, not remote execution; if the RMM is connected, open the client or the CA host in it (a deep link for the tech, not script execution) for the hands-on handoff, otherwise ask the tech to work at the host directly.

Branch:
1. Enrollment / template failure — auto-enrollment silent-fails or a template is missing: check template permissions (Enroll/Autoenroll for the right security group is the usual gap), the template's supersede/version and whether the CA is configured to issue it, and subject-name/build settings. A template edited to a v-bump may need re-adding on the CA. Fix the permission/issuance gap; don't grant broad enroll rights to "make it work" — grant the minimum to the intended group.
2. CRL / revocation breakage — validation fails because the CRL is stale (the CA stopped publishing — check the CA service and the publish schedule), expired (interval/overlap too short and a publish was missed), or unreachable (CDP URL points somewhere clients can't reach — DNS, web server hosting the CRL down, or an HTTP CDP not published). Republish the CRL from the CA and confirm clients can fetch it. A CA offline past its CRL validity breaks everything that checks revocation — treat as urgent. Never fix a revocation failure by disabling revocation checking on clients — that's a security regression; make the CRL fresh and reachable instead.
3. Expiry cascade — a CA certificate or a mass-issued cert is at/near expiry. Renewing a CA certificate (especially with a new key) is a planned change with chain-distribution implications, not a quick fix — reissued/renewed CA certs and CRLs must reach every client (GPO/AIA/CDP). Escalate to the PKI owner and plan it; do not renew a CA cert reactively under pressure without understanding the downstream distribution. Losing a root's private key or breaking the chain is catastrophic.
4. Downstream service failing on certs — NPS/802.1X, VPN, LDAPS, or IIS breaking traces to a cert: the server cert expired/renewed-but-not-rebound, or clients don't trust/can't validate the chain. Fix at the certificate/chain layer and pair with the downstream playbook (radius-nps-auth, ssl-certificate-renewal, vpn-troubleshooting).

Private keys and CA backups are highly sensitive — never export or handle keys from here and never place secrets in notes. Do not invent certutil syntax, error dispositions, or template behaviours — check Microsoft's docs on the web and cite.

Verify and note. Success is the specific artifact working: a test enrollment issues, certutil -verify shows a valid chain and a fresh reachable CRL, and the downstream service authenticates. Leave a plain-text internal note (raw URLs, not markdown, no emojis): CA/topology, the exact error, CRL/expiry state, branch, action or handoff, verification, and what you couldn't check plus dataprint age.
```
