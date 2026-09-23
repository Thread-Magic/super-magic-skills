---
name: Email Security Notice Auto-Close
description: Close an email security gateway notification only when it matches an exact known-safe message signature, such as an intercepted phish or a quarantine digest, and leave anything else open.
category: Vendor Runbooks
tools: [search_tickets, list_ticket_statuses, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: yes
role: [Dispatcher, Security & Compliance Owner]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Email Security Notice Auto-Close

**When to use:** Your email security gateway (Barracuda, Mimecast, Proofpoint and similar) opens a ticket every time it quarantines a message or sends a digest, and technicians close hundreds of them by hand. You want the ones the vendor already fully handled closed, and anything unfamiliar left for a human.

**Run it:** on one ticket · or as a Flow (when a ticket is created whose title or sender matches your email security vendor). Replace the example signatures below with the exact phrases your vendor uses.

## Prompt

```
Decide one thing for this email security notification: CLOSE IT or LEAVE IT OPEN. Follow the steps in order.

Step 1, check for human involvement first. Read every note before the vendor message. If any of these exist, stop, leave one note "Email security auto-triage: human involvement detected, leaving open for manual review." and change nothing else:
- a note saying manual review is needed or that the ticket is not to be automated
- a failed or incomplete phishing or DMARC investigation note
- a status meaning more information is needed
- any technician reply that asks a question, requests information or escalates

Step 2, classify the first vendor message. It must match a signature completely, every listed phrase present.
TYPE A, threat already handled. Example signature: contains BOTH "What should I do? Nothing." AND "already moved the email to the user's Junk folder". The vendor intercepted it; no action needed.
TYPE B, routine quarantine digest. Example signature: contains BOTH "You have <n> new quarantined inbound emails" AND "manage your quarantine preferences". Informational only.
TYPE C, anything else from the vendor, including partial matches.

Step 3, act.
TYPE A: leave the internal note "Email security auto-triage: the message was intercepted and moved to Junk by the gateway. No action required. Closing automatically." then change the status to the automated-closed status for this ticket's own board.
TYPE B: leave the internal note "Email security auto-triage: routine quarantine digest, informational only. No action required. Closing automatically." then change the status the same way.
TYPE C: leave the internal note "Email security auto-triage: not a known safe-to-close pattern. Left open for technician review." Do not change the status.

Look up the automated-closed status for the ticket's own board. If that board has none, treat the ticket as TYPE C.

Golden rule: if you are uncertain at any step, leave it open. Leaving a safe ticket open is always better than closing one that needed attention. Never reply to the sender or the end user.

As a Flow: your entire reply is the note.
```
