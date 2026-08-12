---
name: Windows 11 Readiness Assessment
description: Assess which client devices can upgrade to Windows 11 — CPU generation, TPM, RAM, and edition flags from RMM device details — with an upgrade-blocker list.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, add_ticket_note]
connectors: [NinjaOne]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Windows 11 Readiness Assessment

**When to use:** "Which of <client>'s machines are Windows 11 compatible?", Windows 10 end-of-support planning, or a refresh conversation needing the list of devices that must be replaced.

**Run it:** across a client's Windows workstation fleet, on demand for migration planning (not a Flow — it's an assessment pass, not a per-ticket event).

## Prompt

```
Read hardware and OS facts from the RMM device details for a client's fleet and sort devices into ready / blocked / needs-verification, with the specific blocker named per device. This needs the RMM connected; if absent, say the assessment needs an RMM inventory source and stop.

1. Resolve the client organization, then look up its Windows workstations in the RMM. Verify class on the returned devices — don't trust a class filter (a "workstation" filter can return servers and vice versa). Exclude devices already on Windows 11.
2. If the device list hits a result cap, page through segments and report "at least N assessed" if full coverage is not achievable.
3. For each device, read its details and evaluate against the Windows 11 floor:
   - CPU: 8th-gen Intel Core / AMD Zen 2 (Ryzen 2000-series desktop, 3000 mobile) or newer, from the processor model string. Parse the generation from the model number; when ambiguous, mark "needs verification", not "blocked".
   - TPM 2.0: from the device details where exposed; when the RMM does not report TPM, mark "needs verification".
   - RAM: 4 GB minimum (flag under 8 GB as "upgradeable but poor experience").
   - Storage: 64 GB minimum free-able system disk.
   - OS edition: note Home vs Pro vs LTSC — LTSC and specialty editions follow different upgrade paths.
4. Sort into three buckets: Ready (all checks pass), Blocked (name the blocker — CPU generation is the common unfixable one; RAM/disk are fixable), Needs verification (missing data — usually TPM, offline devices, or unparseable CPU strings).
5. Output: counts per bucket, the blocked list with per-device blocker and whether it is fixable (add RAM) or terminal (CPU -> replace), and the needs-verification list with exactly what to check on-site. Recommend feeding terminal-blocked devices into the Hardware Refresh Forecast skill. Offer a plain-text note (no markdown/emojis).

Guardrails: never declare a device Blocked on missing data — absence of TPM info is "needs verification", not failure; overstating blockers inflates a client's replacement bill. CPU-generation parsing from model strings is heuristic; state the parsed generation next to the verdict so a human can spot-check. Devices offline 30+ days get assessed on stale data — flag the staleness. This skill does not start upgrades: no scripts, no deployments — it produces the assessment; the upgrade itself is a project task.
```
