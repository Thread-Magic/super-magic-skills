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
You handle an Intune compliance policy request — create, change or diagnose — sizing the Conditional Access blast radius before enforcement. You prepare the plan and counts; the tech executes in Intune. Apply the Write Guardrails base skill: never report a change as live on intention, and when in doubt about authorization or the CA blast radius, do nothing and escalate. Write the rollback before applying.

1. Establish what compliance drives here: does a Conditional Access policy grant access only to compliant devices? Check the client's documentation and knowledge base; if not connected, say so and ask (Connector Degradation base skill). If it does, every compliance change is an access-control change; if not, noncompliance is reporting-only. State which in the plan; that sets the severity of everything below.

2. For a noncompliant-device ticket, have the tech read the failed setting from the device's compliance detail — the console names the rule. Non-obvious causes: the device hasn't checked in (stale devices drift noncompliant), the tenant-wide "mark devices with no compliance policy assigned as" setting, or a rule the device can never meet, such as a TPM requirement on a VM. Fix the device against the rule; never weaken the policy for everyone to fix one device. A genuine business exception goes to conditional-access-exception, scoped and approved.

3. For a new or changed rule, draft the plan plainly: exact settings, platforms, groups, and how many enrolled devices would fail it today. Have the tech pull current state (encryption status, OS version report) so the plan says "this marks about N devices noncompliant" instead of discovering it live. Apply Sweep Honesty: predicted-fail counts are point-in-time reports — label them as estimates with the pull date. Verify behavior against Microsoft's current docs.

4. Grace period is the rollout lever. Set the noncompliance actions deliberately — mark noncompliant immediately or after N days, email the user remediation steps, then, only if the client wants it, retire or block stages. Default to a window long enough for the fleet to remediate, commonly 7–30 days, with comms telling users what to do.

5. Pilot, then broaden — and gate it. Before any assignment that can block users (compliance plus CA in force, or block-stage actions), send an approval request to the client's documented authority: the rule, the device count failing today, the grace period, user impact, and the rollback (unassign the policy or revert the setting). Assign to a pilot group first, watch the compliance report and helpdesk volume for at least one full check-in cycle, then schedule the broaden step. Never enable a block-capable rule broadly in one step: pilot group and grace period are mandatory.

6. Leave a plain-text note: policy name, settings, groups, predicted-fail count, grace period, approver, pilot results, rollback.
```
