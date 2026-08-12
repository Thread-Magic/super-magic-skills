---
name: JSON API Response Pattern
description: BASE skill for machine integrations — when an external system calls Super Magic and will parse the reply, respond with only a raw JSON object matching the requested schema. Load when building or reviewing any prompt whose consumer is code, not a person.
category: Automation & Flows
tools: []
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# JSON API Response Pattern

**When to use:** Building a prompt for an external API/webhook caller ("analyze this ticket and return `{severity, category, summary}`"); reviewing an integration that intermittently fails to parse the agent's replies; or any skill step that says "respond in JSON".

**Run it:** on one ticket · across a set · or as a Flow — it's a base output contract you fold into any machine-consumed prompt.

## Prompt

```
An external integration (webhook, RPA platform, partner script) is calling Super Magic
and will feed your reply straight into a parser. One character of prose breaks it. Obey
this contract:

1. The reply is exactly one raw JSON object. Nothing before {, nothing after }. No
   markdown code fences, no "Here is the JSON:", no trailing notes. The first and last
   characters of the reply are { and }.

2. Match the requested schema exactly. Only the requested keys, with the requested names
   and casing. Never add helpful extra fields; never rename; never reorder required
   structure. Unrequested creativity is a parse failure on the caller's side.

3. Express uncertainty inside the schema, never around it. Unknown value → null (or the
   schema's designated sentinel/empty array). If the schema includes a confidence or
   status field, use it. Never explain uncertainty in prose.

4. Types are strict. Numbers as numbers (no "5" for 5, no units baked into numerics),
   booleans as true/false, dates in the format the schema specifies (default ISO 8601).
   Strings must be valid JSON strings — escape quotes and newlines.

5. No fabrication. A schema field the tools couldn't populate gets null, not a plausible
   guess. Machine consumers act on these values.

6. Failure is also JSON. If the task can't be completed at all, return a schema-valid
   object with null/empty values (and the error/status field if one exists) — never an
   apology sentence.

When authoring an integration prompt, include: the exact schema (keys + types + allowed
enums), one example of a fully-populated response, one example of the uncertain/failure
response, and the sentence "Respond with only the raw JSON object — no prose, no code
fences." Test with a case that forces uncertainty and confirm the reply still parses.

This pattern layers on Unattended Output Discipline — all of that contract applies, with
JSON as the artifact. Enum fields: return only values from the allowed list; anything
else is null, not a near-match invention. If the caller's schema is ambiguous, resolve it
at build time with the integration owner — never at run time by improvising.
```
