---
name: Incident Commander Brief
description: An incident commander is taking over a running major incident — assemble everything they need in one read: timeline so far, workstream states, comms state, and the next decision point. Takeover without the 20-minute "so what happened?" retelling.
category: Change & Problem Management
tools: [search_tickets, add_ticket_note, search_members]
connectors: []
scope: single
flow: no
role: [Service & Ops Manager, MSP Owner / Leadership]
outcome: [Faster Resolution & Response]
---

# Incident Commander Brief

**When to use:** "Brief me — I'm taking over as IC / hand the incident to <lead>" / shift change during a long-running major / an executive or senior engineer joining mid-incident / the current IC wants a written checkpoint of where things stand.

**Run it:** on one incident.

## Prompt

```
Build the takeover package for a live major incident changing hands: state, not story.
Build it from the master incident ticket's timeline and linked workstreams, and be honest
about what's unknown.

1. Load the master incident ticket and every linked workstream/child ticket:
   full notes in time order, status transitions, role assignments from
   the declaration.

2. Build the brief in this FIXED order — an incoming IC should be able to stop reading
   after any section and still be net better off:
   - Situation, 3 lines: what's broken, who's affected (clients/users/sites), current
     severity trend (improving / stable / degrading) with the evidence for that trend.
   - Next decision point — up top, not buried: the decision the IC faces soonest, when
     it's due, and the options as currently understood (e.g. "vendor ETA expires 14:00 —
     extend the workaround or start failover; failover takes 2h and is one-way until
     tonight").
   - Timeline — compressed to inflection points: detection, declaration, each mitigation
     attempted and its result, cause hypotheses raised and eliminated. Timestamps from
     ticket records; anything reconstructed is marked "approx." Not every note — the
     turns.
   - Workstreams — per stream: owner, current action, last update time, blocked/unblocked.
     A stream with no update in over an hour is flagged "stale — verify before relying on
     this."
   - Comms state — last internal update sent (when, gist), last client update sent (when,
     gist), next update due per the cadence, and any commitment already made to a client
     (a promised ETA is a decision constraint the new IC inherits).
   - Resources — who's engaged and for how long (fatigue is operational data), which
     vendor cases are open with case numbers from the ticket, who's on deck.
   - Known unknowns — what has NOT been established yet, stated plainly. The brief's
     credibility rests on this section.

3. Deliver in chat to the incoming IC; post the brief as a plain-text note on the master
   ticket marked "IC handover brief — <from> to <to>, <time>" so the
   handover itself is on the timeline.

4. If the ticket record is too thin to build a trustworthy brief (gaps over an hour during
   active response), say so explicitly and list the gaps — the outgoing IC fills them
   verbally and the brief records that they were filled verbally.

Guardrails: state only what the ticket evidence supports; label hypothesis as hypothesis
— a wrong "confirmed" in an IC brief steers the whole response wrong. The brief never
makes the pending decision — it frames it; the IC decides. Include commitments made to
clients verbatim where possible; paraphrasing a promised ETA is how ETAs get accidentally
re-promised. No blame framing in-flight ("the change that caused this") — causal language
stays neutral until the post-mortem settles it. If information is stale or capped, the
brief says so rather than presenting a partial picture as complete.
```
