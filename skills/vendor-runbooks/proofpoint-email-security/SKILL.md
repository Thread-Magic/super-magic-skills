---
name: Proofpoint Email Security
description: A Proofpoint event needs working — a TAP click or attachment-sandbox alert, a quarantine-digest release request, or VAP-driven prioritization. Read permitted-vs-blocked clicks correctly and keep release discipline.
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
You are working a Proofpoint email-security event. This is the vendor specialization of quarantine-release-request and phishing-triage for Proofpoint (Essentials and enterprise TAP deployments). The high-value Proofpoint reads: TAP's permitted-vs-blocked click distinction, attachment sandbox verdicts, and the VAP (Very Attacked People) lens for prioritization. Verify product tier and console paths against Proofpoint's current documentation — Essentials and TAP differ materially, so if the deployment tier lacks a feature (e.g. no TAP), say the visibility is partial rather than guessing. You have no Proofpoint console access — retraction, release approval, and threat details are technician steps you direct and record, never actions you take. Never invent data. When in doubt, do nothing irreversible and escalate.

1. TAP click events → the decisive field is click status: "blocked" (user stopped at click time) vs "permitted" (user reached the destination — either the URL was convicted after the click or policy allowed it). A "permitted" click is never closed as informational — the user reached the destination; exposure is assumed until disproven. A permitted click on a convicted URL is a live incident: phishing-triage on the message; credential-harvesting page involved → compromised-account-containment for the clicker, immediately. For blocked clicks, scope siblings: TAP shows who else received the same threat (technician checks the TAP dashboard); you check prior tickets for related user reports. Never interact with rewritten (urldefense) or original URLs during assessment; record both forms in evidence, click neither.

2. Attachment sandbox convictions → note whether conviction happened pre-delivery (held — contained) or post-delivery (delivered, then convicted — Proofpoint may flag for retraction depending on deployment). Post-delivery convictions: identify recipients, confirm opens with the users via a verified channel, and treat opened-on-endpoint cases as edr-detection-runbook cases on those devices. Sibling scoping is mandatory on convictions — one convicted message almost always has co-recipients.

3. Quarantine-digest release requests → run quarantine-release-request as the spine: verify the requester, read the quarantine reason (spam/bulk vs phish/malware verdict — the latter never releases on say-so; a delayed newsletter is cheap, a released payload isn't), assess sender legitimacy without touching the payload, release to the requesting recipient only. Allowlist ("safe sender") proposals are separate security decisions with a named approver and review date; recurring false positives route to security-noise-tuning.

4. VAP awareness: Proofpoint ranks the client's most-attacked people. Use it as a prioritization multiplier, not a verdict: a phishing report or permitted click involving a VAP-listed user (typically finance, exec, payroll) gets a higher tier and a faster clock per security-alert-response. VAP status raises priority; it never lowers scrutiny of "expected" mail for those users — VAPs are targeted precisely with expected-looking mail. Also feed it back: recommend the client's VAP list inform who gets phishing-resistant MFA and training first (route to account management, not this ticket).

5. Document the decision, not just the action, in the internal note: click status or verdict class, recipients scoped, requester verification for releases, and what the technician executed in the console vs what you recorded. Console actions (retraction, release approval, threat details) are technician steps; you direct and record. Classify per soc-classification-tree; client-facing wording per defensive-writing-standard.
```
