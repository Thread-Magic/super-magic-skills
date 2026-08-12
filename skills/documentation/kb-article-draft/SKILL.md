---
name: KB Article Draft
description: Turn a resolved ticket into a reusable knowledge-base article draft with title, symptoms, cause, numbered resolution, and stripped client specifics.
category: Documentation
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# KB Article Draft

**When to use:** "Turn this ticket into a KB article" / "write this up so the team can fix it next time" — after a resolution worth reusing, a recurring issue solved properly for the first time, or a senior-only fix that should be captured.

**Run it:** on one ticket.

## Prompt

```
Convert the fix that actually worked on a ticket into a clean, reusable KB article
DRAFT. The output is always a draft for human review — never publish, file, or write
it into any documentation platform yourself.

1. Read the full ticket thread: notes, time entries, final resolution. Identify the
   fix that ACTUALLY resolved the issue — not the first thing tried. If the resolution
   is ambiguous or the ticket closed without a confirmed fix, say so and stop — do not
   write an article around a guess.

2. Check the knowledge base (and IT Glue / Hudu where those connectors are enabled)
   for an existing article on the same issue. If one exists, propose an update to it
   instead of a duplicate. If neither IT Glue nor Hudu is enabled, check only the
   Thread KB and note the narrower duplicate check.

3. Draft the article in this structure:
   - Title — symptom-first, searchable (what a tech would type when hitting this).
   - When this applies — the environment, versions, and symptom pattern that make
     this the right article; and when it is NOT the right fix.
   - Symptoms — what the user reports and what the tech observes.
   - Cause — root cause in one or two sentences.
   - Resolution — numbered, imperative steps, each independently verifiable.
   - Prerequisites / access needed — roles, admin portals, tools.

4. Sanitize for reuse: replace client names, usernames, hostnames, IPs, tenant IDs,
   and serial numbers with placeholders (<client>, <user>, <device>, <server>).
   Remove any credentials, MFA secrets, or license keys ENTIRELY — do not
   placeholder them, delete them.

5. Base steps only on what the thread shows resolved the issue. Do not pad with
   generic troubleshooting the ticket does not support, and do not invent links or
   article references.

6. Output the draft in chat, ready to paste into the KB, and note the source ticket
   number for the reviewer. Do not create or update any KB entry yourself — a human
   reviews and publishes.
```
