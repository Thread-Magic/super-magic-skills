---
name: Archive Mailbox Enablement
description: Enable Exchange Online In-Place Archive mailboxes to solve quota issues, with license checks, move-policy expectations, and archive caveats.
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
You prepare an archive-mailbox enablement for a technician to run: confirm fit, check licensing, set expectations. Apply the Write Guardrails base skill — never report the archive as enabled on intention, and when in doubt do nothing and escalate. Never quote storage limits or PowerShell syntax from memory — verify against Microsoft's current docs and module versions.

1. Confirm an archive solves this problem. It helps when the primary mailbox is full of aging mail the user must keep. It doesn't help when the bloat is in Recoverable Items (a hold or retention issue), when the user needs everything offline (archives are online-only in Outlook cached mode), or on mobile — most mobile clients don't show the archive; set that expectation now.

2. Check the license first. In-Place Archive requires Exchange Online Plan 2 (in most E3/E5 bundles), or Plan 1 plus the Exchange Online Archiving add-on. Have the tech confirm the user's actual license; if it's insufficient, present the cost path — don't enable and hope. Check the client's documentation and knowledge base for the licensing standard; if it isn't connected, say so (Connector Degradation base skill).

3. Send an approval request naming the move policy that will apply — an archive changes what the user sees in Outlook and where old mail lives.

4. Prepare execution: `Enable-Mailbox -Identity <user> -Archive`. Confirm which archive/MRM policy applies — the default moves items older than two years; a different age is a retention-tag change (retention-policy-requests), not grounds to skip it. Set the drain expectation in writing: the Managed Folder Assistant moves mail on its own schedule, so the primary shrinks over days, not minutes — if quota pressure is immediate, pair with cleanup from mailbox-quota-management.

5. State the auto-expanding archive caveats before anyone asks, and never call it unlimited:
   - Growth is capped (roughly 1 GB/day) and total space is capped (on the order of 1.5 TB) — verify current limits before quoting them.
   - Once turned on, it cannot be turned off.
   - Auto-expanded storage cannot be moved back or exported in one piece, making offboarding and migration harder (mailbox-migration-prep).
   - It's a storage answer, not a compliance answer; journaling to an archive mailbox is unsupported.
   If the mailbox is under litigation hold, coordinate before changing where content lives: holds follow the mailbox, but surprises in a legal matter are unacceptable (litigation-hold).

6. Verify: the archive appears in Outlook on the web and, after a Managed Folder Assistant cycle, items past the policy age show up. Leave a plain-text note — user, license confirmed, policy, enable date, expectations set (drain time, mobile visibility), and rollback: `Disable-Mailbox -Archive` keeps archive content recoverable for a limited window; state that window from current docs. Log time.
```
