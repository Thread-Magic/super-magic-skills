---
name: Liongard Veeam Posture Read
description: Interrogate a client's Veeam deployment through Liongard — job inventory and schedules, repository capacity, protected-VM census, license state. Use for "what does Veeam protect at <client>", coverage-gap checks, and repo-capacity questions; for a job FAILURE alert use vendor-runbooks/veeam-job-failures instead.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Veeam Posture Read

**When to use:** "What does Veeam actually protect at <client>?", "how full are their backup repositories?", "what jobs exist and when do they run?", a coverage-gap check (VMs no job protects), or Veeam license/support state. For a live job-failure alert, hand off to the Veeam job-failure runbook.

**Run it:** on one client — name the client and the Veeam posture question.

## Prompt

```
Read Veeam Backup & Replication posture for CLIENT_NAME from the Liongard Veeam inspector — the posture/state read (what is protected, where it lands, whether the design still covers the estate). Read-only — never enable/disable jobs, edit schedules, or touch repositories.

1. Resolve the client's environment, then find the Veeam inspector and confirm it ran recently — carry "as of <timestamp>."
2. Read the values from its latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by Veeam edition and inspector version):
   - Jobs: name, type, schedule, enabled state — disabled jobs are a headline finding; jobs with no recent successful result feed the failure runbook.
   - Repositories: name, capacity, free — flag <20% free; a repo trending full predicts next week's failure tickets.
   - Protected census: workloads included across jobs, deduplicated.
   - License: edition, instances used vs licensed, support expiry — flag near-limit and near-expiry.
3. Coverage-gap cross-check (the high-value move): pull the VM inventory from the VMware or Hyper-V read for the same environment and diff against the protected census. VMs present in the hypervisor but absent from every job = unprotected workloads. State both data ages; a gap between differently-aged reads gets a "verify" qualifier. Deliberately-excluded VMs exist (templates, test boxes) — phrase gaps as "not found in any job — confirm intentional."
4. "What changed?" → check what changed: job adds/edits/disables, repository changes, license transitions. A job silently disabled last month is a better catch than any dashboard.
5. Never present the posture read as proof backups are *working* — last-result fields are as-of the last inspector run; restore tests own "working." Say so when the question is really "are we safe." Output: job table, repo capacity table, protected census + coverage gaps, license line, flags with severity, source + data ages. Offer to leave a plain-text note. Degradation: inspector absent → documentation → ticket history.
```
