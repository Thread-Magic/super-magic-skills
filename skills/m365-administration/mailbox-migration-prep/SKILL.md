---
name: Mailbox Migration Prep
description: Build the pre-migration checklist for tenant-to-tenant or on-prem mailbox moves: inventory, breakage list, holds and licensing, and user comms.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Mailbox Migration Prep

**When to use:** A migration is being scoped or scheduled — a tenant-to-tenant move (acquisition, divestiture, rebrand), an on-prem Exchange to Exchange Online onboarding, "what do we need to check before we migrate mailboxes," or a post-migration "X stopped working" ticket that traces back to skipped prep (use the checklist as the diagnostic). Front-load the pain: everything that will break is listed before cutover, the inventory is complete enough to rebuild what the move drops, and users hear about it before their Outlook does.

**Run it:** on one migration engagement — you prepare the checklist and inventory, a technician executes the exports and the move (not a Flow: it needs a human at the console).

## Prompt

```
Build the pre-migration checklist before anyone touches a batch. You prepare it; a technician
runs the exports and the move. Never invent data or claim an unevidenced check.

1. Inventory the source — the rebuild manifest. The tech exports and attaches it; add context
   from the knowledge base, prior tickets and the client's documentation — note it plainly if
   IT Glue or Hudu isn't connected (Connector Degradation base skill). Capture: sizes and item
   counts (Get-Mailbox + Get-MailboxStatistics) for batching and quota risk; types, including
   room/equipment CalendarProcessing settings and shared mailboxes over 50 GB, which need
   licenses on the target; every Full Access, Send As, Send on Behalf and calendar grant;
   forwarding at all three layers; aliases and proxy addresses; distribution lists and M365
   Groups with members and owners; transport rules, connectors, SPF/DKIM/DMARC state;
   litigation and eDiscovery holds plus retention policies. A held mailbox does NOT enter a
   batch without documented legal sign-off — preservation is a lawyer's call, not a tech's.

2. Write the "what breaks" list into the ticket, each with its mitigation:
   - Cross-mailbox permissions and calendar delegations are usually NOT carried — re-grant them
     from step 1.
   - Outlook autocomplete: replies to cached entries bounce unless legacyExchangeDN values are
     stamped as X500 proxy addresses on the target.
   - Outlook profiles and mobile accounts need recreating at cutover.
   - Inbox rules citing old addresses, mailbox forwards and shared-mailbox mappings: re-verify.
   - In-place archives, auto-expanded especially, migrate badly or in pieces.
   - Teams, SharePoint and OneDrive are NOT part of a mailbox migration. Say so.

3. Cutover: MX, autodiscover, SPF/DKIM/DMARC for the moving domain — enable DKIM on the target
   BEFORE cutover so outbound authentication never lapses. A domain lives in one tenant at a
   time, so source-removal sequencing sets the downtime window.

4. Comms and batches. Comms are approval-gated: dates, downtime, what users must redo
   (accounts, signatures, autocomplete), a change freeze before cutover, day-one hypercare.
   Pilot one of every mailbox type with validation criteria, then waves sized to bandwidth and
   desk capacity. Set go/no-go and the rollback point: cheap before MX cutover, a second
   migration after it. Send an approval request for client sign-off.

5. Leave the checklist as a plain-text note, no markdown or emojis (PSA Note Discipline base
   skill): steps 1-4 plus holds, target license gaps, and what blocks a migration date. Log the
   time.

Never promise permissions, delegations or autocomplete will just work after the move; verify
what your migration tool carries and drops against current vendor docs. When in doubt about a
held mailbox or a cutover risk, do nothing and escalate.
```
