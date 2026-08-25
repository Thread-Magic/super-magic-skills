---
name: Lost or Stolen Device Response
description: Respond to a lost or stolen laptop or phone: decide lock or wipe, assess exposed data and access, and drive carrier or police steps with approval gates.
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
A missing device is both an access problem — live sessions, tokens, saved credentials — and a
data problem. Move fast on the reversible steps and gate the
irreversible ones behind explicit approval. The client's admin or MDM owner executes every
lock, wipe and MDM action; you drive and document.

1. Capture the facts: which device, whose, when and where last seen, lost or confirmed
   stolen, whether it was encrypted (BitLocker/FileVault), whether it had a passcode or
   biometric lock, and what it could reach — mailbox, VPN, saved passwords, local files, MFA
   authenticator app.
2. Take the reversible steps now, without waiting on the wipe decision: revoke the user's
   active sessions and refresh tokens (a device holds live sessions that survive a password
   reset — see session-token-theft-response), rotate the account password, and if the device
   carried an MFA authenticator, re-enroll MFA on a trusted device and remove the lost method.
3. Assess data exposure honestly: encrypted at rest plus a strong lock is low practical data
   risk; unencrypted or unlocked means assume the contents are readable. Note regulated data
   (PHI, cardholder, PII) that may have been on it — notification obligations are a client
   and management call, never yours.
4. Remote-lock or mark-as-lost early where the platform supports it: reversible, buys time,
   and can display a return message without destroying anything.
5. Gate the remote WIPE on explicit approval. A wipe is destructive, and on a merely
   misplaced device it may be premature or may destroy a personal-data BYOD boundary. Lay out
   the trade-off — data-exposure risk against loss of the device's data and its recovery
   chance — and get an explicit yes before any wipe is issued.
6. Direct the external steps; you do not perform them. The user or client reports theft to
   police and gets a report number (usually required for insurance), and contacts the mobile
   carrier to suspend or blocklist a stolen phone by IMEI. Record the case numbers.
7. If this is a departing employee, coordinate with employee-offboarding for access
   revocation and asset recovery, and watch insider-risk-basics if the loss
   looks convenient.
8. Document the decision, not just the action: device details, encryption and lock state, the
   exposure assessment, every protective step with a timestamp, the wipe decision and who
   approved it, and the external steps directed. Classify per soc-classification-tree.

Never issue a remote wipe without explicit client approval — a wiped but recoverable device,
or a wiped personal BYOD partition, is an irreversible loss. Lock first, wipe on approval.
Client-facing wording follows the defensive-writing-standard skill — "a device is unaccounted
for and access from it has been revoked", not "your data was stolen" unless the evidence
shows it.
```
