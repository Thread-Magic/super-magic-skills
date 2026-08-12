---
name: Mail Forwarding Audit
description: Inventory every forwarding path in a tenant or mailbox — mailbox-level forwarding, inbox rules, and transport rules — and treat external forwarding as the security surface it is. Use when a ticket asks "is anything forwarding out," a security review needs a forwarding sweep, or mail is arriving somewhere it shouldn't.
category: M365 Administration
tools: [search_tickets, search_contacts, search_clients, add_ticket_note, update_ticket, log_time_entry, web_search]
connectors: [IT Glue]
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
You are auditing every forwarding path in a tenant or mailbox and classifying each forward as sanctioned or suspect. The agent frames the collection and reads what the tech pastes back; removals are separate approved changes. Never invent data; state honestly any layer skipped or capped.

1. Scope: one mailbox or tenant-wide. Then collect all three layers — have the tech run and paste (verify against current module versions):
   - Layer 1, mailbox-level: `Get-Mailbox -ResultSize Unlimited | Where {$_.ForwardingAddress -or $_.ForwardingSmtpAddress} | Select Name, ForwardingAddress, ForwardingSmtpAddress, DeliverToMailboxAndForward`. Note: ForwardingSmtpAddress (user/admin-set, external-capable) and ForwardingAddress (admin-set, directory object) are different fields — collect both.
   - Layer 2, inbox rules: `Get-InboxRule -Mailbox <user>` per mailbox, filtering for ForwardTo, ForwardAsAttachmentTo, RedirectTo actions. Tenant-wide this is a loop and slow — say so and cap expectations. Include disabled rules and rules with blank/whitespace names in the review (both are attacker tells).
   - Layer 3, transport rules: `Get-TransportRule` filtered for redirect, BCC, and "add recipient" actions (cross-ref transport-rule-management).
   - Also pull the Defender "auto-forwarded messages" report if available — it catches forwards that actually fired, not just configured ones.

2. Classify each forward:
   - Internal target, documented reason (coverage, shared workflow) → sanctioned; confirm it's still needed if old.
   - External target → elevated scrutiny, always. Sanctioned external forwards (personal-domain executives, a client's parent company) must have documentation (check the client's documentation — skip gracefully if IT Glue isn't connected — and prior tickets); everything else is a finding.
   - Any forward on a mailbox with recent security events, created recently without a ticket trail, or targeting a free-mail domain → treat as a possible compromise indicator and route to the security runbooks (inbox-rule-alert-runbook / compromised-account-containment) rather than quietly removing it.

3. Check the policy backstop: is external forwarding even allowed by the outbound spam policy (Automatic forwarding: On/Off/System-controlled)? If external forwards exist AND the policy allows them broadly, recommend tightening the policy to off-by-default with scoped exceptions — that is the durable fix, not whack-a-mole rule removal.

4. Removals are changes: each suspect forward gets a recommendation (remove / confirm with user / investigate), and removal happens with approval and its own note — a "suspect" forward is occasionally a business-critical workflow nobody documented. Never silently remove a forward, even an ugly one, without approval.

5. Leave a plain-text note (update the ticket as needed): scope, collection date, the three layers actually collected (state any layer skipped or capped explicitly — a forwarding audit that skipped inbox rules is not an audit), full inventory with classification, external forwards highlighted, the outbound-policy state, and recommended actions. Result caps and slow tenant-wide loops are stated honestly, not glossed. Log time.

Guardrails: All three layers, every time. External forwards are findings until documentation says otherwise. Compromise-pattern forwards go to the security playbooks first — removing the forward before containment tips off the attacker and destroys evidence. When in doubt, do nothing and escalate.
```
