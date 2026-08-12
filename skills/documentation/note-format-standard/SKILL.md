---
name: Note Format Standard
description: Base skill defining the house format, tone, and plain-text PSA-sync rules for internal ticket notes. Other documentation skills reference this standard.
category: Documentation
tools: [add_ticket_note]
connectors: []
scope: both
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Note Format Standard

**When to use:** Loaded as a companion whenever another skill writes or drafts a ticket note, or "format this as a proper internal note" — the shared standard that makes every note on the desk look like it came from one team.

**Run it:** on one ticket · or across any note the desk writes.

## Prompt

```
Apply the house standard to an internal ticket note. This skill defines FORMAT — it
never adds, removes, or reinterprets content; meaning is owned by the calling skill
or technician.

1. Structure every internal note in this fixed order (omit empty sections, keep the
   order):
   1. Summary — one line: what this note records.
   2. Details — what was observed/done/decided, past tense, factual.
   3. Next step — single owner-and-action line, if any.
   4. Source — where the info came from (call, email, alert, meeting) when not obvious.

2. Tone rules: professional, plain language, no blame, no speculation presented as
   fact (prefix hypotheses with "suspected:"), no internal jokes — notes outlive the
   moment and may be read by the client's auditors.

3. PSA plain-text rules whenever a note syncs to a PSA (ConnectWise, Autotask, Halo —
   assume yes unless the desk confirms otherwise; when unsure, write plain text):
   - Plain text only: no markdown (**, #, backticks, tables), no emojis, no smart
     quotes, no em-dashes (use a hyphen or comma).
   - Structure with CAPITALIZED single-word labels and hyphen lists:
     "SUMMARY: ..." / "DETAILS:" / "- item" / "NEXT STEP: ..."
   - Blank line between sections; no line longer than ~100 characters.

4. This standard governs INTERNAL notes. Anything client-visible follows the desk's
   client-communication voice instead — never mix the two in one note.

5. No credentials, one-time codes, or personal data beyond what the workflow requires
   in any note. Desk-specific overrides (their own labels, language, banned words)
   take precedence over these defaults. Non-English desks: same structure, labels
   translated to the desk's working language.

6. When another skill produces a note, reformat its content to this standard without
   changing its meaning, then post it as an internal note only when that skill's own
   confirmation rules are satisfied.
```
