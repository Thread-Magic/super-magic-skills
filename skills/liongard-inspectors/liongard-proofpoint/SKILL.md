---
name: Liongard Proofpoint Read
description: Interrogate a client's Proofpoint Essentials tenant through the Liongard Proofpoint inspector — protected domains, users/licenses, filtering policy, spooling, admins. Use for "what's their Proofpoint config?", mail-security posture checks, or domain-coverage questions during triage.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Proofpoint Read

**When to use:** "What domains does Proofpoint protect for <client>?", a mail-delivery or phishing ticket needing the filtering-policy picture, "which users are licensed / how many seats?", "is email spooling/continuity enabled?", or "did a filtering policy or domain change?".

**Run it:** on one client — name the client and the Proofpoint question.

## Prompt

```
Read Proofpoint Essentials tenant state for CLIENT_NAME from the Liongard Proofpoint inspector. Read-only — Proofpoint policy, domains, and licensing changes are a technician's job in the console.

1. Resolve the client's environment, then find the Proofpoint / Proofpoint Essentials inspector and confirm it ran recently — carry "as of <timestamp>." Mail-security config changes, so an old data read on an active delivery incident deserves a "verify live" caveat.
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Domains: protected-domain list with verification/routing state.
   - Users: licensed users and seat count vs mailbox count.
   - Policy: filtering/quarantine policy summary.
   - Continuity: spooling/continuity enabled flag.
   - Admins: admin list with role.
3. "What changed?" → check what changed on the Proofpoint side: domain adds/removes, policy changes, admin changes — ordered against the incident window.
4. Sanity-check surprising zeros (zero domains) — usually a wrong field angle or partial inspection; re-probe broadly. Admin-list findings are review inputs — "unrecognized admin, verify" phrasing.
5. Output: a compact table, source + data age line, flags (unverified domains, seat/mailbox mismatch, continuity disabled). Offer to leave a plain-text note. Degradation: no Proofpoint inspector → documentation → ticket history → "verify in console."
```
