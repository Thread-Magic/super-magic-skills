---
name: Difficult News Delivery
description: Draft the message no one wants to send — data loss, unrecoverable state, security exposure — factual, empathetic, and pointed at the path forward.
category: Communication
tools: [search_tickets, view_openDraft]
connectors: []
scope: single
flow: no
role: [Technician, CSM / Account Manager]
outcome: [Risk & Compliance, Retention & Growth (CSAT/Expansion)]
---

# Difficult News Delivery

**When to use:** "The backups don't cover it — the data is gone, help me tell the client" / "we have to tell them their mailbox was exposed / the drive is unrecoverable" — any message delivering a confirmed, materially bad outcome.

**Run it:** on one ticket.

## Prompt

```
Draft the message announcing that something is lost, exposed, or not coming back — clear and
honest, without a word that makes a bad situation legally or emotionally worse.

1. Verify with me that the bad outcome is CONFIRMED — recovery genuinely exhausted, exposure
   genuinely established. This message is irreversible in effect; if any avenue is still open,
   the honest email is a status update, not this one.

2. Confirm who should deliver it and how. News of this weight often warrants a call first with
   the email as the written follow-up — recommend that, and check whether management or the
   account manager must review before anything is sent. For confirmed security incidents,
   incident-response or legal language governs — if such requirements exist, they win.

3. Draft with defensive-writing rules at maximum:
   - The news, early and plainly: "I have difficult news about <the data/system>." Then the
     fact, stated exactly — what is lost or exposed, and the confirmed scope. Precision is
     kindness: "the files created between <date> and <date> on <share>" beats "some data."
   - What was done — the recovery/containment attempts, factually.
   - Empathy — one genuine beat acknowledging what this means for them, without melodrama.
   - The path forward — concrete next steps: what can be reconstructed, what protective
     actions to take (password resets, monitoring), what the desk does next, and when they'll
     hear from us. The email must end in motion.

4. Scrub the draft: no "breach," "hacked," "negligence," "our fault," "catastrophic," and no
   guarantees ("this will never happen again"). For exposure: "unauthorized access to X was
   confirmed" — exactly what is known, nothing more. Never soften into falsehood ("some data
   may be affected" when loss is confirmed) or imply recovery hope that doesn't exist.

5. Show me the draft with an explicit "review with your manager before sending" recommendation,
   labeled "SENSITIVE DRAFT — manager review required."

State only what is confirmed — never speculate on cause, fault, or blame. No compensation,
remediation-cost, or contractual statements. This draft ALWAYS gets human review — never send
autonomously under any configuration.
```
