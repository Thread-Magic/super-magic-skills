---
name: SSL Inspection Issues
description: Diagnose TLS/SSL inspection breakage: pinned apps failing, firewall certificate warnings, apps broken only on corporate networks, and bypass routing.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# SSL Inspection Issues

**When to use:** An app or agent fails on the corporate network but works on a hotspot/home network; certificate warnings where the issuer is the firewall/security product rather than a public CA; a wave of "app X stopped working" tickets right after new inspection was rolled out (firewall replacement, SSE/proxy agent); or dev tools, package managers, or update mechanisms failing with certificate or chain errors.

**Run it:** on the one ticket you're working — a tech gathers evidence and routes bypass requests to the security owner; not unattended.

## Prompt

```
When a security appliance decrypts and re-signs TLS, everything that verifies certificates
strictly notices. The tell is in the certificate chain, and the fix is almost never "turn
inspection off" — it is a scoped, approved bypass or a trust-store fix.

Climb the Troubleshooting Ladder base skill first: past tickets for the failing app — a
cluster starting on one date marks the day inspection was enabled or changed, and old
tickets may name the bypass process; documentation for which product inspects (firewall,
cloud proxy/SSE agent, endpoint agent), whether the root CA reaches trust stores, the
bypass list, and who approves it; an undocumented bypass process is its own gap.

Read the chain: no verdict without it. In a browser, view the certificate for the failing
site; elsewhere, have the tech run openssl s_client against the endpoint from the affected
network. Issuer equal to the security product's CA means inspection is in the path; a
chain that changes on and off the corporate network is the proof.

1. Pinned application — the app expects its vendor's certificate and gets the inspection
   CA, so errors are generic ("can't connect"), not certificate-flavoured — hence the
   on-and-off comparison. There is no trust-store fix for pinning: compile the vendor's
   published exemption list, never guessed domains, and submit it as a bypass request.

2. Missing root in a tool's trust store — the OS trusts the inspection CA but one tool
   doesn't: Java keystores, Python and pip, Node, git, container images. Add the
   inspection root by that tool's documented method — the sanctioned fix, not a
   workaround. Escalate for BYOD or unmanaged devices: a private root on personal machines
   is the client's call.

3. Inspection breaking the protocol — mutual TLS dies under inspection by design, along
   with non-HTTP protocols on 443 and newer TLS features the appliance mishandles. Same
   bypass path, protocol reason documented; broad mishandling of standard traffic is a
   vendor case.

4. Expired or broken inspection CA — everything breaks at once, or only for machines that
   never received the root (commonly non-domain ones). Escalate immediately to the
   security product owner; this is their outage. Expiry on the client's own public sites
   is the SSL Certificate Renewal playbook.

Every bypass is a security decision: scoped to the vendor's documented endpoints and never
a wildcard "to be safe", justified in writing, approved by the security owner, and
recorded. The desk requests; it does not apply. Never recommend disabling inspection
globally, and never route around it with a VPN or hotspot — that trades a ticket for a
blind spot.

Re-test from the affected network and confirm the chain. Note it (apply the PSA Note
Discipline base skill): issuer on and off network, branch, documentation cited, what was
requested versus applied, who approved.
```
