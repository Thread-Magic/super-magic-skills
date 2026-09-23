---
name: Alert Client Resolver via Liongard
description: When a security or monitoring alert lands on a catchall company, resolve the real client from the hostname in the alert using Liongard, then PSA configurations, then the ticket text.
category: Triage & Routing
tools: [search_tickets, liongard_device, liongard_environment, search_clients, search_contacts, assign_contact, add_ticket_note]
connectors: [Liongard]
scope: single
flow: yes
role: [Dispatcher, Security & Compliance Owner]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Alert Client Resolver via Liongard

**When to use:** EDR, SIEM or monitoring alerts arrive from a vendor mailbox and land on your catchall company, but the title names a machine ("Threat detected on Machine ACME-WS-014"). You want the ticket re-filed to the client who owns that machine before anyone works it.

**Run it:** on one ticket · or as a Flow (when a ticket on the alert board is created on the catchall company).

## Prompt

```
Re-file this alert ticket to the client who owns the machine it names. One ticket per run; never work a queue. Never close, resolve or change status.

1. Preflight, no writes. Stop if the ticket is closed, or if an internal note from this skill already exists ("CLIENT RESOLVED" or "MANUAL REVIEW REQUIRED" from Alert Client Resolver).

2. Extract the hostname. Look for patterns like "on Machine {HOST}", "Device: {HOST}", "Hostname: {HOST}". Take the text up to the first " by ", " - ", " – " or end of line, trim trailing spaces and dashes, keep hyphens and digits. If the title is cut off, try the description. No hostname: go to step 5.

3. Ask Liongard who owns it. Look the hostname up in Liongard devices twice: once as a hostname match and once as a free-text query. Do not filter by inventory state, managed flag or environment, so archived and discovered devices still count. If found in either, take its environment (if several environments match, use the most recently seen device) and use the environment name as the target client.

4. Fallback: if Liongard has nothing, or the Liongard connector is not available, search the PSA's configurations or assets for the hostname across all companies. A match gives you the target client.

5. Content fallback: scan the title, description and notes for a client name, email domain, contact name or hostname prefix you recognise. One client from one or more signals: use it. Several different clients: flag and stop.

6. Match the target to a PSA client. Search clients by name; if nothing, strip LLC/Inc/Ltd and punctuation and retry once. Zero or more than one plausible match: flag and stop. If it already matches the ticket's company, stop with no writes.

7. Re-file. Find the client's placeholder contact (the generic contact your desk uses for alerts, often named "Null" or "Alerts"). Found: assign the ticket to it. Not found: flag and stop; never pick a real person.

8. Leave one internal note, plain text: "CLIENT RESOLVED by Alert Client Resolver. From <old company> to <new company>. Hostname: <host>. Path: Liongard device / PSA configuration / ticket content. Liongard environment: <name or none>."

Flag means one internal note, "MANUAL REVIEW REQUIRED (Alert Client Resolver): <reason>. Signals: <each signal and the client it pointed to>." and no other change.

Rules: only use values returned by lookups, never invent a client or ID. Reads may retry once; never retry a write. If the first write fails, leave one failure note and stop.

As a Flow: your entire reply is the internal note. No questions, no narration.
```
