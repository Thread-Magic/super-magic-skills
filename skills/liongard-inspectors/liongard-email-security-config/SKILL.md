---
name: Liongard Email Security Config Read
description: Read a client's Mimecast/Proofpoint-class email security config via Liongard: policy posture, connector state, and config drift without admin console.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Email Security Config Read

**When to use:** "How is <client>'s Mimecast/Proofpoint configured?" (policy posture before tuning or an incident review), "did an email-security policy change?" on a sudden spam wave, "are their connectors healthy / is mail actually flowing through the gateway?", or policy evidence for a QBR/security assessment.

**Run it:** on one client — name the client and the email-security question.

## Prompt

```
Read a client's email-security gateway configuration (Mimecast/Proofpoint-class) for CLIENT_NAME from its Liongard inspector — the configuration side, not delivery data. Read-only — policy tuning and connector changes route to a vendor runbook and the client's change process.

1. Find the inspector for the platform the partner actually runs (Mimecast, Proofpoint, or the client's equivalent — check which of the ~300 inspectors is present rather than assuming) and confirm it ran recently; date the data.
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint (field layouts differ sharply per platform — there is no shared schema across email-security inspectors):
   - Policy posture → the policy sections: anti-spam/anti-malware settings, impersonation/anti-spoofing protection, URL and attachment handling (rewrite/sandbox on or off, and for whom), allow/block list sizes.
   - The allow-list is the classic finding: broad domain-level allows (a whole domain allowlisted to "fix" one false positive years ago) bypass filtering silently — report domain-scope allows as findings with a recommendation to re-justify each.
   - Coverage carve-outs → policies scoped to groups rather than the whole org ("URL rewriting on, except the executives group" is the finding, and executives are the target). State enforcement scope with every policy read — "enabled" without "for whom" is not an answer.
   - Connector / mail-flow state → gateway connector/route config as captured, cross-checked against the domain's MX (pair with the internet-domain read): MX pointing past the gateway straight at the tenant means the gateway is decorative for inbound — a critical finding.
   - Drift → check what changed for policy changes, new allow-list entries, connector modifications, dated. On a "suddenly getting spam" ticket, changes in the window come first.
   - Open-ended → ask in plain language, verified before reporting.
3. Cross-check policy changes against ticket history for the authorizing request; an undocumented policy loosening with no ticket is flagged and, if recent and unclaimed, treated as possible tampering — attackers who gain gateway admin weaken policy before campaigns. Config data is not delivery data — never infer delivery outcomes from policy alone.
4. Output: posture summary (protection layers on/off and for whom), findings ranked (bypass routes and unexplained loosenings first), data as-of date. Leave a plain-text note on request. Degradation: no email-security inspector → answer from documentation, tickets, and the M365-side reads (transport rules, connectors) only, labeled "gateway not instrumented."
```
