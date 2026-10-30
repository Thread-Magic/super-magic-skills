---
name: Backup Alert Bundler
description: Bundle backup alert tickets for the same client only when every protected configuration, classification and severity match, and keep a short rolling status label on the parent title from the newest alert.
category: Alert Runbooks
tools: [search_tickets, merge_ticket, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Technician]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Backup Alert Bundler

**When to use:** Your backup platform opens a new ticket for every failed job, boot verification and screenshot check, for the same protected machines on the same appliance. You want one open ticket per real problem, and you want its title to show the latest status at a glance, without ever bundling a warning into a critical or two different machines together.

**Run it:** on one ticket · or as a Flow (when a ticket is created on your backup alerts board). For deciding what the failure means, follow up with Backup Failure Triage (`devices-and-infrastructure/backup-failure-triage`).

## Prompt

```
Bundle this backup alert into an existing ticket only on an exact match, and keep the parent title current.

1. KEYS. From this ticket extract: the client company; every configuration or protected-machine ID in the title (all of them); the appliance or device ID; the severity (for example Critical or Warning); and the type, subtype and item.

2. CANDIDATES. Search open tickets on the same board for the same client created in the last 48 hours.

3. MATCH. A candidate matches only if ALL of these are identical: client, every configuration ID, type, subtype and item, and severity. Critical bundles only with Critical, Warning only with Warning. Any partial match is not a match. No matches: add the internal note "No exact backup alert match. Not bundled." and stop.

4. BUNDLE. The oldest matching ticket is the parent. Merge every newer match, including this ticket, into it, then set each child to your closed status (look up the real status on that board).

5. STATUS LABEL. Read the NEWEST bundled ticket's title for a status line (for example "Boot Verification failed: Blue screen (BSOD)"). Shorten it to a 2 to 3 word label ("Boot Verify BSOD", "Backup Send Error"). If the parent title already ends with " - <old label>", replace that label; never stack labels. Otherwise append " - <label>". No status line: leave the title alone.

6. NOTE. On the parent, add an internal note: how many tickets were bundled, their numbers, the configuration IDs, classification and severity matched on, and the label applied (or "No status label added").

Never bundle across clients, appliances or severities. Never invent IDs. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the final note.
```
