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
Two mandatory questions: is every endpoint's disk encrypted, and if a device died tomorrow could the desk retrieve its recovery key? Coverage without escrow is a lockout; escrow without coverage is a breach.

1. Build the endpoint population from the RMM (pull the device list, verify workstation/laptop class in the details — don't trust a class filter) — this is the denominator. If listings may have capped, the denominator is "at least N" and the audit says so.
2. Gather encryption state per device, best source first: RMM device details where they expose encryption/volume status; the environment's posture in Liongard via its Windows and M365/Entra inspectors (confirm the inspector exists and last ran successfully, then read BitLocker status and escrowed-key presence — state dataprint age); documentation (IT Glue / Hudu) last, with staleness named. Devices with no encryption evidence go in an "unknown" bucket — unknown is not unencrypted, and it is definitely not encrypted.
3. Bucket the fleet: encrypted with key escrowed, encrypted with NO escrow evidence (one dead motherboard from permanent data loss), not encrypted, and unknown. Macs: FileVault status typically needs MDM data (a Liongard/Intune path or MDM export); if no Mac source exists, the Mac fleet is "unknown", stated plainly.
4. Escrow verification — evidence, not assumption: identify where keys should live (Entra/AD, MDM, doc-platform flagged fields, per client policy from docs) and verify presence for audited devices. Presence of a key object is the pass bar; confirming a key unlocks its volume is a hands-on test — recommend it for a sample, never claim it.
5. Flag and route: unencrypted -> remediation ticket (enabling encryption is policy/hands-on, and old hardware without TPM needs per-device assessment); encrypted-without-escrow -> "capture key before anything else" ticket flagged urgent-quiet (no reboots, no firmware updates on that device until the key is escrowed); unknowns -> a verification pass. Check ticket history for an existing encryption project before opening duplicates.
6. Output: coverage summary (encrypted+escrowed / encrypted-no-escrow / unencrypted / unknown, with percentages against the stated denominator), per-bucket device lists, evidence source and freshness per claim, tickets opened. Leave the plain-text summary as a note (no markdown/emojis). For compliance requests, state clearly this is a point-in-time technical audit, not a compliance certification.

Guardrails: recovery keys are NEVER reproduced in any output, note, or ticket — location and existence only (a key pasted into a ticket is itself a security incident). "Unknown" is its own honest bucket — never fold it into either side. Encrypted-without-escrow devices must not be rebooted, firmware-updated, or have TPM changes until the key is captured. Every encryption claim carries its evidence source and age; Liongard data is used only when the inspector shows a successful recent run. This skill enables nothing and rotates nothing. If neither the RMM nor Liongard is available, degrade to docs + ticket history and label it "unverified — evidence-gathering pass required".
```
