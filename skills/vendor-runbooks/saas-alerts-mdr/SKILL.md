---
name: SaaS Alerts MDR
description: Triage SaaS Alerts events in M365 and Google tenants: login anomalies, mail-rule creation, file-activity spikes, privilege changes as identity-plane EDR.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# SaaS Alerts MDR

**When to use:** A SaaS Alerts notification arrives — suspicious login/location, a mail-forwarding or inbox rule created, mass file download/deletion, an admin or role change, a risky OAuth app; a Respond automation fired (e.g. auto-locked an account) and the desk must validate and follow through; or a tech asks how to read a SaaS Alerts event or whether it's a false alarm.

**Run it:** on the alert ticket.

## Prompt

```
Triage a SaaS Alerts event — identity-plane EDR for Microsoft 365 and Google Workspace: the
primitives are sign-ins, OAuth grants, mail rules, file operations, and role changes. Base skills
own the investigation: security-alert-response (routing), compromised-account-containment (the
sweep), impossible-travel-runbook (the sign-in verification ladder). You have no console or
tenant-admin access — unlocks, rule deletions, consent revocations, and Respond changes are
technician steps you direct and record, never take or invent.

1. Parse: identity (UPN), tenant and client, event class, source IP/geo/ISP/device, timestamps,
   and whether a Respond rule already acted. The console is multi-tenant — route on the tenant and
   domain fields; low confidence means no reassignment, flag for a human.

2. If a Respond rule locked the account, containment is claimed-but-verify: confirm by effect that
   sign-in is blocked and sessions revoked before scoping. If nothing fired and the evidence says
   live takeover, contain first. An auto-lockout contains sign-in only — mail rules, OAuth grants,
   MFA methods, and app passwords survive it. Never unlock an auto-locked account on the user's
   say-so; the verification ladder decides.

3. Branch by event class:
   - Login anomaly or impossible travel — VPN and egress plausibility from the client's
     documentation, then prior tickets for this user over ~90 days, then the user on a number on
     file, never contact details from the ticket or the possibly-compromised mailbox.
   - Mail rule or forwarding created — rules that forward, delete, or divert security-relevant
     mail are attacker cleanup until disproven.
   - Risky OAuth grant — the consent is the vector: who consented, when, what scopes; mail
     read/write and offline access are the dangerous ones. Removal is a tenant-admin action.
   - Mass file download or deletion — separate offboarding-week data theft, sync-client noise, and
     ransomware-in-SaaS: check employment status and parallel device events.
   - Privilege or role change — verify against change records and the requester. Unexplained admin
     grants escalate as takeover indicators.

4. Confirmed compromise gets the full sweep: password, MFA methods, sessions, app passwords,
   delegated access, mail rules. A Respond lockout covers sign-in, not persistence.

5. Note the event class, evidence, verification outcome, and what automation did versus what the
   tech did; classify per soc-classification-tree, client-facing wording factual
   (defensive-writing-standard). Recurring benign patterns become scoped tuning (travel windows,
   known egress ranges), never blanket disablement of an alert class; Respond rule changes need
   narrowest scope, a named approver, a review date.

Without documentation, egress ranges are unknown — say so. When in doubt, do nothing irreversible
and escalate.
```
