---
name: Weekly QA Digest
description: Compile the week's closure-QA failures into a digest with per-technician patterns and concrete training suggestions, ready to email or post to the team channel.
category: QA & Closure
tools: [search_tickets, search_members]
connectors: [Zapier: Outlook, Zapier: Microsoft Teams, Zapier: Slack]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Retention & Growth (CSAT/Expansion)]
---

# Weekly QA Digest

**When to use:** Weekly — "build the QA digest" / "summarize this week's QA failures" / "what should I coach on this week?", prepping the team meeting or a one-on-one with quality talking points backed by tickets, or delivering the digest on a schedule to email or a team channel.

**Run it:** across all of the week's QA results (manually or on a schedule).

## Prompt

```
Turn a week of individual QA results into coaching material: which closure criteria keep failing,
for whom, and what one training topic would fix the most misses. Written for a service manager's
Monday, not for a compliance binder.

1. Gather the week's QA evidence: tickets reopened by QA (QA failure notes), tickets closed clean,
   and their per-criterion results where the QA gate posted them. Split searches per board and
   disclose any result caps.

2. Aggregate — don't enumerate. Roll failures up to criterion level ("missing customer
   confirmation: 9 tickets") and per-technician level (resolve names by looking up members). Cite
   two or three representative ticket numbers per pattern, not every instance.

3. Identify per-tech patterns: a criterion one tech fails repeatedly, a tech whose pass rate moved
   sharply week over week, and — equally — a tech whose closures were consistently clean (worth a
   public mention).

4. Attach one concrete training suggestion per pattern, tied to the desk's own standard: "missing
   confirmations → 10-minute refresher on the closure checklist and the confirmation-request
   snippet", "time-entry gaps → wrap-up-before-close habit". Suggestions are about the process, not
   the person.

5. Compose the digest, skimmable in under a minute: headline numbers (closures, QA pass rate, delta
   vs last week); top 3 failing criteria with counts and example tickets; per-tech section (pattern
   + suggestion, framed as coaching); one "clean closures" positive callout.

6. Deliver: show the digest in chat for review, then on request send it via Outlook "Send Email" to
   the manager or post it with Teams "Send Channel Message" (or Slack "Send Channel Message"). Plain
   formatting that survives email and chat rendering.

Never send or post without the manager reviewing the digest first — per-tech quality data is
sensitive. The digest is a coaching document, not a disciplinary record: neutral wording, patterns
not verdicts, no rankings shamed by name; route serious concerns to the manager privately. All
counts come from tickets actually retrieved; disclose result caps rather than presenting an
estimate as exact. Never invent ticket numbers, examples, or trends — if last week's baseline is
unavailable, say so instead of guessing the delta. Zapier delivery requires the member to have
connected the Zapier MCP; without it, deliver in chat and note the limitation. If per-criterion QA
notes are sparse (the QA gate wasn't running), say the evidence is thin and offer to run the EOD
Closed Ticket Audit retroactively instead of fabricating a digest.
```
