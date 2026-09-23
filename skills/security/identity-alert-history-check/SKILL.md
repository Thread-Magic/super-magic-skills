---
name: Identity Alert History Check
description: On a new identity or EDR alert, look back 90 days for prior alerts of the same type for the same user and client, check for a reported trip on unexpected-country alerts, and post the history as an internal note.
category: Security
tools: [search_tickets, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Identity Alert History Check

**When to use:** An identity or EDR alert arrives ("Unexpected country: Denmark by jane@client.com", "Unexpected VPN: <provider>", "Critical incident on host") and the analyst's first question is whether this has happened before, or whether the user told you they were travelling.

**Run it:** on one ticket · or as a Flow (when a ticket is created from your ITDR or EDR vendor, such as Huntress, Blackpoint or SentinelOne).

## Prompt

```
Give the analyst this alert's history before they start. Read-only apart from one internal note.

1. Parse the title. Extract:
- Alert type, e.g. "Unexpected Country", "Unexpected VPN", "Critical Incident".
- The identity: the full email address in the title (or the hostname for device alerts).
- A short subtype keyword: the country, the VPN provider, or the incident descriptor.
- The country, only for unexpected-country alerts.
Common shapes: "<Vendor> <Product> <Severity> Unexpected Country - <Country> by <email> (<Company>)", "<Vendor> <Product> <Severity> Unexpected VPN - <VPN> by <email> (<Company>)", "<Vendor> <Product> Critical Incident ... on <email or host> (<Company>)". If you cannot extract an identity, post "Alert history check skipped: no user or device identified in the title." and stop.

2. Use the client on the ticket itself. Do not parse the company from the title or search for it.

3. Search this client's tickets from the last 90 days, any status, using two short separate search terms, the identity and the subtype keyword. Do not search on the whole title as one phrase; long exact phrases miss matches. Exclude this ticket. If a search may have hit its result cap, say so.

4. Unexpected-country alerts only: search this client's tickets from the last 30 days for the identity plus the country and travel words (travel, vacation, trip, OOO, out of office). Keep only tickets that plausibly show the user reported travel to that country.

5. Post one internal note, plain text:
ALERT HISTORY (last 90 days)
Alert type: <type> | Identity: <identity> | Client: <client>
Prior alerts found: <n>
- #<ticket> <summary> | <date> | <status>
(or) This is the first alert of this kind for this identity in the last 90 days.
Expected travel (last 30 days, <country>): <n> (unexpected-country alerts only)
- #<ticket> <summary> | <date> | <status>
(or) No travel to <country> reported in the last 30 days.

Report what you found; do not judge whether the alert is malicious, and never close, merge, reprioritise or reassign. Never invent a ticket or date. Never contact the user.

As a Flow: your entire reply is the note.
```
