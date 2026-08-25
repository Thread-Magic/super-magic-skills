---
name: Proofpoint Email Security
description: Work Proofpoint email security events: TAP click alerts, attachment-sandbox verdicts, quarantine-digest release requests, and VAP-driven priority triage.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Proofpoint Email Security

**When to use:** A Proofpoint TAP alert lands (URL click, attachment sandbox conviction, message delivered then convicted); a user replies to a Proofpoint quarantine digest asking for a release; or a tech asks how hard to prioritize a phishing report for a particular user.

**Run it:** on the event or release-request ticket.

## Prompt

```
Work a Proofpoint email-security event — the vendor specialization of quarantine-release-request
and phishing-triage for Proofpoint Essentials and enterprise TAP. Essentials and TAP differ
materially — if the tier lacks a feature, say the visibility is partial. Retraction, release
approval and threat details are technician steps you direct and record.

1. TAP click events turn on click status: "blocked" (stopped at click time) versus "permitted"
   (the user reached the destination — convicted after the click, or allowed by policy). A
   permitted click is never informational: assume exposure until disproven, and a permitted
   click on a convicted URL is a live incident — run phishing-triage on the message, and branch
   immediately to compromised-account-containment for the clicker if a credential-harvesting
   page was involved. For blocked clicks, scope siblings: the technician checks the TAP
   dashboard for other recipients while you check prior tickets for related reports. Never open
   a rewritten (urldefense) or original URL while assessing — record both forms as evidence and
   click neither.

2. Attachment sandbox convictions: note whether conviction was pre-delivery (held — contained)
   or post-delivery (delivered then convicted, possibly flagged for retraction). For
   post-delivery convictions, identify recipients, confirm opens with the users on a verified
   channel, and work opened-on-endpoint cases per edr-detection-runbook. Sibling scoping is
   mandatory — one convicted message almost always has co-recipients.

3. Quarantine-digest release requests run quarantine-release-request as the spine: verify the
   requester, read the quarantine reason (spam or bulk versus a phish or malware verdict — the
   latter never releases on say-so; a delayed newsletter is cheap, a released payload isn't),
   assess sender legitimacy without touching the payload, and release only to the requesting
   recipient. Safe-sender proposals are security decisions with a named approver and review
   date; recurring false positives route to security-noise-tuning.

4. Proofpoint ranks the client's most-attacked people (VAPs). Use that as a prioritization
   multiplier, not a verdict — a phishing report or permitted click involving a VAP-listed user
   (typically finance, exec, payroll) gets a higher tier and a faster clock per
   security-alert-response. It never lowers scrutiny: VAPs are targeted precisely with
   expected-looking mail. Feed it back: the VAP list should inform who gets phishing-resistant
   MFA and training first, via account management.

5. Note the click status or verdict class, recipients scoped, requester verification, and what
   the technician executed versus what you recorded; classify per soc-classification-tree.
   Client-facing wording per defensive-writing-standard. When in doubt do nothing irreversible
   and escalate.
```
