---
name: VIP Priority Handling
description: Detect VIP contacts and VIP clients at ticket intake, apply the configured priority bump, and fire the desk's notify rules — without letting VIP status distort classification.
category: Triage & Routing
tools: [search_tickets, search_contacts, search_clients, update_ticket, add_ticket_note, list_ticket_priorities]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Retention & Growth (CSAT/Expansion), Faster Resolution & Response]
---

# VIP Priority Handling

**When to use:** New tickets should be checked for VIP requesters as part of intake, a flow fires on create to apply VIP handling, or "is this person a VIP, and did we handle the ticket accordingly?"

**Run it:** on one ticket · across all new tickets on a board · or as a Flow (when a ticket is created).

## Prompt

```
Spot VIP contacts and clients at intake, bump priority per the configured VIP policy, and post
the notify-rule note so the right people hear about it.

1. Read the ticket: requester, client, current priority, and the issue.

2. Check VIP status two ways: search contacts for a VIP flag/type on the contact record, and
   search clients for a VIP or white-glove tier on the company. Treat only explicit flags/tiers
   as VIP — job titles alone (e.g. "CEO" in a signature) are a lead to verify, not proof. VIP
   status must never be inferred from tone, title, or email domain prestige; unverifiable "I'm
   important" claims get normal handling plus a flag for the account manager.

3. If VIP: apply the configured bump — typically raise priority one level (or to the VIP floor
   level), using the available priority levels. Never lower an already-higher priority; the bump
   is bounded by policy — VIP does not automatically mean the top priority reserved for outages.

4. Fire the notify rules as configured: leave a plain-text internal note tagging the ticket as
   VIP-handled and stating who per policy should be notified (account manager, dispatcher,
   on-call lead). If the desk uses a VIP board or owner routing, apply that too.

5. Report: VIP source (contact flag vs client tier), what changed, and which notify rule fired.
   If not VIP, say so plainly and change nothing.

VIP affects priority and notification only; it must not distort classification, severity facts,
or duplicate handling. Notes are plain text; never put "VIP" language in any client-facing reply
— it's internal handling, and other clients' tickets must never reference tiers. One bump per
ticket, ever: if a VIP-handling note from this skill already exists, stop.

Running as a Flow: reply with exactly one line (logged, not posted): "VIP #<n>: priority <old>
-> <new>, note posted (source: <contact flag|client tier>)." or "NO ACTION." Permitted writes:
the priority bump and the single plain-text VIP-handled note. Board moves and owner routing are
demoted to attended — routing judgment does not run unattended. Deterministic stops, each → NO
ACTION: no explicit VIP flag or tier; contact/company match ambiguous; priority already at or
above the VIP floor; a VIP-handling note from this skill already on the ticket; VIP floor not
configured on the flow. Never write anything client-visible; never lower a priority.
```
