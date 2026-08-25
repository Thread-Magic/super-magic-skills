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
"DNS is broken" is four problems: identify which server answered and what, before
theorizing.

Climb the Troubleshooting Ladder base skill first: past DNS tickets and changes — a new or
decommissioned DC, a firewall or ISP change, scavenging someone enabled (vanishing records
on a cycle = scavenging) — then the documented design: DCs running DNS, forwarders, the
internal domain name (the trap: same name as the public domain), DHCP-DNS registration. Add
Liongard's inspector data where it covers this tenant (Inspector Read Discipline base
skill).

Evidence, verbatim: ipconfig /all on the affected machine (one pointed at the router or a
public resolver explains it), then nslookup the failing name against EACH internal DNS
server — do they disagree?

Branch:
a. Wrong resolver — the machine points at the ISP, router or a public service. Domain
   members use internal AD DNS only: a public secondary gives intermittent failures with no
   failback, so never point them at public DNS, even temporarily. Fix at the DHCP scope or
   the NIC per client standard; bad DHCP options are the DHCP playbook.
b. Forwarder failure (internal fine, external dead) — nslookup an external name against each
   forwarder IP. Dead targets (an old ISP resolver, a decommissioned firewall) or outbound
   53 blocked after firewall work: repoint to working, policy-approved targets, and if root
   hints are the fallback confirm outbound 53 isn't filtered. Firewall and ISP fixes are
   their owners'.
c. Stale or missing records — read the zone's aging and scavenging state first. Scavenging
   deletes records whose timestamp exceeds no-refresh plus refresh, so enabling it on a zone
   of old dynamic records mass-deletes on the first pass. Check whether the lost records
   were dynamic or static, and that refresh fits the DHCP lease. Recovery is re-registration
   (ipconfig /registerdns, a DHCP renewal), not rebuilding statics. Never enable or tune
   scavenging as a quick fix, and never delete records to test — both replicate everywhere.
   Settings go to the infrastructure owner with the math.
d. Servers disagree — different answers per DC means the AD-integrated zone isn't
   replicating, a wrong replication scope, or a stray manual zone: hand to the AD
   replication playbook with the query evidence.
e. Split-brain — the internal domain shares a public name: internal users can't reach the
   public site, or a moved service still resolves old. Every public name used internally is
   hand-maintained in the internal zone: inventory what's shadowed, and say the burden is
   permanent. Never forward the apex zone externally — it breaks AD SRV lookups.

Verify the failing lookup returns the right answer from every internal server and the
symptom is gone, then note it (PSA Note Discipline base skill): symptom, which server
answered what, branch, action or handoff, verification.
```
