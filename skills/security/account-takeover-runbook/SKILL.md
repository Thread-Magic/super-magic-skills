---
name: Account Takeover Runbook
description: Respond to a confirmed account takeover: disable sign-in, revoke sessions, reset MFA, sweep inbox rules and OAuth consents, and notify users.
category: Security
tools: [search_tickets, search_contacts, search_itglue, add_ticket_note, update_ticket, view_openDraft]
connectors: [IT Glue]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Account Takeover Runbook

**When to use:** Impossible-travel, inbox-rule, or phishing triage escalated to suspected takeover; a user reports "someone sent emails from my account"; or a tech says "this account is compromised — walk me through the response."

**Run it:** on one ticket (a suspected or confirmed account compromise).

## Prompt

```
Run the full response to a compromised account in strict order: containment, persistence
eradication, blast radius, notification, and a timestamped record of every step. You direct
the checklist and document; the technician executes every identity-console action. In order:

1. Contain fast, investigate second — start on credible suspicion, without waiting for
   complete evidence. Direct the technician through the compromised-account-containment
   checklist: block/disable sign-in, revoke all active sessions and refresh tokens, reset the
   password. Deliver the new credential out of band on a number on file — never through the
   compromised mailbox, and never on any channel from the suspect session. Timestamp each
   action as it completes.
2. MFA sweep: list the account's registered MFA methods and devices, remove any the user does
   not recognize (attackers register their own for persistence), and re-enroll the legitimate
   method.
3. Persistence sweep beyond MFA: enumerate every inbox rule and forwarding address (attacker
   rules commonly forward externally, or hide replies by moving invoice/password/security
   keywords to RSS Feeds or Deleted Items — often named ".", "..", or a single character);
   review mailbox delegates; review OAuth application consents on the account and revoke
   unrecognized ones.
4. Blast radius: review sent items for outbound phishing or payment-fraud attempts during the
   compromise window, check whether other accounts at the client show similar sign-in
   anomalies, identify files or data shared out, and search related tickets.
   Every recipient of attacker-sent mail becomes a phishing-triage follow-up; any
   payment-fraud attempt branches immediately to vendor-fraud-bec-alert for every targeted
   recipient.
5. Notify: reach the user on a number on file, not via the affected mailbox, and notify the
   client contact per their documented incident policy (check their documentation). This is a
   "compromised account", confirmed at account level — NOT a "breach" unless investigation
   confirms system-level impact, and never "hacked". Draft client-facing messages for a human
   to send; disclosure decisions belong to management.
6. Recovery gate: re-enable sign-in only after password rotation, session revocation, MFA
   re-enrollment and the persistence sweep are ALL confirmed complete.
7. Close out the record: the note carries the full timestamped action log, the evidence, the
   blast-radius findings, and the reasoning behind each decision — insurers, auditors and
   postmortems run off that timeline, so never invent a timestamp, log entry or evidence. Notes are plain text, no markdown or emojis (apply the PSA Note Discipline base
   skill). Classify per soc-classification-tree; closure status stays with management. If
   client-facing impact occurred, queue the security-incident-postmortem skill.
```
