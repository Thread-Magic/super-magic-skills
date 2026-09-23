---
name: SOC Alert Duplicate Merge
description: Close a new SOC or SIEM alert into an older open ticket only when the affected user or device matches exactly and the alert context is the same, checking referenced ticket and SOC case numbers first.
category: Security
tools: [search_tickets, list_ticket_statuses, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Security & Compliance Owner, Dispatcher]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# SOC Alert Duplicate Merge

**When to use:** Your SOC or MDR provider sends the same detection several times (a new email per update, a reply that spawns a ticket, the same impossible-travel alert twice in a day) and analysts end up investigating one incident across three tickets.

**Run it:** on one ticket · or as a Flow (when a ticket is created on the SOC alert board). Run it after the ticket's company has been corrected; it trusts the company on the ticket.

## Prompt

```
Duplicate check for one SOC alert ticket per run. Never work a queue. Assume the company and contact on this ticket are already correct.

Settings: look back 7 days; stop and flag if more than 50 candidates.

1. Preflight, no writes. Stop if the ticket is not on the SOC alert board, is closed, or already has a note from this skill ("SOC-DEDUP-DONE" or "SOC-DEDUP-PARENT").

2. Extract the affected identity, no writes:
- Pipe-delimited SIEM titles ("Priority | Company | Description | Affected"): the last segment, including when wrapped in [EXTERNAL] or "Re:".
- "Compromise suspected: Name (email)": the email.
- "High severity alert: ... on HOST": the hostname.
- Otherwise the first email, else the first hostname, in the summary or description.
- Empty or "Unknown": check the Executive Summary section, then notes oldest first.
Normalise to lowercase; hostnames short-name only. An email never equals a hostname. Still nothing: flag "Affected identity could not be determined" and stop.
Also record any "Re: Ticket# N" number and any SOC case reference, e.g. "1234567:48522".

3. Find candidates, no writes. Keep only open tickets on this board, same company, created within 7 days, not this ticket. A match needs BOTH an exact identity match AND the same alert context (same rule or detection name, same system or threat category). Ignore prefixes, bracket tags and whitespace. Company plus context alone is never enough. Doubt means discard.
Check in order and stop at the first hit: the referenced ticket number, then the SOC case reference (search each half), then the identity scoped to the company, then a standard same-company search.

4. Decide. The parent is the oldest match (lowest ID on a tie). If this ticket is the oldest, do nothing. If a match is already closed as a duplicate, follow it to its root parent. Never cascade merges.

5. Writes, in order, stop on first failure:
a. Change this ticket's status to your automated-closed status (look it up).
b. Note on the parent: "Duplicate #<child> merged into this thread. Company <co>, alert <recap>, affected <identity>. Path: <path>. SOC-DEDUP-PARENT"
c. Note on this ticket: "Closed as duplicate of #<parent>. Company <co>, alert <recap>, affected <identity>. Path: <path>. SOC-DEDUP-DONE"
If (a) succeeds but a note fails, add "MANUAL REVIEW REQUIRED: status changed, notes incomplete" and stop.

Flag = one note "MANUAL REVIEW REQUIRED: <reason>. SOC-DEDUP-DONE", status unchanged.

Only this ticket may be closed. Never close or edit the parent beyond its one note. Never retry a write. As a Flow, your reply is the note or run summary only.
```
