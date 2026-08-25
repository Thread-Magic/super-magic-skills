---
name: Mobile Email Setup
description: Set up corporate mail on a phone — new-device config, sync failures, MDM enrollment prompts, native Mail vs Outlook — holding the BYOD consent boundary.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Mobile Email Setup

**When to use:** "Set up my work email on my new phone" / "email stopped syncing on my phone," "my phone is asking me to install a management profile / register the device — is that legit?", native iOS/Android Mail works for some users but is blocked for others, or a user resists MDM on a personal phone but still wants corporate mail.

**Run it:** on the one ticket you're working — a tech walks the user through it hands-on; not unattended.

## Prompt

```
Mobile mail tickets are policy tickets in a settings costume: whether mail works on a phone
is decided by the tenant's Conditional Access and app-protection policies, not the settings
the user is fiddling with. Make the phone comply with policy, never the reverse.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: prior
mobile-mail tickets reveal the client's standard: Outlook only, MAM, or MDM. Documentation:
the mobile-access policy — sanctioned apps, whether app protection (MAM) or enrolment (MDM)
is required, the BYOD policy, any Conditional Access rule on mobile. Versions: the
phone OS, since policies commonly set OS minimums that can be the whole ticket. Basic auth
to Exchange Online is dead, so never walk a user through a legacy setup demanding server
names and ports. Evidence: the exact prompt or error on the phone, plus the Entra sign-in
log where the desk has tenant access — it names the blocking policy. Then classify the
device, corporate or personal: on BYOD, consent to what the policy requires (app protection
at minimum, enrolment at most) is a precondition, so say plainly what the organization can
and cannot see.

1. New setup on the compliant path — install the sanctioned app, sign in with the work
   account, complete MFA. If app protection applies, warn the user before the "your
   organization is now protecting data in this app" PIN prompt appears. An account that
   authenticates nowhere is an identity ticket.

2. Blocked by Conditional Access — access refused, or native Mail refused while Outlook
   works. Read the failure from the sign-in log: app-protection-required policies block
   clients that can't attest, and native Mail falls there by design. The fix is the
   sanctioned app; an exception is a tenant-admin change, never a workaround.

3. Enrolment prompts — the phone demands device registration mid-setup. Is that expected by
   policy, or a misconfigured target group? On BYOD, pause: confirm consent and offer the
   MAM-only path if the tenant supports it. If the user declines management on a personal
   device, route it to the policy owner.

4. Sync stopped on a working setup — in order: a changed password awaiting re-auth, a
   changed MFA method, the device out of compliance (OS too old after a policy update,
   jailbreak or root detection), or an app-protection PIN lockout. The sign-in log names
   which; an OS the device can't run is a hardware conversation.

Never enrol a personal device, and never present enrolment as mandatory for mail unless the
client's documented policy says so — consent first, and record that the options were
explained. No desk-side Conditional Access exceptions, ever. Close with the user sending and
receiving a test message. Note in plain text (PSA Note Discipline base skill): device class,
app, branch, governing policy, verification. Never note device PINs.
```
