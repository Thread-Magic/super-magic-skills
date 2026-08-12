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
A release request is a Request ticket with an Incident sometimes hiding inside it: the ask
itself can be socially engineered, and the message was quarantined for a reason. Verify both
before anything gets released. You recommend and record; the technician performs the release
in the mail console. Work it in order:

1. Verify the requester: is the request coming from the mailbox owner or a party authorized
   for that mailbox (look up the contact)? A third party pressing for the release of someone
   else's held mail — especially with urgency — is itself a social-engineering marker.
   Confirm through a verified channel if anything feels off.
2. Read WHY the filter held it: spam/bulk score, phishing verdict, malware verdict,
   spoof/authentication failure, or policy rule. The quarantine reason sets the floor for
   how much scrutiny the release needs.
3. Assess the message's legitimacy without interacting with its payload (no clicking links,
   no opening attachments): sender reputation and history with the client (search for prior
   correspondence or prior reports of the sender), whether the business context makes the
   message expected, and whether phishing-triage indicators apply.
4. Decide by verdict class:
   - Malware verdict → never recommend release. Explain why to the requester; offer to
     obtain the content through a verified channel with the real sender instead.
   - Phishing verdict → run the phishing-triage assessment first; only a clear
     false-positive outcome supports release.
   - Spam/bulk or policy hold with a known legitimate sender and expected business context →
     recommend release, and note whether an allowlist adjustment is warranted (route
     recurring false positives to security-noise-tuning).
5. The release itself is the technician's action in the mail console — you recommend and
   record.
6. Document the decision, not just the action: requester verification, quarantine reason,
   evidence weighed, verdict, and who released what when. Classify as a Request per
   soc-classification-tree.

Unattended (Flows) variant:
- The entire reply is a plain-text assessment note posted verbatim — requester-match from
  records, quarantine reason, evidence weighed, recommendation. No narration.
- Unattended recommendations are asymmetric: "do not release" and "needs human review" are
  the ONLY recommendations this variant may post. Recommending release requires verifying
  the requester through a verified channel — a judgment step that stays attended. Malware
  verdict → the note states refusal per policy, always.
- Deterministic input from the flow: the release-request ticket id. Quarantine reason not
  readable from the thread → output nothing. Requester does not match the mailbox owner in
  contact records → flag a possible social-engineering marker and route to human review.
- Permitted writes: the internal note only. No status or priority changes, no client-facing
  replies, and never any interaction with the held message's links or attachments.

Guardrails — always:
- Never recommend releasing a malware-verdict item — no exceptions; anyone insisting
  escalates to management.
- Never interact with the held message's links or attachments during assessment.
- Urgency from the requester is a caution flag, not a reason to skip verification — pressure
  is how bad releases happen.
- When in doubt, don't release — escalate. A delayed newsletter is cheap; a released payload
  isn't. Recommend-and-document is the boundary: you do not perform releases.
```
