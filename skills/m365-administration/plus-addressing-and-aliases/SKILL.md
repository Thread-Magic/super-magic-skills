---
name: Plus Addressing & Aliases
description: Handle requests for extra mailbox addresses: plus addressing for self-service tagging, proxy aliases, and the send-from-alias caveats stated.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Plus Addressing & Aliases

**When to use:** A ticket asks for a separate address for newsletter signups / vendor portals, to give a user an extra address on the client domain, complains "I replied and it came from my main address instead of the alias," or is a rebrand/name-change ("new name as primary, keep old working"). You give a user extra addresses the cheapest correct way: plus addressing when they just need to tag inbound mail, a proxy alias when they need a real alternate address — with the reply-from-alias behavior explained before it becomes a complaint. Identity-wide renames (UPN changes) are a larger change than the alias mechanics here.

**Run it:** on one user — you prepare and verify, a technician drives the module (not a Flow: it needs a human at the console).

## Prompt

```
You give a user extra addresses the cheapest correct way and explain the sending reality before it becomes a complaint. You prepare and verify; the tech drives the module. Never invent data.

1. Triage the actual need (read the ticket for context):
   - Tagging/filtering inbound mail the user controls themselves → plus addressing. `user+anything@domain` already delivers to `user@domain` in Exchange Online (on by default tenant-wide since 2022 — verify the tenant hasn't disabled it: `Get-OrganizationConfig | Select DisablePlusAddressInRecipients`). No admin change, no ticket beyond the explanation; show the user how to create inbox rules on the +tag. Caveats to state: some external websites reject + in address forms, and anyone can strip the tag to reach the base address — it's a filing tool, not privacy.
   - A real alternate address others will use → proxy alias (step 2).
   - A separately-worked identity (support@, sales@) → that's a shared mailbox or group conversation (shared-mailbox-creation / distribution-vs-m365-groups), not an alias.

2. For a proxy alias: confirm the address is unused (not an existing mailbox, alias, DL, or group — check the client's documentation for documented addresses, skip gracefully if not connected), get client approval for a new receivable address on their domain (send an approval request), then prepare for the tech (PowerShell labeled: verify against current module versions): `Set-Mailbox <user> -EmailAddresses @{add="smtp:<alias>@<domain>"}` — lowercase `smtp:` adds an alias; uppercase `SMTP:` changes the PRIMARY address, which changes what everyone sees on outbound mail — never flip primary unless that was the explicit, approved request.

3. State the sending reality before closing: aliases RECEIVE by default; replies go out from the primary address unless send-from-alias is enabled tenant-wide (`Set-OrganizationConfig -SendFromAliasEnabled $true`) and the client (Outlook on the web, newer Outlook builds) supports choosing the From address. Caveats:
   - The setting is tenant-wide — enabling it for one user enables the capability for everyone; that's an approval-worthy scope statement (send an approval request at that scope or decline).
   - Client support is uneven (older Outlook, mobile clients) — verify current client behavior against Microsoft docs before promising a specific user experience.
   - If the user must reliably SEND as the address and the tenant won't enable send-from-alias, the honest alternative is a shared mailbox with Send As (shared-mailbox-delegation).

4. Name-change flavor: add the new address, wait for verification, then swap primary (uppercase SMTP:) keeping the old as an alias so nothing bounces; note that the sign-in UPN is a separate change with its own blast radius (re-auth on devices) — flag it, don't bundle it silently.

5. Verify via evidence: test mail to the new alias/plus address arrives; if send-from-alias was enabled, a test send shows the alias in the recipient's copy. Document what/why/when/rollback — leave a plain-text note: user, addresses added, primary changed or not, tenant settings touched (send-from-alias, plus-addressing state), approver, caveats communicated, and rollback (remove alias / restore prior primary). Log time.

Guardrails: Never change the primary SMTP or the UPN as a side effect of an alias request; each is its own approved change. Send-from-alias is a tenant-wide switch — present it as such, get approval at that scope or decline. Aliases are not a security or privacy boundary; say so when the request is motivated by hiding the real address. Check address collisions before promising an alias; a colliding address errors on write and wastes the approval loop. When in doubt, do nothing and escalate.
```
