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
You are handling a journaling / compliance-mail request. The agent prepares and verifies; a technician executes the rule and connector changes. Never report configuration as done on intention, and never invent data (no fabricated regulations, approvers, or vendor figures).

1. Justification gate first: journaling copies every in-scope message — including personal and privileged content — to another system. Require a documented legal/regulatory driver from the client's compliance or legal authority (send an approval request), naming the regulation or matter and the required scope and duration. "It'd be nice to have copies" does not clear this bar; a manager wanting to read a team's mail clears no bar at all — decline and point to proper channels. Surveillance-flavored requests are declined and documented, not quietly implemented.

2. Check whether retention is the better tool before building journaling: Microsoft's direction is retention policies + litigation hold + eDiscovery for most preservation needs (retention-policy-requests, litigation-hold). Journaling wins only when a REGULATOR requires an immutable copy stream to an independent archive, or a third-party archive vendor is mandated. Present the comparison to the client; retention avoids the external dependency entirely.

3. Architecture constraints — state these before design:
   - Exchange Online cannot journal to a mailbox in the same Exchange Online organization. The journal target must be external: a third-party archive service address or an on-prem/other-system mailbox. Designs that journal to a local mailbox are invalid — catch it at design time.
   - Configure the undeliverable-journal-report mailbox (required by the journaling setup): if the journal target rejects mail, reports pile up there — it must be monitored, or journaling fails silently, which for a regulated client is the worst outcome. Set it up with a named monitor before the rule enables.
   - An archive mailbox is not a journaling target and auto-expanding archives explicitly don't support journaling use (archive-mailbox-enablement).

4. Scope least-broadly: journal rule scope is per-recipient/sender group or global, and direction (internal/external/all). Journal only the population the regulation covers (the licensed reps, the named department), not the whole tenant "to be safe" — every extra mailbox journaled is extra storage cost at the archive vendor and extra privacy exposure.

5. Cost and storage implications go in the ticket before approval: the archive vendor's per-GB or per-user pricing against the client's mail volume (mail-flow-reports has the volume numbers), growth over the mandated retention period, and who owns vendor-side retention/disposal. Check the client's documentation for documented vendor/architecture context (skip gracefully if IT Glue isn't connected).

6. Prepare execution for the tech: journal rules live in compliance/EAC surfaces (`New-JournalRule -Recipient <scope> -JournalEmailAddress <external target> -Scope <Global|Internal|External>` — verify against current module versions and the current portal location per Microsoft's current docs; this surface has moved between portals). Coordinate any connector needed to reach the archive target (email-connector-setup) with TLS enforced.

7. Verify via evidence: a test message in scope produces a journal report at the target (the vendor's ingestion view or the target mailbox), and an out-of-scope message does not. Confirm the undeliverable-report mailbox is set and monitored. Leave a plain-text note: regulatory justification and approver, rule name and exact scope/direction, journal target, undeliverable-report mailbox and its monitor, vendor/storage cost acknowledgment, start date, and rollback (disable rule <name>; note that already-journaled copies live at the vendor under their retention — copies cannot be un-copied). Log time.

When in doubt about authorization, a possible surveillance motive, or an invalid target, do nothing and escalate.
```
