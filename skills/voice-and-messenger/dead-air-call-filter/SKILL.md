---
name: Dead-Air Call Filter
description: Detect voice sessions that were dead air, instant hangups, or robocalls and close them so they don't pollute the queue — with a hard rule that any human speech means it is not dead air. Use on voice-sourced tickets with empty or junk transcripts.
category: Voice & Messenger
tools: [search_tickets, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: single
flow: yes
role: [Dispatcher]
outcome: [Faster Resolution & Response]
---

# Dead-Air Call Filter

**When to use:** a flow runs on every completed voice session to filter non-calls before triage / "sweep the voice board for dead-air tickets and close them" / a ticket's transcript is empty, seconds long, or obviously a recorded solicitation.

**Run it:** on one voice ticket · or as a Flow that fires on each completed voice session to filter junk before triage.

## Prompt

```
Close junk voice sessions cleanly (pocket dials, instant hangups, fax tones, robocalls) —
and refuse to close anything containing a single word of live human speech.

1. Read the ticket's transcript/recap content in full. Note the call duration if present.

2. Classify:
   - Dead air: no transcribed speech at all, or only system prompts from our side ("thank
     you for calling...") with zero caller audio.
   - Instant hangup: call ended within seconds, no caller speech.
   - Robocall/solicitation: recorded-message hallmarks — scripted monologue with no
     interaction, "press 1" prompts, warranty/insurance/utility scripts, synthesized
     cadence markers.
   - Fax/modem/IVR loop: noted tones or repeated identical prompt loops.

3. THE HUMAN-SPEECH RULE: if the transcript contains any live caller speech — even one
   word, even just a name, even "hello? ...hello?" — it is NOT dead air. A caller who said
   "hello" twice and hung up may be a failed connection from a real client: leave it open
   and route it to Voice Catchall Identification / normal triage instead.

4. Ambiguous robocall vs. human: if any line could plausibly be a live person responding to
   prompts, treat it as human.

5. For confirmed junk: change the ticket to the desk's closed/no-action status (find it in
   the desk's status list) and leave a plain-text note: classification, duration, and the
   evidence ("no caller audio for 42s", "recorded car-warranty script, no interaction").

6. For anything kept open: leave a one-line note that the filter reviewed it and why it was
   kept.

7. In sweep mode, output a table: ticket, classification, action, evidence. State it if
   searches may have hit result caps.

Guardrails: any human speech = not dead air, no exceptions — the cost of closing a real
client's failed call is far higher than one junk ticket surviving. Repeated hangups from the
same number within a short window are a signal, not junk (a client whose call keeps
dropping) — keep the latest open and note the pattern. Never delete; close with a note so
the trail survives audit and the pattern stays countable. Do not blocklist or take action
against caller numbers — that's a human policy decision. Plain-text notes for PSA-synced
tickets.

Running unattended (Flows): close only the three deterministic classes — zero caller
speech, sub-threshold instant hangup with zero caller speech, or a transcript matching a
recorded-script pattern with no interactive caller lines. Anything else → leave open, post
"DEAD-AIR FILTER: kept open — <reason>." and stop. One evaluation per ticket; if a filter
note from this skill exists, stop. Never change priority, assignment, or anything besides
status + note. Your entire reply is posted verbatim as the internal note — no narration.
```
