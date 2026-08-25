---
name: Cork Protection Posture
description: Handle Cork cyber-warranty posture signals: identify the required control that slipped and restore it to compliance before warranty coverage lapses.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Cork Protection Posture

**When to use:** A Cork signal fires that a required control is missing, unhealthy, or out of compliance (EDR gap, MFA not enforced, backup failing, email security off); a warranty-eligibility or coverage-at-risk notice needs working; or a tech asks what a Cork posture signal means or whether it's an incident.

**Run it:** on the alert ticket.

## Prompt

```
Triage a Cork Protection posture signal. Cork is the MSP cyber-warranty platform: it monitors
whether a client's stack keeps the controls its warranty requires (EDR deployed and healthy,
MFA enforced, backup running, email security active) and signals when one slips. A posture
signal is usually not an active security incident but a warranty-eligibility gap that, left
unaddressed, can void coverage or reduce a future payout: treat it as compliance remediation
on a business clock, escalating to the security path only when the slipped control also
evidences a live threat. Never interpret warranty terms from
memory: cite the client's documentation and mark anything unconfirmed. You have no Cork or
product consoles — remediation is a technician action in the owning product that you direct
and record, and you never change warranty settings.

1. Read the signal as posture: which control slipped, on which asset or tenant, since when,
   and what the warranty requires for that control. Copy Cork's exact requirement wording.
   Route to the client per the desk's routing rules; low confidence means flag for a human.

2. Confirm the gap is real, not a reporting artifact: verify the control's actual state
   through the owning product's runbook — EDR → the EDR vendor runbook or the
   edr-detection-runbook coverage check; MFA → the identity runbook; backup → the backup
   vendor runbook; email → the email-security runbook. Say which it is: a mis-reported
   control is a Cork data-quality fix, not a scramble.

3. Decide the lane:
   - Pure compliance gap (the control is genuinely off or unhealthy, no threat evidence) →
     remediation on a warranty clock: restore the control, and record the window it was out
     so coverage isn't jeopardized.
   - Gap that also evidences active compromise (EDR disabled by an attacker, backups deleted,
     MFA removed maliciously) → a security incident first: go to security-alert-response
     immediately and treat the warranty gap as secondary. The moment a slipped control looks
     attacker-caused, flip lanes.

4. Prioritize by coverage risk: a lapsed control that voids warranty on a
   high-value client, or one that doubles as an attack indicator, outranks minor hygiene
   drift.

5. Drive remediation through the owning product and confirm Cork re-reads the control as
   compliant — the loop isn't closed until the posture signal clears.

6. Note the slipped control, the real-versus-artifact verdict, the lane, the remediation and
   the re-compliance confirmation. Record when the control slipped and when it was restored —
   that window decides coverage, so never obscure it.
   Client-facing wording per defensive-writing-standard — frame it as protecting their
   coverage, not blame.

Without documentation access the client's required-control set and warranty terms may be
unknown — say so before declaring a gap.
```
