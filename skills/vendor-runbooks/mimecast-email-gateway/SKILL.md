---
name: Mimecast Email Gateway
description: Work Mimecast gateway events: held-message release requests, URL Protect click alerts, and impersonation-protect hits. Treat allowed clicks as incidents.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Mimecast Email Gateway

**When to use:** A user asks to release a message Mimecast held (or replies to a held-message digest); a URL Protect alert fires because a user clicked a rewritten link; or an impersonation-protect alert lands (suspected CEO-fraud / lookalike sender).

**Run it:** on the event or release-request ticket.

## Prompt

```
Work a Mimecast email-gateway event — the vendor specialization of quarantine-release-request
and phishing-triage, covering held-message releases, URL Protect clicks and Targeted Threat
Protection impersonation alerts. You have no Mimecast console —
releases, permits and log pulls are technician actions you recommend and record. Never
invent event detail; when in doubt, don't release.

1. Run held-message releases on quarantine-release-request — verify the requester, no payload
   interaction, urgency is a caution flag — plus the Mimecast layer:
   - The hold reason sets the scrutiny floor: spam scanning, attachment policy (blocked type
     or sandbox verdict), impersonation protect, or a content/administrative policy. A
     sandbox-malware or impersonation hold is never released on requester say-so, and a
     malware verdict is never released at all.
   - Separate user-releasable digest items (ask why they didn't; the class is often
     admin-only for a reason) from the admin-hold queues the technician works.
   - Release to the requesting recipient only. "Permit sender" is a separate allowlist
     decision with its own named approver, narrowest scope (sender address over domain) and a
     review date — never a rider on a release.

2. Read URL Protect events on the click outcome: blocked at click time, or allowed (scanned
   clean, or the user proceeded through a warning). An allowed click is never informational: the user
   reached the destination, so work it as exposure until that destination is confirmed benign. If the URL is later confirmed bad, run phishing-triage on the message, and treat a
   credential page as credential exposure — compromised-account-containment for the clicker.
   On blocked clicks, confirm no sibling deliveries of the same URL (the tech pulls the
   Mimecast click logs; you check prior tickets). Record the decoded original destination of
   any rewritten Mimecast URL, and never click either form.

3. Treat impersonation alerts — lookalike domain, display-name match, new-domain sender — as
   business email compromise: continue with vendor-fraud-bec-alert or typosquat-domain-alert.
   Never "release and warn" a held impersonation hit carrying a finance request; verify with
   the impersonated party on a number on file.

4. Send recurring false positives to security-noise-tuning: the narrowest permit (sender
   address over domain, domain over policy loosening), a named approver, a review date.

5. Note the decision, not just the action: hold reason or click outcome, requester
   verification, evidence, who released or permitted what and when. Classify per
   soc-classification-tree; client-facing wording per defensive-writing-standard.

Name what the tech should pull from Mimecast — click logs, hold queue, policy match — rather
than guessing at it. When in doubt do nothing irreversible and escalate.
```
