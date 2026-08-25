---
name: IRONSCALES Phishing
description: Work IRONSCALES phishing incidents and user banner reports: mailbox-level detection, automated remediation, and correct model-training feedback.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# IRONSCALES Phishing

**When to use:** An IRONSCALES incident fires (a classified phishing/malicious/suspicious campaign, or an auto-remediation across mailboxes); a user banner-report ("Report Phishing") comes through for analyst decision; or a tech asks how to read an IRONSCALES verdict or how far a remediation reached.

**Run it:** on the alert ticket.

## Prompt

```
Triage IRONSCALES, the mailbox-level anti-phishing platform — the vendor specialization of
security-alert-response and phishing-triage, which own the canon. Two things define it:
detection sits inside the mailbox, so it sees post-delivery threats and can remediate across
every affected inbox at once, and its in-mailbox banner lets users report suspected phishing
in one click, producing a stream of employee reports of varying quality. You have no
IRONSCALES console — remediation, classification changes and tenant purges are technician
steps you direct and record.

1. Parse the incident: classification (phishing, malicious, suspicious, spam, safe), the
   themis/AI confidence signal, sender and authentication results, URLs and attachments, the
   number of affected mailboxes in the campaign cluster, and the remediation state —
   auto-remediated (pulled from inboxes), pending analyst decision, or report-only. Copy
   IRONSCALES' exact wording. Route to the client per security-alert-response on the tenant
   or domain fields; low confidence means flag for a human.

2. Use the mailbox-level advantage: IRONSCALES clusters the same campaign across every
   recipient, so confirm the reach — did the pull cover all clustered mailboxes, or only
   some? Reach is a claim until confirmed, and a partial pull leaves live copies. Any
   un-remediated recipient is live: check interaction (click, reply, credential entry) per
   phishing-triage. Delivered and clicked on credential harvesting →
   compromised-account-containment for that user. Interaction opens the identity path whether
   or not the message was later remediated.

3. Triage banner-reports proportionately. A user report is a signal, not a verdict: classify
   on evidence, not on the reporter's alarm — but never dismiss one silently, because the
   classification trains the model and shapes the user's future reporting. These reports are
   a security asset: a true positive gets remediated tenant-wide and the
   reporter acknowledged; a false alarm gets a clear, kind explanation.

4. Scope beyond the cluster: check prior tickets for the same client and sender or URL over
   roughly 90 days for the same actor behind earlier campaigns.

5. Keep classification discipline: marking a message safe or malicious in IRONSCALES feeds
   the AI, so hold a "safe" verdict to the same evidence bar as closing the ticket. Never
   mark a message safe to quiet a frequent reporter — it mistrains the model and blinds the
   desk to the next real one.

6. Note the classification, the remediation reach, the interaction check and the
   report-triage outcome; classify per soc-classification-tree. Client-facing wording per
   defensive-writing-standard.

Without documentation the client's mailbox scope and licensed features may be unknown — say
so. Never invent data; when in doubt do nothing irreversible and escalate.
```
