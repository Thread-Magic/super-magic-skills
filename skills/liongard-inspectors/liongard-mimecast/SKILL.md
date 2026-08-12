---
name: Liongard Mimecast Read
description: Interrogate a client's Mimecast tenant through the Liongard Mimecast inspector — managed domains, users/licenses, policies, connectors/routing, admins. Use for "what's their Mimecast config?", mail-security posture checks, or domain-coverage questions during triage.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Mimecast Read

**When to use:** "What domains does Mimecast manage for <client>?", a mail-delivery or phishing ticket needing the policy/routing picture, "which users are licensed / how many seats?", "what gateway/connector routing is configured?", or "did a policy or connector change?".

**Run it:** on one client — name the client and the Mimecast question.

## Prompt

```
Read Mimecast tenant state for CLIENT_NAME from the Liongard Mimecast inspector. Read-only — Mimecast policy, domains, connectors, and licensing changes are a technician's job in the console.

1. Resolve the client's environment, then find the Mimecast inspector and confirm it ran recently — carry "as of <timestamp>." Mail-security config changes, so an old data read on an active delivery incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Domains: managed-domain list with verification/routing state.
   - Users: licensed users and seat count vs mailbox count.
   - Policy: gateway/impersonation/anti-spam policy summary.
   - Connectors: inbound/outbound routing config.
   - Admins: admin list with role.
3. "What changed?" → check what changed on the Mimecast side: domain adds/removes, policy/connector changes, admin changes — ordered against the incident window.
4. Sanity-check surprising zeros (zero domains) — usually a wrong field angle or partial inspection; re-probe broadly. Admin-list findings are review inputs — "unrecognized admin, verify" phrasing.
5. Output: a compact table, source + data age line, flags (unverified domains, seat/mailbox mismatch, unexpected connector routing). Offer to leave a plain-text note. Degradation: no Mimecast inspector → documentation → ticket history → "verify in console."
```
