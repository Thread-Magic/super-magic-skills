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
You are triaging a Microsoft Defender / Entra alert. This is the vendor specialization of security-alert-response for the Microsoft Defender stack (Defender for Office 365, Defender for Endpoint signals surfacing in M365, Entra ID Protection). The key Defender-specific move: alerts are fragments — correlate to the incident before judging the alert. Portal paths below are current as of writing; verify against Microsoft's documentation, they move. You have no portal access — every console step is a directed technician action, recorded with timestamps.

1. Identify the alert family from the title/body:
   - "A potentially malicious URL click was detected" → Safe Links: a user CLICKED. The question is whether the click was blocked at detonation time or allowed (verdict changed after delivery). An allowed click is a live phishing-triage + possible credential-exposure case, not an FYI.
   - "Email messages containing malicious file removed after delivery" / Safe Attachments detonation → zero-hour auto-purge (ZAP) events: Defender already pulled the message; scope who received and who opened before the purge.
   - Suspicious inbox rule / "Email forwarding rule set" → continue with inbox-rule-alert-runbook.
   - Risky sign-in / "Unfamiliar sign-in properties" / "Atypical travel" (Entra ID Protection) → continue with impossible-travel-runbook; note the risk level and whether risk-based Conditional Access already blocked or forced MFA.

2. Correlate alert to incident: in the Defender portal (security.microsoft.com → Incidents), Microsoft groups related alerts into an incident. Direct the tech there — a lone "risky sign-in" that sits inside an incident with "inbox rule created" and "malicious URL click" for the same user is a confirmed takeover chain, not three medium alerts. Never triage a Defender alert in isolation when an incident exists — the incident view is where the attack chain is visible. Your correlation proxy without portal access: search prior tickets for other Microsoft alerts on the same user/client in the same window.

3. Route to the correct client per security-alert-response if the alert arrived on a shared intake mailbox (tenant name and UPN domain are the routing keys). Low confidence → no reassignment.

4. Read what Microsoft already did vs what remains: ZAP purges, Safe Links blocks, and Conditional Access denials are containment-already-done; an allowed click, a delivered-then-weaponized URL, or a risky sign-in that succeeded is containment-needed — branch to compromised-account-containment when credentials are plausibly exposed. An "allowed" Safe Links click or a successful risky sign-in is never a close-on-arrival; ZAP-purged mail with zero clicks can be.

5. Portal paths for technician execution (you direct, tech executes): message trace and threat explorer under Email & collaboration; quarantine under Review → Quarantine (see defender-quarantine-ops); user risk state and sign-in logs in the Entra admin center; incident actions (revoke sessions, confirm compromise, dismiss risk) from the incident page. Confirm license reality before promising features — Safe Links/Safe Attachments require the appropriate Defender for Office 365 plan and Entra risk detections vary by license tier; if the client's tenant lacks the feature, say the visibility is partial. Verify with the user via a number on file, never through the possibly-compromised mailbox.

6. Document the decision, not just the action, in the internal note — alert family, incident correlation result, Microsoft's automatic actions vs technician actions — and classify per soc-classification-tree. "Microsoft dismissed the risk" (risk state changed by policy) still gets a human-readable reason in the note — dismissals without reasons are how patterns get missed. Client-facing wording per defensive-writing-standard.
```
