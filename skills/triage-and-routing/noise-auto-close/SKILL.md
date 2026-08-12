---
name: Noise Auto-Close
description: Close pure-noise tickets — bounce-backs, vendor auto-replies, thanks-only messages, reconnected offline alerts — behind independent stop conditions.
category: Triage & Routing
tools: [search_tickets, update_ticket, add_ticket_note, list_ticket_statuses]
connectors: []
scope: both
flow: yes
role: [Dispatcher]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Noise Auto-Close

**When to use:** Bounce-back / mailer-daemon tickets, vendor or OOO auto-replies, thanks-only replies that spawned a new ticket, or device-offline alerts whose device already reconnected — and a flow that sweeps the intake board for noise.

**Run it:** on one ticket · across the intake board · or as a Flow (when a ticket is created).

## Prompt

```
Close only what is provably noise. This skill is built to abort loudly rather than close a
real request.

1. Read the full ticket, every message, headers included where available.

2. Classify against the noise catalog: (a) delivery failure / mailer-daemon, (b) automated
   vendor/system acknowledgment, (c) out-of-office autoresponder, (d) thanks-only courtesy
   message with no request, (e) offline→reconnected alert pair (see step 3).

3. For class (e) — offline→reconnected pairing: a device-offline ticket qualifies only when
   a matching "reconnected / back online" event exists for the SAME device (exact device
   identifier match, not name similarity) within the configured pairing window, found as a
   companion ticket or subsequent message. Run the recurrence check FIRST: search offline
   alerts on this device over the last 30 days — 3 or more flap cycles means the device is
   flapping, a real reliability issue, NOT noise. Flapping → close nothing; route as a genuine
   investigation ("device flapping: N offline events in 30 days"). If the recurrence check
   passes and the pair is confirmed, the close applies to BOTH tickets, each with a plain-text
   pairing note naming the companion and the offline/reconnected timestamps.

4. Verify ALL independent stop conditions pass before closing — evaluate each one, don't
   collapse them into a gut call:
   - The sender is automated (noreply/mailer-daemon/auto-submitted headers) OR the entire
     content is a courtesy phrase with no question, request, or new information;
   - No message from a human contains a question, request, error description, or attachment
     for action;
   - No open sibling context makes it meaningful (a bounce that proves the client's mail is
     broken is a real issue, not noise);
   - No human tech has replied or logged work on it.

5. If any condition fails, abort: leave the ticket open and leave a plain-text note saying
   why it was not auto-closed. Any sign of a real user message anywhere in the thread aborts
   the close — this rule beats every classification.

6. If all pass, close the ticket (to the closed status) and leave a plain-text note naming
   the noise class and conditions checked. For class (e), close both tickets of the pair,
   each note naming its companion.

Thanks-only detection requires the whole message to be courtesy content ("thanks, but it's
still broken" is a real message). Never reply to noise senders — close silently with an
internal note only. Notes are plain text.

Running as a Flow: your entire reply is the internal note, verbatim: "NOISE AUTO-CLOSE:
<class>. Conditions passed: sender-automated, no-human-request, no-incident-signal,
no-tech-work." or "NOT CLOSED: failed <condition>." For pairs: "NOISE AUTO-CLOSE:
offline-reconnected pair with #<companion>. Offline <time>, reconnected <time>. Flap check:
<n> events/30d." or "NOT CLOSED: flapping (<n> events/30d) — routed for investigation."
Exactly one close per run per ticket (a confirmed pair counts as its two members); no other
field changes; never send any outbound message. When in doubt on any condition, do nothing —
a false close costs more than a noisy queue.
```
