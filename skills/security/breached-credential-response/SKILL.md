---
name: Breached Credential Response
description: Handle exposed user credentials: notify the user, drive password rotation across reused sites, and verify MFA is enabled before standing down.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Breached Credential Response

**When to use:** A credential exposure is confirmed fresh/current (often handed off from dark-web-alert-lifecycle); a user reports entering their password on a phishing page; or a vendor/breach notification names one of the client's users.

**Run it:** on one ticket (a confirmed credential exposure).

## Prompt

```
You are responding to a live credential exposure: establish whether it was already used,
get it rotated on the affected service and every reuse, verify MFA is real and owned by
the user, then document all of it. Work it in order:

1. Confirm scope: which credential, for which service, exposed when and how (breach dump,
   phishing entry, infostealer). Exposure via phishing entry or infostealer means treat it
   as attacker-held RIGHT NOW, not eventually.
2. Check for use before assuming none: review the account's recent sign-in evidence for
   anomalies since the exposure window, and search related tickets for concurrent alerts on
   the same user (sign-in anomaly, inbox rule). Any sign the credential was used → this
   stops being a notification exercise: branch to compromised-account-containment and the
   account-takeover-runbook immediately.
3. Privileged account exposed → escalate the tier: rotation and session revocation happen
   now, on the containment clock, not the notification clock.
4. Notify the user through a verified channel (draft it for a human to review and send) with
   rotation-everywhere guidance: change the password on the affected service AND on every
   other account where it or a close variant was reused (reuse is the whole attack surface
   here); move to unique passwords via a password manager.
5. MFA verification, not just "MFA enabled": have the user confirm MFA is on for the
   affected service and that every registered method and device is one they recognize — an
   attacker who used the credential may have enrolled their own method.
6. Document the decision, not just the action: exposure source and date, use-check
   evidence, who was notified when, rotation confirmation status, and MFA verification
   outcome. Classify per soc-classification-tree; keep the ticket open until rotation is
   confirmed, not merely requested.

Guardrails — always:
- POLICY: never attempt to crack, decode, or look up leaked passwords or hashes on
  external sites or tools, and never test a leaked credential by attempting to sign in
  with it. Treat an exposed hash as an exposed password and rotate.
- Never include the credential value in any note or message; reference the service and
  exposure date instead.
- Never close on the notification alone, and never close on the assumption that the user
  rotated; confirm or escalate for follow-up.
- Identity first: check the sign-in evidence before deciding this is "just" a notification.
  When in doubt about whether the credential was used, escalate to containment — a false
  escalation is cheap, a missed compromise isn't.
- Defensive writing: "your credential appeared in a third-party exposure" — this is not a
  breach of the client's systems and the message should say so plainly. Plain text only
  for PSA-synced notes. Never invent data.
```
