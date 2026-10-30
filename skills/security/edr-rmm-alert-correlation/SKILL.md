---
name: EDR and RMM Alert Correlation
description: Match an EDR threat ticket that landed on your catch-all company with the RMM ticket for the same machine and file, move it to the real client, and merge it in with an audit note.
category: Security
tools: [search_tickets, search_contacts, assign_contact, merge_ticket, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Security & Compliance Owner, Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# EDR and RMM Alert Correlation

**When to use:** Your EDR console (for example SentinelOne) emails threats from a shared mailbox, so they land on your catch-all company, while your RMM (for example NinjaOne) opens a ticket for the same event already mapped to the right client. Analysts work two tickets for one threat, and the EDR one has no client.

**Run it:** on one ticket · or as a Flow (when an EDR threat ticket is created on the catch-all company). Run it before any duplicate-merge skill, since it corrects the company those skills trust.

## Prompt

```
Pair an EDR threat ticket with its RMM ticket, fix the EDR ticket's client, and merge. Only work on OPEN tickets.

1. IDENTIFY. The EDR ticket's title looks like "<EDR> - <threat type> - machine <MachineName>" and sits on the catch-all company. The threat type varies (active, suspicious, malicious, detected); match on the prefix and the machine suffix, not a specific word. The RMM ticket sits on the real client. From the EDR ticket take the machine name from the title and the file name from the body (a line like "Name: <file>"). If you started from the RMM ticket, find the EDR counterpart the same way.

2. FIND THE COUNTERPART. Search open tickets for the machine name, including messages. A candidate matches only if BOTH the machine name is in its title and the same file name appears in its body or messages. Skip anything that fails either check.

3. NO MATCH. Add the internal note "No matching EDR/RMM ticket found." to the EDR ticket and stop. Two or more matches: change nothing, list them in an internal note and stop.

4. MOVE THE EDR TICKET. Record the old company (catch-all) and the new company (the RMM ticket's client). Find a valid contact at the new company (the RMM ticket's contact, else that client's primary contact) and assign it to the EDR ticket, which moves it to that client. Never assign to the catch-all. If the new company resolves to the catch-all or no contact exists, stop and note why.

5. MERGE. Only after the move is confirmed, merge the EDR ticket into the RMM ticket (the RMM ticket is the parent), then set the EDR ticket to your duplicate alert status (look up the real status on that board).

6. AUDIT NOTE on the parent: "EDR/RMM correlation completed. EDR ticket moved from <old company> to <new company>. Matched on machine <name> and file <file>. EDR ticket #<number> merged into this ticket."

Never merge on machine name alone. Never invent ticket numbers. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the audit note, or the one-line reason you stopped.
```
