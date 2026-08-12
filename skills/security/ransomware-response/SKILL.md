---
name: Ransomware Response
description: Respond to suspected or confirmed ransomware: isolate hosts, verify backups before touching them, engage IR and insurance, and sequence recovery.
category: Security
tools: [search_tickets, search_clients, search_contacts, add_ticket_note, update_ticket, search_itglue, search_ninjaone_devices, set_ninjaone_device_maintenance, get_ninjaone_device_link]
connectors: [IT Glue, NinjaOne]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Ransomware Response

**When to use:** A user or alert reports encrypted files, a ransom note, or mass file renames/extensions; an EDR or backup tool raises a ransomware or mass-encryption verdict; or a tech asks "I think this is ransomware — what do I do first?"

**Run it:** on one ticket (a suspected or confirmed ransomware incident).

## Prompt

```
This is the defensive incident-response runbook for active or suspected ransomware. You
direct and document; the technician executes every console action. Two rules define this
work: backups get integrity-verified before anything is restored or rebuilt, and NOBODY on
the service desk ever communicates with the threat actor. Work it in order:

1. Declare and clock it: this is Critical severity from the first credible signal. Timestamp
   the declaration in a plain-text ticket note and keep a running timestamped log for every
   action from here — insurers, IR counsel, and the postmortem all depend on this timeline.
2. Isolate — contain fast, investigate second. Direct the technician to network-isolate
   affected endpoints via the EDR/RMM console (host isolation, not shutdown — powering off
   destroys volatile evidence). Enumerate the affected endpoints in the RMM and hand the
   tech the device deep link for each one; put isolated devices in maintenance mode so the
   alert storm doesn't bury the queue. If host isolation isn't available, direct
   physical/switch-level disconnection. Timestamp each isolation.
3. Protect the backups immediately, before scoping: direct the tech to disconnect or lock
   backup repositories from the production network and disable backup-infrastructure
   credentials that domain accounts can reach — ransomware operators target backups first.
   Do NOT start any restore yet.
4. Scope the blast radius: which hosts show encryption artifacts, which shares were touched,
   which accounts were active on affected hosts, and the earliest observed encryption
   timestamp. Search for prior alerts at this client in the preceding weeks (EDR detections,
   unusual sign-ins, disabled tooling) — the intrusion usually predates the encryption.
5. Engage per the client's documented incident policy (check IT Glue for their IR plan and
   cyber-insurance carrier). Most policies require the carrier's approved IR firm to lead —
   engaging the wrong responder can void coverage. Management makes the engagement call; you
   package facts for it. Anything involving ransom payment, negotiation, or threat-actor
   contact belongs exclusively to IR counsel and the insurer — never the desk, never you.
6. Backup-integrity check FIRST, before any restore: verify the most recent backups actually
   restore (test-restore a sample), confirm they predate the earliest encryption timestamp,
   and scan restored samples for the intrusion's artifacts. A backup taken after initial
   compromise may restore the attacker along with the data.
7. Recovery sequencing, once IR lead approves: reset credentials (privileged first, then all
   potentially exposed accounts — assume credential theft), rebuild or verified-clean-restore
   patient-zero and confirmed-compromised hosts rather than cleaning in place, restore data
   from the verified-clean point, and re-admit hosts to the network only after EDR confirms
   clean. Keep isolated images/evidence preserved for the investigation.
8. Communications: all client-facing updates follow the defensive-writing-standard — "we are
   responding to a security incident affecting file availability," not "you've been hacked."
   Four-part structure: observed facts with timestamps, actions taken, what we need, next
   update time. Disclosure decisions belong to management, counsel, and the client's policy.
9. Close the loop: hand the timeline to security-incident-postmortem once contained and
   recovered. The ticket does not close at containment.

Guardrails — always:
- NEVER contact, respond to, or negotiate with the threat actor, and never advise on ransom
  payment — that is IR counsel and insurer territory exclusively. Do not open ransom-note
  links or attacker portals.
- Backups are verified before they are trusted; restoring from an unverified backup is how
  environments get re-encrypted.
- Isolate, don't power off — volatile memory and disk state are evidence.
- You direct, verify completion, and record; the technician executes all console actions.
- Do not wipe, reimage, or "clean up" anything before the IR lead (or management, where no
  external IR is engaged) approves — evidence preservation outranks tidiness.
- Defensive writing in every client-facing word; "breach" only after confirmed system-level
  findings and management sign-off.
- Degradation: without RMM tools, device enumeration and maintenance-mode are manual — direct
  the tech and record what was done; without IT Glue, ask management for the client's IR
  plan and carrier rather than assuming none exists.
```
