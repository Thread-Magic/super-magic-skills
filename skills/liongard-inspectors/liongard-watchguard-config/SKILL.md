---
name: Liongard WatchGuard Config Read
description: Interrogate a client's WatchGuard Firebox posture via Liongard: Fireware version, subscription/licensing, policy inventory, VPN config, admin accounts.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard WatchGuard Config Read

**When to use:** "What Fireware version is <client>'s Firebox on?", "are their WatchGuard subscriptions (WebBlocker, Gateway AV, APT Blocker, support) current?", the BOVPN/mobile-VPN inventory, "did the Firebox config change before this started?", or an admin-access review. For live-alert response, hand off to the WatchGuard alert runbook.

**Run it:** on one client — name the client and the WatchGuard question.

## Prompt

```
Read WatchGuard Firebox configuration posture for CLIENT_NAME from the Liongard inspector — state/posture only; live-alert response belongs to the WatchGuard alert runbook. Read-only — changes, renewals, and upgrades are human-owned.

1. Resolve the client's environment, then find the WatchGuard / Firebox inspector and confirm it ran recently — carry "as of <timestamp>."
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Fireware version — report verbatim; recommend verifying against WatchGuard's current advisories rather than asserting EOL/vulnerable from memory.
   - Subscriptions: per-service status + expiry — flag expired or <90 days, and translate to impact ("WebBlocker stops filtering"). Read expiries verbatim with the data age attached (may have renewed since last run).
   - Policies: count and any-any allows; disabled logging on allow policies.
   - VPN: BOVPN gateways/tunnels and mobile-VPN types enabled.
   - Admins: account list; default admin still active alongside named accounts is a flag.
3. "What changed?" → check what changed: policy, admin, firmware, and subscription-state changes ordered against the window (time-adjacency, bounded by inspector cadence). If the request originated from a live WatchGuard alert, gather config context here then continue in the alert runbook — don't duplicate its escalation logic.
4. Never reproduce VPN pre-shared keys or credential material in notes. Output: facts + subscription table, source + data age, flags. Offer to leave a plain-text note. Degradation: inspector absent → documentation → ticket history → "verify on device."
```
