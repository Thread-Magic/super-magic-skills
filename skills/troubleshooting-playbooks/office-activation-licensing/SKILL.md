---
name: Office Activation & Licensing
description: Fix Office / Microsoft 365 Apps activation — Product Deactivated, unlicensed mode, repeated prompts, shared-computer/RDS errors — detect the license type.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Office Activation & Licensing

**When to use:** "Product Deactivated" / "We couldn't verify your subscription" banners or red title-bar warnings; Office dropping into reduced-functionality/unlicensed mode after working fine; activation errors on RDS/AVD/shared PCs or after a reimage/rename; or "account already has the maximum number of installs" complaints. Sign-in problems beyond activation (MFA, Conditional Access) belong to m365-signin-issues.

**Run it:** on the one ticket you're working — a tech drives detection and repair hands-on; not unattended.

## Prompt

```
The first fact decides everything: Microsoft 365 Apps (subscription), volume-licensed (KMS
or MAK), or retail/OEM? Have the tech run ospp.vbs /dstatus (path varies by Office version
and bitness): LICENSE NAME and DESCRIPTION say Subscription, KMS_Client, MAK or
Retail(Grace), and File > Account names who is signed in. Two licenses at once, a retail
remnant beside a subscription, is a classic cause.

Climb the Troubleshooting Ladder base skill for the rest: past tickets for this user and
for the same banner across the client — many at once is tenant-side (lapsed subscription,
payment, a reassignment sweep), an account conversation, not a tech fix; then
documentation for the licensing standard, KMS host and shared-computer expectations.

1. Microsoft 365 Apps — check the server side first: the user holds a license with the
   Apps service plan enabled and the subscription is active. If clean, it is cached client
   state: sign out, clear stale Microsoft identities from the OS credential store, sign
   back in, then Microsoft's documented license-reset steps. "Maximum installs" means
   deactivating stale devices on the account page.

2. Shared computer activation on session hosts — confirm SCA is enabled; without it Office
   hits per-user install limits and fails oddly, a deployment error, not a user issue.
   With SCA on, the per-user token in %localappdata% may be stale or blocked: check it
   persists (FSLogix Office container roaming is the standard design) and isn't
   AV-blocked. SCA needs a qualifying business or enterprise plan.

3. Volume license (KMS_Client) — read the remaining grace and last activation. KMS needs
   the _vlmcs._tcp SRV record in internal DNS and the count threshold met; machines that
   never touch the KMS host expire at 180 days, so field laptops on KMS are a design
   smell. Exhausted MAK counts are a licensing-owner conversation.

4. Retail, OEM or mixed remnants — a leftover trial or preinstall key shadowing the real
   license, dstatus showing both. Remove the stray with ospp.vbs /unpkey for the partial
   key shown, then activate the intended one.

Stubborn client-side cases, in order: quick repair, online repair (a reinstall — schedule
it), then full removal with Microsoft's uninstall tool and a fresh install per the
client's standard.

Never remove a key or reset licensing state before capturing dstatus: it is the evidence
and the rollback map. Never assign a spare license off the client's SKU standard. No
activation workarounds ever: no KMS emulators, no trial tricks, no registry hacks masking
an unlicensed state. Under-licensing goes to the account owner; tenant-wide failures are
fixed at billing level.

Success is dstatus or File > Account showing the intended license activated, banner gone.
Note it (apply the PSA Note Discipline base skill): license type, branch, server-side
facts, actions, verification.
```
