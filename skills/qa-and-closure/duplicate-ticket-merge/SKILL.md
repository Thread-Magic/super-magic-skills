---
name: Merge Duplicate Tickets
description: Find duplicate tickets — a client who wrote in twice, a re-forwarded alert, the same issue split across threads — confirm they're really the same, and merge them into one so the desk works a single thread.
category: QA & Closure
tools: [search_tickets, merge_ticket, add_ticket_note, update_ticket, list_boards]
connectors: []
scope: both
flow: no
role: [Dispatcher, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Merge Duplicate Tickets

**When to use:** A client emailed twice and now there are two tickets; a monitoring alert re-fired and opened a second thread; you're handed two ticket numbers and asked "are these the same?"; or a periodic sweep of a board to collapse duplicates before they get worked twice.

**Run it:** on a specific pair I name · or across a board (find and merge the duplicates you're confident about).

## Prompt

```
Find and merge duplicate tickets so the desk works one thread instead of several — but only
merge pairs you're genuinely confident are the same issue, and never merge across clients.

Scope:
- If I name two tickets, evaluate just that pair.
- If I name a board (or say "scan for duplicates"), search that board's open tickets and look
  for duplicate clusters. Search per board and say so if a search may have capped — never imply
  you scanned everything when results were limited.
- If I give you nothing, ask which ticket, pair, or board to check before doing anything.

For each candidate pair or cluster, confirm they are truly duplicates before merging. Two tickets
are duplicates only when ALL of these hold:
1. Same client company AND same contact (or the same underlying alert source). Never merge tickets
   from two different companies — stop and leave them alone if the companies differ.
2. Same underlying issue — the same problem, request, or alert, not just a similar topic. "Outlook
   won't open" and "password reset" from the same person are two issues, not a duplicate.
3. Overlapping in time / still live — a brand-new ticket that duplicates one closed six months ago
   is usually a fresh recurrence, not a merge; flag those instead of merging.

Read the title, description, and the latest messages on each ticket to judge sameness — do not
decide from the title alone. When you're unsure, treat it as NOT a duplicate.

Choose which ticket survives (the primary): keep the oldest/earliest one, or the one with the most
work already logged (assignee, time entries, client replies), so no history is lost. The other
ticket merges into it.

Before merging, show me each pair you intend to merge: both ticket numbers, client, the shared
issue in one line, which one survives, and why you're confident. Merge only after I confirm —
merging is not reversible, so never merge unattended and never merge a pair you had to guess at.

After a confirmed merge, leave a plain-text internal note on the surviving ticket recording which
ticket numbers were merged in and the one-line reason. Notes bound for the PSA are plain text — no
markdown, no emojis.

Output a summary: pairs merged (with the surviving ticket number), pairs you flagged as
uncertain and left alone (with why), and anything that looked like a recurrence rather than a
duplicate. Do not invent ticket numbers or clients; if a search may have capped, say so.
```
