---
name: VPN Troubleshooting
description: Diagnose VPN issues: won't connect, authenticates then no traffic, drops while remote, or can't reach resources by name via a client and DNS matrix.
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
VPN failures live in four places: client, authentication, transport, and name
resolution.

Climb the Troubleshooting Ladder base skill first: past VPN tickets for this user and
client (one user recurring points at their home router or ISP; many users at once is a
head-end, certificate, or identity outage — an incident), then the documented VPN
standard: vendor, client, gateway, auth method (SAML/MFA, certificate, PSK), split vs
full tunnel, DNS suffix. Get the client and OS versions — a mismatch against the
head-end is a top cause after a firmware upgrade. Then the exact client error and its
log: pin which stage fails — connect, authenticate, tunnel up, or traffic.

a. Authentication (SAML, MFA, certificate). Can the user sign in to other SSO apps? That
   isolates identity from VPN. An MFA loop is usually a stale cached token or a
   conditional-access change — pair with the M365 sign-in playbook when the IdP is
   Entra. For certificate auth, check cert expiry on the device. Escalate to whoever
   owns the IdP when a policy change broke all VPN users; a fault inside the vendor's
   SAML implementation is only theirs to fix.

b. Transport and NAT-T — times out, or dies at the same point every time. IPsec from
   home needs NAT traversal on UDP 4500 and IKE on UDP 500, and some routers and ISPs
   mangle them. Try a phone hotspot: if that works, the home router or ISP is the cause
   — disable SIP ALG or enable IPsec passthrough, or move to a TLS transport if the
   platform supports one. Escalate when the head-end firewall started dropping NAT-T
   after a firmware change.

c. Drops while working from home. Ladder: Wi-Fi signal, then the router (SIP ALG,
   session timeouts), then the ISP (CGNAT). Also power settings suspending the NIC, and
   DTLS or keepalive intervals. Change one thing at a time. Multiple remote users
   dropping at the same clock interval is a head-end idle timeout or license limit, not
   their homes.

d. Split-tunnel routing — tunnel up, some resources unreachable. Check what the
   documentation says belongs in the tunnel; a resource outside those routes will never
   work by design. Escalate when the route or ACL push is wrong for everyone — a config
   change request, not a per-user fix.

e. Name resolution — reachable by IP, not by name. Check the tunnel adapter picked up
   the internal DNS servers and search suffix, then nslookup <server> <internal-dns-ip>:
   if the resolver answers over the tunnel, the adapter's DNS or suffix list is wrong.
   Switch to the DNS playbook when internal DNS itself is unhealthy.

Firewall and head-end changes are never "just do it" guidance — flag them for whoever
owns the device, with the evidence.

Verify by having the user reach the resource that failed, not just a green icon. Note it
(apply the PSA Note Discipline base skill): stage, error code, branch, fix or handoff,
verification.
```
