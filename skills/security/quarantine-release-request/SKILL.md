---
name: Quarantine Release Request
description: Handle a quarantined email release request: verify the requester, assess why the filter caught it, and recommend release or refusal with reasoning.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: yes
role: [Technician, Security & Compliance Owner]
outcome: [Faster Resolution & Response, Always-On Coverage]
---

# Quarantine Release Request

**When to use:** A user asks "can you release this email from quarantine?"; a quarantine-digest reply or release-request ticket lands on the board; or a tech wants a second opinion before releasing a held message.

**Run it:** on one ticket · or as a Flow (triggered on a quarantine-release request ticket).

## Prompt

```
A release request is a Request ticket with an Incident sometimes hiding inside: the ask can be
socially engineered, and the message was quarantined for a reason. Verify both before anything
is released. You recommend and record; the technician performs the release in the mail console.

1. Verify the requester. Is it the mailbox owner or a party authorized for that mailbox? Look
   up the contact. A third party pressing for release of someone else's held mail — especially
   with urgency — is itself a social-engineering marker. Confirm through a verified channel if
   anything feels off.
2. Read WHY the filter held it: spam or bulk score, phishing verdict, malware verdict, spoof
   or authentication failure, or policy rule. The quarantine reason sets the floor for how much
   scrutiny the release needs.
3. Assess the message without touching its payload — no clicking links, no opening attachments.
   Weigh sender reputation and history with the client (search for prior correspondence or
   reports of that sender), whether the business context makes the message expected, and
   whether phishing-triage indicators apply.
4. Decide by verdict class:
   - Malware → never recommend release. Explain why, and offer to obtain the content through a
     verified channel with the real sender.
   - Phishing → run the phishing-triage assessment first; only a clear false positive supports
     release.
   - Spam, bulk or policy hold from a known legitimate sender in expected business context →
     recommend release, and note whether an allowlist adjustment is warranted; route recurring
     false positives to security-noise-tuning.
5. Note the decision, not just the action: requester verification, quarantine reason, evidence
   weighed, verdict, and who released what when. Classify as a Request per
   soc-classification-tree.

As a Flow: your entire reply is the plain-text assessment note — requester match from records,
quarantine reason, evidence weighed, recommendation. No narration. Unattended recommendations
are asymmetric: "do not release" and "needs human review" are the ONLY ones this variant may
post, because recommending release requires verifying the requester through a verified channel,
which stays attended. A malware verdict states refusal per policy, always. Quarantine reason
not readable from the thread → output nothing. Requester doesn't match the mailbox owner in
records → flag a possible social-engineering marker and route to human review. The
internal note is the only permitted write: no status or priority changes, no client-facing
replies.

Never recommend releasing a malware-verdict item — no exceptions; anyone insisting escalates to
management. Urgency from the requester is a caution flag, not a reason to skip verification.
When in doubt, don't release — escalate. A delayed newsletter is cheap; a released payload
isn't.
```
