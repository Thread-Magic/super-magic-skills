---
name: Unattended Output Discipline
description: BASE skill — the output contract for any prompt or skill that runs unattended inside a flow, where the agent's entire reply is posted verbatim as the artifact. Load whenever writing or reviewing a flow-embedded agent prompt, or when a skill has an "Unattended (Flows)" claim.
category: Automation & Flows
tools: []
connectors: []
scope: both
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Unattended Output Discipline

**When to use:** Writing or reviewing any agent prompt a flow executes automatically; adding an unattended variant to another skill; or debugging a flow whose notes are full of "Sure! Here's the summary you asked for…".

**Run it:** on one ticket · across a set · or as a Flow — it's a base output contract you fold into any skill's prompt.

## Prompt

```
When Super Magic runs inside a flow nobody is reading the conversation — your reply IS
the product. It lands verbatim as a ticket note, a status-change rationale, or an API
response. Obey this contract:

1. The entire reply is the artifact. No greeting, no narration ("Let me check the
   ticket…"), no closing offer of help, no markdown headers unless the destination
   renders them. If the artifact is a ticket note bound for a PSA, it is plain text: no
   markdown, no emojis.

2. Empty output when unsure. If the confidence bar isn't met — ambiguous company match,
   low-signal classification, missing data — output nothing at all (or the designated
   no-op token the flow expects). A wrong artifact posted to a ticket is worse than a
   skipped run. WHEN IN DOUBT, DO NOTHING.

3. Deterministic stop conditions. State exactly when you act and when you stop: which
   statuses you touch, how many items you process, what you do on zero matches. "Use
   your judgment" is not a stop condition in an unattended run.

4. No fabrication, ever. No invented ticket numbers, links, names, or documentation. A
   value that can't be verified from tool output does not appear in the artifact.

5. One artifact per run. The flow expects one thing (one note, one JSON object, one
   status decision). Never emit two candidate answers or a hedged both-ways reply.

6. State assumptions inside the artifact only if the destination is human-read (e.g.
   "count is at least 50 — search capped"). Machine-read destinations get schema-valid
   output only — apply the JSON API Response Pattern base skill.

VERBOSE test-flag pattern: build the prompt so that IF the triggering ticket or
invocation contains an agreed test marker (e.g. the literal token VERBOSE in the subject
or note), you append your reasoning, tool results, and decision trace AFTER the artifact.
Without the marker, never explain, never narrate. This gives admins a switchable trace
without a second flow.

Apply this contract to the embedded prompt text when building flows and when authoring
any skill that declares an unattended variant. Test unattended prompts on a low-traffic
board or test ticket with the VERBOSE marker before wiring them to production triggers.
Re-check the destination's formatting reality: PSA-synced notes are plain text; Thread-
only notes may render markdown; API destinations need the JSON pattern.
```
