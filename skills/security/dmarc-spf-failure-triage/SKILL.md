---
name: DMARC SPF Failure Triage
description: Diagnose SPF, DKIM, and DMARC email authentication failures: distinguish real spoofing attempts from sender misconfiguration and explain to the client.
category: Security
tools: [search_tickets, liongard_domain, add_ticket_note, update_ticket, view_openDraft]
connectors: [Liongard]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# DMARC SPF Failure Triage

**When to use:** "Our emails are going to spam / being rejected" tickets; a recipient reports a message from the client's domain failed authentication; or a DMARC aggregate/failure report or gateway alert lands as a ticket.

**Run it:** on one ticket (an email-authentication failure).

## Prompt

```
Authentication failures split into two very different tickets: someone spoofing the domain
(security event) or a legitimate sender missing from the records (plumbing). Tell them
apart and produce the right response for each, plus a client explanation that doesn't cause
panic. Work it in order:

1. Establish direction first — it decides everything: is the CLIENT'S outbound mail failing
   at recipients (likely misconfiguration), or is INBOUND mail claiming to be from the
   client or a partner failing checks on arrival (possible spoof)?
2. Read the domain's current published records in Liongard when enabled (SPF includes, DKIM
   selectors, DMARC policy and alignment mode). Note the as-of date.
3. Misconfiguration signals: the failing source is a legitimate service (a newly adopted
   marketing platform, CRM, or ticketing tool) missing from SPF; DKIM unsigned on one
   sending route; a recent DNS or provider change (search for recent change tickets);
   failures affecting ALL mail from one system rather than scattered lure-like messages.
4. Spoof signals: sending IP unrelated to any provider the client uses; message content
   carrying lures (payment, credentials, urgency); targets concentrated in finance or
   executives; sender display tricks. If headers are available, run email-header-analysis
   for the detailed parse. Spoof verdict → treat the message stream as phishing
   (phishing-triage) and reassure the impersonated party.
5. Produce the fix path for misconfiguration as RECOMMENDATIONS: add the missing
   include/sender to SPF, enable DKIM signing on the route, correct alignment — for the DNS
   owner to implement. Never change DNS yourself; you have no such access.
6. Draft the safe client explanation (defensive-writing-standard, for a human to review and
   send): plain language — "an email authentication check failed; this usually means either
   a sending service isn't registered in your domain's records, or someone attempted to
   send mail pretending to be your domain — here's which one this was and what we're doing."
   No jargon dump, no "you were hacked," no blame.
7. Document the decision, not just the action: direction, evidence, verdict, and the
   recommended fix or security response.

Guardrails — always:
- Never recommend weakening DMARC (dropping to p=none or removing the record) as a "fix"
  without flagging that it trades away spoofing protection — that call belongs to the
  client.
- DNS changes are recommendations only; implementation belongs to whoever owns the zone.
- A spoof verdict is a security event — classify and respond as one; don't close it as a
  mail-flow nuisance.
- Never close on assumption: "probably a misconfig" without identifying WHICH legitimate
  sender is failing is a guess, not a verdict. When in doubt, escalate.
- Degradation: Liongard absent → ask for the records or work from the failure report
  contents, and state the visibility gap. Never invent record contents.
```
