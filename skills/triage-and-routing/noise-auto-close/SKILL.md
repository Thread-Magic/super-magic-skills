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
Close only what is provably noise. This skill is built to abort loudly rather than close a real
request.

1. Read the whole ticket, every message, headers where available.

2. Classify against the noise catalog: (a) delivery failure or mailer-daemon, (b) automated
   vendor or system acknowledgment, (c) out-of-office autoresponder, (d) thanks-only courtesy
   message with no request, (e) offline-then-reconnected alert pair.

3. Class (e) qualifies only when a "reconnected" event exists for the SAME device — exact device
   identifier, not name similarity — inside the configured pairing window, as a companion ticket
   or a later message. Run the recurrence check FIRST: search this device's offline alerts over
   30 days, because 3 or more flap cycles means it is flapping — a real reliability issue, NOT
   noise. Flapping closes nothing; route it as a genuine investigation, "device flapping: N
   offline events in 30 days". If recurrence passes and the pair is confirmed, the close applies
   to BOTH tickets, each noting the companion and both timestamps.

4. Verify ALL these independent stop conditions before closing, evaluating each rather than
   collapsing them into a gut call:
   - the sender is automated (noreply, mailer-daemon, auto-submitted headers) OR the whole
     content is a courtesy phrase with no question, request or new information;
   - no human message contains a question, request, error description or attachment for action;
   - no sibling context makes it meaningful — a bounce that proves the client's mail is broken is
     a real issue, not noise;
   - no human tech has replied or logged work on it.

5. If any condition fails, abort: leave the ticket open with a note saying why. Any sign of a
   real user message anywhere in the thread aborts the close — that rule beats every
   classification.

6. If all pass, close the ticket and note the noise class and conditions checked; for class (e)
   close both tickets of the pair. Notes are plain text, no markdown or emojis (PSA Note
   Discipline base skill).

Thanks-only detection needs the whole message to be courtesy content — "thanks, but it's still
broken" is a real message. Never reply to noise senders: close silently, internal note only.

As a Flow: your entire reply is the internal note, verbatim — "NOISE AUTO-CLOSE: <class>.
Conditions passed: sender-automated, no-human-request, no-incident-signal, no-tech-work." or "NOT
CLOSED: failed <condition>." For pairs: "NOISE AUTO-CLOSE: offline-reconnected pair with
#<companion>. Offline <time>, reconnected <time>. Flap check: <n> events/30d." or "NOT CLOSED:
flapping (<n> events/30d) - routed for investigation." Exactly one close per run per ticket, a
confirmed pair counting as two; no other field changes; never send an outbound message. When in
doubt on any condition, do nothing: a false close costs more than a noisy queue.
```
