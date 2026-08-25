---
name: Defender M365 Alerts
description: Triage Microsoft Defender and Entra alerts: Safe Links or Safe Attachments detonation, suspicious inbox rules, risky sign-in. Correlate to the incident.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Defender M365 Alerts

**When to use:** A Defender or Microsoft 365 security alert lands as a ticket (email notification or SIEM/PSA integration); a tech asks where in the Microsoft portals to work a given alert; or multiple Microsoft alerts arrive for the same user and need correlating.

**Run it:** on the alert ticket.

## Prompt

```
Triage a Microsoft Defender / Entra alert — the vendor specialization of security-alert-response
for Defender for Office 365, Defender for Endpoint and Entra ID Protection. Console steps are
technician actions you direct and record.

1. Identify the alert family from the title:
   - "A potentially malicious URL click was detected" → Safe Links: a user CLICKED. Blocked at
     detonation, or allowed because the verdict changed after delivery? An allowed click is a
     live phishing-triage and credential-exposure case.
   - "Malicious file removed after delivery" / Safe Attachments detonation → zero-hour
     auto-purge: the message was pulled; scope who received and who opened it first.
   - Suspicious inbox rule or forwarding rule set → inbox-rule-alert-runbook.
   - Risky sign-in, unfamiliar sign-in properties, atypical travel (Entra ID Protection) →
     impossible-travel-runbook; note the risk level and whether risk-based Conditional Access
     already blocked or forced MFA.

2. Correlate the alert to its incident before judging it: Microsoft groups related alerts into
   an incident at security.microsoft.com → Incidents. A risky sign-in sitting in an incident
   with "inbox rule created" and "malicious URL click" for one user is a takeover chain, not
   three medium alerts. Without portal access, use prior tickets for other Microsoft alerts on
   that user. Route per security-alert-response when the alert landed on a shared intake mailbox
   — tenant name and UPN domain are the routing keys, and low confidence means flag for a human,
   not reassign.

3. Separate what Microsoft already did from what remains. ZAP purges, Safe Links blocks and
   Conditional Access denials are containment done; an allowed click, a URL weaponized after
   delivery, or a successful risky sign-in is containment needed — branch to
   compromised-account-containment when credentials are plausibly exposed. ZAP-purged mail with
   zero clicks can close on arrival; an allowed click never does.

4. Direct the technician's portal work: message trace and threat explorer under Email &
   collaboration; quarantine under Review → Quarantine (defender-quarantine-ops); user risk
   state and sign-in logs in the Entra admin center; revoke sessions, confirm compromise and
   dismiss risk from the incident page. Check the license: Safe Links and Safe Attachments need
   the right Defender for Office 365 plan and Entra risk detections vary by tier, so say the
   visibility is partial when the tenant lacks one. Verify with the user on a number on file,
   never through the possibly-compromised mailbox.

5. Note the alert family, the correlation result, and Microsoft's automatic actions versus
   technician ones; classify per soc-classification-tree. "Microsoft dismissed the risk" still
   needs a human-readable reason. Client-facing wording per defensive-writing-standard.
```
