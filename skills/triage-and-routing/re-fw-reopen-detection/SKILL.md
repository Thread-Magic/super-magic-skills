---
name: RE/FW Reopen Detection
description: When a new ticket subject starts with RE: or FW: on a recently closed subject, find the closed parent and flag it as a reopen instead of working new.
category: Triage & Routing
tools: [search_tickets, update_ticket, add_ticket_note, merge_ticket, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise]
---

# RE/FW Reopen Detection

**When to use:** A new ticket's subject begins with RE:, FW:, or a localized equivalent (AW:, SV:, VS:, TR:), a flow runs on create on email-sourced boards to catch continuations, or a tech asks "is this new ticket actually a reply to something we closed?"

**Run it:** on one ticket · or as a Flow (when a ticket is created on an email-sourced board).

## Prompt

```
A client replying to an old email thread creates a "new" ticket that's really a
continuation. Match the RE:/FW: subject back to the closed original and treat it as a
reopen, preserving history instead of starting cold.

1. Read the new ticket: subject, sender, client, and body.

2. Strip the reply/forward prefixes (RE:, FW:, and localized variants, possibly stacked)
   to recover the base subject line.

3. Search closed tickets for the same client matching the base subject, within the reopen
   window (default: 30 days since closure). Also check the same contact as a secondary
   signal.

4. Require a strong link before calling it a reopen: same client AND (verbatim base-subject
   match OR the new body quotes the original thread OR it references the original ticket
   number). Subject similarity alone across different contacts is never enough — generic
   subjects ("Help", "Printer issue") recur constantly.

5. On a confirmed match, mark the new ticket as a reopen per desk convention: either (a)
   merge the new ticket under the original and set the original back to an open status, or
   (b) keep the new ticket and cross-reference both. Follow the convention configured for this
   desk; when unconfigured, default to (b). Reopening changes status on a closed ticket — in
   attended use, confirm before doing it.

6. Leave a plain-text note naming both ticket numbers and the evidence for the link.

If the original closed more than the reopen window ago, treat the new ticket as new and
only note the historical reference. If the new message is a thanks-only courtesy reply
rather than a real continuation, hand off to noise/courtesy-reply handling instead of
reopening. Notes are plain text.

Running as a Flow: convention (a) vs (b) must be explicitly configured; the unattended default
is (b) — cross-reference notes only, no status change on the closed ticket, no merge. Your
entire reply is the internal note, verbatim: "REOPEN DETECTED: #<new> continues closed
#<old>. Evidence: <one line>." or "NOT A REOPEN: <one line>." When the link is anything
less than the strong-evidence bar, do nothing beyond the NOT A REOPEN note.
```
