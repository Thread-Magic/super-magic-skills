---
name: Conditional Access Exception
description: Exclude a user, app, or location from a conditional-access policy with a written risk note, approval, expiry, and revert plan. Use when a ticket asks to bypass, exclude from, or "make an exception to" a sign-in or CA policy.
category: Onboarding & Access
tools: [search_tickets, search_contacts, search_clients, search_knowledge_base, search_itglue, add_ticket_note, update_ticket, schedule_ticket, send_approval, log_time_entry]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Conditional Access Exception

**When to use:** "Exclude <user> from the MFA policy — their app can't handle it" / "this service account keeps getting blocked by conditional access" / "add an exception for <application>/<location> to the sign-in policy" / a recurring sign-in failure whose requested fix is a policy carve-out.

**Run it:** on one ticket — a security-posture change, so approval- and human-gated.

## Prompt

```
Process this CA exclusion as a controlled risk acceptance: write the risk down in plain
language, get the right person to approve it, and make the exception die on schedule
instead of living forever.

1. Understand the block first: which policy, which condition, why it fires for this
   user/app. Often the right fix is NOT an exception — a compliant device, an app
   registration change, or modern-auth configuration removes the need. Propose the
   non-exception fix when one exists.

2. If an exception is genuinely needed, write the risk note in plain language: what
   protection is being removed, for which identity/app/location, what an attacker could
   do with it, and any compensating controls (still has MFA, IP-restricted, monitored
   sign-ins). This note travels with the approval.

3. Identify the approver from the client's policy (check the knowledge base and their IT
   documentation in IT Glue). CA exceptions are security-posture changes: the approver
   is the client's documented security/IT authority, NOT the blocked user's manager.
   Send the risk note for sign-off (send an approval request, or use the client's
   channel) and wait for it.

4. Scope minimally: one identity or app, the narrowest condition, via a dedicated
   exclusion group where possible (auditable and reversible) rather than editing the
   policy body.

5. Set the expiry: agree a review-or-remove date with the approver (default to the
   shortest workable window, not "permanent"). Create the tracked revert — schedule a
   follow-up or open a dated follow-up ticket — to remove or re-justify at expiry.

6. Apply, verify the user/app now works AND that the policy still applies to everyone
   else, and post a plain-text note: policy, exclusion, risk summary, approver, expiry,
   revert reference. Log time.

Guardrails: no exception without a written risk note and sign-off from the client's
security authority — user or manager convenience is not approval. Always propose the
non-exception fix when one exists; the note should say why alternatives were rejected.
Every exception has an expiry and a tracked revert before it goes live. Never broaden an
existing exclusion group "because it's already there" — each identity added is its own
approval. Service accounts excluded from MFA need compensating controls named in the
note (IP restriction, credential rotation, monitoring) — an exclusion with none is a
finding, not a fix.
```
