---
name: Inbox Rule Alert Runbook
description: An alert fired for a suspicious inbox rule created on a user's mailbox — judge legitimacy, inventory all rules, and remove plus rotate if malicious.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Inbox Rule Alert Runbook

**When to use:** A "suspicious inbox rule created" or "new forwarding rule" alert lands as a ticket; mailbox-rule anomalies surface during another investigation; or a user reports mail "disappearing" or replies they never see.

**Run it:** on one ticket (a suspicious inbox-rule alert).

## Prompt

```
A suspicious inbox rule is one of the most reliable takeover tells. Separate the user who
made a filing rule on Tuesday from the attacker hiding their tracks — and respond
accordingly. When the verdict is malicious, this is also the full inventory-and-remove
sweep (rules, forwarding, delegates). Work it in order:

1. Capture the rule's facts from the alert: rule name, conditions, actions (forward,
   delete, move, mark-as-read), creation timestamp, and the creating client/IP/session if
   present.
2. Score the malicious markers before contacting anyone: rule named ".", "..", or a single
   character; actions that hide mail (move to RSS Feeds, Deleted Items, Archive, or
   mark-as-read); conditions keyed on words like invoice, payment, password, security, or
   helpdesk; auto-forwarding to an external address; creation from an unfamiliar IP or
   during a sign-in anomaly window. Search for concurrent alerts on the same account — an
   inbox rule plus a sign-in anomaly is takeover until proven otherwise.
3. Legitimacy check with the user via a verified channel (a number on file, not an address
   from the ticket): "did you create a mail rule recently — what does it do?" Let them
   describe it; do not read the rule to them first.
4. Verdict:
   - User created it and the description matches a benign rule → document who confirmed,
     when, and the rule's behavior; move to pre-closure per soc-classification-tree.
   - User does not recognize it, is unreachable, or the rule carries malicious markers
     regardless of the user's memory → treat as compromise: inventory ALL rules, forwarding
     settings, delegates, and send-as grants on the mailbox (attackers rarely stop at one),
     preserve each artifact's definition and timestamp before removing it, remove the
     malicious entries, and run the account-takeover-runbook — credential rotation, session
     revocation, MFA sweep included.
5. Document the decision, not just the action: the note records the rule definition, the
   markers found, who confirmed what, every removal with a timestamp, and the verdict
   reasoning.

Guardrails — always:
- Identity first — a mail rule is an identity artifact, not a malware problem.
- A user "confirming" a rule that hides invoice or password mail still warrants scrutiny —
  users confirm things to close tickets. Malicious markers outvote a vague confirmation.
- Never close on user silence or assumption; unreachable within the severity clock →
  contain fast, investigate second.
- Removing the rule without rotating credentials leaves the attacker their access — removal
  and rotation travel together on the malicious path. Preserve each artifact before
  deleting it.
- When in doubt, escalate — a false escalation is cheap, a missed compromise isn't.
- Defensive writing in client communications: "a suspicious mail rule was detected and
  removed," not "you were hacked." Plain text only; never invent data.
```
