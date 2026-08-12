---
name: Group Membership Request
description: Handle a security group membership change by stating what the group actually grants, getting the right approver, and setting a review date on the change.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Group Membership Request

**When to use:** "Add <user> to the VPN users group" / "<user> needs the finance-apps security group" / "remove <user> from admins" — especially a group add requested with no explanation of what it unlocks.

**Run it:** on one ticket — an access-control decision, so approval- and human-gated.

## Prompt

```
Process this security-group change as an access-control decision, not a list edit: the
note must say in plain language what the group grants, who approved it, and when it
gets reviewed.

1. Identify the exact group and the user (look up the contact). Determine what the group
   actually grants — check the group description, the client's documentation (knowledge
   base / IT Glue), and what resources/policies reference it. If you cannot determine
   what a group grants, STOP: that's a question for the client's admin, not a grant to
   make blind.

2. Classify sensitivity. Groups granting admin rights, security-tool access, financial
   systems, or conditional-access bypass are high-sensitivity: they require the
   client's documented high-privilege approver, not just a manager. Ordinary resource
   groups need the group owner or manager per policy.

3. Get approval before the change (send an approval request, or use the client's
   channel), presenting the plain-language statement of what the group grants so the
   approver knows what they're signing.

4. Apply least privilege: if a narrower group satisfies the stated need, propose that
   instead.

5. Execute. For on-prem/synced groups, change in AD, run an AD Connect delta sync, and
   verify membership propagated before reporting done.

6. Set a review date: permanent grants get the client's standard access-review cycle
   noted; temporary grants get an expiry and a tracked revert (follow-up note or
   scheduled ticket).

7. Post a plain-text note: group name, what it grants (the plain-language statement —
   this is the point of the note), user, approver, rationale, and review/expiry date.
   Log time.

Guardrails: never add to a group whose effect you cannot state — "it fixes the error"
is not a known effect. High-sensitivity groups require the documented high-privilege
approver; manager approval is not sufficient for admin-grade groups. Every grant
carries a review date or expiry. Removals requested outside offboarding get confirmed
with the group owner — removing someone can break their access mid-task. When in doubt
about sensitivity or approver, escalate; do not grant.
```
