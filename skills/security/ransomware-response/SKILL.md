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
Defensive runbook for active or suspected ransomware. You direct and document; the tech
executes every console action. Declare Critical on the first credible signal and keep a
timestamped log of every action — insurers, IR counsel and the postmortem run on it.

1. Isolate before investigating. Have the tech network-isolate affected endpoints from the
   EDR or RMM console — host isolation, never power-off, which destroys volatile evidence.
   Enumerate the devices, hand over a deep link for each, and set maintenance mode. No
   isolation feature: physical or switch-level disconnection. Timestamp each.
2. Protect backups next, before scoping: disconnect or lock backup repositories from the
   production network and disable backup credentials any domain account can reach —
   operators target backups first. No restore yet.
3. Scope: hosts with encryption artifacts, shares touched, accounts active on those hosts,
   earliest observed encryption timestamp. Check the preceding weeks of alerts — EDR
   detections, odd sign-ins, disabled tooling; the intrusion predates the
   encryption.
4. Engage per the client's documented IR plan and cyber-insurance carrier: most policies
   require the carrier's approved IR firm to lead, and the wrong responder can void
   coverage. Management makes that call — you package the facts.
5. Verify backups before restoring: test-restore a sample, confirm it predates the earliest
   encryption timestamp, and scan it for the intrusion's artifacts — a backup taken after
   initial compromise restores the attacker with the data.
6. Once the IR lead approves, sequence recovery: reset credentials, privileged first, then
   every exposed account — assume theft; rebuild or clean-restore patient zero and
   confirmed-compromised hosts rather than cleaning in place; restore from the verified-clean
   point; re-admit hosts only after EDR confirms them clean. Preserve the isolated images as
   evidence.
7. Client updates follow the defensive-writing-standard skill — factual, no blame or
   speculation. Each: facts with timestamps, actions taken, what you need, next update time. Say "breach" only after confirmed system-level
   findings and management sign-off; disclosure is management's, counsel's and the client's
   policy's call. Hand the timeline to security-incident-postmortem; the ticket does not
   close at containment.

Never contact or negotiate with the threat actor and never advise on paying — that is IR
counsel's and the insurer's alone; don't open ransom-note links or attacker portals. Nothing
is wiped, reimaged or cleaned up before the IR lead (or management, absent external IR)
approves — evidence outranks tidiness. No RMM: enumeration and maintenance mode are manual —
direct the tech and record it. No documentation system: ask management for the IR plan and
carrier.
```
