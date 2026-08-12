---
name: Spam Sender Triage
description: Close tickets from known-spam senders and patterns — after verifying a human did not forward the message in for investigation.
category: Triage & Routing
tools: [search_tickets, search_contacts, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Spam Sender Triage

**When to use:** Tickets from senders or domains on the desk's known-spam list, obvious cold-sales or marketing blasts landing on intake, or a flow that sweeps new email tickets against the spam pattern list.

**Run it:** on one ticket · across all new email tickets on intake · or as a Flow (when an email ticket is created).

## Prompt

```
Close tickets from known-spam senders against a pattern list — but first check the one case
that matters: a human forwarded it in on purpose, asking "is this legit?"

1. Read the ticket: sender address, subject, full body, and any forwarding wrapper.

2. Human-forward check FIRST — it always runs first and always wins: if the subject carries
   FW:/RE: or the body quotes the spam beneath a human's message, identify the forwarder and
   check whether they're a known client contact. A client forwarding spam is usually asking
   for a verdict (is this phishing? should I worry?) — that's a real ticket. Stop and route it
   as a security/phishing question instead of closing.

3. Match the true sender against the known-spam patterns configured for this desk: exact
   sender addresses, sending domains, and subject/body patterns. Require a pattern-list match,
   not a vibe.

4. Confirm no client contact is a participant in the thread and no tech has logged work on it.

5. Close the ticket (to the closed/spam status) and leave a plain-text note naming the matched
   pattern.

6. If the sender is new junk not on the list, do not close; flag it and suggest the pattern to
   add — list maintenance is a human decision.

Never reply to spam senders and never unsubscribe on the client's behalf. If the "spam"
impersonates the client's own domain or a vendor they use, treat it as potential phishing
targeting the client — route to security triage, do not close. Notes are plain text; name the
exact pattern matched for auditability.

Running as a Flow: your entire reply is the internal note, verbatim: "SPAM CLOSED: sender
<address> matched pattern <pattern>." / "NOT SPAM-CLOSED: forwarded by <contact> - routed for
review." / "NOT SPAM-CLOSED: no pattern match." Deterministic stops: any human forwarder → no
close; any client contact in thread → no close; any tech activity → no close; no pattern match
→ no close. The close is the only permitted write besides the note. When in doubt, do nothing.
```
