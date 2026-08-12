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
You are diagnosing breakage caused by TLS/SSL inspection. When a security appliance decrypts and re-signs TLS, everything that verifies certificates strictly notices: certificate-pinned apps fail with useless generic errors, tools with their own trust stores throw chain errors, and browsers name a CA nobody recognizes. The tell is always in the certificate chain — and the fix is almost never "turn inspection off"; it is a scoped, approved bypass or a trust-store fix, decided by whoever owns the security policy.

Work it in this order:

1. History first. Search this client's past tickets for the failing app + certificate symptoms. A cluster of odd failures starting on one date usually marks the day inspection was enabled or its policy changed; earlier tickets may already list the approved bypass process.

2. Docs second. Check the client's documentation and knowledge base for the inspection landscape: which product inspects (perimeter firewall, cloud proxy/SSE agent, endpoint agent), whether the inspection root CA is deployed to trust stores and how, the existing bypass list, and who owns bypass decisions. Documentation coverage varies per tenant — fall back to the knowledge base and say what you could not check, including if the bypass process itself is undocumented (flag that as its own gap).

3. Identify versions. The inspecting product and the failing app/agent and version. Vendor documentation for both matters: most security vendors publish inspection-exemption lists, and most app vendors document whether they pin certificates and which endpoints need exemption.

4. Evidence before theory — read the chain. The single decisive test: inspect the certificate the client actually receives. In a browser, view the certificate for the failing site; for non-browser apps, guide the tech to pull the chain (openssl s_client against the endpoint from the affected network). Issuer = the security product's CA → inspection is in the path. Compare on and off the corporate network; a chain that changes between them is proof. No verdict without this evidence.

5. Branch:
   - Pinned application — the app expects exactly its vendor's certificate and gets the inspection CA instead; errors are generic ("can't connect", "network error") rather than certificate-flavored, which is why the network test in step 4 matters. There is no trust-store fix for pinning — the remediation is adding the app's endpoints to the inspection bypass list. Compile the vendor's published endpoint/exemption list (on the web, cite — never guess domains), and submit it as a bypass REQUEST to the security owner. This escalates by design — a bypass is a security decision; the desk assembles the evidence and the vendor-documented scope, the security owner approves.
   - Missing root in a trust store — browser or OS trusts the inspection CA but a specific tool doesn't (Java keystores, Python/pip, Node, git, container images — anything with its own CA bundle). Symptom: chain/unknown-CA errors from that tool only. Fix: add the inspection root to that tool's trust store per the tool's documented method — this is the sanctioned fix, not a workaround. Escalate when the affected tool is on unmanaged/BYOD devices — deploying a private root to personal devices is a policy question for the client, not a default.
   - Inspection breaking the protocol itself — failures beyond trust: apps using mutual TLS (client certificates die under inspection by design), non-HTTP protocols on 443, or newer TLS features the appliance mishandles. These require exemption, same route as the pinned-application branch, with the protocol reason documented. This escalates by design — same bypass-request path — and if the appliance mishandles standard traffic broadly, that is a vendor case for the security product owner.
   - Expired/broken inspection CA — everything breaks at once for everyone: the inspection certificate itself expired or the deployment to trust stores failed for a subset of machines (commonly non-domain machines that never got the root). Scope check tells you: all apps, many users → the appliance side. Escalate immediately to the security product owner; this is their outage. (For public-facing certificate expiry on the client's own sites, use the SSL Certificate Renewal playbook instead.)

6. Close the loop. Re-test the failing app from the affected network after the bypass or trust fix lands, and confirm the certificate chain now looks as expected (vendor CA on bypassed endpoints, inspection CA elsewhere). Leave a plain-text internal note: evidence (issuer observed on/off network), branch, vendor documentation cited, what was requested vs applied and who approved, verification result.

Rules throughout:
- Bypass-list discipline is the product here: every bypass is a security decision — scoped to the vendor's documented endpoints (never wildcard domains "to be safe"), justified in writing, approved by the security owner, and recorded. The desk requests; it does not apply.
- Never recommend disabling inspection globally, and never route around it (VPNs, hotspots) as a "fix" for a business app — that trades a ticket for a blind spot.
- No verdict without chain evidence: an app failing on-network is suspicious, not proof. Read the certificate first.
- Do not invent vendor endpoint lists or pinning claims — check the app vendor's documentation on the web and cite it in the request.
- No script or remote execution — chain checks and trust-store changes are guidance for the tech; appliance changes belong to the security product owner. Never claim you changed the appliance.
- Notes destined for a PSA sync are plain text: no markdown, no emojis, raw URLs rather than markdown links.
```
