---
name: Alert Site to Client Mapping
description: Read the network or site name from a vendor alert ticket and assign the right client contact from a lookup table you maintain, so the ticket leaves the vendor's alert contact and downstream flows can match it.
category: Triage & Routing
tools: [search_tickets, assign_contact, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Alert Site to Client Mapping

**When to use:** A network or cloud vendor (Meraki, a Wi-Fi controller, an ISP portal) sends every alert from one address, so every ticket lands on your own company under the vendor's alert contact. The only clue to the real client is a network or site name in the body.

**Run it:** on one ticket · or as a Flow (when a ticket is created whose contact is the vendor's alert contact). Chain a second Flow whose trigger is "same board, contact is NOT the vendor alert contact" to bundle duplicates (for example triage-and-routing/alert-storm-merge): this skill's contact change is what makes that second Flow fire.

## Prompt

```
Map this vendor alert to its client by the network or site name, then assign that client's contact.

1. Extract the network or site name from the body. Look for "in the <Name> network", "on the <Name> network", "Network: <Name>" or "Site: <Name>". If there is no space before "network" (e.g. "HQ - Northnetwork"), strip "network" and use what comes before it. Fall back to the title. If nothing can be found, stop silently: no note, no change.

2. Match the name against this table, top to bottom, first match wins. Replace the example rows with your own.

| Rule | Pattern | Contact to assign | Client |
|---|---|---|---|
| Starts with | ACME - | <contact ID or name> | Acme Health |
| Exact | Contoso HQ | <contact> | Contoso Inc |
| Starts with any of | FAB, FBK | <contact> | Fabrikam |
| Contains | Northwind Campus | <contact> | Northwind School |

Names must match the rule exactly as written; do not fuzzy-match. "ACME - North" and "ACME - South" can map to the same client, but never map a name to a client just because it looks similar.

3. On a match, assign the listed contact to the ticket. Use only the contact in the table; never search for or pick a different person. If the assignment fails, leave one internal note: "SITE MAPPING FAILED: <site> matched <client>, but the contact assignment failed: <error>."

4. No match: change nothing and leave one internal note: "SITE MAPPING: no table entry for network '<name>'. Add it to the mapping skill, or assign the client by hand."

5. On success, leave one internal note, plain text: "SITE MAPPING: network '<name>' mapped to <client>, contact <contact> assigned." If a later bundling step posts its own summary, you may skip this note so the ticket carries one combined note.

Never change the status, priority or board. Never guess a client for an unknown site. If the ticket's contact is already a real client contact, not the vendor alert contact, stop: it has already been mapped.

As a Flow: your entire reply is the note, or nothing when you stopped silently.
```
