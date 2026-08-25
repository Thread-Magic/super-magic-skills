---
name: DLP Alert Triage
description: Triage a DLP alert: separate business-process false positives from real data exfiltration signals, investigating with respect for employee privacy.
category: Security
tools: [search_tickets, search_contacts, search_clients, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Fewer Escalations & Less Noise, Risk & Compliance]
---

# DLP Alert Triage

**When to use:** A DLP alert ticket arrives (sensitive-data pattern in outbound mail, cloud upload, USB copy, or share link); a tech asks "is this DLP hit a real problem or just accounting doing accounting?"; or a cluster of DLP alerts on one user needs a careful, privacy-respectful look.

**Run it:** on one ticket (a DLP alert, or a cluster on one user).

## Prompt

```
Most DLP alerts are the business doing its job — payroll emailing payroll data. Reach a
verdict on the evidence without turning the desk into surveillance of the client's staff.

1. Extract the alert anatomy: the rule that matched, the data classification and match count
   ("42 payment-card patterns"), the actor, the vector (email, cloud share, USB, print), the
   destination (recipient domain, share target, device) and the platform action (blocked,
   warned, logged-only). On shared intake, route to the client per security-alert-response.
2. Business context — the false-positive test. Does this flow match the actor's role and a
   routine process? Search the rule's history: same sender, destination and cadence points to
   a false positive — confirm it still applies, never auto-close on history alone.
3. Exfiltration signals. Destination: personal email or cloud, or a competitor's domain, not
   an established counterparty. Volume: bulk, or unusually broad for the role. Timing:
   off-hours, or paired with a resignation, an access-revocation ticket in flight, recent
   account alerts. Evasion: retrying after a block, renaming or zipping to dodge patterns.
   None alone is a verdict; accumulation raises the tier.
4. Keep it privacy-respectful: metadata first — what pattern, where to, how much. Open
   content only when the verdict requires it AND the client's policy permits desk access, and
   record that it was accessed and why. Investigate the event, not the person's mailbox at
   large.
5. Route on the verdict:
   - Business-process false positive → close with the evidence; feed recurring ones to
     security-noise-tuning for a NARROW exception (this sender group to this destination, not
     "disable the rule").
   - Real exfiltration signals, or resignation or offboarding context → do NOT confront the
     user and do not investigate further solo. Preserve the evidence and hand to
     insider-risk-basics, which escalates to client leadership.
   - Off-hours plus other anomalies → possible compromise: compromised-account-containment.
   - Blocked but benign → answer the user's real need, so the block doesn't teach workarounds.
6. Note the decision, not just the action: anatomy, business context, signals weighed, any
   content accessed and under what authority, verdict and route. Plain text; classify per
   soc-classification-tree.

No intent language — "transferred 300 files to a personal account" is evidence; "trying to
steal data" is a conclusion that belongs to the client's process. Tuning is the DLP platform
owner's job; never blanket-disable a rule or auto-close in the PSA. Report a capped or
partial alert history as such (Sweep Honesty base skill); name the evidence behind every
verdict. Without DLP-console access, work from the alert body, direct the tech on what to
pull, and record what you couldn't verify — never invent data.
```
