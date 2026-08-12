---
name: Multi-Issue Ticket Splitter
description: Detect when one ticket bundles two or more distinct problems and split it into cross-linked sibling tickets, one purpose each, with tech confirmation.
category: Triage & Routing
tools: [search_tickets, create_ticket, update_ticket, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Multi-Issue Ticket Splitter

**When to use:** A ticket clearly describes two or more unrelated problems ("my laptop is slow, also we need a license for the new hire, and the conference room TV is broken"), a tech says "split this ticket", or intake flags bundled requests needing different owners or boards.

**Run it:** on one ticket.

## Prompt

```
Propose a split of a bundled ticket into one-ticket-per-problem siblings, get the tech's
sign-off on the list, then create cross-linked tickets.

1. Read the full ticket, including all messages — later replies often add or resolve asks.

2. Identify candidate distinct problems: different systems, different affected users, or
   different request types (incident vs purchase vs access). Two symptoms of one root
   cause are ONE problem — never split those; when unsure, keep together and say why.

3. Present the proposed split to the tech: for each sibling, a one-line purpose, suggested
   board/type, and which original text supports it. Explicitly mark anything you're unsure
   belongs separate.

4. Wait for the tech to confirm, edit, or reject the purposes. The confirmed list — not
   your draft — defines the split. No confirmation → no split.

5. Keep the original ticket as the anchor for the first (or primary) problem. For each
   additional confirmed problem, open a new ticket under the same client and contact, titled
   with its confirmed purpose, copying in only the relevant text. The client's own words
   travel with each sibling — quote, don't paraphrase away detail.

6. Cross-link everything: leave a plain-text note on each sibling listing all related ticket
   numbers and each one's purpose, and update the original's description/note to state what
   was split out and where. Every sibling must carry the cross-link note; an unlinked
   sibling is a lost ticket.

Do not close or reassign the original as part of the split unless the tech asks. Notes are
plain text; no invented ticket numbers — link only tickets you actually created.
```
