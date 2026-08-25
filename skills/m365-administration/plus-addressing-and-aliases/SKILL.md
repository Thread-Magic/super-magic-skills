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
Give the user extra addresses the cheapest correct way, before the sending behavior
becomes a complaint. The tech drives the module. Apply the Write Guardrails base
skill — never invent data; when in doubt do nothing and escalate.

1. Triage the actual need:
   - Tagging inbound mail the user filters themselves — plus addressing.
     `user+anything@domain` already delivers to `user@domain`, on by default tenant-wide
     since 2022; verify with `Get-OrganizationConfig | Select
     DisablePlusAddressInRecipients`. No admin change: show them inbox rules on the +tag.
     Caveats — some external sites reject "+" in address forms, and anyone can strip the
     tag. Neither a +tag nor an alias is a privacy or security boundary; say so when the
     request is about hiding the real address.
   - A real alternate address others will use — proxy alias, step 2.
   - A separately-worked identity (support@, sales@) — a shared mailbox or group
     conversation (shared-mailbox-creation, distribution-vs-m365-groups), not an alias.

2. Proxy alias: confirm the address is unused — no existing mailbox, alias, DL or group; check the client's documentation (Connector Degradation base skill if IT Glue is
   off). A collision errors on write. Get client approval for a
   new receivable address on their domain, then for the tech (verify module versions):
   `Set-Mailbox <user> -EmailAddresses @{add="smtp:<alias>@<domain>"}`. Lowercase `smtp:`
   adds an alias; uppercase `SMTP:` changes the PRIMARY — what everyone sees on outbound
   mail. Never flip primary unless that was the explicit, approved request.

3. State the sending reality up front. Aliases RECEIVE by default; replies leave from the
   primary unless send-from-alias is enabled tenant-wide (`Set-OrganizationConfig
   -SendFromAliasEnabled $true`) and the client app supports picking the From address.
   - Tenant-wide: enabling it for one user enables it for everyone. Approve at that scope
     or decline.
   - Client support is uneven (older Outlook, mobile) — verify against Microsoft's current
     docs before promising one.
   - If the user must reliably SEND as the address and the tenant won't enable it, the
     honest answer is a shared mailbox with Send As (shared-mailbox-delegation).

4. Name change: add the new address, verify, swap primary (uppercase `SMTP:`), keep the old
   as an alias so nothing bounces. The sign-in UPN is a separate change with its own blast
   radius (device re-auth) — flag it, never bundle it silently.

5. Verify: mail to the new alias or plus address arrives; if send-from-alias was enabled, a
   test send shows the alias in the recipient's copy. Note it (PSA Note Discipline base
   skill: plain text, no markdown) — addresses added, primary changed or not, tenant
   settings touched, approver, caveats communicated, rollback (remove alias, restore prior
   primary). Log time.
```
