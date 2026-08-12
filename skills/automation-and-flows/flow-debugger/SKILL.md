---
name: Flow Debugger
description: Diagnose why a flow or intent didn't fire on a ticket — filters vs actual attributes, flow ordering, board scoping, trigger-event mismatch. Use when asked "why didn't my flow run", "the intent didn't trigger", or "this automation isn't working".
category: Automation & Flows
tools: [list_flows, get_flow, list_intents, get_intent, search_tickets, list_flow_filter_attributes, list_flow_filter_attribute_values]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Flow Debugger

**When to use:** "Ticket <number> should have triggered the P1 flow — why didn't it?" / "my intent never fires even when users type the trigger phrase" / "this flow works on one board but not another."

**Run it:** on the one ticket that should have triggered — manually on demand (a diagnostic pass has no Flow trigger of its own).

## Prompt

```
Compare an automation's configuration against the ticket it should have caught, filter by
filter, and name the exact mismatch. Diagnose FIRST, change second — never edit a flow or
intent as part of the investigation. Reading flow/intent configuration is admin-only;
without it, ask the member to paste the flow's configuration and debug from that.

1. Fetch both sides: open the flow (or intent) configuration, and read the ticket's actual
   attributes at the time of the event.

2. Check the cheap causes first, in order:
   - Active? An inactive flow fires on nothing.
   - Trigger event — "created" flows never see tickets that arrived matching and were
     later updated into scope; "status changed to X" only fires on the transition, not on
     tickets already sitting in X.
   - Board scoping — is the ticket's board in the flow's scope?

3. Walk every filter in a pass/fail table: filter, expected value, ticket's actual value,
   verdict. Look up the filter's real allowed values to catch value-string mismatches ("High"
   vs "P2 - High"). Attribute values may lag after a recent update elsewhere — re-read the
   ticket before trusting a surprising value.

4. Check ordering and competition: list the other flows on the same trigger — an
   earlier flow may have changed the attribute (moved the status) before this one
   evaluated, or already claimed the ticket.

5. For intents: compare the user's actual message text against the trigger phrases; check
   whether another intent's phrases matched first; check whether the message arrived on a
   channel intents don't cover.

6. Output: the single named root cause (or ranked candidates if genuinely ambiguous), the
   pass/fail table as evidence, and the minimal proposed fix. If the ticket genuinely
   matches every filter and the flow was active, say so plainly and recommend raising it
   with Thread support — do not invent an explanation. Apply the fix only after explicit
   confirmation.
```
