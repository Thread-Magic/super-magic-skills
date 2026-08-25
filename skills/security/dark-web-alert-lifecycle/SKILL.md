---
name: Dark Web Alert Lifecycle
description: Work dark-web and credential-exposure alerts: age stale exposures, document closure notes, and notify affected users with rotation guidance.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: both
flow: yes
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Always-On Coverage]
---

# Dark Web Alert Lifecycle

**When to use:** A dark-web monitoring alert lands as a ticket (exposed email, password, hash, or PII); a batch of credential-exposure alerts needs working; or a Flow auto-processes the dark-web alert board.

**Run it:** on one ticket · across a batch of credential-exposure alerts · or as a Flow (triggered when a dark-web alert ticket is created).

## Prompt

```
Dark-web feeds resurface the same decade-old leaks endlessly. Separate stale re-reports
(close with a note) from fresh exposures (notify, rotate, verify MFA) — with a hard policy
line on what never happens to the leaked data itself. Work this alert, or each alert in the
batch I point you at, in order:

1. Parse the alert: affected identity/email, breach source if named, the breach or first-seen
   date, and the exposed data classes (plaintext password, hash, PII, email-only).
2. Age check: exposure dated more than 90 days ago → close with a plain-text note recording
   the source, the date, the data classes, and the rationale ("stale exposure, outside the
   actionable window"). Search for a prior ticket on the same identity + source and reference
   it if found.
3. Date missing or unparseable → do NOT take the stale path. No date, no auto-close: treat
   it as fresh, or leave it for a human.
4. Fresh path (90 days or newer): look up the contact, confirm they are a current employee,
   and draft a notification for a human to review and send with rotation guidance — change
   the exposed password on the affected service AND everywhere it was reused, move to a
   password manager and unique passwords, verify MFA is on with methods the user recognizes.
   A departed employee's exposure goes to the client contact rather than the individual; flag
   any still-active accounts. Branch to breached-credential-response for a confirmed-current
   credential, and to compromised-account-containment if there is any sign the credential was
   already used.
5. Document the decision, not just the action: verdict, age math, data classes, and what was
   sent to whom. Classify per soc-classification-tree; closure statuses stay with management.

POLICY, no exceptions: never crack, decode or look up a leaked password or hash on an
external site or tool — no hash-lookup services, no paste sites, no "checking if it still
works" — and never sign in with a leaked credential to verify it. Submitting client data to a
third party is itself a data exposure. Treat any exposed hash as a compromised password and
rotate it. Never put the exposed password or hash value in a client-facing message; identify
the exposure by service and date. This is a "credential exposure notification", not a breach
of the client's systems — say so, and never invent data.

As a Flow: your entire reply is the internal note, posted verbatim — plain text, no
narration, no questions. Two autonomous outcomes only: stale path (date parsed, older than 90
days) → write the closure note and set the pre-closure status; fresh path → write a triage
note stating the exposure facts and that user notification is required, leaving the ticket
open for a human. Never send client email autonomously. Missing or ambiguous date,
unrecognized identity, or any parsing doubt → do nothing, leave the ticket untouched.
```
