---
name: DHCP Server Issues
description: Diagnose DHCP problems — APIPA 169.254 addresses, wrong-subnet leases, scope exhaustion, stuck failover pairs, and rogue DHCP servers on the LAN.
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
ipconfig /all on an affected machine is the first evidence: address, lease times and the
"DHCP Server" field say whether this is no answer, the wrong answerer or the wrong answer.

Climb the Troubleshooting Ladder base skill first: past DHCP or "no network" tickets and
what changed (new AP or ISP router, VLAN work, a lease cleanup), then the documented design
— DHCP servers, scope ranges, failover, IP helper/relay location, reservation conventions.
Where Liongard covers it, use its inspector data and timeline (Inspector Read Discipline
base skill). Then release and renew and watch what answers; read scope stats, the event log
(1020, 1046, failover) and the lease list.

Branch:
1. APIPA or no answer at a site or VLAN — service down, scope deactivated, or a broken
   relay. Broadcasts don't cross VLANs without an IP helper: if the server's own VLAN leases
   fine and a remote one doesn't, it's the relay — the network owner's if they manage it.
2. Exhaustion (new devices fail, stats near 100%) — compare lease duration to churn; an
   8-day default on a guest or BYOD VLAN exhausts fast, and outages leave stale leases. In
   order: shorten the lease, widen the range, clear expired leases — never active ones,
   which forces conflicts. Re-addressing escalates.
3. Wrong answer (unexpected range, wrong gateway/DNS) — read the "DHCP Server" field.
   Unsanctioned means a rogue, usually a consumer router or an AP in router mode: trace its
   MAC in the switch table, repatch it, recommend DHCP snooping. An untraceable rogue is the
   network owner's, with the MAC evidence. If sanctioned, fix the scope options — wrong DNS
   pairs with the internal DNS playbook.
4. Failover unhealthy — read both partners' state. Communication-interrupted with both up is
   connectivity or time between them; partner-down means one is truly gone, and the survivor
   takes full control only after the MCLT elapses or an operator confirms. Never rebuild or
   deconfigure failover as a quick fix, and never add an overlapping scope — a
   self-inflicted rogue.
5. Reservation vs exclusion — a reservation pins one IP to one MAC (device stays on DHCP);
   an exclusion just stops the server handing that range out. Still leasing elsewhere after
   a reservation: wrong MAC or another scope. Conflicts on "static" gear: the address sits
   in the pool unexcluded. Fix per the documented convention.

Never restart the DHCP service or deactivate a scope to test a theory, and let the network
owner approve scope-option changes; a typo in gateway or DNS is a site outage. AD
authorization guards only against rogue Windows DHCP servers — consumer gear never asks AD.
Verify: the machine renews the right address and options from a sanctioned server, or scope
stats show headroom. Note it (PSA Note Discipline base skill): symptom, evidence, branch,
action or handoff, verification.
```
