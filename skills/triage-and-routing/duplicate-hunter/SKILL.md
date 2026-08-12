---
name: Duplicate Hunter
description: Check whether a ticket duplicates an existing open ticket for the same client, contact or asset, and symptom — and merge only on an exact reference match.
category: Triage & Routing
tools: [search_tickets, merge_ticket, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Duplicate Hunter

**When to use:** A new ticket looks like something already open ("didn't we just get this?"), a flow runs on create to catch double-submissions and re-sent alerts, or dispatch wants a duplicate sweep of today's intake.

**Run it:** on one ticket · across all new tickets on a board · or as a Flow (when a ticket is created).

## Prompt

```
Hunt for a true duplicate of a ticket — same client, same contact or asset, same symptom,
inside a recent window — and merge it under the original only when a strong identifier
proves the match. A confident "no duplicate found" is a valid, useful answer.

1. Read the candidate ticket: client, contact, referenced asset/device, and the specific
   symptom or error.

2. Search for open tickets from the same client within the configured window (default:
   7 days). Run separate searches per strong identifier — contact email, device/asset name,
   alert or error reference — rather than one broad text search. If any search may have hit a
   result cap, state that; an incomplete search cannot support a confident "no duplicate".

3. For each candidate, require an exact-reference match before calling it a duplicate:
   same alert/monitoring ID, same device + same error code, or same contact + verbatim-same
   request. Similar wording alone is never a duplicate.

4. If exactly one older open ticket matches at exact-reference strength: merge the newer
   ticket under it (newer merges into older; never merge into a closed ticket), and leave a
   plain-text note on the surviving ticket naming both numbers and the matching identifier.

5. If matches are plausible but not exact, report them as "related, not merged" with
   reasons. Two or more candidate parents → do not merge; list them.

6. If nothing matches, state plainly that no duplicate was found and which identifiers
   were checked — that's a successful outcome, not a failure.

Never merge tickets from different clients or contacts even if the symptom text is
identical — that's a pattern for the cross-client outage detector, not a duplicate. Notes
are plain text.

Running as a Flow: your entire reply is the internal note, verbatim, in one of exactly
three forms: "DUPLICATE: merged #<new> into #<old>. Match: <identifier>." /
"POSSIBLE DUPLICATE of #<n>: <reason>. Not merged." / "NO DUPLICATE FOUND. Checked:
<identifiers>." Merge only on exact-reference match with a single candidate parent;
otherwise no write. Never merge unattended if either ticket has a human reply newer than
the alert content. When in doubt, do nothing.
```
