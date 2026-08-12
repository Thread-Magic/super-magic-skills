---
name: Cross-Client Outage Detector
description: Spot the same symptom appearing across multiple clients within a short window, flag a possible vendor or major incident, and propose a parent incident ticket.
category: Triage & Routing
tools: [search_tickets, search_clients, create_ticket, add_ticket_note]
connectors: []
scope: global
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Cross-Client Outage Detector

**When to use:** Several tickets with a similar symptom arrived from different clients recently, a tech senses "haven't we seen this a few times today?", or dispatch runs a periodic sweep for emerging vendor/major incidents.

**Run it:** across all recent tickets · or as a Flow (when a new ticket is created, to check for a pattern).

## Prompt

```
Detect the cross-client pattern, name the suspected shared dependency, and propose (never
silently create) a parent incident. Three clients reporting the same mail delay in an hour is
probably one upstream incident, not three tickets.

1. Take the symptom fingerprint from the triggering ticket (or the stated symptom): affected
   service, error text, and behavior.

2. Search recent tickets (default window: 4 hours) for the same symptom family across ALL
   clients, split per board to respect result caps; say so if a search may have capped, since
   undercounting hides outages.

3. Group hits by client. The pattern threshold: same symptom at 3+ distinct clients inside
   the window (2+ if the symptom names the same vendor/service explicitly). Distinct clients
   means distinct companies — multiple sites of one client is a client-level incident, not
   cross-client; say which you found.

4. Identify the plausible shared dependency: a common vendor, cloud service, ISP/region, or a
   shared platform. Say "unknown shared cause" when you can't name one — never guess a vendor
   into the record.

5. If the threshold is met, propose a parent incident: a draft new ticket (title,
   affected-client list, symptom summary, suspected dependency, first-seen time) presented for
   confirmation. On approval, open it and leave a plain-text note on each child ticket
   referencing the parent number. Never merge the children — they stay open under their own
   clients for per-client communication and SLA tracking; linked by note, not merged.

6. If below threshold, report the near-pattern (counts, clients, window) and recommend a
   re-check interval — a negative finding is still useful.

Flag and propose; never declare. Wording stays factual: "possible upstream/vendor incident,"
never "vendor X is down" or breach language without confirmation. If searches capped, present
counts as "at least N" and recommend a narrower re-run. Never invent affected clients, vendors,
or ticket numbers — every listed child must be a real ticket you found.

Running as a Flow: detect and alert only. The entire reply is either the plain-text alert —
"POSSIBLE CROSS-CLIENT INCIDENT: <symptom family> at <k> distinct clients since <first-seen
time>. Tickets: #<n>, #<n>, ..." plus the suspected shared dependency or "unknown shared
cause" — or exactly "NO PATTERN." Threshold not met → NO PATTERN (a near-miss is never reported
as an incident). If any search capped, append " (SWEEP PARTIAL)". A multi-site single-client
cluster → NO PATTERN. Permitted writes: none — creating the parent and noting children require
human confirmation and stay attended.
```
