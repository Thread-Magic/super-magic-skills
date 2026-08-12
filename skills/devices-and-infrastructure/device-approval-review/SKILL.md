---
name: Device Approval Review
description: Work the RMM pending-device approval queue — sort expected devices (onboarding, replacements) from unexpected ones, and approve or reject each with a recorded rationale. Use for "review pending devices" or when new agents show up awaiting approval.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, set_ninjaone_device_approval, search_tickets, search_contacts, add_ticket_note]
connectors: [NinjaOne]
scope: global
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Device Approval Review

**When to use:** "Any devices pending approval?" / periodic approval-queue hygiene, or a new agent install is waiting and a tech asks whether to approve it.

**Run it:** across the pending-approval queue, on demand (not a Flow — approvals need requester confirmation, not unattended firing).

## Prompt

```
Separate expected pending devices (a new-hire laptop you just onboarded) from unexpected ones (a hostname nobody recognizes), approving or rejecting each with the reasoning written down. This needs the RMM connected; if absent, say the approval queue is unavailable.

1. Pull the pending queue from the RMM, filtered to pending-approval devices. If the list may be capped, say "at least N pending" and page through.
2. For each pending device, gather identity evidence from its RMM details: hostname, registered organization, OS, last-logged-on user, first-seen time.
3. Classify expected vs unexpected:
   - Expected: matches an open/recent onboarding/replacement/project ticket (read ticket history for the hostname, user, or client over the last 30-60 days); hostname follows the client's naming convention; last-logged-on user resolves to a known contact (look up the contact); registered under the right organization.
   - Unexpected: no matching ticket, hostname off-convention, unknown user, wrong organization, or a device class that makes no sense for the client (a random server at a workstation-only client).
4. Expected devices: confirm the batch with the requester, then approve them in the RMM, and note the rationale (which ticket/user it maps to) on the related ticket (plain text, no markdown/emojis).
5. Unexpected devices: do NOT reject silently and do NOT approve. Present each with the evidence gap and a recommendation — an unknown enrollment can be benign or a security signal, so recommend verifying with the client contact first. Reject in the RMM only on explicit instruction, and record why.
6. Output: a table of pending devices with classification, evidence, and action taken or recommended.

Guardrails: never approve on hostname plausibility alone — approval requires a corroborating signal (ticket, known user, or explicit requester confirmation); approving an attacker's enrollment is the failure mode this exists to prevent. Never reject unattended — rejection can orphan a legitimately deployed machine mid-onboarding; rejections are always human-confirmed. Wrong-organization registrations are fixed by re-registration, not by approving into the wrong tenant — flag, don't approve. Result-cap honesty on queue and ticket searches.
```
