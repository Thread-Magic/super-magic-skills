---
name: Liongard Google Workspace Read
description: Answer Google Workspace tenant questions via Liongard: super admin roles, 2SV coverage, license usage, and Drive-sharing posture for Google clients.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_identity, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Google Workspace Read

**When to use:** "Who are the super admins in <client>'s Google Workspace?", 2SV coverage / MFA posture for a Google-shop client, license usage vs. paid, or external Drive-sharing posture before a security review.

**Run it:** on one client — name the client and the Google Workspace question.

## Prompt

```
Answer a Google Workspace question for CLIENT_NAME from the Liongard Google Workspace inspector. Read-only — role, 2SV, and license changes route to a technician.

1. Find the Google Workspace inspector for this client and confirm it ran recently; date the data.
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint (Google schemas differ from Microsoft — do NOT transplant M365 field angles):
   - Admin roles → user role assignments, super admins first. Every super admin explainable; unexplained recent grants escalate. The reconciled cross-system identity view helps when the client also runs AD or M365.
   - 2SV coverage → enrolled vs. not per user, AND whether 2SV is enforced or merely allowed at domain/OU level — that distinction IS the finding ("allowed but 62% enrolled" is a policy gap). Privileged accounts without 2SV are critical and lead the output. Never blur "2SV enforced" and "2SV enrolled" — say which one the data supports.
   - Licenses → SKU assignments vs. total, suspended-but-licensed accounts (money leaking), archived-user licensing where captured.
   - Drive sharing → domain sharing settings (external sharing on/off, link-sharing defaults, whitelisted domains). Setting-level only — per-file sharing audits are out of the data's reach; say so rather than implying coverage.
   - Stale accounts → active users by last-login where captured; cross-check ticket history for offboarding before recommending suspension.
   - Changes → check what changed for admin grants, setting flips, user lifecycle events.
   - Open-ended → ask in plain language, verified before reporting.
3. Super-admin findings lead regardless of the question. Output: answer, evidence, data as-of timestamp, enforcement-vs-enrollment distinction stated wherever 2SV appears. Leave a plain-text note on request. Degradation: no Google Workspace inspector → documentation and ticket history only, labeled "not instrumented"; for a Google-primary client, flag the gap to account management.
```
