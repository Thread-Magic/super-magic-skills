---
name: Lost or Stolen Device Response
description: A user reports a lost or stolen laptop or phone — work the lock/wipe decision, assess what data and access were on it, and drive the carrier/police steps, with the destructive actions gated on explicit approval.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Lost or Stolen Device Response

**When to use:** A user reports a lost, stolen, or misplaced company laptop, phone, or tablet; a device is unaccounted for after travel, theft, or an employee departure; or suspicious activity suggests a device is in the wrong hands.

**Run it:** on one ticket (a lost or stolen device report).

## Prompt

```
A missing device is both an access problem (it holds sessions, tokens, saved credentials)
and a data problem (what's stored or reachable on it). Move fast on the reversible
protective steps, assess exposure, and gate the irreversible ones — remote wipe above all —
behind explicit approval. Wipe/lock/MDM actions are executed by the client's admin/MDM
owner; you drive and document. Work it in order:

1. Capture the facts fast: which device, who, when/where last seen, lost vs. confirmed
   stolen, whether it was encrypted (BitLocker/FileVault), whether it had a
   passcode/biometric lock, and what it could reach (mailbox, VPN, saved passwords, local
   files, MFA authenticator app).
2. Take the reversible protective steps immediately — these don't need the wipe decision:
   revoke the user's active sessions and refresh tokens (a device holds live sessions that
   survive a password reset — see session-token-theft-response), rotate the account
   password, and if the device carried an MFA authenticator, re-enroll MFA on a trusted
   device and remove the lost one's method.
3. Assess data exposure honestly: encrypted-at-rest + strong lock = low practical data
   risk; unencrypted or unlocked = assume contents are readable. Note regulated data (PHI,
   cardholder, PII) that may have been on it — this can carry notification obligations and
   is a client/management call, not yours.
4. Remote-lock early (reversible) if the platform supports it — locking or marking-as-lost
   buys time and can display a return message without destroying anything.
5. Gate the remote WIPE on explicit approval: a wipe is destructive and, for a merely lost
   (recoverable) device, may be premature or may destroy a personal-data BYOD boundary. Lay
   out the trade-off to the client — data-exposure risk vs. loss of the device's data and
   recovery chance — and get an explicit yes before any wipe is issued.
6. Drive the external steps as guidance to the user/client: report theft to police and get
   a report number (often required for insurance and due diligence); contact the mobile
   carrier to suspend/blocklist a stolen phone (IMEI). You do not perform these — you direct
   and record them.
7. Handle offboarding overlap: if this is a departing employee, coordinate with
   employee-offboarding for access revocation and asset recovery, and watch for the insider
   angle (insider-risk-basics) if the loss looks convenient.
8. Document the decision, not just the action: device details, encryption/lock state,
   data-exposure assessment, every protective step with a timestamp, the wipe decision and
   who approved it, and external steps directed. Classify per soc-classification-tree.

Guardrails — always:
- Remote wipe is destructive and approval-gated — never issue one without explicit client
  approval; a wiped-but-recoverable device (or a wiped personal BYOD partition) is an
  irreversible loss. Lock first, wipe on approval.
- Revoke sessions/tokens regardless of the wipe decision — the device holds live
  authenticated access that a password reset alone won't kill.
- Wipe, lock, and MDM actions are executed by the client's admin/MDM owner — you drive and
  document; you do not perform destructive device actions yourself.
- You do not contact police or carriers on the user's behalf — direct the user/client and
  record the report/case numbers.
- Encryption + lock materially changes the data-risk verdict — assess before declaring
  exposure; don't overstate, don't understate.
- Regulated-data exposure and any breach-notification question are client/management
  decisions — surface, recommend, do not decide.
- Defensive writing: "a device is unaccounted for and access from it has been revoked," not
  "your data was stolen" unless evidence shows it. Plain text only. When in doubt, revoke
  access now and lock — hold the wipe for approval.
```
