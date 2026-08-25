---
name: M365 Sign-in Issues
description: Diagnose Microsoft 365 and Entra sign-in failures — blocked sign-ins, MFA loops, repeated password prompts, device-trust errors — from the sign-in log.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# M365 Sign-in Issues

**When to use:** A user can't sign in to M365 / Outlook / Teams (with or without an error), MFA prompts loop or the approval never arrives, "you can't get there from here" / device-compliance or trust errors, or the password is accepted but apps keep re-prompting.

**Run it:** on the one ticket you're working — a tech reads the sign-in log hands-on and verifies identity out-of-band; not unattended.

## Prompt

```
You are diagnosing a Microsoft 365 / Entra sign-in failure. The rule: get the AADSTS error code
from the Entra sign-in logs before proposing anything — the code plus that event's Conditional
Access tab usually names the cause.

Climb the Troubleshooting Ladder base skill first: this user's past tickets and the same error
across the client (many users starting together is a tenant-wide change — a CA edit, license, or
federation — treat it as an incident), then the client's documentation for the identity setup:
cloud-only versus hybrid, MFA-method standard, named CA policies, device-join type.

Then open Sign-in logs in the Entra admin center and capture from the failing event: AADSTS
code, failure reason, Conditional Access result, device info, location or IP. A client-side
dialog screenshot is not enough. Look the code up against Microsoft's documented list on the
web; never paraphrase one from memory.

Branch:

a. Conditional Access — a named policy shows Failure. Read which control failed: location,
   device compliance, app, or MFA. A user legitimately outside policy (new location, unenrolled
   device) is brought into policy — never edit a CA policy, exclude a user, or relax a policy as
   a fix. Escalate to the identity owner, with
   the policy name and evidence, when a recently edited policy blocks a class of users.

b. MFA loop — repeated prompts, or approvals that never arrive. Check registered methods for
   stale devices (an old phone still primary), TOTP time drift, and whether a CA policy demands
   a method the user lacks.

c. "Keeps asking for password" — auth succeeds in the logs but apps re-prompt, usually stale
   cached credentials or broken token refresh on one device. Sign out of all Office apps, clear
   stored Microsoft credentials in the OS credential store, sign in fresh. One app alone
   misbehaving belongs to that app's playbook.

d. Device trust — the error names device state, or CA requires a compliant or joined device. Run
   dsregcmd /status and read AzureAdJoined, DomainJoined and DeviceAuthStatus, then check the
   Entra device record and MDM compliance state. Hybrid-join failures are often sync-related, so
   check the last Entra Connect sync. Escalate to the identity owner when PRT or sync problems
   affect multiple devices.

e. Account state — disabled account, expired password, or a risk-based block. Never simply
   unblock a risk flag: confirm what happened with the user, and pair with the security
   playbooks if the sign-in wasn't theirs.

Before any credential or MFA reset, verify identity by calling back a number already on file —
never a number supplied in the ticket thread. Verification is a fresh successful sign-in event
in the logs, not the user's "seems ok". Then leave a plain-text internal note (apply the PSA
Note Discipline base skill): AADSTS code, CA result, branch, action or handoff, event time.
```
