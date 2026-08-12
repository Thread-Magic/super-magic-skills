---
name: DHCP Server Issues
description: Diagnose DHCP problems — machines getting APIPA 169.254 addresses, wrong-subnet leases, scope exhaustion, failover pairs stuck, a rogue device answering — starting from what address the client actually received and which server gave it.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, liongard_launchpoint, liongard_metric, liongard_timeline, web_search]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# DHCP Server Issues

**When to use:** Machines getting 169.254.x.x (APIPA) or "no network" on wired/wireless at a site; devices receiving addresses from an unexpected range or with wrong gateway/DNS; "only some machines get addresses" / new devices fail while existing ones work (exhaustion); or a DHCP failover pair showing communication-interrupted or partner-down.

**Run it:** on the one ticket you're working — a tech drives the ipconfig evidence and server checks hands-on, not unattended.

## Prompt

```
You are diagnosing a DHCP problem. The rule: ipconfig /all on an affected machine first — the address, lease times, and "DHCP Server" field tell you whether the problem is no answer, the wrong answerer, or the wrong answer. Never restart the DHCP service as step one.

History first. Search the client/site's past tickets on DHCP or "no network" symptoms and recent changes: a new AP or ISP router installed (rogue-DHCP classic), VLAN work, server maintenance, or a "cleanup" of leases or reservations. Whole-site sudden failure after equipment install points at a rogue or a helper-address change.

Docs second. Check the client's documentation and knowledge base for the network design: which server(s) run DHCP, scope ranges per VLAN, failover configuration, where IP helper / DHCP relay lives, and the client's reservation conventions. If Liongard inspectors cover the DHCP server or network gear, use its inspector data for scope/lease config and its change timeline for recent changes — state the dataprint age. Documentation and Liongard coverage vary per tenant — note anything you could not check.

Get the evidence before theorizing. Guide the tech on an affected machine: ipconfig /all (capture address, subnet, gateway, DNS, lease obtained/expires, and the DHCP Server field), then ipconfig /release + /renew and watch what answers. On the server: scope statistics (percent in use), the event log for events 1020/1046/failover events, and the lease list for the affected subnet. ipconfig/release/renew and server console reads are guidance for the tech to run; there is no remote execution from here.

Branch:
1. APIPA / no answer at one site or VLAN — either the DHCP service/scope is down, the scope is deactivated, or the relay path is broken (IP helper missing/wrong after switch or firewall changes — DHCP broadcasts don't cross VLANs without it). If machines on the server's own VLAN lease fine but a remote VLAN doesn't, it's the relay, not the server. Escalate when the helper/relay lives on network gear managed by another party.
2. Scope exhaustion (new devices fail, stats near 100%) — check lease duration vs device churn (8-day default leases on a guest/BYOD VLAN exhaust fast), and whether a chunk of the range is consumed by stale leases from an event/outage. Remedies in order of preference: shorten lease on high-churn scopes, widen the range, or clean genuinely expired/bad leases. Deleting active leases forces conflicts — don't. Escalate when re-addressing/subnet redesign is the real fix.
3. Wrong answer (unexpected range, wrong gateway/DNS) — read the ipconfig "DHCP Server" field. If it's not a sanctioned server, you have a rogue DHCP — typically a consumer router or an AP in router mode someone plugged in. Locate it via the switch MAC table for that server's MAC and remove/repatch it; where the switching supports it, recommend DHCP snooping so this can't recur. If the server IS sanctioned but options are wrong: fix the scope options (wrong DNS handed out pairs with internal-dns-server-issues). Escalate when you can't trace the rogue — network owner with the MAC evidence.
4. Failover pair unhealthy — read the failover state on both partners before acting. Communication-interrupted with both servers up = connectivity/time between them; partner-down = one is actually gone. Understand the mode (load balance vs hot standby) and MCLT implications: in partner-down, the surviving server only takes full control after the MCLT elapses or an operator confirms partner-down. Do not deconfigure/rebuild failover as a quick fix, and never run two independent overlapping scopes as a workaround — that's a self-inflicted rogue. Escalate when the failed partner needs rebuild/restore.
5. Reservation vs exclusion confusion — device "randomly changes IP" or a static-needed device conflicts. A reservation hands a specific IP to a specific MAC (device stays on DHCP); an exclusion just stops the server from handing that range out (something else is expected to use it statically). Symptoms: reservation created but device still gets a lease elsewhere → wrong MAC or device is inside another scope; conflicts on "static" gear → someone excluded nothing and the static IP sits inside the pool. Fix per the client's documented convention; update the documentation when you correct one.

Never delete active leases, deactivate a scope, or deconfigure failover as a diagnostic step — each one takes clients down. Never stand up a second overlapping scope or an ad-hoc DHCP source as a workaround. Confirm with the client's network owner before changing scope options that affect every device (gateway, DNS) — a typo there is a site outage. AD authorization guards against rogue Windows DHCP servers only — do not treat "server is authorized" as proof no rogue exists; consumer gear doesn't ask AD.

Verify and note. Success = the affected machine completing release/renew with the correct address, options, and DHCP Server field from a sanctioned server; for exhaustion, scope stats back at healthy headroom. Leave a plain-text internal note (raw URLs, not markdown): symptom, ipconfig evidence (server field, address), branch, change made or handed off, verification and time, and what you couldn't check.
```
