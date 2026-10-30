---
name: Alert Threshold Problem Ticket
description: When a flapping alert (VPN drops, agent on/off, device offline) fires past a count in a time window for one site or device, open or update one rolling problem ticket and close the counted duplicates into it.
category: Alert Runbooks
tools: [search_tickets, create_ticket, add_ticket_note, update_ticket, list_ticket_statuses, list_boards]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Alert Threshold Problem Ticket

**When to use:** A monitor keeps tripping for the same site or device (a VPN tunnel that drops ten times a day, an endpoint agent that toggles enabled and disabled, a link that blips) and each event opens its own ticket. One blip is noise; a pattern needs an owner. You want a threshold that turns the pattern into one tracked problem ticket and closes the individual alerts into it.

**Run it:** on one ticket · or as a Flow (when an alert ticket of that type is created). Set the count and window per alert type; production desks use values like 10 in 48 hours for VPN drops and 4 in 24 hours for agent status changes. For an incident that recurs over weeks with a workaround, use Problem Ticket Creation (`escalation/problem-ticket-creation`) instead.

## Prompt

```
Turn a flapping alert into one rolling problem ticket once it crosses the threshold.

Settings (edit per alert type): THRESHOLD = <10>, WINDOW = <48> hours, PROBLEM TITLE = "<Alert> issue at <site or device>", BOARD = <the board alerts of this type belong on>.

1. KEY. From this ticket's title, extract the key that identifies the source: the company plus the network or tunnel name, or the machine name. Cannot extract it: make no changes and add an internal note "Could not extract the alert key from the title. Manual review needed." Stop.

2. COUNT. Search open and closed tickets of the same type and subtype whose titles contain the key, updated within WINDOW. Exclude the problem ticket itself. Always include this ticket, even if search has not indexed it yet. Store the total as COUNT. If the search may have capped, say COUNT is a minimum.

3. BELOW THRESHOLD. If COUNT is under THRESHOLD, take no action and stop.

4. PROBLEM TICKET. Search for an open ticket titled PROBLEM TITLE.
- Found: add an internal note listing the counted tickets, one per line: "<n> | #<number> | <title> -> <status> | <created>".
- Not found: create it on BOARD under the same company, with a description: "There have been <COUNT> <alert> events in the past <WINDOW> hours. Please review." followed by the same list.
Never assign a technician to the problem ticket; leave scheduling to your normal process.

5. CLOSE DUPLICATES. For each counted ticket that is still open and is not the problem ticket: add an internal note "Closed as duplicate alert. See problem ticket #<number> - <PROBLEM TITLE>", then set it to your duplicate or alert-closed status (look up the real status on that board). Skip tickets already closed. Never close the problem ticket.

6. SUMMARY. On the problem ticket, add an internal note: the total count, which tickets were closed as duplicates, and the latest state from the newest ticket (for example up or down, enabled or disabled).

Never invent ticket numbers or counts. Notes are plain text, no markdown or emojis.

As a Flow: your entire reply is the summary note, or nothing when below threshold.
```
