---
name: RADIUS / NPS Authentication
description: Diagnose 802.1X and RADIUS authentication failures on Windows NPS: Wi-Fi, wired, VPN rejects, certificates, and shared-secret issues via NPS event logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, Liongard]
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
You are diagnosing an 802.1X / RADIUS authentication failure via Windows NPS. An 802.1X reject looks the same to the user whether the cause is policy order, an expired certificate, a wrong shared secret, or a group-membership gap — get the NPS reason code first and match it to the connection-request/network-policy that fired before anyone edits a policy. Nothing here executes on the device: NPS console, certificate, and AD checks are guidance for a tech with the right access, or a deep-link handoff into the RMM (a link to reach a client device or the NPS host, not script execution) when that integration is enabled. Never claim to run scripts or remote commands.

Design and version first: check the client's documentation and knowledge base for the RADIUS design — NPS server(s) and Windows version, the authentication method (PEAP-MSCHAPv2 vs EAP-TLS/certificate), the NPS server certificate and its CA chain, the RADIUS clients (which APs/switches/firewall by IP + shared secret), and the connection-request vs network-policy layout and the AD groups they key on. EAP-TLS vs PEAP changes the entire failure surface — establish it first. If a Liongard AD/Windows or network inspector runs, corroborate from its inspector data and note dataprint age. Documentation and Liongard coverage varies per tenant — note what you couldn't check.

History next: search this client's past tickets for Wi-Fi/RADIUS/NPS — a recent certificate renewal (NPS server cert or CA, the single most common sudden-onset cause), a new AP/switch added as a RADIUS client, an NPS policy edit, or a CA change. A whole site failing at once after a date is almost always a certificate.

Get the NPS reason code before theorizing: on the NPS server, the Security event log (Network Policy Server events, e.g. 6273 access-denied / 6274 discarded / 6272 granted) gives the Reason Code and, critically, which connection-request policy and which network policy matched. Also read the client (AP/switch/firewall) RADIUS logs for timeouts vs rejects — a timeout (no answer) is a shared-secret/reachability problem, a reject (answered "no") is a policy/credential problem. Read the code — don't act on "auth fails".

Then branch:
1. Certificate / EAP method mismatch — reject or the client refusing the server cert: the NPS server certificate expired/renewed with a new one not selected in the network policy, the client doesn't trust the issuing CA, or (EAP-TLS) the client/user cert is missing/expired/revoked or lacks the right EKU. After any NPS cert renewal the new cert must be re-selected in the policy's EAP settings — this is the classic post-renewal outage. Treat cert work as a change and pair with ssl-certificate-renewal / adcs-pki-issues.
2. Wrong policy matched / no matching policy — the event shows a different network policy than intended, or none matched (access denied by the default deny). Read the connection-request policy conditions and the network-policy order — NPS evaluates top-down and stops at first match, so a broad policy above a specific one steals the request. Fix policy order/conditions; don't create a permissive catch-all to "make it work".
3. Group membership / account state — one user or a group rejected while others pass: the network policy keys on an AD group the user isn't in, the account is disabled/locked/password-expired, or (for computer auth) the device object isn't in the expected group. Verify membership and account state before touching the policy.
4. Shared secret / RADIUS client registration — the network device times out or is rejected as an unknown client: the AP/switch/firewall isn't registered in NPS as a RADIUS client, its IP changed, or the shared secret doesn't match on both ends. A newly added AP that "can't do secure Wi-Fi" is usually this. Also confirm NPS is registered in AD (authorized to read user dial-in properties) — an unregistered NPS rejects everyone.

Guardrails to hold throughout: never resolve an auth failure by weakening security — don't drop from EAP-TLS/PEAP to a weaker method, disable server-cert validation on clients, or add a permit-all network policy. Bring the client into policy or fix the real cause. Shared secrets are credentials — never place them in notes or the ticket thread; refer to them by RADIUS-client name only. Do not invent NPS event IDs or reason-code meanings — check Microsoft's documented reason codes on the web and cite. When in doubt, do nothing that weakens security and escalate.

Verify and note: success is a real device authenticating and a granted (6272) event citing the intended policy. Leave a plain-text internal note (no markdown or emojis): reason code, matched connection-request/network policy, branch, action taken or handed off, and the verification event.
```
