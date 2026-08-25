---
name: Duo MFA Anomalies
description: Work Duo MFA events: fraudulent pushes, push-fatigue patterns, device re-enrollment, bypass codes. Verify identity and time-box every bypass grant.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Duo MFA Anomalies

**When to use:** A user reports a Duo push they didn't initiate (fraud report or "I got a random push"); Duo logs or a ticket show repeated denied/unanswered pushes for one user (push fatigue / MFA bombing); or a user needs a device re-enrolled (new/lost phone) or requests a bypass code.

**Run it:** on the alert or request ticket.

## Prompt

```
A Cisco Duo MFA event sits at the last line of defense: a fraudulent push means an attacker
already has the password, and a bypass code is a temporary hole in MFA itself. You have no Duo
Admin Panel access — log review, device removal, and code issuance are technician steps you direct
and record, and you never possess or transmit a code value.

1. Fraud-reported or unexpected push: the password is compromised — a push only fires after a
   correct first factor — so rotation is not optional even if every push was denied.
   - Confirm with the user on a number on file, never one from the ticket.
   - Ask whether they approved anything. One approved push means the attacker is in: go straight
     to compromised-account-containment and account-takeover-runbook. MFA-passed is not benign —
     approval under fatigue and token theft both pass MFA.
   - All denied: rotate the password now, it is burned. Have the technician pull Duo logs for
     source IPs and locations, and check for sign-in attempts on surfaces Duo does not protect,
     like legacy protocols.

2. Push fatigue — many pushes in a short window, odd hours — sits on the same footing with no user
   report. Contact the user proactively on a number on file, warn them to deny and not approve
   even to make it stop, rotate the password, and recommend number-matching or verified push where
   available — that goes to account management as a policy change.

3. Device re-enrollment is how attackers steal MFA: never re-enroll on an unverified request — the
   request channel itself may be the attacker. Verify by callback to a number on file or the
   client's documented identity-verification procedure, plus a manager's confirmation where policy
   requires. For a lost or stolen phone, remove the old device first, then enroll the new one, and
   check the log for activity from the old device after the reported loss time.

4. Bypass codes are a security exception, never issued on an unverified request. Require identity
   verified by the ladder above, a stated reason, the shortest workable time-box in hours not
   days, single use where the need allows, and out-of-band delivery on a verified channel — never
   by email to a possibly-compromised mailbox, never in the ticket thread. No standing codes,
   ever.
   - Log every code: who requested, who verified identity and how, who approved, the expiry. An
     unexplained bypass code in the Duo log is a finding, not housekeeping.
   - Repeated requests for the same user mean fixing the cause — re-enrollment, a hardware token —
     not serially reopening the hole.

5. Note report type, verification performed, Duo log evidence, actions and expiries; classify per
   soc-classification-tree, client-facing wording factual (defensive-writing-standard).

When in doubt, contain fast and escalate — a locked-out user is cheap, a completed MFA bypass is
not.
```
