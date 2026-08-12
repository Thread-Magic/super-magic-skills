---
name: Time Entry Cleanup
description: Turn raw, rough time notes into clean, standardized time entries — client-facing and internal versions — recording only work the engineer explicitly stated was done.
category: Documentation
tools: [search_tickets, log_time_entry, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Time Entry Cleanup

**When to use:** A tech pastes rough shorthand ("rst pw, tested ok, told usr") and wants a proper time entry, or several raw entries need standardizing before invoicing review, or a call wrap-up needs to become a billable entry.

**Run it:** on one ticket.

## Prompt

```
Normalize messy time notes into the desk's standard time-entry format, splitting
client-facing wording from internal detail, without ever inventing or upgrading work.

1. Read the raw notes; pull surrounding context from the ticket ONLY to resolve
   references (which ticket, which <user>, which <device>) — never to add work items.

2. Rewrite each entry in clear past tense using the fixed field order:
   1. Issue — what was reported.
   2. Work performed — what the engineer explicitly stated they did.
   3. Result — outcome as stated.
   4. Next steps — only if the engineer stated one.

3. ZERO-ASSUMPTION RULE (absolute): include only what the engineer explicitly said
   was done. Never convert a recommendation, intention, or "should" into a completed
   action ("recommended a reboot" must NOT become "rebooted"). No inferred work, no
   inferred verification, no inferred durations. If a duration was not stated, ASK —
   do not estimate silently. If notes are ambiguous, ask or mark it [unclear - confirm].

4. Apply banned-word replacements per house style — typical set: "fixed" ->
   "resolved"; "messed up" -> "misconfigured"; "should be fine" -> "verified working"
   ONLY if verification was stated, otherwise "pending user confirmation". Honor the
   desk's own banned list when provided.

5. Produce two versions when requested:
   - Client-facing — plain professional language, no internal shorthand, no blame,
     no vendor grumbling, plain text (PSA-safe). Never put internal-only remarks
     (blame, client friction, security suspicions) into this version.
   - Internal — full technical detail, hypotheses, and follow-up flags.

6. Output the cleaned entries with durations. Only log the time entry / leave an
   internal note after the technician confirms both the text and the time amount —
   entries affect billing. When in doubt, output text only and let the tech submit.
```
