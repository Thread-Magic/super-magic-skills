---
name: After-Hours Voicemail Digest
description: Build a morning digest of overnight voicemails and after-hours calls — urgent items first, callbacks owed with deadlines, and which tickets were created.
category: Voice & Messenger
tools: [search_tickets, list_boards, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Always-On Coverage]
---

# After-Hours Voicemail Digest

**When to use:** "What came in on the after-hours line last night?" / a scheduled morning run before the desk opens / the Monday edition covering the whole weekend.

**Run it:** across all overnight voice/voicemail tickets in the window — run it manually or from an external scheduler (not a Flow; Flows fire on ticket events, they can't schedule a digest).

## Prompt

```
Build the first thing the dispatcher reads: everything the phone lines collected while the
desk was closed, ordered by what will hurt first — urgent issues, then callbacks owed with
deadlines, then the routine remainder.

1. Establish the window: close of business yesterday (or Friday, on Mondays) to now, in the
   desk's timezone.

2. Read the voice- and voicemail-sourced tickets created or updated in the window. Split
   searches per board/source if needed for cap honesty, and say so if any search may have hit
   a result cap.

3. Exclude tickets Dead-Air Call Filter closed as junk, but count them in one summary line
   ("6 junk calls filtered") — a junk spike is itself worth a human glance.

4. For each real item, extract from the ticket and its intake notes: caller, client, issue
   one-liner, stated urgency evidence, and any "CALLBACK OWED:" line (from Voicemail to
   Ticket) with its deadline.

5. Order the digest:
   a. Urgent — stated business stoppage, security concern, or a callback deadline that
      expires this morning. Lead with these.
   b. Callbacks owed — number, who, by when; soonest deadline first.
   c. Routine intake — one line each.
   d. Footer — counts: total calls, tickets created, junk filtered, anything left
      unidentified (flag Voice Catchall Identification candidates).

6. Every line carries its ticket number. Flag repeat callers (same number/contact more than
   once in the window) — repetition overnight usually means something is down.

7. Output the digest in chat (or as the run's post). Offer, don't assume, to leave a
   "surfaced in morning digest" note on the urgent tickets.

Guardrails: the digest reports; it does not act — no priority changes, no assignments, no
callbacks marked done. Urgency must trace to stated words in the source ticket; the digest
must not upgrade or downgrade what intake recorded. Missed items are worse than long digests:
if searches were capped or a board couldn't be read, say exactly what wasn't covered. No
invented deadlines — a callback with no stated time gets the desk's standard SLA, labeled as
such. Keep client/caller references to what recipients need (name + client); no full
transcripts.

Running it unattended: run it manually on demand or from an external scheduler that invokes
Super Magic; a Flow can only reach it via Run Skill on a qualifying ticket event. When it runs
unattended, output deterministic sections in the order above, plain text, every line with a
ticket number; empty sections stated as "none" rather than omitted. If zero real items: post
the one-line "No after-hours voice activity in window. <n> junk calls filtered." — never stay
silent, absence of the digest must not be ambiguous with absence of calls. Never write to
tickets in unattended mode; the digest post is the entire output.
```
