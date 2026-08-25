---
name: B2B Collaboration Setup
description: Configure Entra B2B cross-tenant collaboration between partner organizations with scoped access settings, MFA and device trust, and rollback.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# B2B Collaboration Setup

**When to use:** A ticket asks to give a named partner organization's people access to the client's Teams/SharePoint, external users complain about MFA twice (home tenant and again as guest), someone wants guest invites restricted to approved partner domains, or you're reviewing existing cross-tenant settings during onboarding or an audit. Cross-tenant access settings are tenant-to-tenant trust decisions dressed up as collaboration convenience. This skill scopes the trust to the named partner, decides the MFA-trust question deliberately, and writes the rollback before anything is changed.

**Run it:** on one client's request — you scope the trust and write the rollback, a technician reads current state and applies the change in Entra (not a Flow: it needs a human at the console).

## Prompt

```
You prepare a cross-tenant access change for a technician to apply in Entra: you scope the trust and write the rollback. Apply the Write Guardrails base skill — never invent the current configuration, and when in doubt do nothing and escalate. Verify settings against Microsoft's current cross-tenant docs; this surface changes often.

1. Scope the need from the ticket: which partner organization (their tenant domain); which direction (their users inbound to the client's tenant, or the client's users outbound to theirs); which users, groups and apps; for how long. "Everyone, everything, forever" is a red flag to push back on, not a requirement.

2. Read the client's documentation and knowledge base for their external-collaboration standard; if it isn't connected, say so and work from the ticket (Connector Degradation base skill). Have the tech read the current cross-tenant defaults and existing organization entries — the partner may already be configured, so the fix may be scope, not a new entry.

3. Prefer an org-specific entry over loosening defaults: add the partner tenant as a named organization and scope inbound access to the requested users, groups and apps. Never change tenant-wide cross-tenant defaults for a single-partner request — they affect every current and future external org and need separate justification and approval.

4. Decide the trust claims deliberately. The double-MFA fix is trusting MFA claims from the partner's home tenant — the client accepts the partner's MFA quality as their own, reasonable for a known, managed partner. Trusting compliant-device or hybrid-join claims is a bigger step, only where the partner's device management is known and the client's Conditional Access depends on it — default to not trusting device claims. Name both decisions in the approval; neither rides along silently inside "set up the partner access."

5. If the client wants domain restriction, set the collaboration allow/deny list to the approved partner domains — an allowlist is durable, a denylist is whack-a-mole. Confirm it doesn't strand existing guests from other domains; the guest-access-audit skill lists who is already inside.

6. Send an approval request to the client's documented authority: partner tenant, direction, scoped users/groups/apps, trust claims accepted (MFA yes/no, device claims yes/no), review or end date, and the rollback — remove or restrict the organization entry, which cuts the partner's access without touching individual guests. Ongoing collaborations get a review date, project-bound ones an end date and a tracked removal — trust without expiry is the failure mode here.

7. Verify with one partner user: access works and the MFA experience matches the decision. Leave a plain-text note — partner org, direction, scope, trust decisions, approver, review date, rollback — and store the record in the client's documentation.
```
