---
name: Journaling & Compliance Mail
description: Handle Exchange journaling and compliance-copy requests with legal justification, external journal targets, cost impact, and retention alternatives.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Journaling & Compliance Mail

**When to use:** A ticket asks to journal all mail for FINRA/SEC/insurance compliance, BCC every message to/from a department to an archive, set up a feed to a compliance archive vendor, or review/retire an old journal rule. Implement journaling only when it is actually the right tool — with legal justification on record, a valid target architecture (Exchange Online cannot journal to itself), and the client aware of what the copy stream costs and exposes.

**Run it:** on one client's request — you prepare and verify, a technician executes the rule and connector changes (not a Flow: it needs a human at the console).

## Prompt

```
Handle a journaling or compliance-mail request. You prepare and verify; a technician executes
the rule and connector changes. Never invent regulations, approvers or vendor figures.

1. Justification gate first. Journaling copies every in-scope message, personal and privileged
   content included, into another system. Require a documented legal or regulatory driver from
   the client's compliance or legal authority, naming the regulation, scope and duration; send
   an approval request. Decline surveillance-flavoured requests (a manager wanting to read a
   team's mail clears no bar); document the decline.

2. Check whether retention is the better tool. Microsoft's direction for most preservation
   needs is retention policies, litigation hold and eDiscovery. Journaling wins only when a
   regulator requires an immutable copy stream to an independent archive, or a third-party
   archive vendor is mandated. Put the comparison to the client.

3. Architecture constraints:
   - Exchange Online cannot journal to a mailbox in the same organization; the target must be
     external — a third-party archive address or an on-prem mailbox.
   - Configure the undeliverable-journal-report mailbox and name its monitor before the rule
     enables: if the target rejects mail, reports pile there and journaling fails silently.
   - An archive mailbox is not a journaling target, and auto-expanding archives don't support
     journaling.

4. Scope least-broadly. Rule scope is per recipient or sender group or global, with a direction
   (internal, external, all). Journal only the population the regulation covers — every extra
   mailbox is storage cost and privacy exposure.

5. Cost goes in the ticket before approval: vendor per-GB or per-user pricing against the
   client's mail volume, growth over the mandated retention period, and who owns vendor-side
   disposal. Check the client's documentation for vendor context; note it if IT Glue isn't
   connected (Connector Degradation base skill).

6. Prepare execution: New-JournalRule -Recipient <scope> -JournalEmailAddress <external target>
   -Scope <Global|Internal|External>, in the compliance or EAC surface; verify the module and
   portal location against Microsoft's docs. Any connector reaching the target has TLS
   enforced.

7. Verify: an in-scope test message produces a journal report at the target, an out-of-scope
   one does not, and the undeliverable-report mailbox is set and monitored. Leave a plain-text
   note, no markdown or emojis (PSA Note Discipline base skill): justification and approver,
   rule name with exact scope and direction, target, undeliverable-report mailbox and monitor,
   cost acknowledgement, start date, and rollback — disable the rule; copies already at the
   vendor cannot be un-copied. Log the time.

When in doubt about authorization or an invalid target, do nothing and escalate.
```
