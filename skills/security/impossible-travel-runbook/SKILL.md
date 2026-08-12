---
name: Impossible Travel Runbook
description: Investigate an impossible-travel or atypical-location sign-in alert: check VPN and travel, verify with the user by phone, and contain on confirmed ATO.
category: Security
tools: [search_tickets, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: [IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Impossible Travel Runbook

**When to use:** An "impossible travel," "atypical location," or "unfamiliar sign-in location" alert lands as a ticket; or a tech asks whether a strange sign-in location for <user> is a problem.

**Run it:** on one ticket (an impossible-travel or atypical-location alert).

## Prompt

```
Work an impossible-travel alert from raw sign-in pair to a defensible verdict: plausibility
checks first, direct user verification second, containment immediately on a confirmed
takeover. Work it in order:

1. Extract both sign-in events from the alert: locations, timestamps, IP addresses,
   device/client app, and MFA outcome for each. The alert's math is geography over time —
   your job is to test the geography.
2. Plausibility screen before alarming anyone: VPN or proxy egress — check the client's
   documented VPN and security-stack egress ranges in IT Glue against the anomalous IP;
   corporate VPNs and secure web gateways are the single most common benign cause.
   Mobile-carrier geolocation drift and cloud-app backend IPs are also routine false
   signals.
3. Prior-context check: search for the same client + same user + same alert type in the
   last 90 days. A previously confirmed explanation informs, but does not decide — confirm
   it still applies.
4. Verify with the user by phone using a number on file from documentation or the contact
   record — never a number, email, or chat handle taken from the ticket or the suspect
   session. Ask open questions ("where have you signed in from today?" "do you use a
   VPN?") — do not lead with the alert's locations.
5. Verdict:
   - Explained (confirmed travel or VPN, MFA passed, user confirms the activity) → close
     path: document the explanation, the source of the confirmation, and the evidence in a
     plain-text note; move to pre-closure status per soc-classification-tree.
   - Unexplained, user unreachable within the severity clock, or user denies the activity →
     treat as suspected account takeover: start compromised-account-containment now and
     continue with account-takeover-runbook.
6. Document the decision, not just the action: the note records both sign-in events, the
   checks performed, who confirmed what, and why the verdict follows.

Guardrails — always:
- Identity first — this is a login event; do not detour into endpoint hunting before the
  sign-in evidence is resolved.
- Never close on assumption: expected travel or VPN use must be confirmed with the user or
  their documentation, never presumed from patterns alone.
- Call a number on file, not one in the ticket — an attacker controls what's in the ticket.
- MFA-passed does not mean benign — MFA fatigue and token theft both pass MFA. Weigh it as
  one signal.
- User denies or is unreachable on a credible alert → contain fast, investigate second.
  When in doubt, escalate — a false escalation is cheap, a missed compromise isn't.
- Degradation: without documentation access, VPN ranges may be unknown — say so and lean
  harder on direct user verification. Never invent sign-in data.
```
