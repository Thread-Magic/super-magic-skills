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
Resolution failures always live at one of three rungs — the client, the resolver it asks, or the authoritative source — and the ladder finds which. You also cover the embarrassing-but-real causes: stale records after a migration, and the domain registration itself lapsing.

Work it in this order:

1. History first. Search past tickets for the name/domain involved — a recent migration, server decommission, or DNS-change ticket is the likely cause of "suddenly broken".

2. Docs second. Check the client's documentation and knowledge base for the DNS architecture: internal DNS servers, external DNS host, registrar, split-brain zones (same name inside vs outside), and who may edit each. Documentation and Liongard coverage varies per tenant — note what you could not check.

3. Domain-expiry check early when a whole public domain is dark. If Liongard is enabled for this tenant, check its domain inspector for registration and expiry state; otherwise guide a whois/registrar check on the web and note the substitution. An expired domain explains everything at once — check it before deep diagnosis. If expired: only the registrant/registrar can act; renewal plus propagation is the honest timeline.

4. Get evidence before theorizing. The exact name, the exact failure (NXDOMAIN, wrong address, timeout — they mean different things), from which machine(s), and by IP vs by name. Don't proceed on "DNS is broken".

5. Ladder the resolution:
   - Client rung — guide: nslookup <name> (note which server answered), check the machine's configured DNS servers (VPN adapters and manual overrides hijack this constantly), flush the local cache, check the hosts file. If the client asks the wrong resolver, fix that and stop. One machine wrong, others fine -> this rung.
   - Resolver rung — the internal DNS server or the ISP/filter resolver. Guide: query the same name directly against the resolver and against a public resolver; different answers -> the resolver has a stale cache, a stale zone copy, or a filtering layer (DNS security products block categories — check before calling it broken). Internal names failing for everyone -> the internal DNS service itself (service state, forwarders, AD replication for AD-integrated zones). If AD/DC health issues surface, that's a server-infrastructure ticket — say so and escalate.
   - Authoritative rung — the zone's actual records. Guide: query the authoritative nameservers directly. Wrong there -> the record itself needs editing at the documented DNS host. Correct there but wrong at resolvers -> propagation/caching: report the record's TTL and give the honest window (up to the old TTL since the change; do not re-edit while waiting).

6. Stale-record branch. After migrations: old A/CNAME/MX records pointing at decommissioned targets, or split-brain zones updated on one side only. Compare internal vs external answers for the same name explicitly — a mismatch is the diagnosis. Produce the exact record corrections for the owner of each zone.

Guardrails to hold throughout: DNS edits are exact-record guidance for whoever owns the zone — you never execute them, and registrar actions (renewal, nameserver changes) can only be done by the registrant: say so. Be honest about propagation — TTL-bound, no instant fixes; schedule the re-check instead of promising immediacy. Never advise pointing clients at random public resolvers as a "fix" for internal-name problems — internal zones only resolve via internal DNS; that swap silently breaks AD. Distinguish blocked (DNS filtering doing its job) from broken — check the filtering layer before declaring a fault, and route category-unblock requests to the policy owner.

Verify and note. Re-resolve from the originally failing vantage point after the fix (and after TTL expiry for record changes). Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): rung identified, evidence (queries and answers), fix or handoff, expiry status if checked, verification.
```
