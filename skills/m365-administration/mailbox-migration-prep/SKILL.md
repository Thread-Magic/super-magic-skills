---
name: Mailbox Migration Prep
description: Build the pre-migration checklist for tenant-to-tenant or on-prem-to-cloud mailbox moves — full inventory, the list of things that break, holds and licensing checks, and the user comms plan. Use when a migration is being scoped or scheduled, before anyone touches a migration batch.
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
You are building the pre-migration checklist before anyone touches a migration batch. The agent prepares the checklist and inventory; a technician executes exports and the move. Never claim something was checked without the evidence — the inventory is attached to the ticket, not asserted. Never invent data.

1. Inventory the source — this is the rebuild manifest. Have the tech export and attach (verify against current module versions); pull documented client context from the client's documentation (connector-gated — skip gracefully if neither is connected), the knowledge base, and prior tickets:
   - Mailboxes with sizes and item counts (`Get-Mailbox` + `Get-MailboxStatistics`) — sizes drive batch planning and flag anything near target-side quotas.
   - Mailbox types: shared, room/equipment (with their CalendarProcessing policies — see resource-mailbox-setup), and which shared mailboxes are over 50 GB (they'll need licenses on the target).
   - All permission grants: Full Access, Send As, Send on Behalf, calendar grants (mailbox-permissions-audit is the collection playbook).
   - All forwarding, all three layers (mail-forwarding-audit).
   - Aliases/proxy addresses per mailbox, DLs and M365 Groups with membership and owners, transport rules, connectors, and DKIM/SPF/DMARC state.
   - Litigation/eDiscovery holds and retention policies — mailboxes under hold do NOT move without legal sign-off; migration can disturb preservation and that is a lawyer conversation, not a tech one (litigation-hold).

2. Write the "what breaks" list into the ticket — tenant-to-tenant breaks more than clients expect; state each with its mitigation:
   - Cross-mailbox permissions and calendar delegations: usually NOT migrated by tools — plan to re-grant from the step-1 inventory.
   - Outlook autocomplete / X500: replies to old cached entries bounce unless legacyExchangeDN values are stamped as X500 proxy addresses on target — put this in the plan explicitly; it is the number-one post-migration ticket generator.
   - Outlook profiles and mobile accounts: typically need recreation on cutover — that is desk workload; schedule for it.
   - Inbox rules referencing old addresses, mailbox-level forwards, and shared-mailbox mappings: re-verify post-move.
   - In-place archives (and especially auto-expanded archives — they migrate badly or not in one piece; see archive-mailbox-enablement) get their own line in the plan.
   - Teams/SharePoint/OneDrive content is NOT covered by a mailbox migration — scope it separately and say so, or the client will assume.

3. DNS and identity cutover plan: MX, autodiscover, SPF/DKIM/DMARC records for the moving domain (dkim-enablement on the target BEFORE cutover so outbound authentication never lapses); domain removal from the source tenant sequencing (a domain can only live in one tenant at a time — cutover order matters and drives the downtime window).

4. Comms plan — approval-gated because it is maximally user-visible: who is told what and when (dates, expected downtime, what users must do: re-add accounts, re-check signatures, expect autocomplete quirks), a freeze window for mailbox changes before cutover, and day-one hypercare staffing. Send an approval request for client sign-off on the schedule.

5. Batch strategy: pilot group first (include one of every mailbox type), validation criteria for the pilot, then waves sized to bandwidth and desk capacity. Define the go/no-go and the rollback point (before MX cutover, rollback is cheap; after, it is a second migration — write that down).

6. Output: the prep checklist as a plain-text ticket note — inventory attached/referenced, what-breaks list with mitigations, DNS sequence, comms schedule, batch plan, holds flagged, license gaps on target — and the explicit list of open questions blocking a migration date. Log time.

Guardrails: Held mailboxes do not enter a batch without documented legal sign-off. Never promise permissions, delegations, or autocomplete will "just work" post-migration — plan their re-creation from the inventory. Scope honesty: mailbox migration ≠ tenant migration; name what is out of scope (SharePoint, OneDrive, Teams) in the note. Migration tooling capabilities change — verify current tool behavior (what it does and does not carry) against vendor docs / Microsoft's current docs for the chosen tool rather than asserting from memory. When in doubt about a held mailbox or a cutover risk, do nothing and escalate.
```
