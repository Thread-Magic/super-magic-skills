---
name: EOL Product Notice
description: Draft the client notice that a product or OS they run is reaching end-of-life — verified EOL date, honest risk framing, concrete upgrade paths, and a decision deadline — without fear-selling.
category: Communication
tools: [search_tickets, search_itglue, search_hudu, web_search, view_openDraft]
connectors: [IT Glue, Hudu]
scope: both
flow: no
role: [Technician]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# EOL Product Notice

**When to use:** "<product/OS version> goes end-of-life on <date> — draft the client notice" / a lifecycle review found devices on soon-unsupported software and affected clients need to be told with options.

**Run it:** on one client's notice · or across all affected clients as per-client variants.

## Prompt

```
Draft the message that turns a vendor's EOL calendar into a client decision: what stops on
which date, what that actually exposes them to, their options, and when the desk needs an
answer to act in time.

1. Verify the EOL facts before drafting. Confirm online against the vendor's OFFICIAL lifecycle
   documentation: the exact date, and what actually ends on it (security updates vs feature
   updates vs paid extended support). EOL, end-of-support, and end-of-sale are different events
   — name the right one. If vendor sources conflict or can't be confirmed, say so and ask me to
   confirm rather than publishing a guessed date.

2. Establish this client's exposure: which of their systems run the affected product — from me,
   from documentation (check IT Glue / Hudu where connected), and ticket history. Name the
   affected scope in client terms ("your 4 office desktops," "the server running <application>")
   — a generic EOL notice with no "this affects you because" gets ignored.

3. Draft:
   - What is reaching end-of-life and the verified date, first line.
   - What changes on that date, factually: "no further security updates" — and what that means:
     newly discovered vulnerabilities remain unpatched, and running unsupported software may
     affect compliance or cyber-insurance requirements WHERE the client has such requirements.
     No doom scenarios, no "hackers are waiting."
   - Upgrade paths as options, each with one line of what it involves: upgrade in place, replace
     hardware, migrate to <successor>, or (where offered) paid extended support as a bridge.
     Only include paths that actually exist. Cost/effort figures only if I supply them.
   - Decision deadline: the date by which the client must choose so the work can be scheduled
     before EOL — worked back from lead time I confirm, and clearly distinct from the EOL date.

4. Close with the concrete next step: reply with a preferred option, or book a short call.

5. Show me the draft for review, labeled "EOL NOTICE DRAFT." If many clients are affected,
   produce per-client variants (scope differs); a mass generic blast is the fallback, not the
   default.

Never publish an unverified EOL date — verify against the vendor's current documentation at
draft time; cached lifecycle dates go stale. Factual consequences only, no absolutes ("you will
be breached"), no fear-selling. Never state compliance or insurance impact as fact for a
specific client unless their requirements are known. Quotes, prices, and timelines come from me
only. Without IT Glue/Hudu, build scope from me and ticket history and say the inventory basis
is partial.
```
