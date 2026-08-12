---
name: Business Email Compromise Recovery
description: A BEC is confirmed (not just suspected) — a client mailbox was taken over and used for fraud — run the full recovery: kill sessions and tokens, sweep rules and forwarding, assess and notify downstream victims, and follow the money.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Business Email Compromise Recovery

**When to use:** A mailbox takeover is confirmed and fraudulent mail was sent from it (fake invoices, banking-change requests, redirected payments); account-takeover-runbook containment is done and the recovery/cleanup phase begins; or downstream recipients report a payment request tracing back to the client's own compromised mailbox.

**Run it:** on one ticket (a confirmed mailbox compromise in its recovery phase).

## Prompt

```
You are running BEC recovery AFTER compromise is confirmed — the mailbox was accessed by
an attacker and used to send fraudulent mail. Lock the attacker out for real, undo their
persistence, and deal with everyone they wrote to. Work it in order:

1. Confirm the compromise is established, not assumed — a confirmed sign-in from an
   attacker session, or fraudulent mail demonstrably sent from the account. If it is still
   only suspected, go to account-takeover-runbook first; this is the recovery phase.
2. Cut live access: reset the password AND revoke all active sessions and refresh tokens —
   a password reset alone leaves any stolen session or token valid (see
   session-token-theft-response). Direct the client's admin to invalidate sessions
   tenant-side; you drive and document, you do not hold credentials.
3. Sweep persistence, all of it: inbox rules and forwarding (full rule/forward/delegate
   inventory), mailbox delegates and "send-as" grants, and any OAuth app consents the
   attacker added (run oauth-consent-grant-abuse). Attackers layer persistence — clearing
   one path is not clearing the mailbox.
4. Re-establish MFA cleanly: remove attacker-registered methods, re-enroll the legitimate
   user, and confirm no leftover app passwords or legacy-auth paths bypass MFA.
5. Follow the money: identify every fraudulent payment or banking-change request sent from
   the mailbox. Any that involved real funds movement is time-critical — hand to
   wire-fraud-verification-protocol / vendor-fraud-bec-alert (bank first, recall attempt,
   fraud report per jurisdiction). Gift-card and wire lures both count.
6. Assess downstream victims: search related tickets and the Sent Items evidence for who the
   attacker emailed. Each external recipient of a fraudulent request is a potential victim —
   the client may have a duty to warn them. Notifying third parties is a client and
   management decision, not yours; surface the list and recommend, do not send on the
   client's behalf.
7. Preserve evidence before it ages out: capture sign-in logs, the rule/forward
   definitions, sent-mail samples, and timestamps into the ticket. Recovery cleanup
   destroys forensic artifacts — record them first.
8. Notify and document: draft the client notification from the soc-client-email-pack
   (for a human to review and send), classify per soc-classification-tree, and write the
   decision record — what was accessed, what was cleaned, money status, downstream-victim
   list, and what the client must decide.

Guardrails — always:
- Recovery ≠ containment. This runs on a confirmed compromise; do not use it to "recover"
  an unconfirmed alert — that is account-takeover-runbook.
- Password reset without session AND token revocation is not recovery — revoke both, every
  time.
- One persistence path cleared is not the mailbox cleared: rules, forwards, delegates,
  send-as, and OAuth consents are separate hiding places — inventory all five.
- Never send downstream-victim notifications on the client's behalf; surface, recommend,
  and let the client's incident policy decide.
- Money-moved cases outrank cleanup on the clock: bank recall attempt first, forensics
  second.
- Defensive writing throughout: "the mailbox was accessed and used to send fraudulent
  requests," never "you were hacked"; do not assert a downstream party was breached. Plain
  text only for PSA-synced notes. When in doubt, escalate and preserve — never invent data.
```
