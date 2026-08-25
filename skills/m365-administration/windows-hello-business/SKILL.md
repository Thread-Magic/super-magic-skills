---
name: Windows Hello for Business
description: Deploy or troubleshoot Windows Hello for Business: prerequisites by join type, tenant-wide vs targeted enablement, and hybrid on-prem access issues.
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
You prepare the plan and compile prerequisites; the tech executes the Intune and tenant
configuration. Verify current trust-model guidance against Microsoft's docs; deployment models
change.

1. Establish the trust model first. Cloud-only Entra-joined devices are the simplest path.
   Hybrid-joined uses cloud Kerberos trust, the current recommended model; the older key and
   certificate trust models carry heavy PKI baggage. Name the model before any settings work.

2. Prerequisites (tech verifies, you compile): TPM 2.0 — without it Hello is software-backed
   and weaker, decide whether policy requires it; supported Windows versions; MFA available for
   credential enrollment; and for hybrid, healthy Entra Connect plus the cloud Kerberos trust
   object on-prem. Biometrics need a fingerprint reader or IR camera; PIN is the floor. Check
   the client's device standard in their documentation; note it if IT Glue or Hudu isn't
   connected (Connector Degradation base skill).

3. Choose the scope. The tenant-wide enrollment setting turns Hello on for everyone at next
   enrollment — not a pilot instrument. Prefer a targeted Intune account-protection policy
   assigned to a pilot group, then rings. Set PIN complexity from the client's standard and
   whether biometrics are allowed, default yes where hardware exists. Answer the predictable "a
   PIN is weaker than my password" in the comms: the PIN is device-bound and useless without
   this machine's TPM, is never transmitted, and unlocks a hardware-protected key.

4. Approval and pilot. Send an approval request to the client authority covering trust model,
   rings, PIN policy, comms, and rollback: unassigning the policy stops new provisioning but
   enrolled credentials persist, and removing those is a separate per-device action. Never push
   users through provisioning without prior comms (Write Guardrails base skill). Pilot users
   verify provisioning launches at sign-in, MFA prompts during setup, and — hybrid — on-prem
   file share and printer access work.

5. Troubleshooting:
   - Provisioning never launches: check dsregcmd /status (join state, PRT present), MFA
     availability, whether the policy applied at check-in, and TPM state if policy requires it.
   - Hybrid on-prem access fails after a Hello sign-in: the cloud Kerberos trust chain — Entra
     Connect sync of the trust object, domain controller reachability, user sync scope. The fix
     is completing the trust configuration, NOT disabling Hello.
   - Biometrics flaky but PIN fine: a hardware or driver problem.

6. Leave a plain-text note, no markdown or emojis (PSA Note Discipline base skill): trust
   model, scope, settings, approver, pilot results including the hybrid resource test, and
   rollback reference. Schedule the ring-broadening steps.

When in doubt about the hybrid trust chain or authorization, do nothing and escalate.
```
