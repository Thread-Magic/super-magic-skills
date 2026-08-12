---
name: Vacation Handoff Pack
description: Pre-PTO handoff prep listing which tickets need transferring, which need watching, and a per-ticket one-liner brief so cover techs can act fast.
category: Personal Productivity
tools: [search_tickets, search_members, update_ticket, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Vacation Handoff Pack

**When to use:** "I'm off next week — prep my handoff" / "what do I need to hand over before vacation?" / "I'm out Thursday–Friday, what needs covering?" — triages every open ticket into transfer / watch / safe and writes the covering tech a per-ticket one-liner so context doesn't leave with you.

**Run it:** across your own open tickets — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
You are building my pre-PTO handoff. Scope everything to MY own open tickets.

1. Collect: my absence dates, and who is covering — a named tech (look them up) or
   "the queue" if coverage is pooled.

2. Read all my open tickets and triage each into EXACTLY one bucket. If the result may
   be capped, say so — a handoff built on a partial list is dangerous, so flag it
   rather than presenting it as complete.
   - Transfer: will need action during the absence — active troubleshooting mid-flight,
     client expecting a response, SLA that will breach in-window, scheduled work inside
     the window.
   - Watch: probably quiet but could wake up — waiting on vendor/client where a reply
     may arrive; the covering tech acts only if it moves.
   - Safe: genuinely dormant (long-hold, scheduled beyond my return date). No coverage
     action needed.

3. For every Transfer and Watch ticket, write the one-liner brief — the sentence the
   covering tech actually needs, not a summary of the summary: current state, the next
   expected event, and the trap if there is one ("#1234 <client> — replacement switch
   arrives Tue, install same day; site contact is <user>, don't reboot the old one
   before EOD backups"). Point to where credentials/docs live by reference ("creds in
   the docs tool under the client's network folder") — never paste credentials into the
   pack.

4. Flag the specials: any VIP client, any fragile client relationship, and anything I
   know that isn't written in the ticket — ask me "anything in your head that isn't in
   these tickets?" and fold my answer into the relevant one-liners.

5. Present the full pack for review: buckets, one-liners, and the proposed transfers.
   Nothing has changed yet.

6. On my explicit confirmation ONLY:
   - Reassign Transfer tickets to the covering tech.
   - Leave an internal handoff note on each transferred/watched ticket carrying its
     one-liner (plain text — no markdown or emojis, it may sync to a PSA) so the context
     lives on the ticket, not just in chat. Start each note with a recognizable prefix
     ("HANDOFF <dates>:") so it's findable and cleanable on return.

7. Output the final pack in a copyable format for the covering tech, ordered by
   urgency, with the absence dates and return date at the top.

No reassignment or notes without my explicit confirmation of the reviewed pack. Never
paste credentials, and never invent context — one-liners state only what the thread
shows plus what I explicitly told you. Watch-bucket discipline: do not transfer
everything "to be safe" — burying the covering tech guarantees the real transfers get
less attention; justify each Transfer. If no covering tech is identified for a
Transfer-bucket ticket with a hard in-absence deadline, flag it LOUDLY at the top —
that ticket is the whole reason this skill exists.
```
