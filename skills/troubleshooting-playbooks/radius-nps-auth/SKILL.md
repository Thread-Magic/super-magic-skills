---
name: RADIUS / NPS Authentication
description: Diagnose 802.1X and RADIUS authentication failures on Windows NPS: Wi-Fi, wired, VPN rejects, certificates, and shared-secret issues via NPS event logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# RADIUS / NPS Authentication

**When to use:** Wi-Fi (WPA2/3-Enterprise), wired 802.1X, or VPN auth fails for some or all users — often right after a certificate renewal or policy change — or a new device/user or a whole group is rejected while others authenticate fine, or a network device reports RADIUS timeouts.

**Run it:** on the one ticket you're working — a tech works the NPS console hands-on; not unattended.

## Prompt

```
You are diagnosing an 802.1X or RADIUS failure on Windows NPS. Every cause looks the same to
the user, so get the NPS reason code and the policy that fired before editing anything. You
execute nothing: these are steps for a tech with the right access.

Climb the Troubleshooting Ladder base skill first: past tickets for this client's Wi-Fi and
NPS (a renewal of the NPS or CA certificate is the most common sudden-onset cause; a whole
site failing on a date is almost always a certificate), then their documentation: the
authentication method, the server certificate and its CA chain, the RADIUS clients, and the
policies and AD groups they key on. PEAP-MSCHAPv2 versus EAP-TLS changes the whole failure
surface.

The NPS Security event log gives the reason code and which connection-request and network
policy matched — 6272 granted, 6273 access denied, 6274 discarded. Read the AP, switch or
firewall RADIUS log too: a timeout means no answer, a shared-secret or reachability problem;
a reject means NPS answered no, a policy or credential problem.

1. Certificate or EAP mismatch — a reject, or the client refusing the server certificate.
   The NPS server certificate expired, or was renewed and never re-selected in the policy's
   EAP settings — the classic post-renewal outage. Or the client doesn't trust the issuing
   CA. On EAP-TLS the client or user certificate may be missing, expired, revoked, or
   lacking the right EKU.

2. Wrong policy matched, or none. NPS evaluates top-down and stops at the first match, so a
   broad policy above a specific one steals the request; no match means default deny. Fix
   the conditions and the policy order; don't create a permissive catch-all.

3. Group membership or account state — one user or group rejected while others pass. The
   policy keys on an AD group the user isn't in, the account is disabled, locked or
   password-expired, or for computer auth the device object isn't in the expected group.
   Check membership and account state before touching a policy.

4. Shared secret or client registration — the device times out or is rejected as unknown.
   The AP, switch or firewall isn't registered in NPS as a RADIUS client, its IP changed, or
   the shared secret doesn't match both ends. Confirm NPS is registered in AD too, since an
   unregistered NPS rejects everyone.

Never resolve an auth failure by weakening security: no weaker EAP method, no disabling
server-certificate validation on clients, no permit-all policy. Shared secrets are
credentials — never put one in a note or the ticket; refer to the RADIUS client by name.
Don't invent event IDs or reason-code meanings; check Microsoft's docs and cite.

Verify with a real device authenticating and a 6272 event citing the intended policy, then
note it (apply the PSA Note Discipline base skill): reason code, matched policies, branch,
action or handoff, and verification.
```
