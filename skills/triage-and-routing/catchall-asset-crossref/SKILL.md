---
name: Catchall Asset Cross-Reference
description: Find the real client for a catch-all or no-company ticket by matching the hostname, device or asset it names against your RMM, documentation tool and recent tickets, when the sender and body give no company.
category: Triage & Routing
tools: [search_tickets, search_ninjaone_devices, search_itglue, search_hudu, search_knowledge_base, search_clients, search_contacts, assign_contact, add_ticket_note]
connectors: [NinjaOne, IT Glue, Hudu]
scope: single
flow: yes
role: [Dispatcher]
outcome: [Time & Cost Savings (Capacity), Faster Resolution & Response]
---

# Catchall Asset Cross-Reference

**When to use:** Alerts and forwarded mail land on your catch-all company with no useful sender domain: a backup job from a service account, a firewall notice, a "server X is down" email. The ticket does name a machine, though, and your RMM or documentation knows whose machine it is.

**Run it:** on one ticket · or as a Flow (when a ticket lands on the catch-all company). Run `triage-and-routing/catchall-routing` first, and this second for the tickets its evidence ladder could not place.

## Prompt

```
Place this catch-all ticket on its real client using the assets it names. On evidence, or not at all.

1. Skip if the ticket already has a real client, or already carries a routing note.

2. EXTRACT every hostname, device name, serial, configuration or asset name from the title, body and alert fields.

3. DISCARD your own infrastructure: a service account or credential that belongs to your MSP (for example "DOMAIN\<your MSP>" or a backup service account) points at you, not the client. Never route to your own company on that alone.

4. SEARCH each asset, in this order: RMM devices; documentation tool assets and configurations; your knowledge base; recent tickets that already sit on a real client. Skip any source that is not connected.

5. DECIDE.
- Exactly one client from any source: that is explicit-company strength evidence. Use it.
- Two or more different clients: ambiguous. Change nothing; list the candidates and their sources.
- No match: change nothing.

6. CONTACT at the matched client: the contact named in the ticket if they exist there; else that client's primary contact, noting it was a fallback. No contacts at all: note it and stop. Assign the contact, which moves the ticket to that client.

7. NOTE (internal, plain text): "CATCHALL ASSET ROUTING: matched <asset> in <source> to <client>. Contact: <name> (<direct or fallback>). Changed: <what>." Or "CATCHALL ASSET ROUTING: no confident match. Assets checked: <list>. Left for human review."

One routing note per ticket. Never close or recreate a ticket. Never invent clients, contacts or assets; say if a search may have capped.

As a Flow: your entire reply is the note.
```
