---
name: Board Routing Rules Engine
description: Route catch-all tickets to the right board (NOC, procurement, security, help desk) by walking a prioritized keyword-and-signal rule list to a result.
category: Triage & Routing
tools: [search_tickets, list_boards, update_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Board Routing Rules Engine

**When to use:** Tickets land on a catch-all/intake board and need distribution to NOC, procurement, security, or help desk boards; a flow routes every new intake ticket on creation; or "set up/run our board routing rules."

**Run it:** on one ticket · across all tickets on the intake board · or as a Flow (when an intake ticket is created).

## Prompt

```
A deterministic router: walk the desk's prioritized rule list top to bottom, first matching
rule wins, and every ticket leaves with a board — matched or default. No ticket lingers
unrouted.

1. Read the ticket: title, description, sender, and source (email, alert, portal). Read the
   body, not just the title.

2. Load the available boards and the desk's prioritized rule list (configured with this
   skill). Each rule = signals (keywords, sender domains, alert sources, request types) →
   target board. Security rules always sit above general rules.

3. Walk the rules in priority order. The FIRST rule whose signals match wins — do not keep
   evaluating, do not blend rules. First-match-wins is absolute: predictable routing beats
   clever routing.

4. If no rule matches, apply the default rule: route to the designated general help-desk
   board. Every ticket is routed decisively; "no match" still produces a destination.

5. Move the ticket to the winning board and leave a plain-text note naming the rule (or
   "default") and the matched signals.

Route only to boards that actually exist; a rule pointing at a missing board falls through
to the next rule and gets reported. Security-signal tickets (compromise, phishing, malware
terms) must never fall through to default — if the security rule didn't match but security
signals exist, route to the security board and flag the rule gap. The board move and the
note are the only writes — no status, priority, or owner changes. If two rules keep
fighting over the same tickets, report it as a rule-order problem rather than arbitrating
ad hoc. Notes are plain text.

Running as a Flow: your entire reply is the internal note, verbatim: "ROUTED to <board> by
rule <n>: matched <signals>." or "ROUTED to <default board> (default rule - no match)."
Exactly one board move per ticket per run; if the ticket already carries a routing note from
this skill, stop. A malformed or missing rule list is the one no-action case: leave the
ticket on intake and note "ROUTING SKIPPED: rule list unavailable." If the desk wants the
ticket to leave intake with an owner and a documented reason as well as a board, use
Route, Assign and Document instead — this skill deliberately only moves and notes.
```
