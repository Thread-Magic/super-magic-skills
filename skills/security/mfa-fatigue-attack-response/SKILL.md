---
name: MFA Fatigue Attack Response
description: A user is getting a flood of MFA push prompts they didn't start (push bombing / MFA fatigue) — treat the password as already known, contain the account, and drive the tenant toward number-matching so approval spam stops working.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# MFA Fatigue Attack Response

**When to use:** A user reports a burst of MFA push notifications they didn't trigger; a "multiple MFA attempts" or "MFA fatigue" alert lands as a ticket; or a user says they "approved one by accident" to stop the prompts (treat as approval-until-proven-otherwise).

**Run it:** on one ticket (an MFA push-bombing report or alert).

## Prompt

```
Repeated unsolicited MFA prompts mean an attacker already has the password and is hammering
push approval, betting the user taps "approve" to make it stop. Contain the account on that
assumption and close the door the attack came through. Work it in order:

1. Establish the facts: which account, how many prompts, over what window, and the critical
   question — did the user approve ANY of them? An accidental approval flips this from
   attempted to possible successful takeover.
2. Treat the password as compromised from the start. Unsolicited push spam means the
   attacker already passed the first factor — the password is known. Rotation is not
   optional.
3. Contain now if any prompt was approved, or if prompts are ongoing: reset the password
   AND revoke active sessions/tokens (a stolen session survives a password reset — see
   session-token-theft-response), then run account-takeover-runbook for the blast-radius
   sweep (rules, forwarding, consents).
4. If no prompt was approved and the burst has stopped: still rotate the password (it is
   known), then reset/re-verify the MFA method and confirm no attacker-registered factors
   were added.
5. Close the attack vector at the tenant level: recommend the client's admin enforce
   number-matching / verified-push (so blind "approve" no longer works) and, where
   available, move high-value accounts to phishing-resistant methods (FIDO2/passkeys). This
   is the fix that stops re-runs — flag it as the priority remediation, driven by the
   client's admin, not you.
6. Verify with the user via a channel not dependent on the account under attack (a number on
   file, not an address from the ticket) before standing down.
7. Document the decision, not just the action: prompt count and window, approval status,
   what was rotated/revoked, and the number-matching recommendation with its owner. Classify
   per soc-classification-tree.

Guardrails — always:
- Unsolicited MFA spam = password already known. Always rotate; never close as "they didn't
  approve, no harm."
- One approved prompt is a possible takeover — escalate to full containment, do not
  soft-close on the user's reassurance.
- Password reset without session/token revocation leaves a live attacker session; revoke
  both.
- Number-matching enforcement is a tenant-wide config change owned by the client's admin —
  recommend and drive it; never flip tenant security settings yourself.
- Verify the user through a channel independent of the account being attacked.
- Defensive writing: "repeated MFA prompts were detected and the account was secured," not
  "you were hacked." Plain text only. When in doubt, contain and rotate.
```
