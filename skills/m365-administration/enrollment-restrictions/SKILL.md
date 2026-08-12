---
name: Enrollment Restrictions
description: Configure or explain Intune enrollment restrictions — personal vs corporate device rules, platform blocks, device limits, and how "corporate" is actually determined. Use for "stop personal devices from enrolling", "block Android from management", or when a restriction is bouncing legitimate enrollments.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# Enrollment Restrictions

**When to use:** Enrollment restrictions decide who gets into management at the front door — "only company-owned devices should enroll in <client>'s Intune," "block <platform> devices from enrolling" / OS-minimum requirements, "users are enrolling too many devices" / device-limit questions, or a legitimate device being rejected at enrollment (restriction as the suspect — often found via the intune-enrollment-troubleshooting ladder). The "personal vs corporate" rule only works if the tenant actually tells Intune which devices are corporate, so configure the rules with that dependency stated up front instead of discovering it when the block does nothing.

**Run it:** on one client's request — you prepare the rules and predictions, a technician executes in Intune (not a Flow: it needs a human at the console).

## Prompt

```
You are configuring or explaining Intune enrollment restrictions with the corporate-identification dependency made explicit. The agent prepares the rules and predictions; the technician executes in Intune. Never report a restriction as live on intention — never invent data.

1. Current state and intent. Check the knowledge base and the client's documentation (skipping gracefully if not connected) for the client's device standard (corporate-only? BYOD allowed on mobile but not Windows?). The tech reads the existing device platform restrictions and device limit restrictions, including priority order — restrictions apply by highest-priority assignment per user, and a forgotten high-priority rule for a small group explains most "restriction doesn't work for these users" mysteries. Check restriction priority order on every change; a new rule below an old broad one silently loses.

2. State the corporate-identification dependency plainly. "Block personally owned" only blocks what Intune considers personal, and corporate status comes from: Autopilot registration, Apple Business Manager/automated enrollment, corporate device identifiers (serial/IMEI pre-registration), or enrollment by a device enrollment manager. No identification pipeline = every BYOD phone looks exactly like a corporate one (or everything looks personal). If the client wants a personal-block, the plan must include how corporate devices are identified — otherwise the restriction is theater. Never promise "personal devices are blocked" without a working corporate identification method — name the method in the note or don't make the claim.

3. Design the restriction set:
   - Platform blocks: block platforms the client will not support or secure. Blocking a platform stops NEW enrollments only — already enrolled devices stay managed; retiring them is separate work.
   - OS minimums: align with the compliance policy floor (see intune-compliance-policies) so devices can't enroll below what compliance will immediately flag.
   - Personal-device blocks: per platform, backed by step 2's identification method. For BYOD populations being blocked from full enrollment, pair with app protection policies (see app-protection-policies) so "blocked from MDM" doesn't mean "unprotected mail on personal phones." Blocking BYOD enrollment without offering the MAM path (where the client licenses it) pushes users to unprotected access or shadow workarounds — say so in the plan and let the client choose deliberately.
   - Device limits: per-user enrollment cap; remember the separate Entra device cap also applies and the lower one wins in practice.
   Verify current platform/OS behavior against Microsoft's current docs.

4. Predict the bounce. Before applying: who currently enrolls in a way the new rule would reject? (Recent enrollments by platform/ownership from the console.) A restriction that would have bounced last month's legitimate enrollments needs its scope fixed before it goes live, not after the new-hire's laptop fails on day one.

5. Approval gate. Send an approval request to the client authority: the rules, which future enrollments they will reject, the corporate-identification dependency and its status, the BYOD fallback (MAM or nothing), and rollback (revert the restriction or priority change — takes effect for new enrollments immediately). Restriction changes affect new enrollments, not enrolled devices — plans and client comms must not imply existing BYOD devices get removed (that is a separate, approval-gated retirement workstream).

6. Verify and document what/why/when/rollback. Test one in-scope and one out-of-scope enrollment if feasible. Leave a plain-text note: rules configured, priority order, corporate identification method, approver, test results, rollback. Fold restriction errors (e.g., 0x80180014) into the client's enrollment-troubleshooting documentation so the next bounced device is diagnosed in minutes.

When in doubt about authorization or scope, do nothing and escalate.
```
