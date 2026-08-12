---
name: Archive Mailbox Enablement
description: Enable an Exchange Online archive (In-Place Archive) when it actually solves the quota problem — license check, move-policy expectations, and auto-expanding archive caveats stated honestly. Use when a mailbox is full and archiving is on the table, or a ticket asks to "turn on the archive."
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Archive Mailbox Enablement

**When to use:** A mailbox is at or near quota and cleanup alone won't hold (see mailbox-quota-management for the decision tree that leads here), a ticket asks to "turn on the archive for <user>," or someone reports "the archive is full too" / asks about auto-expanding archive. This skill enables an online archive for the right reason with the right expectations: the license supports it, the retention/move policy will actually drain the primary mailbox, and nobody was promised "unlimited storage."

**Run it:** on one mailbox — you confirm fit, check licensing, and set expectations, a technician runs the PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You are preparing an archive-mailbox enablement for a technician to execute. You confirm fit, check licensing, and set expectations; the tech runs the PowerShell and confirms the license. Never report the archive as enabled on intention, and never quote storage limits from memory — verify against Microsoft's current documentation.

1. Confirm the archive solves THIS problem — read the ticket for context. An archive helps when the primary mailbox is full of aging mail the user must keep. It does not help when the bloat is in Recoverable Items (that's a hold/retention issue), when the user needs everything available offline (archives are online-only in Outlook cached mode), or on mobile (most mobile clients don't show the archive — set that expectation now).

2. License check before promising anything: the In-Place Archive requires Exchange Online Plan 2 (in most E3/E5 bundles) or Plan 1 plus the Exchange Online Archiving add-on. Have the tech confirm the user's actual license; if it's insufficient, present the cost path to the client before enabling. Never enable on an insufficient license and hope. Check the client's documentation or the knowledge base for the licensing/standard where connected (skip gracefully if absent).

3. Approval: enabling an archive changes what the user sees in Outlook (a new archive branch) and where old mail lives — user-visible, so send an approval request to the client contact including which move policy applies.

4. Prepare execution for the tech (PowerShell labeled: verify against current module versions):
   - Enable-Mailbox -Identity <user> -Archive
   - Confirm which archive/MRM policy applies — the default moves items older than two years to the archive. If the client wants a different age, that is a retention-tag change (coordinate with retention-policy-requests), not a reason to skip the default.

5. Set the drain expectation in writing: the Managed Folder Assistant moves mail on its own schedule — the primary mailbox shrinks over days, not minutes. If quota pressure is immediate, pair this with short-term cleanup from mailbox-quota-management.

6. Auto-expanding archive caveats — state these before anyone asks for it, and never describe it as "unlimited":
   - It is not unlimited: growth is capped (roughly 1 GB/day) and total auto-expanded space is capped (on the order of 1.5 TB) — verify current limits against Microsoft's documentation before quoting numbers.
   - Once auto-expanding archiving is turned on, it cannot be turned off.
   - Auto-expanded storage cannot be moved back or exported in one piece; offboarding and migration get harder. Flag this to any client planning a tenant migration (mailbox-migration-prep).
   - It is a storage answer, not a compliance answer — journaling to an archive mailbox is unsupported.
   If the mailbox is under litigation hold, coordinate before changing where content lives — holds follow the mailbox, but surprises in a legal matter are never acceptable (cross-ref litigation-hold).

7. Verify via evidence: archive appears for the user in Outlook on the web, and after a Managed Folder Assistant cycle, items older than the policy age begin appearing in the archive. Document what/why/when/rollback: leave a plain-text note with user, license confirmed, policy in effect, enable date, expectations set (drain time, mobile visibility), and rollback (Disable-Mailbox -Archive keeps archive content recoverable for a limited window — state that window from current docs, don't guess). Log time.

When in doubt about license sufficiency or a litigation hold, do nothing and escalate.
```
