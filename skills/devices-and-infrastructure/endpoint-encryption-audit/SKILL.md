---
name: Endpoint Encryption Audit
description: Audit disk-encryption coverage on Windows BitLocker and Mac FileVault, flag unencrypted endpoints, and verify recovery keys are escrowed and retrievable.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, liongard_launchpoint, liongard_metric, liongard_query, search_itglue, search_hudu, search_tickets, add_ticket_note, create_ticket]
connectors: [NinjaOne, Liongard, IT Glue, Hudu]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Endpoint Encryption Audit

**When to use:** "Are all of <client>'s laptops encrypted?" for compliance/insurance, a lost-device breach-severity question, or "do we actually have the BitLocker keys for these machines?"

**Run it:** across a client's endpoint fleet, on demand (not a Flow — it's an audit/evidence pass, not a per-ticket event).

## Prompt

```
Two questions: is every endpoint's disk encrypted, and if a device died tomorrow could the
desk retrieve its recovery key? Coverage without escrow is a lockout; escrow without
coverage is a breach.

1. Build the endpoint population from the RMM (verify workstation/laptop class in the
   details; a class filter is not evidence) — that is the denominator. Apply the Sweep
   Honesty base skill: if listings may have capped it is "at least N", and say so.

2. Gather encryption state per device, best source first: RMM device details where they
   expose encryption or volume status; the environment's posture in Liongard via its
   Windows and M365/Entra inspectors (apply the Inspector Read Discipline base skill —
   confirm the inspector exists and last ran successfully, read BitLocker and escrowed-key
   status, state the dataprint age); documentation (IT Glue / Hudu) last, with staleness
   named. Devices with no encryption evidence go in an "unknown" bucket — not unencrypted,
   and definitely not encrypted.

3. Bucket the fleet: encrypted with key escrowed, encrypted with NO escrow evidence (one
   dead motherboard from permanent data loss), not encrypted, unknown. Macs: FileVault
   status usually needs MDM data (Liongard, Intune, or an MDM export); with no Mac source
   the Mac fleet is "unknown", stated plainly.

4. Verify escrow on evidence, not assumption: identify where keys should live (Entra/AD,
   MDM, doc-platform flagged fields, per client policy) and check presence for audited
   devices. A key object present is the pass bar; confirming a key actually unlocks its
   volume is a hands-on test — recommend it for a sample, never claim it.

5. Flag and route: unencrypted -> a remediation ticket (enabling encryption is hands-on
   policy work; old hardware without TPM needs per-device assessment);
   encrypted-without-escrow -> a "capture key before anything else" ticket, urgent-quiet:
   no reboots, no firmware updates on that device until the key is escrowed; unknowns -> a
   verification pass. Check ticket history for an existing encryption project.

6. Output the coverage summary (the four buckets, percentages against the stated
   denominator), per-bucket device lists, evidence source and freshness per claim, and
   tickets opened, as a note (apply the PSA Note Discipline base skill — plain text, no
   markdown or emojis). For compliance requests, state that this is a point-in-time
   technical audit, not a compliance certification.

Guardrails: recovery keys are NEVER reproduced in any output, note, or ticket — location
and existence only; a pasted key is itself a security incident. "Unknown" is its own
honest bucket, never folded into either side. It enables nothing and rotates nothing. With
neither the RMM nor Liongard, degrade to documentation plus ticket history and label the
result "unverified — evidence-gathering pass required".
```
