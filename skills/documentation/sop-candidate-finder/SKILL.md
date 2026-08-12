---
name: SOP Candidate Finder
description: Sweep recently resolved tickets for documentation-worthy resolutions like recurring fixes and vendor workarounds, ranking SOP and KB article candidates.
category: Documentation
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu]
connectors: [IT Glue, Hudu]
scope: global
flow: yes
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# SOP Candidate Finder

**When to use:** "What should we document from last month's tickets?" / "find resolutions we keep re-solving from scratch" — a documentation push, a slow week that needs a writing backlog, or capturing a departing senior tech's knowledge.

**Run it:** across all resolved tickets in a window · or as a Flow (triggered to run the sweep on demand).

## Prompt

```
Mine resolved tickets for the fixes worth writing down, check whether documentation
already exists, and return a ranked candidate list ready to feed into sop-builder or
kb-article-draft. Read-only: this skill searches and reports; it never creates docs
or modifies tickets.

1. Pull resolved/closed tickets for the window (default: last 30 days). Run SEPARATE
   searches per signal rather than one broad pull:
   - Recurrence — same symptom/category resolved 3+ times (across clients or
     repeatedly for one <client>). Recurrence claims need matching symptoms and
     resolutions, not just similar wording in titles.
   - Senior-only knowledge — resolutions that always land on the same senior member
     or required escalation to resolve.
   - Vendor workarounds — resolutions referencing a vendor case, hotfix, or non-
     obvious workaround.
   - High effort — resolutions with large logged time that a procedure could compress.

2. For each candidate, check the knowledge base (plus IT Glue / Hudu where connected)
   for existing coverage. Drop candidates already well documented; flag ones covered
   by a stale or partial doc as "update" rather than "new". If IT Glue / Hudu are not
   connected, note existing-coverage checks used the Thread KB only.

3. Rank remaining candidates by expected payoff: frequency x effort per occurrence x
   breadth (multi-client beats single-client). Senior-only knowledge gets a retention
   bump regardless of frequency.

4. Output a ranked table: candidate topic, evidence (real ticket numbers and counts),
   signal type, existing-doc status (none / stale / partial), suggested next step
   (sop-builder for procedures, kb-article-draft for fix write-ups). RESULT-CAP
   HONESTY: if any search hits its cap, say counts are "at least N" — never present a
   capped count as exact. Cite real ticket numbers; do not invent tickets, counts, or
   doc links.

5. Offer to draft the top candidate.

UNATTENDED (Flow): the entire reply is the ranked candidate table in plain text — no
narration, no offer to draft. Capped searches labeled "at least N"; doc platforms not
connected named as unchecked. No candidates -> reply exactly "NO SOP CANDIDATES." — a
run never pads the list to look productive. Permitted writes: none — drafting and any
ticket writes stay attended.
```
