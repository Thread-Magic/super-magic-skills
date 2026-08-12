---
name: New Ticket First Touch
description: One-pass first touch on a new ticket: classify it, check duplicates, pull similar resolved tickets, and draft an acknowledgment for the tech to review.
category: Triage & Routing
tools: [search_tickets, search_knowledge_base, run_assistive_ai, add_ticket_note, update_ticket, list_ticket_priorities]
connectors: []
scope: both
flow: yes
role: [Dispatcher, Technician]
outcome: [Faster Resolution & Response, Time & Cost Savings (Capacity)]
---

# New Ticket First Touch

**When to use:** "First touch this ticket" / "give me the full first pass on this" — a tech picks up a fresh ticket and wants classification, duplicate check, prior-resolution context, and a draft reply in one go, or intake wants a consistent first-touch package on every new ticket.

**Run it:** on one ticket · across all new tickets on a board · or as a Flow (when a ticket is created).

## Prompt

```
Everything a good dispatcher does in the first five minutes, in one pass: what is this, have we
seen it, how did we fix it last time, and a ready-to-review acknowledgment — so the tech starts
warm instead of cold.

1. Read the full ticket: all messages, requester, client, current fields.

2. Classify: issue category, proposed priority (using the desk's definitions and the available
   priority levels; security/multi-user forces high), and Incident vs Request. Base it on the
   body, never the title alone. Classification and priority are proposals until confirmed —
   nothing in the note may read as if a fix was applied.

3. Duplicate check: search open tickets for the same client on strong identifiers (contact,
   device/asset, error reference) within a recent window. Report exact matches as suspected
   duplicates with numbers; do not merge here (that's the duplicate-hunter skill's job).

4. Prior-resolution pull: search resolved tickets for the same or similar symptom (same client
   first, then any client), and check the knowledge base for a matching article. Cite only real
   ticket numbers and articles found — never invent references; say so if a search may have
   capped.

5. Draft the acknowledgment: confirm receipt in plain language, restate the issue in one
   sentence, state the next step, no promised times unless desk policy sets one. Match the
   client's language if the ticket is non-English. Never let it promise fixes, timelines, or
   causes that aren't established.

6. Post the package as one plain-text internal note: classification, duplicate findings,
   similar-resolution pointers, and the draft reply clearly marked DRAFT - FOR TECH REVIEW.
   Apply field changes only if the tech confirms. Never send the acknowledgment to the client
   from this skill.

The internal note is plain text — no markdown, no emojis — for PSA compatibility.

Running as a Flow: the entire reply is the plain-text internal note posted verbatim —
classification proposal, duplicate findings, similar-resolution pointers, and the
acknowledgment clearly marked DRAFT - FOR TECH REVIEW. No greeting, no narration, no markdown.
One note per ticket, ever — if a first-touch note from this skill already exists, output
nothing. Permitted write: the internal note only; field changes stay attended. Sections that
fail their confidence bar are marked, never guessed: classification uncertain →
"CLASSIFICATION: UNCLEAR - needs tech review"; no genuine duplicates or priors → "none found."
Ticket unreadable or body empty → output nothing.
```
