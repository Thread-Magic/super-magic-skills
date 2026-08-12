---
name: Liongard Okta Read
description: Answer Okta tenant questions from the Liongard Okta inspector — app assignments, admin roles, MFA policies, and deactivated-user hygiene — for clients using Okta as their identity front door.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_identity, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Okta Read

**When to use:** "Who are the Okta admins at <client> / any new admin grants?", "what does their Okta MFA policy actually enforce?", per-user app-assignment reads for access reviews and offboarding, or a deactivated-user hygiene sweep.

**Run it:** on one client — name the client and the Okta question.

## Prompt

```
Answer an Okta question for CLIENT_NAME from the Liongard Okta inspector. Read-only — role removals, policy changes, and deactivations route to a technician.

1. Find the Okta inspector for this client and confirm it ran recently; date the data.
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint (Okta field names — Status, Factors, Profile — vary by inspector version):
   - Admins → admin role assignments, Super Administrator first, then Org/App/Group admins. Small dedicated count, every entry explainable; unexplained recent grants escalate immediately — a Super Admin can rewrite MFA policy and app assignments tenant-wide.
   - MFA policy → the authentication/sign-on policy sections: which factors are enforced, for which groups, and which rules carve out exceptions. The exceptions ARE the audit — a strict default with a legacy rule excluding a group is the finding. Also read per-user enrolled factors (angle to verify: active users with zero enrolled factors). Never summarize a policy by its default rule alone.
   - App assignments → apps and their assigned users/groups. For an access review, per-user app list; for rationalization, apps with zero active assignments. Group-based assignment means group membership is the real access — trace it, don't stop at direct assignments.
   - Lifecycle hygiene → users by status (ACTIVE, SUSPENDED, DEPROVISIONED, long-lived PROVISIONED/STAGED). Suspended-for-months accounts get the offboarding cross-check against ticket history — suspended is reversible and keeps app grants in limbo.
   - Changes → check what changed for admin grants, policy modifications, app additions.
   - Open-ended → ask in plain language, verified with targeted reads.
3. When Okta is fed by AD or HR, reconcile against the cross-system identity view / the AD read — active in Okta but disabled at the source (or vice versa) is a sync/offboarding gap. Unexplained Super Admin grants are live leads, not report lines — verify with the client's authorized contact; unclaimed → account-takeover footing.
4. Output: answer, evidence, data as-of timestamp, policy-exception findings stated explicitly. Leave a plain-text note on request. Degradation: no Okta inspector → documentation and ticket history only, labeled "not instrumented"; for an Okta-fronted client, recommend the inspector — it's the single highest-leverage read for that stack.
```
