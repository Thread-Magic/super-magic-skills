---
name: MSA Change Management
description: Work through what an agreement change — tier, scope, seats, sites — means operationally: what changes on the desk, who must be notified, and how effective dating is handled.
category: Client Lifecycle
tools: [search_clients, search_contacts, search_tickets, create_ticket, add_ticket_note, list_boards]
connectors: []
scope: single
flow: no
role: [CSM / Account Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# MSA Change Management

**When to use:** "<client> upgraded to the <tier> plan effective <date> — what needs to change?"; "<client> added 15 seats / a new site — process the change"; or "<client> is dropping after-hours coverage — who needs to know and what do we update?"

**Run it:** on one client's agreement change — a manual coordination pass, not a Flow.

## Prompt

```
A signed amendment is the easy part; you handle the rest — translating an agreement change
into desk configuration, notifications, and clean effective dating so nothing is billed,
routed, or supported under the wrong terms.

1. Capture the change precisely from the requester: what changed (tier, scope, seat count,
   sites, coverage hours), the effective date, and who authorized it. If any of the three is
   missing, ask — never process an agreement change on inference.

2. Confirm the client (look it up) and pull current context (its open tickets and the
   boards).

3. Build the operational delta — what actually changes on the desk:
   - Tier changes: SLA targets, priority handling, after-hours entitlement, covered services.
   - Seat/site changes: contacts to add or deactivate, new locations for routing and
     scheduling, monitoring coverage to extend or trim.
   - Scope changes: ticket types now in or out of contract; what becomes billable vs
     included.
   Only include items the change actually affects — no boilerplate checklist padding.

4. Build the notification list — who must know before the effective date: the service desk
   (changed handling rules), dispatch (coverage/sites), finance/billing (rate and seat
   changes), the technicians who own the client's recurring work, and the client's own
   contacts where their experience changes. Draft each notification in one or two lines,
   labeled DRAFT.

5. Handle effective dating explicitly:
   - Everything switches on the effective date, not the signing date and not today.
   - Open tickets spanning the boundary: state the rule (work before the date under old
     terms, after under new) and flag straddling tickets with a billing note.
   - If the change is retroactive, flag it to finance rather than back-dating anything.

6. Open a tracking ticket ("MSA change — <client>: <summary>, effective <date>") carrying
   the delta, notification list, and dating rules as a plain-text note. Confirm before
   creating.

7. Output the operational delta, notification drafts, effective-dating rules, and the
   tracking ticket reference.

Guardrails: never process a change without the authorizing source (who approved it,
effective when) — ambiguity goes back to the AM, not into the system. This records and
coordinates the change; it does not modify billing systems or contracts — rate and invoice
changes are flagged to finance, executed there. No invented contract terms: if the tier's
SLA or entitlements aren't documented in reach, mark "confirm against agreement".
Client-facing notification drafts contain no internal commentary or ticket IDs and are sent
by a human. Effective-date discipline is the core value — when in doubt about a boundary
case, flag it rather than deciding it. Notes destined for PSA sync are plain text.
```
