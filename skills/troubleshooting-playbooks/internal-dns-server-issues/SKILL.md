---
name: Internal DNS Server Issues
description: Fix AD-integrated internal DNS — stale records, external dead while internal works (or reverse), records vanishing — distinct from public DNS/domain.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, liongard_launchpoint, liongard_metric, liongard_timeline, web_search]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Internal DNS Server Issues

**When to use:** Internal names resolve to wrong/old IPs or stop resolving after a weekend, internal resolution works but the internet fails from domain machines (or only at one site), records for live machines keep disappearing, or the client's internal domain overlaps a public one and some names go to the wrong place. (Public records, registrars, SPF/MX belong to the dns-domain-issues and dmarc-spf-dkim-setup playbooks, not this one.)

**Run it:** on the one ticket you're working — a tech drives the lookups hands-on and makes changes with the infra owner's approval; not unattended.

## Prompt

```
You are diagnosing the client's internal AD-integrated DNS servers. The rule: identify which server answered and what it answered before theorizing — "DNS is broken" is four different problems. Work these in order.

1. History first. Search this client's past tickets on DNS symptoms and for recent changes: a new DC, a decommissioned DC, a firewall/ISP change, or scavenging "cleanup" someone enabled. Records vanishing on a cycle strongly suggests a scavenging change — find when it started.

2. Docs second. Check the client's documentation and knowledge base for the DNS design: which DCs run DNS, forwarder targets, the internal domain name (is it a .local, a subdomain of the public domain, or — the trap — the same name as the public domain?), and the DHCP-DNS registration setup. If Liongard's Active Directory / DNS-capable inspectors run for this tenant, use its inspector data for zone and forwarder config and its change timeline for recent changes — state the dataprint age. Documentation and Liongard coverage varies per tenant — note anything you could not check.

3. Get the evidence before theorizing. Guide the tech (these are commands the tech runs — you do not execute anything remotely): `ipconfig /all` on an affected machine (which DNS servers is it actually using — a machine pointed at the router or 8.8.8.8 explains "internal names don't resolve" instantly), then `nslookup <name> <specific-DC-IP>` against EACH internal DNS server to see whether they disagree, then the same lookup for an external name. Capture verbatim answers, not "it didn't work".

4. Branch on the evidence:
   a. Client pointed at the wrong resolver — the machine's DNS is the ISP/router/public. Domain members must use internal AD DNS only (public resolvers as secondary cause intermittent, maddening failures because there is no failback). Never point domain members at public DNS, even "temporarily as secondary." Fix at DHCP scope options or the NIC, per client standard. Escalate when DHCP is handing out the wrong DNS servers — pair with the dhcp-server-issues playbook.
   b. Forwarder failure (internal OK, external dead) — on the DNS server, test the configured forwarders directly (`nslookup <external-name> <forwarder-IP>`). Dead forwarder targets (old ISP resolvers, a decommissioned firewall) or blocked outbound 53 after a firewall change. Fix is updating forwarders to working, policy-approved targets; if root hints are the fallback, confirm outbound DNS isn't filtered. Escalate when the firewall/ISP side is not yours to change.
   c. Stale or missing records / scavenging accidents — records for live machines gone, or ancient records answering. Read the zone's aging settings and the server scavenging state before judging: scavenging deletes records whose timestamp exceeds no-refresh+refresh — enabling it on a zone with old static-looking dynamic records mass-deletes on the first pass. Check whether the vanished records were dynamic (timestamped) or static, who registers them (machine vs DHCP "always dynamically update" with the DnsUpdateProxy setup), and whether refresh intervals fit the DHCP lease. The recovery is re-registration (`ipconfig /registerdns`, DHCP renewal), not hand-recreating hundreds of static records that will go stale again. Never enable or "tune" scavenging as a quick fix and never delete records to test a theory — a wrong aging setting or a deletion mass-removes records, and both replicate everywhere. Propose settings with the math (no-refresh + refresh vs DHCP lease) and let the client's infra owner approve; scavenging design is a change-management decision.
   d. Servers disagree (same query, different answers per DC) — AD-integrated zone not replicating, wrong zone replication scope, or a stray secondary/manual zone on one server. This is replication territory — hand off to the ad-replication-issues playbook with the disagreeing servers and the query evidence.
   e. Split-brain traps — internal domain shares the name of (or overlaps) a public domain. Symptoms: internal users can't reach the public website ("www works but <domain> doesn't"), or a public service moved and internal DNS still answers with the old pinned record. Every public name used internally must be maintained by hand in the internal zone. Inventory which public records are shadowed before changing anything, and set honest expectations: this maintenance burden is permanent until the design changes. Never "fix" it by forwarding the apex zone externally — that breaks AD SRV lookups.

If the problem turns out to be public records, a registrar, or mail DNS — that is the dns-domain-issues / dmarc-spf-dkim-setup playbooks, not this one.

Verify and note. Success = the same nslookup that failed now returning the right answer from every internal server, and the end-user symptom gone. Leave a plain-text internal note (plain text, no markdown or emojis, raw URLs not links): symptom, which server answered what (verbatim), branch, change made or handed off, verification queries and time, and anything you could not check (documentation/Liongard coverage, dataprint age).
```
