---
name: Defender Quarantine Ops
description: Review Microsoft 365 Defender quarantine items and release requests using Defender portal paths, verdict types, and disciplined release mechanics.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# Defender Quarantine Ops

**When to use:** A "You have messages in quarantine" digest reply or user release request lands as a ticket; a release request appears in the portal awaiting admin approval; or a tech asks whether a specific quarantined message is safe to release.

**Run it:** on the release-request ticket.

## Prompt

```
Handle a Microsoft 365 quarantine review or release request — the vendor specialization of
quarantine-release-request. The release logic (verify the requester, respect the verdict
class, never touch the payload, when in doubt don't release) lives in the generic skill; you
add where things are in the Microsoft portal and what the Defender verdict and policy
machinery mean. You have no portal access — the technician performs the portal action, you
recommend and record. Use plain-text notes, no markdown or emojis, for anything syncing to
a PSA.

1. Run quarantine-release-request first. All of its guardrails apply, malware verdicts
   included. Everything below is the Defender layer.

2. Locate the item: security.microsoft.com → Email & collaboration → Review → Quarantine.
   Match on recipient, subject and received time. Default retention is limited (30 days for
   most verdicts), so note the expiry before a legitimate release is lost. Expiry is not a verdict — an expired item is gone, not exonerated.

3. Read the Defender quarantine reason as the scrutiny floor:
   - High-confidence phishing or malware → never recommend release; get the content through a
     verified channel with the real sender instead. Users cannot self-release these by
     default, so a request for one arriving "from the user" deserves extra requester scrutiny.
   - Phishing that isn't high-confidence → run phishing-triage; release only on a clear
     false-positive outcome.
   - Spam, bulk, or a transport-rule or policy hold → a known legitimate sender plus expected
     business context supports release.
   - Spoof or authentication failure (SPF, DKIM, DMARC) → check whether the "legitimate"
     sender genuinely fails authentication, and route recurring cases to
     dmarc-spf-failure-triage on the sender's side or to the client's tolerance policy. Never
     release a spoof verdict because the display name looks familiar.

4. Separate the two release flows: a user-requested release sits in the portal awaiting admin
   approval (approve or deny is the technician's portal action), versus an admin-initiated
   release. Release to the specific requesting recipient, not to all recipients, unless every
   recipient's need is verified. Watch the quarantine-policy context: if users can self-release
   a verdict class, an admin-release request for that class is odd — ask why before acting.

5. Send recurring false positives to security-noise-tuning: the narrowest fix (a Tenant
   Allow/Block List entry for the sender or domain, or a transport-rule adjustment) with a
   named approver and a review date, never a blanket allow. Release and allow are different
   decisions — releasing one message does not require allowlisting the sender.

6. Document per the generic skill: requester verification, quarantine reason, evidence,
   verdict, and who released what and when.
```
