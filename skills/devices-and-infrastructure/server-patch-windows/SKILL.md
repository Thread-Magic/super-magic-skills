---
name: Server Patch Windows
description: Plan and verify per-client server patching — map each server to its maintenance window, sequence reboots correctly, and run post-patch verification passes.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, set_ninjaone_device_maintenance, get_ninjaone_device_link, connectwise_rmm_search_devices, connectwise_rmm_get_device, search_itglue, search_hudu, add_ticket_note, create_ticket, schedule_ticket]
connectors: [NinjaOne, ConnectWise RMM, IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Server Patch Windows

**When to use:** "When are <client>'s servers patched?" / building or auditing the window map, planning this month's cycle, or the morning-after "did everything come back?"

**Run it:** across a client's servers, on demand for planning or morning-after verification (not a Flow — it's a cycle-planning/verification pass, not a per-ticket event).

## Prompt

```
Three deliverables: the window map, the reboot sequence, and the morning-after
verification pass. You plan, sequence, gate and verify — this integration cannot trigger
patch deployment or run scripts.

1. WINDOW MAP: from documentation (IT Glue / Hudu), the client's agreed windows and
   blackout constraints (month-end for accounting clients, seasonal freezes); from the
   RMM, the server list with patch status (verify server class in the details; a class
   filter is not evidence). Every server gets a row: window, policy, last patched,
   pending-reboot age. Servers with no assigned window are finding number one.

2. REBOOT SEQUENCE inside each window, by dependency, not alphabetically — infrastructure
   the others need comes back first: virtualization hosts before their guests (host
   reboots are hypervisor-alerts work, usually a separate window), storage/NAS before the
   servers mounting it, databases before the app servers consuming them. Domain
   controllers: NEVER reboot all DCs at once. Patch them serially, verify each is back and
   advertising (logons and DNS answering) before the next, and schedule DCs last so the
   rest patches while authentication stays redundant. Undocumented dependency order is
   labelled inferred and confirmed with a human.

3. PRE-WINDOW PREP: confirm the in-scope servers' backups completed recently (backup tool
   status, or backup-failure-triage) — a failed backup the night before patching is a stop
   signal for that server: no patching unless the client accepts that risk in writing. Put
   the in-scope devices into maintenance mode for the window duration only.

4. VERIFICATION PASS, per server: back online; uptime reflects the reboot (a server that
   "patched" without rebooting when one was required has not finished); no new critical
   alerts; key services running; patch activity shows success, not failure. Then what the
   RMM cannot see — app answering, shares mounted, LOB logins — as a hands-on checklist
   with a deep link into the device, or user confirmation in the morning.

5. EXCEPTIONS: failed patches, missed windows, and pending reboots that never cleared each
   get a ticket with the evidence, not a silent retry next month. End maintenance mode
   explicitly — expired-but-suppressed alerting is how the next incident gets missed.

6. Output the window map or verification report, the sequence with rationale, per-server
   results (pass / fail / unverified) and exception tickets, as a note (apply the PSA Note
   Discipline base skill — plain text, no markdown or emojis). Schedule next cycle's prep
   as a follow-up ticket.

Guardrails: "patched" comes from patch-activity evidence, not the schedule elapsing —
report unverified servers as unverified. With no RMM, produce the map and sequence from
documentation and hand execution to the patching tool's operator; never fabricate patch
status.
```
