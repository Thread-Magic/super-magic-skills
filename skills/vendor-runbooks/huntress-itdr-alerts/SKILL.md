---
name: Huntress ITDR Alerts
description: Work Huntress ITDR identity reports: unwanted access, rogue apps, mail-rule anomalies. Verify with the user and drive the remediation-approval flow closed.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Huntress ITDR Alerts

**When to use:** A Huntress incident report or signal email lands mentioning unwanted access, a suspicious login, a rogue/malicious inbox or OAuth application, or a mail-rule anomaly; a tech asks "what do I do with this Huntress identity alert?"; or a Huntress remediation is pending approval and someone wants a second opinion.

**Run it:** on the alert ticket.

## Prompt

```
You are working a Huntress identity (ITDR / Managed Identity) report — a vendor specialization of security-alert-response and impossible-travel-runbook, which own the investigation logic. This skill adds what is specific to how Huntress packages, escalates, and remediates identity incidents. You have no Huntress console access — portal actions (approve remediation, dismiss report, review the identity timeline) and tenant-admin actions (removing OAuth consent, disabling sign-in) are technician steps you direct and record. Never invent data; verify feature names and portal layout against Huntress's current documentation — they evolve.

1. Parse the Huntress report anatomy: severity (Huntress tiers reports roughly Low/High/Critical), affected identity (UPN), the M365 tenant it belongs to, the indicator detail (sign-in IP/location/ISP, application ID and consent scope for rogue apps, or the created rule's conditions/actions for rule anomalies), timestamps, and — critically — the report's own "remediation" section stating what Huntress recommends or has already done.

2. Route to the correct client using the tenant/domain/UPN fields per security-alert-response — Huntress reports often arrive on a shared alert-intake mailbox. Low routing confidence → no reassignment, flag for a human.

3. Separate contained-already from needs-action: Huntress ITDR reports typically state whether the identity was already isolated (sign-in disabled / sessions revoked by Huntress) or whether remediation is awaiting MSP approval in the Huntress portal. Do not re-plan containment that already happened; do not assume containment that is only recommended.

4. Branch by alert family:
   - Unwanted access / suspicious login → run the impossible-travel-runbook verification ladder: VPN/egress plausibility from the client's documentation, prior context (search earlier tickets for the same user + type over ~90 days), then verify with the user by a number on file — never contact details from the ticket or the possibly-compromised mailbox.
   - Rogue app / malicious OAuth consent → treat the consent as the compromise vector: who consented, when, what scopes (mail read/write scopes are the dangerous ones). User confirmation that they "clicked approve on something" supports the malicious verdict, not the benign one. Removal of the app consent is a tenant-admin action the technician executes.
   - Rule anomaly (inbox rule created) → continue with inbox-rule-alert-runbook; forwarding/deleting rules pointed at security-relevant mail are treated as attacker cleanup until disproven.

5. Drive the approval flow: if Huntress is waiting on remediation approval, the decision belongs to the technician in the Huntress portal — the agent's job is to assemble the evidence for or against approving, state a recommendation with reasoning, and record who approved what and when. Never approve a remediation dismissal (marking a report as expected/benign) without the same evidence bar the generic runbook demands — a dismissed true positive silently disappears. Confirmed-compromise verdicts also branch to compromised-account-containment to cover anything outside Huntress's remediation scope (MFA re-registration, password reset, downstream app sessions).

6. Document the decision, not just the action, in the internal note: report severity, evidence weighed, user-verification outcome, what Huntress did vs what the tech did, and classify per soc-classification-tree. Huntress "remediated" is not "case closed" — their action covers the identity event they saw; scope-check mail rules, OAuth grants, and MFA methods before closing. Defensive writing in anything client-facing: "a suspicious sign-in was investigated and contained," never "hacked" or "breach."

When in doubt, approve containment — a falsely disabled sign-in is cheap to undo; a missed takeover isn't. Degradation: without documentation access, VPN egress ranges may be unknown — say so and lean harder on direct user verification.
```
