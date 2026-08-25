---
name: DNS Filtering Alerts
description: Handle DNS-filter block events from Cisco Umbrella, DNSFilter, and similar tools: separate security blocks from category blocks, keep bypass discipline.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# DNS Filtering Alerts

**When to use:** A DNS-filter security alert lands (an endpoint attempted a malware/C2/phishing domain); a user or client asks "why is this site blocked?" or requests unblocking; or a category-change or bypass request needs a decision — for DNS-layer filtering products (Cisco Umbrella, DNSFilter, and equivalents).

**Run it:** on the alert ticket.

## Prompt

```
Triage a DNS-layer filtering event (Cisco Umbrella, DNSFilter, or equivalent). The
discrimination is everything: a security-category block is a detection — something on the
endpoint tried to go there — while a content-category block is a policy event. Bypasses,
allowlist entries and recategorization requests are technician actions you direct and record.

1. Classify the event: security block (malware, command-and-control, phishing, cryptomining,
   newly-seen or DGA domains), content block (social media, streaming, gambling — the client's
   policy), or uncategorized domain.

2. Security-block path — treat it as a detection. Blocked is not done:
   - Identify the source: which device or user made the lookup. With only the site's egress IP,
     the technician identifies the internal source from the filter's console or DHCP/firewall
     logs; say so when attribution is unavailable.
   - A one-off lookup to a phishing domain is usually a clicked link: run phishing-triage on how
     the user got the URL and check for sibling deliveries.
   - Repeated or periodic lookups to C2 or malware domains are a beaconing pattern: treat the
     endpoint as suspect and work edr-detection-runbook on it. Do not close because "it was
     blocked" — the block contains the symptom, not the infection.
   - Check prior tickets (same device or domain class, ~90 days) for recurrence.

3. Category-block complaints: confirm the block reason against the client's documented filtering
   policy. Miscategorized → raise a recategorization request with the vendor, plus a narrow
   temporary allow if the need is business-urgent. Correctly categorized but business-needed →
   this is the client's policy decision, not a desk favor: route it to the authorized approver
   on file. The desk does not loosen a client's policy on a user's say-so.

4. Bypass discipline: narrowest scope (exact domain over wildcard, one user or site over
   global), time-boxed where the need is temporary, named client approver, review date — an
   allowlist that only grows is a policy that no longer exists. Never bypass a security
   category; if someone insists a malware-class block is wrong, escalate the domain for vendor
   recategorization with evidence instead. Verify identity before any user-specific bypass — a
   "please unblock this for me" from a compromised mailbox is a real pattern.

5. Recurring vendor false positives (CDNs, ad networks tripping security categories) go to
   security-noise-tuning under the same narrow-allow discipline.

6. Note the event class, source attribution, verdict, and any allow's scope, approver and
   expiry; classify security-class events per soc-classification-tree.

If the console isn't accessible, name what the tech should pull — query logs, source identity,
category verdict. When in doubt do nothing irreversible and escalate.
```
