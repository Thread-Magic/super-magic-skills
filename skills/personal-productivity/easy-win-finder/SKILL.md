---
name: Easy Win Finder
description: "Recommend an easy ticket that just came in" — surface quick-win candidates from the queue that match the requesting technician's skills, with why each is quick.
category: Personal Productivity
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Easy Win Finder

**When to use:** "Recommend an easy ticket that just came in" / "I've got 20 minutes — what can I knock out?" / "give me a quick win" / a new tech asking "what's a good starter ticket right now?" — quick wins matched to *this* tech's own close history, for the gap between meetings or momentum after a brutal ticket.

**Run it:** across the boards you work (or your own queue) — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
You are finding me a quick win — a ticket resolvable in one short touch by ME
specifically, based on what I've closed before. Easy is relative; make it easy for me.

1. Establish the candidate pool: unassigned tickets on the boards I work (default), or
   my own queue if I say "from my tickets". Prefer recently arrived tickets — that's
   the "just came in" case. If the search may be capped, say so; don't present a
   partial scan as the whole queue.

2. Build my skill fingerprint from my own history — read my recently closed work — to
   find the categories I close fast and clean. This is what makes a ticket easy for me.
   (Look me up if you need to resolve who I am.)

3. Score candidates for quick-win-ness:
   - Category matches my fast-close fingerprint.
   - Single, clearly stated issue — no multi-issue essays, no "everything is broken".
   - Known resolution pattern (same category closed in <=1–2 touches recently here).
   - Client is reachable/responsive; no pending vendor or approval dependency.
   - No red flags: VIP-sensitive thread, negative sentiment, prior reopen,
     security-flavored content.

4. Recommend the top 1–3, each with: ticket number, client (short), the ask in one
   line, why it's quick FOR ME ("you've closed 6 of these this month, median 12
   minutes"), and the expected resolution path in a sentence.

5. Be honest when there's no easy win: say the queue has none rather than dressing up
   a grenade — and offer the least-bad option labeled as such ("nothing quick;
   lightest is #123 but the client is already frustrated"). Never disguise complexity
   to make a recommendation land — a mispredicted "easy win" costs trust in every
   future recommendation. State uncertainty when the thread is thin, and never invent
   ticket numbers or close-history figures.

6. Respect queue fairness: quick-win picking must not bypass SLA-driven priority. If
   something urgent outranks any easy win, say so first ("heads up: #456 breaches in
   an hour — that first?"). Exclude tickets another tech is actively working, even if
   they look unassigned by status alone — check for recent activity by others.

7. If I pick one, offer the standard pickup — assign it to me and set the appropriate
   status — but recommend only: never assign or change a ticket without my explicit
   confirmation.

Skill fingerprints are my private coaching data for my own picks; do not use this to
rank or compare technicians.
```
