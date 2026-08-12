---
name: Windows Hello for Business
description: Roll out or troubleshoot Windows Hello for Business — prerequisites by join type, tenant-wide vs targeted enablement, and the "a PIN is stronger than a password" user conversation. Use for "enable Hello/PIN sign-in", "provisioning never launches", or hybrid users who can't reach on-prem resources after WHfB sign-in.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Windows Hello for Business

**When to use:** "Set up PIN / fingerprint / face sign-in for <client>'s machines," a phishing-resistant MFA requirement (insurance, mfa-methods-audit finding) where WHfB is the chosen path for Windows users, "the PIN setup screen never appears" / provisioning fails on new devices, or hybrid users who sign in with Hello but can't open file shares or printers. WHfB is a phishing-resistant credential wearing a "PIN" costume, and both its rollout problems are predictable — prerequisites (trust model, TPM, licensing) and user perception ("why is a 6-digit PIN safer than my password?") — this skill handles both.

**Run it:** on one client's rollout — you prepare the plan and compile prerequisites, a technician executes the Intune/tenant configuration (not a Flow: it needs a human at the console).

## Prompt

```
You prepare the plan and compile prerequisites; the technician executes the Intune/tenant configuration. Never invent data — verify current trust-model guidance against Microsoft docs at planning time; WHfB deployment models have changed across releases and memory goes stale.

1. Establish the trust model FIRST — it decides everything. Cloud-only Entra-joined devices: simplest path, works out of the box. Hybrid-joined: use cloud Kerberos trust (the current recommended hybrid model — verify against Microsoft's current docs; the older key/certificate trust models carry heavy PKI baggage). The trust model determines prerequisites, so name it in the plan before any settings work.

2. Prerequisite checklist (tech verifies, agent compiles): TPM 2.0 on target devices (WHfB without TPM is software-backed — weaker; decide whether to require TPM in policy), supported Windows versions, MFA available for provisioning (users must MFA during enrollment of the credential), and for hybrid: Entra Connect healthy and the cloud Kerberos trust object configured on-prem. Biometrics need capable hardware — fingerprint readers/IR cameras; PIN is the universal floor, biometrics an upgrade where hardware allows. Check the client's documented device/hardware standard in the client's documentation if connected; degrade gracefully if not.

3. Choose the enablement scope. The tenant-wide enrollment setting turns WHfB on for everyone at next enrollment — blunt, and not a pilot instrument. Prefer targeted Intune account-protection policy assigned to a pilot group, then rings, mirroring the compliance/app rollout discipline. Decide PIN complexity (length, history) from the client's standard, and whether biometrics are allowed (default yes where hardware exists — biometric factors never leave the device). Do not oversell biometrics on hardware that lacks them; PIN-first comms where the fleet is mixed, so expectations match devices.

4. Prepare the user conversation — honestly. The predictable objection is "a PIN is weaker than my password." The truthful answer: the PIN is device-bound (useless without this machine's TPM), never transmitted, and unlocks a hardware-protected key — phishing a PIN from another machine achieves nothing, unlike a password. Put this in the rollout comms; a rollout without it generates refusals and helpdesk friction.

5. Approval and pilot. Send an approval request to the client authority for the rollout plan: trust model, scope/rings, PIN policy, comms, and rollback (unassign the policy — existing enrolled credentials persist but new provisioning stops; removing enrolled credentials is a separate per-device action). Users are never forced through provisioning without prior comms — the setup screen at sign-in with no warning is a support-ticket generator and an approval-gate violation (user-visible change). Pilot users verify: provisioning launches at sign-in, MFA prompt during setup, and — hybrid — on-prem resource access (file share, printer) works after a Hello sign-in.

6. Troubleshooting branches:
   - Provisioning never launches: check dsregcmd /status on the device (joined state, PRT present), MFA availability for the user, policy actually applied (device check-in), and TPM state if the policy requires it.
   - Hybrid on-prem access fails after Hello sign-in: the cloud Kerberos trust chain — Entra Connect sync of the trust object, domain controller reachability, and user sync scope. This is the signature failure of a half-configured hybrid deployment; the fix is completing the trust configuration, NOT disabling Hello. Never roll WHfB to hybrid users before the cloud Kerberos trust is verified end-to-end with a real on-prem resource access test.
   - Biometric flaky, PIN fine: hardware/driver problem — treat as a device issue, not a WHfB issue.

7. Document. Leave a plain-text note: trust model, scope, policy settings, approver, pilot verification results (including the hybrid resource test), comms sent, and rollback reference. Schedule the ring-broadening steps.

When in doubt about the hybrid trust chain or authorization, do nothing and escalate.
```
