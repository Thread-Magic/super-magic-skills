---
name: Defensive Writing Standard
description: Language standard for security writing: use when drafting client notifications, incident updates, postmortems, and alert closures to avoid overstatement.
category: Security
tools: []
connectors: []
scope: both
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# Defensive Writing Standard

**When to use:** Drafting any client-facing security message (alert notifications, incident updates, verdicts, closure summaries); writing postmortems, monthly security reports, or insurance/audit narratives; or reviewing a technician's draft before it goes to a client during a security event.

**Run it:** on one draft · or across a set of security messages you're reviewing.

## Prompt

```
Apply the vocabulary and structure rules for security communication. Words like "breach"
carry legal, contractual, and insurance meaning — in many jurisdictions they trigger
notification obligations — and overstated language creates exposure for both the MSP and
the client. Other security skills load this standard rather than restating it. Apply it in
order:

1. Classify the event's confirmation status before choosing words:
   - Unconfirmed signal → "alert," "detection," "reported message," "suspicious activity."
   - Confirmed account-level event → "unauthorized sign-in," "compromised account" (only
     after evidence).
   - Confirmed system-level event, verified by investigation → only then is "breach"
     available, and only if the client's incident policy and management agree.
2. Apply the banned-word rules: never "hacked" in any client-facing text; never "breach"
   for anything below a confirmed system-level event; never absolutes like "your data is
   safe" or "no data was accessed" without log evidence that proves it.
3. Structure every client-facing security message in four parts: what we observed (facts
   with timestamps), what we have done, what we need from you, and when the next update
   will come.
4. Strip speculation: no guessed root causes, no attacker attribution, no impact estimates
   ahead of evidence. "We are investigating" is a complete and correct sentence.
5. Final pass: every factual claim in the draft must trace to a timestamped observation in
   the ticket. Anything that doesn't gets removed or reworded as "under investigation."

Guardrails — always:
- Reserve "breach" for confirmed system-level events; never use "hacked."
- Never overstate before facts are confirmed — understatement is recoverable, overstatement
  is not. No absolute safety claims without the evidence to back them.
- Plain text only for notes that sync to a PSA; no markdown or emojis there.
- This standard governs wording, not disclosure decisions — what to tell a client and when
  remains a management and client-incident-policy call.
- Keep sentences translatable: short, literal, no idioms — many desks operate in more than
  one language.
```
