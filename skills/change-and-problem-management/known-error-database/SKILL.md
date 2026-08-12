---
name: Known Error Database
description: Maintain the KEDB with every known error in one findable symptom, cause, and workaround format — deduplicated on arrival and retired when the fix ships.
category: Change & Problem Management
tools: [search_knowledge_base, search_tickets, add_ticket_note, update_ticket]
connectors: []
scope: both
flow: no
role: [Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise]
---

# Known Error Database

**When to use:** a problem record reached KNOWN ERROR state and needs its KEDB entry written / "is this a known error?" (checking a live incident) / a fix shipped and the entry needs retiring / a periodic KEDB hygiene sweep.

**Run it:** on one known error · or as a KEDB hygiene sweep.

## Prompt

```
Maintain the desk's memory of "we know why this happens and here's what to do about it."
The value is entirely in hygiene: one entry per error, a fixed format a stressed tech can
scan, ruthless retirement when fixes ship. A KEDB full of stale entries is worse than none.

CREATING AN ENTRY:
1. Verify the source: a KEDB entry requires a problem record with an evidenced root cause.
   A hunch from one ticket is not a known error — route that to the problem track first.
2. Dedupe before writing: search the knowledge base for existing entries matching the symptom
   class and root cause. Same root cause, different symptom wording → extend the existing
   entry's symptom list; never create a sibling. Similar symptoms but a genuinely
   different root cause → new entry, cross-referenced to its lookalike ("similar symptoms,
   different cause: see <entry>").
3. Write the entry in the fixed format, stored in the desk's KB (draft via the desk's
   pipeline; a human publishes where publishing is gated):
   - Title: symptom-first, in the words a searching tech would use, not cause-first.
   - Symptoms: observable signs, error text verbatim where available.
   - Affects: systems/versions/configurations in scope — and out of scope where known.
   - Root cause: the confirmed cause, one paragraph, linked to the problem record.
   - Workaround: the documented workaround (or a pointer), including its cost and hold
     time. "No workaround — escalate to <path>" is a valid and important entry.
   - Status line: problem record reference, current state, entry review date.
4. Back-link: note on the problem record that the KEDB entry exists, so lifecycle
   transitions know what to retire.

LOOKUP (live incident):
5. Search the KEDB by symptom and error text before deep diagnosis. On a match, cite the
   entry and its workaround with the entry's date and status so the tech can judge
   freshness. Do not invent entries or links; no match means say "no KEDB match," not a
   plausible-sounding near miss.

RETIREMENT:
6. When the problem closes FIXED (verified), retire the entry: mark it "RESOLVED — fix
   deployed <date>, entry retained for history" rather than deleting, so old ticket links
   still resolve, but make its non-current status unmissable at the top. When the problem
   closes ACCEPTED RISK, mark the entry permanent with its scheduled review date.
7. Hygiene sweep: list entries past their review date, entries whose linked problem record
   moved states without the entry updating, and near-duplicate pairs — with a recommended
   action each. Retirement recommendations go to a human; the agent doesn't bulk-delete
   knowledge.

Guardrails: no entry without an evidenced root cause and a problem record behind it. Dedupe
is mandatory on every create. Never fabricate entry references, ticket numbers, or links
during lookup — a false "known error" match sends a tech confidently down the wrong path.
Retired means visibly retired — a fixed error's workaround must not remain
findable-as-current. Entries are sanitized: symptom/cause/workaround in general terms; no
client names, credentials, or environment-specific identifiers beyond KB conventions.
```
