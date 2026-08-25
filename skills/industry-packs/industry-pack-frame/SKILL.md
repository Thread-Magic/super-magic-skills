---
name: Industry Pack Frame
description: Base skill defining how a vertical pack works — the client's calendar first, then blast radius against it, the desk-vs-vendor boundary, and the regulator's data rules.
category: Industry Packs
tools: [search_tickets, search_itglue, search_hudu, add_ticket_note]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Industry Pack Frame

**When to use:** Supporting a client in a regulated or deadline-driven vertical — accounting, legal, healthcare, financial services, construction, manufacturing — or writing a pack for one.

**Run it:** on the one ticket you're working — it's the shared frame each vertical pack layers its specifics onto.

## Prompt

```
A vertical pack is ordinary support with three things bolted on: a calendar that changes
what "urgent" means, a boundary the desk must not cross, and a regulator with opinions
about data. Establish all three first.

1. The calendar first, always. Every one of these verticals has a period where the stakes
   change — a filing deadline, a court date, an audit, a month-end close. In it, two
   regimes apply: a change freeze (no discretionary maintenance, migrations or upgrades;
   emergencies only, with the client's explicit sign-off) and a raised urgency floor (a
   fault that's a P3 in a quiet week is a P1 the day before a deadline). When impact is
   unclear, ask when their next deadline is — the most useful question in these accounts.

2. Pull context against it. Review this client's app history — seasonal failures recur
   annually with known fixes — and check their documentation for the stack, hosting
   provider, vendor contracts and where the compliance document lives. Say what you could
   not verify: a regulated client with no documented compliance plan is itself a flag for
   the account owner.

3. Triage by blast radius times calendar, not blast radius alone: a firm-wide outage in
   season is top severity and immediate dispatch; the same fault for one user out of
   season is normal work.

4. Hold the boundary. The environment is the desk's: network path, workstation,
   peripherals, a security agent quarantining a freshly-updated binary. The client's
   professional work is not — filings, case content, clinical decisions, financial
   positions. Say so plainly rather than helping and hoping. Application defects, data
   corruption and hosting faults are vendor territory: escalate with the case number, the
   deadline stated in it, and a follow-up cadence. Never operate on the application's data
   path outside vendor procedure, and never improvise a rollback of a mid-season update.

5. The regulator's data rules are not optional. Never paste regulated identifiers or
   client content into tickets — no identity numbers, no record contents, no screenshots
   of open work; reference by account or portal ID where unavoidable. Check
   security-control changes against the client's compliance document and flag its owner
   when they diverge; the MSP is often named in it. A suspected compromise means contain,
   record facts, flag the compliance owner at once — regulatory notification is theirs.
   Never give legal or regulatory advice.

6. Verification is the professional running their real workflow, not a component
   responding. Then note it (apply the PSA Note Discipline base skill), scrubbed of
   regulated data: app and versions, scope, calendar context, verbatim error, branch,
   vendor case, any compliance flag, and how it was verified.

Layer this on the LOB Application Framework
(troubleshooting-playbooks/lob-application-framework), and apply the Write Guardrails base
skill before anything that sends, closes or changes state.
```
