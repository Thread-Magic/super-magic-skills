---
name: DNS & Domain Issues
description: Diagnose DNS resolution and domain-expiry problems by laddering client to resolver to authoritative — stale records, intranet failing, whole domain dark.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search, liongard_domain]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# DNS & Domain Issues

**When to use:** A user can't reach a site or server by name but others can (or by IP works); internal names resolve wrong or not at all and new DNS changes "aren't taking effect"; the client's public website or mail is suddenly unreachable for everyone; or someone asks "did our domain expire?" (or wants a pre-emptive domain/record hygiene check).

**Run it:** on the one ticket you're working — a tech ladders the resolution hands-on and hands DNS edits to the zone owner; not unattended.

## Prompt

```
Resolution failures live at one of three rungs — the client, the resolver it asks, or the
authoritative source. Ladder them to find which.

Climb the Troubleshooting Ladder base skill first: past tickets for the name or domain (a recent
migration, decommission or DNS change is the likely cause of "suddenly broken"), then the
client's documentation for the DNS architecture — internal and external DNS hosts, registrar,
split-brain zones, and who may edit each. Get the evidence: the exact name, the exact failure
(NXDOMAIN, wrong address and timeout differ), from which machines, and by IP versus by name.

Check domain expiry early when a whole public domain is dark: Liongard's domain inspector where
it is enabled, otherwise whois or the registrar, noting the substitution. An expired domain
explains everything at once; only the registrant or registrar can act, and the honest timeline
is renewal plus propagation.

Then ladder:

1. Client rung — run nslookup and note which server answered, check the machine's configured DNS
   servers (VPN adapters and manual overrides hijack this constantly), flush the local cache,
   check the hosts file. One machine wrong while others are fine is this rung: if it asks the
   wrong resolver, fix that and stop.

2. Resolver rung — the internal DNS server, or the ISP or filtering resolver. Query the same name
   against it and against a public resolver. Different answers mean a stale cache, a stale zone
   copy, or a filtering layer; DNS security products block by category, so distinguish blocked
   from broken and route unblock requests to the policy owner. Internal names failing for
   everyone points at the internal DNS service: service state, forwarders, AD replication. AD or
   domain-controller health is a server-infrastructure ticket — escalate it.

3. Authoritative rung — query the zone's nameservers directly. Wrong there means the record needs
   editing at the documented DNS host. Correct there but wrong at resolvers is propagation:
   report the record's TTL, give the honest window, and do not re-edit while waiting.

4. Stale records — after a migration, look for A, CNAME or MX records pointing at decommissioned
   targets, or a split-brain zone updated on one side only. Compare internal and external answers
   for the same name; a mismatch is the diagnosis. Produce the exact record corrections for each
   zone's owner.

DNS edits are exact-record guidance for the zone owner; only the registrant can take registrar
actions. Never point clients at a public resolver to "fix" internal names — internal zones
resolve only via internal DNS, and that swap silently breaks AD.

Verify by re-resolving from the failing vantage point, after TTL expiry for record changes. Then
leave a plain-text internal note (apply the PSA Note Discipline base skill): rung, queries and
answers, fix or handoff, expiry status, verification.
```
