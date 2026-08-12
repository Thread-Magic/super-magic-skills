---
name: Liongard AWS Read
description: Answer AWS account questions via Liongard AWS inspector: IAM users, access-key age, root/MFA posture, S3 exposure, security groups, resource census.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard AWS Read

**When to use:** "Who has IAM access to <client>'s AWS / any access keys older than 90 days?", "are any S3 buckets public?", an AWS resource census for scoping or offboarding, or AWS change context on an incident.

**Run it:** on one client — name the client and the AWS question.

## Prompt

```
Answer an AWS question for CLIENT_NAME from the Liongard AWS inspector. Read-only — no IAM, bucket-policy, or security-group changes originate here.

1. Find the AWS inspector for this client and confirm it ran recently; date the data. Note the inspected account/region scope — multi-account clients may have one inspector on one account, so "none found" always carries "in inspected scope."
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint:
   - IAM hygiene → IAM users: console vs. programmatic access, MFA enabled, access-key age and last-used, attached policies (angles to verify: users with MFA disabled, keys older than 90 days). Root-account MFA status, if captured, leads the report regardless of the question.
   - Ownership test on every IAM user: keys belong to a person or a documented service. Cross-check unrecognized users against ticket history and documentation; an unclaimed IAM user with active keys is treated like an unexplained admin and escalates if recent.
   - S3 exposure → buckets flagged public or with permissive ACLs/policies. Public buckets are findings, not stats — flag with purpose known/unknown, route remediation to a technician.
   - Network exposure → security groups allowing 0.0.0.0/0 on management or database ports.
   - Census → EC2 (type, state), RDS, Lambda, load balancers. Stopped-but-provisioned and oversized resources are cost-review candidates — configuration signals only, never dollar figures.
   - Changes → check what changed for IAM changes, security-group modifications, new resources in an incident window.
   - Open-ended → ask in plain language, verified with targeted reads before anything actionable is reported.
3. Key age is risk, not proof of abuse — recommend rotation through the client's change process; never present rotation as done. Root-account and public-bucket findings lead the output whenever present.
4. Output: direct answer, evidence rows, data as-of timestamp, inspected-scope statement. Leave a plain-text note on request. Degradation: no AWS inspector → ticket history and documentation only, labeled "not instrumented"; meaningful AWS with no inspector is itself a recommendation.
```
