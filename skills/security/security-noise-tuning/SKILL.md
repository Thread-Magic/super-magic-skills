---
name: Security Noise Tuning
description: Reduce recurring false-positive security alerts: quantify the FP rate, build an evidence pack, and recommend a retune at the source tool.
category: Security
tools: [search_tickets, add_ticket_note]
connectors: []
scope: global
flow: no
role: [Security & Compliance Owner, Service & Ops Manager]
outcome: [Fewer Escalations & Less Noise, Time & Cost Savings (Capacity)]
---

# Security Noise Tuning

**When to use:** A tech or lead says "we keep closing this same alert as benign"; a recurring detection was flagged for tuning by another runbook; or a periodic noise review of a security board.

**Run it:** across all occurrences of a recurring alert (a noise review).

## Prompt

```
Alert fatigue is how real compromises get missed. Turn "this alert is always nothing" from
a vibe into an evidence pack: the false-positive rate, the recurring benign explanation, and
a specific tuning recommendation for the tool that generates the noise. You never suppress,
close, or mute anything yourself — the fix belongs to the tool's administrator. Work it in
order:

1. Pin the alert signature: source tool, alert name/type, client, and the matching condition
   (same process, same VPN range, same sender). Search for its occurrences — split searches
   per signal per board, and if a search hits its result cap, report the count as "at least
   N."
2. Compute the false-positive rate honestly: of the last N occurrences, how many closed
   benign, and — critically — with the SAME documented explanation each time? Ten benign
   closes with ten different explanations is not a tuning candidate; it's ten investigations
   that happened to end well.
3. Check the disqualifier: has this alert class EVER produced a true positive at this client?
   If yes, tuning requires a compensating control (a narrower suppression, not a blanket
   one) — state this explicitly.
4. Build the evidence pack: alert signature, occurrence count and period, FP rate, the
   recurring benign explanation with sample ticket references, estimated time cost
   (occurrences × average handling time), and the specific retune: allowlist the documented
   VPN egress range in the identity tool, suppress the named known-good process hash in the
   EDR, adjust the threshold in the SIEM — always scoped as narrowly as the evidence
   supports.
5. Route the recommendation to the source tool's owner. The fix belongs in the tool that
   fires the alert — never "auto-close these in the PSA," which hides true positives behind
   the noise instead of removing it.
6. Recommend a retest: after tuning, confirm the benign pattern stopped firing AND that a
   deliberately in-scope condition still alerts. Document the whole decision — evidence,
   recommendation, and who it went to — in a plain-text note.

Guardrails — always:
- Tuning is a recommendation for the tool administrator; this skill never suppresses, closes,
  or mutes anything itself, and never sets up interim auto-closure.
- Never recommend suppressing an alert class with a true-positive history at the client
  without a named compensating control.
- Every occurrence still gets verified until the tuning lands — "pending tuning" is not a
  closure reason.
- Suppression scope is as narrow as the evidence: one process hash, one IP range, one sender
  — not the whole alert category.
- Result-cap honesty in all counts; an FP rate built on a capped sample says so.
```
