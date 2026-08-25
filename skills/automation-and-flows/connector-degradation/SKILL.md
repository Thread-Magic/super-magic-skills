---
name: Connector Degradation
description: Base skill defining how a skill behaves when an integration it wants isn't connected — do the job with what's native, name the gap, never fake the missing source.
category: Automation & Flows
tools: [search_itglue, search_hudu, search_knowledge_base]
connectors: []
scope: both
flow: yes
role: [Technician, Service & Ops Manager]
outcome: [Always-On Coverage]
---

# Connector Degradation

**When to use:** Authoring or reviewing any skill that reaches for IT Glue, Hudu, NinjaOne, Liongard, TimeZest, or any other integration — because it will run on desks where that integration is off.

**Run it:** on one ticket · across a set · or as a Flow — it's a base contract you fold into any connector-gated skill.

## Prompt

```
Integrations are per-tenant. A skill that assumes one is on breaks silently on every desk
where it isn't — and the failure looks like a bad answer, not a missing connector. Handle
the absence deliberately.

1. Reach, then check. Try the source. If it isn't connected, isn't authorized, or returns
   nothing, that is a fact about coverage, not a dead end — carry on with what's native
   (ticket history, the knowledge base, the client record, web search) and finish the job
   at whatever confidence that supports.

2. Say what you couldn't check, in the output. One line, specific: "Client documentation
   wasn't available, so the site's VPN details are unverified." Not "some sources were
   unavailable." The reader needs to know which part of your answer is thinner than the
   rest and what would firm it up.

3. Never fill the gap with invention. No remembered defaults, no "typically the gateway
   is…", no naming a document you didn't open. If the source that would have answered it
   is missing, the answer is "unknown, and here's how to find out" — a plausible guess in
   a permanent record is worse than an admitted gap.

4. Don't let a missing connector change the recommendation silently. If the advice would
   be different with the documentation in hand, say so: "Recommending a reboot; if IT
   Glue were connected I'd check the documented maintenance window first."

5. Degrade to guidance when the action is the missing piece. If the skill's job was to
   *do* something through the connector — raise a scheduling request, reset an alert,
   look up a device — and the connector is off, produce the finished instruction for a
   person to carry out, and say plainly that you couldn't perform it. Never simulate the
   action, and never substitute a different channel to make it look done.

6. Coverage varies inside a connector too. A tenant can have IT Glue connected and still
   have nothing documented for this client, and an RMM can be connected but not deployed
   to this device. "Connected" is not "covered" — check for the specific record, and
   report an empty result as empty rather than as an answer.

State the connectors a skill genuinely needs in its `connectors:` frontmatter, and write
the prompt so it still returns something useful with none of them.
```
