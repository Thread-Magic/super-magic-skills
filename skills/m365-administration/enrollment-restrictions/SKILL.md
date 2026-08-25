---
name: Enrollment Restrictions
description: Configure Intune enrollment restrictions: personal vs corporate device rules, platform blocks, device limits, and corporate identifier logic.
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
Configure or explain Intune enrollment restrictions with the corporate-identification
dependency made explicit. You prepare the rules and predictions; the tech executes in Intune.
Never report a restriction as live on intention.

1. Current state and intent. Check the client's documentation for their device standard —
   corporate-only, or BYOD on mobile but not Windows? Note it if IT Glue or Hudu isn't
   connected (Connector Degradation base skill). The tech reads the existing platform and
   device-limit restrictions including priority order: restrictions apply by highest-priority
   assignment per user, so a new rule below an old broad one silently loses. Check priority on
   every change.

2. State the corporate-identification dependency. "Block personally owned" blocks only what
   Intune considers personal, and corporate status comes from Autopilot registration, Apple
   Business Manager or other automated enrollment, pre-registered corporate device identifiers
   (serial, IMEI), or enrollment by a device enrollment manager. With no identification
   pipeline the restriction is theater. Never promise "personal devices are blocked" without
   naming the working identification method in the note.

3. Design the restriction set:
   - Platform blocks stop NEW enrollments only; enrolled devices stay managed, and retiring
     them is separate work.
   - OS minimums align with the compliance policy floor.
   - Personal-device blocks, per platform, backed by step 2's identification method. Pair a
     blocked BYOD population with app protection policies where licensed, so blocked-from-MDM
     doesn't mean unprotected mail on personal phones.
   - Device limits: the per-user enrollment cap; the separate Entra device cap also applies and
     the lower wins.
   Verify current platform behavior against Microsoft's docs.

4. Predict the bounce: from recent enrollments by platform and ownership, who enrolls today in
   a way the new rule would reject? Fix the scope before it goes live, not after a new hire's
   laptop fails on day one.

5. Approval gate. Send an approval request to the client authority with the rules, the future
   enrollments they will reject, the identification dependency and its status, the BYOD
   fallback, and rollback (revert the restriction or priority change, effective for new
   enrollments immediately). Restriction changes never remove already-enrolled devices; don't
   let the plan or comms imply otherwise.

6. Verify and document. Test one in-scope and one out-of-scope enrollment if feasible. Leave a
   plain-text note, no markdown or emojis (PSA Note Discipline base skill): rules, priority
   order, identification method, approver, test results, rollback. Fold errors such as
   0x80180014 into the client's enrollment-troubleshooting documentation.

When in doubt about authorization or scope, do nothing and escalate.
```
