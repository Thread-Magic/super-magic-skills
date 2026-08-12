---
name: Voice Call QA Review
description: Review AI-handled voice calls against a rubric — caller identified, issue captured, commitments accurate, clean handoff — with transcript evidence cited.
category: Voice & Messenger
tools: [search_tickets, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Dispatcher]
outcome: [Faster Resolution & Response, Fewer Escalations & Less Noise]
---

# Voice Call QA Review

**When to use:** "QA the AI-handled calls from yesterday" / "did the Voice AI handle this call properly?" (single-ticket review) / a weekly Voice AI quality sweep feeding tuning decisions.

**Run it:** across the AI-handled calls in a window, or on a single call ticket — run it manually (not a Flow; there's no schedule trigger).

## Prompt

```
Grade calls the Voice AI answered: a fixed rubric, pass/fail per criterion, every finding
pinned to a transcript line. The output tells a service manager which calls to listen to and
what to tune. This is read-and-recommend — it changes no configuration and touches no ticket
state.

1. Collect the calls: read the voice-sourced tickets in the window, or load the single ticket
   given. Read each transcript and the ticket the call produced. State it if result caps may
   have truncated a sweep.

2. Grade each call against the rubric, each criterion pass/fail/not-applicable with a quoted
   transcript line as evidence:
   a. Identification — did the AI establish who was calling and from which client, or
      correctly use known caller-ID context? Unidentified caller passed through without an
      identification attempt = fail.
   b. Issue captured — does the ticket's issue match what the caller actually described?
      Missing symptoms the caller stated, or added symptoms they didn't, = fail.
   c. Commitments accurate — everything the AI promised ("someone will call you back within
      the hour", "I've created a ticket") must be true and recorded on the ticket. A
      promise with no corresponding ticket artifact = fail; this is the top severity.
   d. Handoff clean — if transferred: was the reason captured, did context travel with it
      (caller didn't re-explain), did the AI set a correct expectation? If handled
      end-to-end: did the call end with a clear statement of outcome?
   e. Scope discipline — the AI stayed inside what it can actually do; no invented
      capabilities, prices, or policy answers.

3. Per call, produce: verdict (clean / minor issues / needs review), failed criteria with
   quotes, and one specific tuning suggestion where a pattern is visible (missing intent,
   bad prompt phrasing, gap in identification flow).

4. Sweep mode: roll up a summary — calls reviewed, pass rate per criterion, the 2-3
   recurring failure patterns, and the specific calls a human should listen to.

5. Offer to leave per-ticket findings as plain-text notes; post only on confirmation.

Guardrails: grade only what the transcript shows — no penalty and no credit for tone you
can't quote; transcription artifacts (garbled words) are noted, not counted against the AI.
A commitment inaccuracy (promised action that didn't happen) is always the headline finding.
This skill grades and recommends; it does not change Voice AI configuration, reopen tickets,
or contact clients. Sample honestly: if reviewing a subset, say which subset and how it was
chosen — never present a sample as the whole. No caller names in the rolled-up report beyond
what's needed to locate the ticket; reference tickets by number.
```
