---
name: Kaseya Dark Web Monitoring
description: Work Kaseya Dark Web ID compromise alerts: parse alert anatomy (source, date, data classes) and run the age-and-notify lifecycle with a no-crack policy.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: both
flow: yes
role: [Security & Compliance Owner]
outcome: [Risk & Compliance, Always-On Coverage]
---

# Kaseya Dark Web Monitoring

**When to use:** A Dark Web ID compromise alert or scheduled compromise report lands as a ticket; a batch of Dark Web ID findings for a monitored domain needs working; or the skill is embedded in a Flow that processes the dark-web alert board.

**Run it:** on one alert · across a batch of findings you point it at · or as a Flow (triggered when a dark-web alert ticket is created).

## Prompt

```
Work a Kaseya Dark Web ID compromise alert. dark-web-alert-lifecycle owns the lifecycle — age
it, close stale with a note, notify fresh with rotation guidance; you add how Dark Web ID
structures its records and which fields decide stale versus fresh.

POLICY, no exception ever: never attempt to crack, decode or look up a leaked password or
hash on any external site or tool; never test a leaked credential by signing in; treat any
exposed hash as a compromised password and rotate it. Never put the exposed password or hash
value in a client-facing message — identify it by service and date.

1. Parse the record: the monitored identity (an address on the watched domain), the
   compromise source (a named breach, or a generic label like "ID theft forum" or "botnet"),
   the date found versus the breach date, password visibility (visible plaintext, partially
   masked, hash, or blank), and any PII classes. Age on the older, breach-origin date — "date
   found" is when the feed saw it, not when it leaked, and aging on the wrong field
   auto-closes fresh botnet finds.

2. Run dark-web-alert-lifecycle on those fields. A parseable origin date older than 90 days
   takes the stale path: close with the documented note (source, date, data classes,
   rationale, prior-ticket reference). No parseable date, no auto-close — treat it as fresh
   or leave it for a human.

3. Vendor escalators on the fresh path:
   - Source labeled botnet or infostealer → the credential likely came off a currently or
     recently infected device, not an old third-party breach: alongside rotation, the user's
     devices need an EDR review (edr-detection-runbook) or the stealer re-harvests the new
     password. When only "date found" exists and the source is botnet or infostealer, treat
     it as fresh.
   - A visible plaintext password matching the client's current pattern, or confirmed current
     by the user → breached-credential-response immediately; any sign of use →
     compromised-account-containment.
   - Departed employees → route to the client contact per the generic skill; flag any account
     still active.

4. Work batch reports per identity: each gets its own verdict, and a report is never closed
   wholesale because most rows are stale. State caps honestly if it was truncated.

5. Document the verdict, age math, source class, data classes, and what was sent to whom.
   Classify per soc-classification-tree. This is a credential exposure
   notification, not a breach of the client's systems — say that explicitly. A client-facing
   notification can be drafted for review.

Unattended (Flows) variant: the whole reply is the plain-text internal note; only stale-close
and fresh-triage-note outcomes are autonomous; never send client email autonomously; a botnet or infostealer source, a
missing date, or any parsing doubt means do nothing and leave it for a human.
```
