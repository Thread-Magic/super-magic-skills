---
name: Travel Access Window
description: Open a temporary conditional access exception for a traveling user with automatic expiry and a tracked revert task so location policies stay in place.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, update_ticket, schedule_ticket, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Travel Access Window

**When to use:** "<user> is traveling to <country> next week and will get blocked" / "user abroad can't sign in — location policy is blocking them" / "open up access for <user> from <date> to <date>" / a sign-in-blocked ticket whose cause turns out to be travel.

**Run it:** on one ticket — a scoped, approval-gated exception a human confirms.

## Prompt

```
Let this traveler keep working without permanently weakening the client's
conditional-access posture: a scoped exception, an end date, and a revert task that
actually exists.

1. Gather the window: user (look up the contact), destination(s), departure and return
   dates, which policy will block them (named-location block, compliant-device
   requirement, etc.). Check the client's travel-access policy in the knowledge base /
   IT Glue documentation — many clients have a pre-approved procedure; follow it if so.

2. Verify the travel is legitimate: the request should come from or be confirmed by the
   user's manager or the client's authorized contact — not solely from an email
   claiming to be the traveling user (a classic compromise pretext). If the user is
   already abroad and locked out, verify identity by the Password & MFA Recovery ladder
   (callback on a number on file) before opening anything.

3. Scope the exception minimally: this user only, the travel countries only, the travel
   dates only. Prefer adding the user to a dedicated travel-exception group over editing
   the policy itself. Do NOT disable MFA — travel is a reason for MFA, not against it.

4. Get approval per the Conditional Access Exception rules (send an approval request, or
   use the client's channel) with the risk note: what's being relaxed, for whom, where,
   until when.

5. Apply the exception with an automatic expiry where the platform supports it
   (time-bound group membership or dated policy condition). Regardless of platform
   expiry, create the revert task: schedule a follow-up (or a dated follow-up ticket)
   for the return date to remove the exception and verify the policy is back to normal.

6. Post a plain-text note: user, countries, window, policy touched, approver, expiry
   mechanism, revert task reference. Tell the user what will work while traveling and
   when access reverts. Log time.

ON RETURN: run the revert task — remove the exception, verify the policy applies to the
user again, note completion on the original ticket.

Guardrails: never open a travel window on the traveler's say-so alone — verify through
the manager or a number on file. Never disable MFA as a travel accommodation. Every
window has an end date and a tracked revert task before the exception goes live — no
revert task, no exception. Scope to the user, countries, and dates; never widen a policy
globally to unblock one traveler. If the "travel" pattern looks like compromise
(impossible travel, urgent pressure, new payment requests), stop and route to
security-alert handling.
```
