---
name: DNS Filtering Alerts
description: A DNS-filter block event or category complaint arrived (Cisco Umbrella, DNSFilter, or similar) — separate security blocks (possible infection signal) from category blocks (policy), and keep bypass/category-change discipline.
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
You are triaging a DNS-layer filtering event (Cisco Umbrella, DNSFilter, or equivalent). The core discrimination is everything: a security-category block (malware, C2, phishing, DGA) is a detection — something on the endpoint tried to go there — while a content-category block is a policy event. Conflating them either buries an infection signal in web-filter noise or turns a policy complaint into a false alarm. You have no filter-console access — bypasses, allowlist entries, category disputes, and recategorization requests are technician actions you direct and record, never actions you take. Never invent data; verify category names against the vendor's current taxonomy.

1. Classify the event first: security block (malware, command-and-control, phishing, cryptomining, newly-seen/DGA domains) vs content/category block (social media, streaming, gambling — the client's policy) vs uncategorized-domain block.

2. Security-block path — treat as a detection, not a success story. "Blocked" is not "resolved" for security categories:
   - Identify the source: which device/user made the lookup (roaming client or network egress — if only the site's egress IP is known, the technician identifies the internal source from the filter's console or DHCP/firewall logs; say so if attribution is unavailable).
   - One-off lookup to a phishing domain → likely a clicked link: run phishing-triage on how the user got the URL; the block prevented the page, but check for sibling deliveries.
   - Repeated/periodic lookups to C2/malware domains → beaconing pattern: treat the endpoint as suspect — edr-detection-runbook on that device; do NOT close because "it was blocked." The block is containment of the symptom, not the infection.
   - Prior context by searching earlier tickets (same device/domain class, ~90 days) for recurrence.

3. Category-block complaint path:
   - Confirm the block reason and the client's documented filtering policy (in the client's documentation). If the site is miscategorized by the vendor → the fix is a category-dispute/recategorization request to the vendor plus, if business-urgent, a narrow temporary allow.
   - If correctly categorized but business-needed → this is a client policy decision, not a desk favor: route to the client's authorized approver on file. The desk does not loosen a client's own policy on a user's request — verify authorization per the client's documentation, never on the requesting user's say-so.

4. Bypass/allow discipline: narrowest scope (exact domain over wildcard, specific user/site over global), time-boxed where the need is temporary, named client approver recorded, and a review date — every allow entry gets an owner and a review date, because an allowlist that only grows is a policy that no longer exists. Never bypass a security category — if someone insists a malware-class block is wrong, escalate the domain for vendor recategorization with evidence instead of allowing it. Identity-check before any user-specific bypass — a "please unblock this for me" from a compromised mailbox is a real pattern.

5. Recurring vendor false positives (CDNs, ad networks tripping security categories) → security-noise-tuning with the same narrow-allow discipline.

6. In the internal note, document: event class, source attribution, verdict, any allow's scope/approver/expiry. Console changes are technician actions the agent directs and records. Classify per soc-classification-tree for security-class events.

Degradation: if the filter's console isn't accessible to the desk, name exactly what the tech should pull (query logs, source identity, category verdict) rather than inferring from the ticket alone. When in doubt, do nothing irreversible and escalate.
```
