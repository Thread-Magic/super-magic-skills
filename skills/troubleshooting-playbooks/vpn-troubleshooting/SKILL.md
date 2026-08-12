---
name: VPN Troubleshooting
description: Diagnose VPN problems — won't connect, authenticates then no traffic, drops while working from home, or can't reach internal resources by name — via a client/auth/transport/DNS matrix.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# VPN Troubleshooting

**When to use:** "<user> can't connect to the VPN" / "VPN connects but nothing loads"; "VPN keeps dropping when I work from home"; "connected to VPN but can't reach <server> by name"; or an MFA/SSO prompt looping during VPN sign-in.

**Run it:** on the one ticket you're working — a tech works it with the user; not unattended.

## Prompt

```
You are diagnosing a VPN problem by separating it into the four places these failures actually live — client, authentication, transport, and name resolution — and giving branch-specific remediation guidance plus escalate-when lines. Remediation is guidance for the tech or user; nothing executes remotely.

1. History first. Search this user's and this client's past tickets for the VPN. Same user recurring -> local environment (home router/ISP). Many users at once -> head-end, certificate, or identity outage; treat as an incident.

2. Docs second. Check the client's documentation and knowledge base for the VPN standard: vendor, client software, gateway address, auth method (SAML/MFA, certificate, PSK), split vs full tunnel, DNS suffix. Documentation coverage varies per tenant — fall back to the knowledge base and say what you could not check.

3. Identify versions — never assume. VPN client name and version, OS version, and whether the client was recently updated. Version mismatch against the head-end is a top cause after firmware upgrades.

4. Get the error before theorizing. Exact client error text/code and the client's own log. "Doesn't work" has at least four meanings — pin down which stage fails: connect, authenticate, tunnel up, or traffic/name resolution.

5. Branch:
   a. Authentication (SAML/MFA/certificate) — fails at sign-in or loops. Check whether the user can sign in to other SSO apps (isolates identity vs VPN). MFA loop -> often a stale cached token or an identity conditional-access change; pair with the M365 sign-in playbook if the IdP is Entra. Certificate auth -> check cert expiry on the device. Escalate when an identity policy change broke all VPN users — route to whoever owns the IdP; if the failure is inside the vendor's SAML implementation, only the vendor can fix it — say so.
   b. Transport / NAT-T — client times out, or connects then dies at the same point every time. From home networks, IPsec needs NAT traversal (UDP 4500) and IKE (UDP 500); some routers or ISPs mangle these. Guide: try a phone hotspot — if that works, the home router/ISP path is the culprit; disable SIP ALG / enable IPsec passthrough on the router, or move the client to a TLS-based transport if the platform supports it. Escalate when the head-end firewall drops NAT-T after a firmware change — network resource, and possibly a vendor case.
   c. "Drops while working from home" — connects fine, dies intermittently. Ladder: Wi-Fi signal -> router (SIP ALG, session timeouts) -> ISP (CGNAT). Also check the laptop's power settings suspending the NIC, and DTLS/keepalive intervals. Guide one change at a time so cause is identifiable. Escalate when multiple remote users drop at the same clock interval -> head-end session/idle timeout or license limit, not the homes.
   d. Split tunnel routing — VPN is up, some resources unreachable. Determine what's supposed to be in the tunnel (the documentation). A resource outside the split-tunnel routes will never work by design — say so rather than chasing it. Escalate when the route/ACL push from the head-end is wrong for everyone — config change request, not a per-user fix.
   e. DNS suffix / name resolution — reachable by IP but not by name. Check the tunnel adapter got the internal DNS servers and search suffix. Guide: nslookup <server> <internal-dns-ip> to prove the resolver works over the tunnel; if it does, the client's adapter DNS config or suffix list is wrong. Escalate when internal DNS itself is unhealthy — switch to the DNS playbook.

   Firewall/head-end changes are never "just do it" guidance — flag them for the resource who owns the device, with the evidence attached. If the defect is in the VPN vendor's client or firmware, state that only the vendor can fix it and offer the documented workaround. Never guess gateway addresses, transport ports, or auth methods — pull from client documentation or ask; do not invent vendor KB articles, verify on the web.

6. Verify and note. Have the user reach the actual resource that failed, not just get a green icon. Leave a plain-text internal note (PSA-safe: no markdown or emojis): stage that failed, error code, branch, fix or handoff, verification.
```
