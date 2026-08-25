---
name: Todyl Platform
description: Route Todyl alerts by plane: SASE network, endpoint EDR, or identity and SIEM detection. Each plane needs a different runbook from the same platform.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Todyl Platform

**When to use:** A Todyl detection, SIEM rule hit, or network-security event arrives as a ticket; a tech asks "is this Todyl alert an endpoint thing or a network thing?"; or a client on Todyl's MXDR tier sends an escalation and the desk must split their work from ours.

**Run it:** on the alert ticket.

## Prompt

```
Triage a Todyl alert — the vendor specialization of security-alert-response for Todyl's
converged platform (SASE network, SIEM, endpoint security, MXDR add-on). Alerts from three
planes arrive looking identical, so classify the plane first; it decides which runbook applies.
Isolation, SGN policy changes and SIEM rule edits are technician steps you direct and record.

1. Classify the origin plane. An identity detection triaged as an endpoint event misses the
   account takeover.
   - Network/SASE (secure gateway, DNS/web filtering, firewall-as-a-service): a block is an
     attempt signal — something on the endpoint tried to reach a bad destination. Work it per
     dns-filtering-alerts: security-category block → check the initiating device and process;
     content block → policy event, not an incident. A network block does not mean the endpoint
     is clean.
   - Endpoint (EDR/NGAV) → edr-detection-runbook: verdict, action taken, containment matrix,
     scope-check.
   - Identity/SIEM (rules over M365, identity and log telemetry — impossible travel, mail rules,
     privilege changes) → impossible-travel-runbook, inbox-rule-alert-runbook,
     compromised-account-containment.

2. Parse the anatomy per security-vendor-generic's five questions and route on the
   tenant/organization field — the console is multi-tenant, so never route on name similarity.

3. Correlate across planes: a SIEM identity detection, a network block and an endpoint event for
   the same user or device in a tight window are one incident, not three tickets. Search prior
   tickets for siblings and merge into one investigation anchored on the earliest event. The
   duplicate is corroboration — merge it, never close it as noise.

4. Contain per plane, as technician actions you direct and record: endpoint isolation for EDR
   verdicts; network containment at the SGN layer cuts access without touching the endpoint,
   useful for remote or unmanaged devices; identity containment (disable sign-in, revoke
   sessions) happens in the identity provider, not in Todyl.

5. On the MXDR tier the vendor's SOC pre-triages — apply the arctic-wolf-mdr handshake: read
   their escalation as completed triage, verify containment claims by effect, execute the
   MSP-side actions, and keep the response-authority split documented (mdr-client-onboarding).

6. Note the plane, correlated events, verdict, containment and decisions; classify per
   soc-classification-tree. Noisy SIEM rules become tuning proposals via security-noise-tuning,
   never silent disablement. Rule tuning and network allowlist changes are security decisions:
   narrowest scope, named approver, review date. Client-facing wording per
   defensive-writing-standard.

If the licensed module mix isn't documented, have the tech confirm it from the console rather
than assume it. When in doubt do nothing irreversible and escalate.
```
