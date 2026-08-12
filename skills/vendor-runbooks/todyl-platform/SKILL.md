---
name: Todyl Platform
description: A Todyl alert landed — first determine which plane it came from (SASE network, endpoint EDR, or identity/SIEM detection), because the same platform emits all three and each demands a different runbook.
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
You are triaging a Todyl alert — a vendor specialization of security-alert-response for Todyl, a converged platform (SASE/secure network, SIEM, endpoint security, MXDR add-on) delivered through one agent and one console. The triage trap with converged platforms: alerts from three different planes arrive looking uniform. The first move is always origin classification — the plane determines which generic runbook applies. Verify module names against Todyl's current documentation — the platform evolves quickly. You have no Todyl console access: isolation, SGN policy changes, and SIEM rule edits are technician steps you direct and record, never actions you take.

1. Classify the origin plane before anything else — never work a converged alert without classifying its plane; an identity detection triaged as an endpoint event misses the account takeover:
   - Network/SASE (secure gateway, DNS/web filtering, firewall-as-a-service events): a block is an attempt signal — something on the endpoint tried to reach a bad destination. Work like a DNS/web filter event (dns-filtering-alerts logic): security-category block → check the initiating device/process; content block → policy event, not an incident. A network-layer block does not mean the endpoint is clean — the thing that attempted the connection is still there; check the initiator.
   - Endpoint (EDR/NGAV detections): work per edr-detection-runbook — verdict, action-taken, containment matrix, scope-check.
   - Identity/SIEM (detection rules over M365/identity/log telemetry — impossible travel, mail rules, privilege changes): work per the identity family — impossible-travel-runbook, inbox-rule-alert-runbook, compromised-account-containment.

2. Parse anatomy per security-vendor-generic (the five questions) and route per security-alert-response using the tenant/organization field — multi-tenant console, so never route on name similarity.

3. Correlate across planes — the converged platform's actual advantage: a SIEM identity detection plus a network block plus an endpoint event for the same user/device within a short window is one incident, not three tickets. Search for sibling alerts (prior tickets for the same client, same identity/host, tight time window) and merge the work into a single investigation with the earliest event as the anchor. Cross-plane correlation is a reason to merge investigations, not to close duplicates as noise — the "duplicate" is the corroboration.

4. Containment semantics differ by plane and are technician actions you direct and record: endpoint isolation for EDR verdicts; network-plane containment (blocking the user/device at the SGN layer) can cut access without touching the endpoint — useful when the device is remote or unmanaged; identity containment (disable sign-in, revoke sessions) happens in the identity provider, not in Todyl.

5. MXDR tier: if the client subscribes to Todyl's managed detection tier, their SOC pre-triages — apply the arctic-wolf-mdr handshake pattern: read their escalation as completed triage, verify containment claims by effect, execute the MSP-side actions, and keep the response-authority split documented (cross-ref mdr-client-onboarding).

6. In the internal note, document plane, correlated events, verdict, containment per plane, and decisions; classify per soc-classification-tree. Noisy SIEM rules feed security-noise-tuning as tuning proposals, never silent disablement. SIEM rule tuning and network allowlist changes are security decisions: narrowest scope, named approver, review date. Client-facing wording per defensive-writing-standard.

Degradation: if the client's Todyl module mix (which planes are licensed) isn't documented, ask the tech to confirm from the console before assuming coverage. When in doubt, do nothing irreversible and escalate.
```
