---
name: Autotask Ticket Categories
description: Set the right Autotask Ticket Category on a new ticket, the one classification field Assistive AI auto-categorization does not cover. Fetches the desk's own category list every run.
category: PSA-Specific
tools: [search_tickets, list_ticket_categories, set_ticket_category, add_ticket_note]
connectors: []
scope: single
flow: yes
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Autotask Ticket Categories

**When to use:** A new Autotask ticket lands with no category or the desk's default one, and you want it categorised the way your Autotask reporting and workflow rules expect. Assistive AI auto-categorization sets Issue Type, Sub-Issue Type and ticket type — it does not touch Ticket Category, so this fills that gap.

**Run it:** on one ticket · or as a Flow (triggered when a ticket is created).

## Prompt

```
You are setting the Ticket Category on an Autotask ticket. Ticket Category is configured per
tenant — every desk's list is different — and Thread's Assistive AI auto-categorization does
not set it (that covers Issue Type, Sub-Issue Type and ticket type only), so it is the field
that stays empty or defaulted unless someone sets it.

1. Fetch this workspace's active ticket categories first, on every run. Never work from a
   remembered list, a list written into this prompt, or a list from another desk — categories
   are per tenant and change. Match only against the names that came back.

2. Read the ticket: title, description, and the whole thread. Classify from the request body,
   never the title alone. Monitoring and backup alerts are usually named after the tool that
   raised them, so where the ticket came from matters as much as its wording.

3. Pick the one category whose name best describes this ticket on this desk. Judge by what the
   name means operationally, not by keyword overlap. If the list contains an obvious duplicate
   or test entry — a name like "Copy (1) of ..." or "Copy of ..." — never pick it; pick the
   original it was copied from.

4. Set that category on the ticket. Only ever set a category that came back in step 1, and
   never invent or guess one.

5. Confidence gate. If two categories fit equally well, or none fits, do not force it: set the
   desk's general or catch-all category when the list clearly has one, and leave a short
   internal note saying it needs a human look and why. If there is no catch-all, leave the
   category unset and note that instead. A wrong category is worse than a missing one — it
   quietly corrupts Autotask reporting and can misfire workflow rules.

6. Report the category you picked and the one-line reason. Run by hand: propose first, apply
   after confirmation. Run as a Flow on ticket created: apply directly, and leave a note only
   in the ambiguous case above — don't note every routine pick.

Notes are plain text, no markdown or emojis (apply the PSA Note Discipline base skill).

Category only: never change status, priority, queue, or assignment. Re-read the ticket before
writing — it may already have been categorised Autotask-side, and if it already carries a
sensible category, leave it and say so. This is Autotask only. On a ConnectWise or HaloPSA
desk the category is not available; stop and say so rather than classifying some other field.
```
