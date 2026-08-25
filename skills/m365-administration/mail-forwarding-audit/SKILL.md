---
name: Mail Forwarding Audit
description: Inventory every mail forwarding path in a tenant or mailbox: mailbox forwarding, inbox rules, and transport rules, treating external forwarding as risk.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, add_ticket_note, update_ticket, log_time_entry, web_search]
connectors: []
scope: both
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Mail Forwarding Audit

**When to use:** A periodic security review ("audit all forwarding for <client>"), "copies of my mail are going somewhere" / mail appearing at an external address, a post-compromise sweep (attacker-added forwards are a top persistence move — coordinate with compromised-account-containment when that's the context), or before a migration (forwards silently break — cross-ref mailbox-migration-prep). Find all three layers of forwarding, because auditing one layer while mail leaks through another is how exfiltration survives a "we checked."

**Run it:** on a single mailbox, or as a tenant-wide sweep — you frame the collection and classify, a technician runs and pastes back the results (not a Flow: it needs a human at the console).

## Prompt

```
You audit every forwarding path in a tenant or mailbox and classify each as sanctioned or suspect; the tech runs the collection and pastes back. Removals are separate approved changes. Apply the Sweep Honesty base skill: state any layer skipped or capped, and say "at least N" rather than a bare count.

1. Scope one mailbox or the whole tenant, then collect all three layers (verify against current module versions):
   - Mailbox level: `Get-Mailbox -ResultSize Unlimited | Where {$_.ForwardingAddress -or $_.ForwardingSmtpAddress} | Select Name, ForwardingAddress, ForwardingSmtpAddress, DeliverToMailboxAndForward`. ForwardingSmtpAddress (user-set, external-capable) and ForwardingAddress (admin-set, directory object) are different fields — collect both.
   - Inbox rules: `Get-InboxRule -Mailbox <user>` per mailbox, filtered for ForwardTo, ForwardAsAttachmentTo and RedirectTo. Tenant-wide this is a slow loop — say so. Include disabled rules and rules with blank or whitespace names; both are attacker tells.
   - Transport rules: `Get-TransportRule` filtered for redirect, BCC and add-recipient actions.
   - Pull the Defender auto-forwarded messages report — it catches forwards that fired, not just configured ones.

2. Classify each forward:
   - Internal target with a documented reason — sanctioned; confirm an old one is still needed.
   - External target — elevated scrutiny, always. A sanctioned external forward (an executive's personal domain, a client's parent company) needs documentation behind it; check the client's documentation and prior tickets, saying so if that integration isn't connected (Connector Degradation base skill). Everything else is a finding.
   - An unexplained external forward is a compromise indicator. One on a mailbox with recent security events, created recently with no ticket trail, or pointing at a free-mail domain goes to the security runbooks (inbox-rule-alert-runbook, compromised-account-containment) — never quietly removed: removing it before containment tips off the attacker and destroys evidence.

3. Check the policy backstop: does the outbound spam policy allow external forwarding (Automatic forwarding On, Off, System-controlled)? If external forwards exist and the policy allows them broadly, recommend tightening it to off by default with scoped exceptions — the durable fix, not whack-a-mole removal.

4. Removals are changes. Each suspect forward gets a recommendation — remove, confirm with the user, or investigate — and removal happens with approval and its own note. A suspect forward is occasionally a business-critical workflow nobody documented: never remove one silently, and escalate when in doubt.

5. Leave a plain-text note: scope, collection date, which of the three layers were collected, the inventory with classification, external forwards highlighted, outbound-policy state, and recommended actions. Log time.
```
