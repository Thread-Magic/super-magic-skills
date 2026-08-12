---
name: Server Patch Windows
description: Plan and verify per-client server patching — map every server to its agreed maintenance window, sequence reboots correctly (dependencies first, domain controllers last and never together), and run the post-patch verification pass. Use for "when do <client>'s servers patch", planning a patch cycle, or verifying last night's window.
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
Three deliverables around server patching: the window map (which server patches when, per agreement), the reboot sequence (dependencies up in order, both domain controllers never down together), and the morning-after verification pass. This skill plans, sequences, gates, and verifies — this integration cannot trigger patch deployment or run scripts.

1. Build the window map: from documentation (IT Glue / Hudu), the client's agreed maintenance windows and blackout constraints (month-end for accounting clients, seasonal freezes); from the RMM, the actual server list with patch status (verify server class in the details — don't trust a class filter). Every server gets a row: window, patch policy, last patched, pending reboot age. Servers with no assigned window are finding number one.
2. Sequence reboots inside each window by dependency, not alphabetically: infrastructure the others need comes back first (virtualization hosts before their guests — host reboots are hypervisor-alerts territory and often a separate window; storage/NAS before servers mounting it; database servers before the app servers that consume them). Domain controllers: NEVER reboot all DCs simultaneously — patch serially, verify each is back and advertising (logons/DNS answering) before the next, and schedule DCs last so everything else patches while authentication stays fully redundant. Where the true dependency order is undocumented, say the order is inferred and get it confirmed.
3. Pre-window prep: confirm backups for the in-scope servers completed recently (via the backup tool's status or backup-failure-triage findings — a failed backup the night before patching is a stop signal for that server), and suppress alert noise deliberately by putting the in-scope devices into maintenance mode for the window duration only.
4. During/after — the verification pass, per server: device back online in the RMM, uptime reflects the reboot (a server that "patched" without rebooting when a reboot was required has not finished), no new critical alerts, key services running, patch activity shows success not failure. Then the service-level checks the RMM cannot see — application answering, shares mounted, LOB app logins — as a hands-on checklist handoff (a deep link into the device in the RMM) or user confirmation in the morning.
5. Exceptions handling: failed patches, servers that missed the window, and pending reboots that never cleared each get a ticket with the evidence, not a silent retry next month. End maintenance mode explicitly — expired-but-suppressed alerting is how the next real incident gets missed.
6. Output: the window map (or verification report), reboot sequence with rationale, per-server verification results (pass / fail / unverified), and exception tickets opened. Leave the plain-text summary as a note (no markdown/emojis); schedule the next cycle's prep as a follow-up ticket.

Guardrails: both/all domain controllers down at once is never acceptable — serial DC patching with verification between is non-negotiable in every sequence. No patching a server whose latest backup failed or is stale unless the client explicitly accepts the risk in writing. Maintenance mode is set for the window and lifted after verification — never left open-ended. "Patched" claims come from patch activity evidence, not from the schedule elapsing — report unverified servers as unverified. Dependency order without documentation backing is labeled inferred. If the RMM integration is absent, produce the window map + sequence from documentation and hand execution to the patching tool's operator; do not fabricate patch status.
```
