---
name: AD Replication Issues
description: Fix Active Directory replication failures using repadmin — GPO version mismatches, password changes not propagating, and event IDs 1311/1388/1988.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# AD Replication Issues

**When to use:** Changes (password resets, new users, group membership) show up on some DCs but not others; replication event IDs like 1311/1388/1988/2042/2087 or "target principal name is incorrect" between DCs; a GPO version mismatch across DCs; or a DC that was restored from backup/snapshot or was offline a long time.

**Run it:** on the one ticket you're working — this is a hands-on diagnosis a tech drives, not something to run unattended.

## Prompt

```
AD replication presents as everything else — stale passwords, missing users at one site,
GPO weirdness, Kerberos errors. Read repadmin output before theorizing; anything destructive
is stop-and-escalate. One DC means no replication problem.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: any recent
DC restore, snapshot revert, P2V or long outage; a reverted VM snapshot is the USN rollback
headline. Documentation: DC and site count, PDC emulator holder, virtualization platform.
Evidence, on any DC: repadmin /replsummary (largest delta, fails per DC), then repadmin
/showrepl on the failing DC for the error per partner and naming context, and dcdiag
/test:replications. Capture every error code exactly.

Before branching, check the largest delta against the tombstone lifetime — verify the
forest's actual value (180 days modern, 60 on some legacy). If the delta nears or exceeds
it, replication is deliberately blocked (error 8614, event 2042) to keep lingering objects
out. Stop. Do NOT set "Allow Replication With Divergent and Corrupt Partner"; it invites
deleted objects back into the forest. Lingering objects already present (events 1388/1988,
error 8606) are the same story: removal runs advisory-mode first, per naming context,
against a clean reference DC. Escalate to the senior AD resource with the delta, both DCs
and the tombstone value.

1. DNS or connectivity (8524 DNS lookup failure, 1722 RPC unavailable) — the benign case.
   Each DC must point at working AD DNS, never public DNS; the failing DC's
   <DSA-GUID>._msdcs.<forest> CNAME must resolve; inter-site ports must be open.

2. Security or Kerberos (8456/8457 rejecting replication, -2146893022 target principal name
   incorrect, event 1388) — usually secure channel or time skew; Kerberos tolerates about
   five minutes. Check time sync first, then events 2103/2095.

3. USN rollback (events 2095/2103, a paused DSA, or 8456/8457 with a restored DC in the
   history) — a DC came back by snapshot or unsupported restore and its partners have seen
   the future. The quarantine is intentional: do NOT clear the pause registry keys or force
   replication. The remedy is demote and repromote — senior work. Identify, freeze, escalate.

4. SYSVOL out of sync while AD replication is clean — that is DFSR (event 2213 dirty
   shutdown, 4012 content frozen past MaxOfflineTimeInDays), not AD. Authoritative versus
   non-authoritative sync decides which DC's SYSVOL wins and can lose data — escalate with
   the event IDs and which copy is current.

Never run metadata cleanup, lingering-object removal, authoritative restores or registry
unblocks from a ticket. Success is repadmin /replsummary at zero fails, deltas in minutes,
and a test change reaching all DCs. Note in plain text (PSA Note Discipline base skill):
symptom, errors verbatim, branch, escalation, verification.
```
