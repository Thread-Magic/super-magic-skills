---
name: Troubleshooting Ladder
description: Base skill defining the order every troubleshooting playbook works in — history, documentation, blast radius, versions, verbatim evidence, then branch — and how it closes out.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Troubleshooting Ladder

**When to use:** Working any technical playbook on a ticket, or writing one. It's the shared spine every playbook in this category stands on — the order that stops a tech theorizing before they have evidence.

**Run it:** on the one ticket you're working — a tech drives the hands-on steps; nothing here executes on a device.

## Prompt

```
Most wrong diagnoses come from skipping straight to a theory. Climb these rungs in order,
every time, before you branch on the specific technology.

1. History first. Search this client's past tickets for the same symptom, the same device,
   the same user. A recent identical ticket often holds the whole answer. Several recent
   tickets point at a shared cause — a server, a firmware release, a network change — not
   at this endpoint. Note what changed and when it started; sudden onset on a specific
   date is a change until proven otherwise.

2. Documentation second. Check the client's documentation and knowledge base for how this
   environment is actually built — not how you'd expect it to be. Coverage varies per
   tenant: say plainly what you could not check, and never fill the gap from memory (see
   the Connector Degradation base skill).

3. Scope the blast radius before you diagnose. One user, one device, one site, or
   everyone? Each points at a different layer, and it is the cheapest question you will
   ask. If it's unclear, ask — never assume.

4. Establish versions and design before theorizing. OS build, application version, driver
   or firmware, and which of the possible architectures this client is on. An
   out-of-support version changes what's advisable, so note it. Guessing here wastes the
   next hour.

5. Get the error verbatim. The exact message, code, event ID, or vendor error text —
   from the panel, the log, or the tool output. "It's not working" is not evidence, and a
   paraphrased error is not searchable. Never invent an error code, KB number, or vendor
   link; when a code drives your recommendation, verify its current meaning on the web
   rather than from memory — vendor behavior shifts between releases.

6. Only now, branch. Pick the branch the evidence supports, and say which piece of
   evidence sent you there. If two branches are live, test the cheap discriminator first
   rather than working both.

7. Verify, then note. Success is the failing artifact working again and the user
   confirming it — not a step completed. Say how you verified and when. Then leave an
   internal note: symptom, scope, verbatim evidence, branch taken, action or handoff, and
   the verification (apply the PSA Note Discipline base skill).

Rules that hold on every rung:

- You never execute anything. Every remediation is guidance for a tech or user to run, or
  a deep-link handoff into the RMM. Never claim to have run a script, pushed a driver, or
  executed a remote command.
- Escalate rather than improvise when the fix is owned elsewhere — a vendor defect, a
  firewall change, an ISP, a client decision about data. Say plainly who owns it and hand
  over the evidence.
- Changes with site-wide blast radius are recommendations to the owner, not ad-hoc edits
  from a ticket.
```
