---
name: Knowledge Base Taxonomy
description: Design the category and tag structure for a knowledge base so articles are findable — a coherent hierarchy, a controlled tag vocabulary, and naming/placement rules — grounded in what the desk actually documents rather than an idealized tree.
category: Documentation
tools: [search_knowledge_base, search_tickets, search_itglue, search_hudu, notion-search, notion-create-pages, notion-update-page]
connectors: [IT Glue, Hudu, Notion]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Knowledge Base Taxonomy

**When to use:** "Our KB is a mess — design a category and tag structure that makes articles findable," standing up a new KB before articles pile in, or consolidating sprawled near-duplicate tags into a controlled vocabulary.

**Run it:** across the whole knowledge base.

## Prompt

```
Design how the knowledge base is organized so people can find articles: a category
hierarchy that matches how the desk works, a controlled tag vocabulary (not free-for-
all tags), and the rules for where a new article goes and how it's named. The outcome
is the taxonomy DESIGN and placement rules — this skill does not rewrite, re-tag,
move, or delete existing articles.

1. Ground the design in reality: inventory the current knowledge base for categories,
   tags, and article spread; review ticket history to see what the desk actually deals
   with (the topics that generate volume are the categories that must exist); check IT
   Glue / Hudu (where connected) and Notion (if the member connected it) for how
   documentation is organized elsewhere so the taxonomy aligns rather than conflicts.

2. Design the CATEGORY HIERARCHY — shallow and intuitive (aim for two levels; deep
   trees hide articles): organize by how people search (by product/system, by issue
   type, by audience — tech-facing vs end-user), matching the ticket-volume topics
   from step 1. Every category gets a one-line definition of what belongs in it. Flag
   current categories that are empty, overlapping, or catch-all ("Misc") for merge or
   retirement.

3. Design the CONTROLLED TAG VOCABULARY — a defined, finite set (not open free-text):
   distinct axes (product, vendor, symptom, audience) so tags compose instead of
   colliding; consolidate existing near-duplicate tags into canonical terms and list
   the mapping (old -> canonical); state that tags are chosen from the vocabulary, not
   invented per article.

4. Write the PLACEMENT & NAMING rules: how to title articles for search (symptom-
   first, consistent with kb-article-draft), which category and tags a new article
   gets, and a short decision guide for ambiguous cases. Include a governance note:
   who owns the taxonomy and how new categories/tags are added (a controlled change).

5. GROUNDED IN REAL USAGE, NOT AN IDEALIZED TREE — categories and tags must reflect
   what the desk documents and searches for, not an abstract taxonomy nobody uses.
   Shallow and controlled beats comprehensive. RESULT-CAP HONESTY: KB and ticket
   searches may cap — note the volume analysis is a sample, not a census.

6. Output the taxonomy design (hierarchy + definitions), the tag vocabulary with the
   consolidation mapping, the placement/naming rules, and a migration note listing
   existing articles/tags to re-file. Docs tools are search-only; write the taxonomy
   doc into Notion ONLY when the member has connected it and confirmed the destination
   — otherwise paste-ready blocks. Without IT Glue/Hudu, design from the Thread KB and
   ticket history alone and say so.
```
