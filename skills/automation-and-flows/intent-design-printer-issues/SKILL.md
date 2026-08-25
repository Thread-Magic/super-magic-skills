---
name: Printer Issues Intent Design
description: Design the printer-problems intent: three top self-help fixes first, then an escalated ticket that already carries the diagnostics collected from the user.
category: Automation & Flows
tools: [list_intents, get_intent, create_intent, update_intent, set_variation_arguments, set_variation_replies, update_variation, search_tickets, search_knowledge_base]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Printer Issues Intent Design

**When to use:** "Build an intent for printer problems" / "printer tickets are constant and always the same three fixes" / Intent Mining ranked printing as a high-volume, high-automatability candidate.

**Run it:** as a build task on request — you're designing a customer-facing intent, not acting on tickets, so there's no Flow trigger for this one.

## Prompt

```
Build a printer intent that walks the user through the three fixes that resolve most printer
tickets and, when they fail, creates a ticket with the diagnostics already captured so the tech
skips the twenty questions. Building intents is admin-only; if you can't, output the spec for an
admin to apply.

Follow automation-and-flows/intent-builder: update an overlapping intent rather than duplicate it;
ground triggers in real tickets; show the full spec and a test plan (5 matches, 3-5 near-misses
from the watch-outs below) and write only on explicit confirmation; do NOT activate — the admin
does that once the tests pass. Ground the three rungs in this desk's own
resolution notes, replacing any rung the data says rarely works, and link the knowledge base's
printer articles rather than restating them.

Spec:
- Triggers: "printer not working", "can't print", "cant print", "printer offline", "print job
  stuck", "nothing comes out of the printer", "printer says offline", "printing problem", "printer
  error", "documents stuck in queue". Watch-outs: "need a new printer" is a
  hardware request; "add a printer for a new user" is onboarding; "scan to email broken" may be a
  separate flow.
- Arguments, gathered before and during self-help: which printer (name and location, <device>);
  one user or everyone nearby, which scopes device vs server or queue; what happens (nothing, an
  error message — capture the exact text, garbage output, stuck in queue); what they already
  tried.
- Reply flow, the three-rung ladder: (1) restart the printer — power off, wait 30 seconds, power
  on, retry; (2) clear the local queue — cancel the stuck jobs and reprint, in plain steps for the
  client's OS mix; (3) reconnect from the computer side — restart the computer, or remove and
  re-add or set-default where the environment allows user-level fixes. Ask "did that fix it?" after
  each rung and stop the moment it works, closing as deflected. (4) If all three fail, create a
  ticket carrying printer identity and location, scope, exact error text and the rungs tried.
- Handoff rule: multiple users affected skips straight to the ticket — a likely queue or
  print-server issue, and a probable outage never stays in a self-help loop. No credential steps
  and no admin-rights driver installs in self-help; those go on the ticket.
- Variations per client: fleet names and locations, whether users may add printers themselves,
  the managed-print vendor to mention, OS mix for step phrasing.
- Success metric: deflection rate on printer conversations, plus diagnostics completeness on the
  tickets still created.

Guardrails: self-help steps must be safe for a non-technical user — no admin credentials, no
registry or driver surgery, nothing that could take other users' printing down. Never present a
generic fix as "what usually works here" without evidence. Diagnostics block in plain text.
```
