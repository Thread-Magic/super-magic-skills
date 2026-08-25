---
name: Security Vendor Generic
description: Handle security alerts from any vendor without a dedicated runbook: extract alert anatomy, map severity to desk tiers, build a vendor escalation package.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Security Vendor Generic

**When to use:** A security alert lands from a product with no dedicated skill in this category; a new security vendor appears in a client's stack and the desk needs a working method today; or a tech asks "how do I even read this alert?"

**Run it:** on the alert ticket.

## Prompt

```
Triage a security alert from a product with no dedicated runbook. security-alert-response
owns routing, tiering and the investigation canon; you add the vendor-agnostic extraction
and escalation mechanics. Console actions are technician steps you direct and record; never
invent alert detail.

1. Make the alert answer five questions; record which ones it cannot:
   - WHO: the affected identity, device or tenant, and which client (route per
     security-alert-response, never on name similarity).
   - WHAT: detection type and the vendor's verdict language, copied verbatim.
   - WHEN: event time versus detection time versus alert time — the gaps are exposure
     windows.
   - WHERE: source and target (IP, host, mailbox, app).
   - ACTION TAKEN: what it claims it already did (blocked, quarantined, isolated) versus
     detect-only.

2. Map severity onto the desk's tiers per security-alert-response from the evidence, not the
   label: a vendor "critical" for a blocked commodity event can be Medium; a vendor "low"
   showing detect-only on a credential stealer is not Low. State the mapping and why; never close
   on the vendor's label alone, either way.

3. Work the containment matrix — "the product says blocked" is a claim until confirmed.
   Claimed contained and verifiable → verify in the console or by effect, then investigate
   scope. Claimed but unverifiable → treat as uncontained until the technician confirms.
   Detect-only, allowed, or no action field → treat as live and contain first, per
   edr-detection-runbook for endpoints or compromised-account-containment for identities.

4. Investigate per the generic runbook for the event class: identity → the
   impossible-travel-runbook family; endpoint → edr-detection-runbook; email →
   phishing-triage or quarantine-release-request; exposure feed → dark-web-alert-lifecycle.
   Identity first when the event is a login. Read the vendor's documentation for field
   meanings; mark anything inferred as inferred.

5. When the product itself must answer — unexplained verdict, suspected product fault,
   remediation only the vendor can do — build the escalation package first: alert or
   incident ID and exact timestamps with timezone, tenant identifier, product and agent
   versions, raw alert text, what was checked and ruled out, actions taken with times, and
   the specific question. One complete package in the ticket.

6. Note the decision: the five-question extraction, the severity rationale, the containment
   outcome and the verdict. Classify per soc-classification-tree; write client-facing
   wording per defensive-writing-standard. Exclusions and allowlists are security decisions
   whatever the vendor: narrowest scope, named approver, review date. If this vendor keeps appearing, flag that it deserves its own runbook.

When in doubt do nothing irreversible and escalate.
```
