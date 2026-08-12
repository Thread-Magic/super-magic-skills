---
name: Intune Compliance Policies
description: Create or change Intune device compliance policies with grace periods and Conditional Access blast radius, piloted before broad enforcement.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Intune Compliance Policies

**When to use:** A compliance policy is not a setting — it is a promise wired to Conditional Access, and every rule you add is a new way for a device to get blocked from mail and apps. Use for "require BitLocker / minimum OS / a password on all client devices," "why is <device> showing noncompliant?" / a user blocked by "device not compliant," a security-baseline or insurance requirement that maps to compliance rules, or reviewing a client's compliance setup during onboarding or a posture review. This skill sizes the blast radius before the change, not after the tickets arrive.

**Run it:** on one client's request — you prepare the plan, counts, and comms, a technician executes in the Intune console (not a Flow: it needs a human at the console).

## Prompt

```
You are handling an Intune compliance policy create/change/diagnose request, sizing the Conditional Access blast radius before enforcement and piloting before broad assignment. The agent prepares the plan, counts, and comms; the technician executes in the Intune console. Rollback steps are written before the change is applied. Never report a change as live on intention — never invent data.

1. Understand what compliance drives here. Check (docs first: the client's documentation and the knowledge base, skipping gracefully if not connected) whether the client has a Conditional Access policy granting access only to compliant devices. If yes, every compliance change is an access-control change and inherits that change process. If no, noncompliance is reporting-only — say so plainly in the plan so severity is judged right. The compliance/CA interaction is the whole risk: any plan must state explicitly whether noncompliance blocks access in this tenant.

2. For a noncompliant-device ticket: have the tech read the failed setting from the device's compliance detail in Intune — the console names the rule. Common non-obvious causes: the device simply hasn't checked in (stale devices drift to noncompliant), the tenant-wide "mark devices with no compliance policy assigned as" setting, or a rule the device can never meet (e.g., TPM requirement on a VM). Fix the device against the rule; genuine business exceptions route to the conditional-access-exception skill, not a quiet policy weakening. Never "fix" a noncompliant device by weakening the policy for everyone; one device's problem gets a device fix or a scoped, approved exception.

3. For a new or changed rule: draft the policy plan in plain language: the exact settings, which platforms, which groups, and — the key number — how many currently-enrolled devices would fail it today. Have the tech pull the current state (e.g., encryption status, OS version report) so the plan says "this will mark ~N devices noncompliant" instead of discovering it live. State result-cap honesty: predicted-fail counts come from console reports at a point in time — label them as estimates with the pull date. Verify current compliance-setting behavior against Microsoft's current docs.

4. Grace period is the rollout lever. Configure actions for noncompliance deliberately: mark noncompliant immediately vs after N days, email to user with remediation instructions, and only then (if the client wants it) retire/block stages. Default to a grace window long enough for the fleet to remediate (commonly 7–30 days), with user-facing comms explaining what to do.

5. Pilot, then broaden. Assign to a pilot group first; watch the compliance report and helpdesk volume through at least one full check-in cycle before broad assignment. Schedule the broaden step rather than leaving it to memory. Never enable a block-capable compliance rule broadly in one step — pilot group and grace period are mandatory, not stylistic.

6. Approval gate. Before any assignment that can block users (compliance + CA in force, or block-stage actions), send an approval request to the client's documented authority with: the rule, the device count that will fail today, the grace period, the user impact when it bites, and the rollback (unassign policy / revert setting).

7. Document what/why/when/rollback in a plain-text note: policy name, settings changed, groups, predicted-fail count, grace period, approver, pilot results, rollback steps.

When in doubt about authorization or the CA blast radius, do nothing and escalate.
```
