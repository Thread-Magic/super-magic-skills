---
name: PSA Note Visibility Rules
description: For any PSA-synced desk (ConnectWise, Autotask, HaloPSA) — apply each PSA's internal-vs-external note semantics correctly and run the leak-prevention checklist before writing any note, since a wrong-visibility note goes straight to the client.
category: PSA-Specific
tools: [search_tickets, add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Technician, Service & Ops Manager]
outcome: [Risk & Compliance, Fewer Escalations & Less Noise]
---

# PSA Note Visibility Rules

**When to use:** Writing any note on a PSA-synced ticket where visibility matters (which is all of them), a tech asking "will the client see this?", or drafting notes for an unattended skill/flow.

**Run it:** on one ticket · across all tickets a note-writing sweep touches · or as a Flow (triggered on the event that would post a note).

## Prompt

```
You are deciding note visibility on a PSA-synced ticket (ConnectWise Manage, Autotask, HaloPSA)
BEFORE writing. Every PSA splits ticket notes into client-visible and internal-only, and each does
it differently. A note written with the wrong visibility is an instant leak — internal candor,
pricing, security details, or another client's name landing in the customer's portal or email.

1. Re-read the ticket to see how existing notes are typed on this ticket and confirm the client-
   facing channel (portal, email thread) is what you think it is.

2. Decide the audience first — client-visible or internal — and only then write. Per-PSA semantics
   to respect:
   - ConnectWise Manage: Discussion entries are customer-facing; Internal and Resolution note
     types have their own visibility flags. Time-entry notes can surface on invoices regardless of
     ticket-note visibility.
   - Autotask: notes carry a publish setting (internal vs client-visible); replies to client-
     originated tickets typically notify the client. Time-entry summaries can appear on invoices.
   - HaloPSA: visibility rides on the action used — customer-visible actions email/portal-publish
     the note; private actions do not.
   Where this tenant's exact mapping is unverified, treat every note as potentially client-visible
   until confirmed.

3. Run the leak-prevention checklist on any note that is (or might be) client-visible:
   - No internal candor (frustration, blame, "this client always...").
   - No other client, partner, or unrelated person named.
   - No credentials, secrets, or security-sensitive detail (vulnerability specifics, unconfirmed
     "breach" language).
   - No pricing, rates, margins, or internal cost discussion.
   - No speculation stated as fact; no promised dates not actually committed.
   - Plain text only — markdown and emojis degrade or leak formatting artifacts through PSA sync.

4. Internal notes still meet a bar: factual, professional, no credentials — internal notes get
   exported, migrated, and subpoenaed. "Internal" lowers the audience, not the standard.

5. Write the note at the decided visibility. In your output, state the visibility you used and why.
   If the tenant's note-type mapping cannot be confirmed, put nothing sensitive in any note and
   say so.

Always: default-deny — unknown visibility = client-visible; write accordingly or don't write. Re-
read before writing — a ticket that closed PSA-side may email closure notes differently, and your
note may land in a client-facing closure digest. Never fix a leaked note by deleting evidence
silently — a leak that reached the client is an incident: flag it to the desk lead with the note
text and timestamp. Time-entry notes are a separate leak surface (invoices); never assume ticket-
note visibility rules cover them. Unattended/Flows variant: your entire reply may be posted verbatim
as the note — no narration, no headers, plain text, and when visibility is uncertain, output
nothing.
```
