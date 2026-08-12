---
name: Liongard Windows Server Read
description: Interrogate a client's Windows Servers through Liongard — installed roles, local admin members, services, patch level, OS version and EOL flags. Use for "what does this server do", local-admin audits, EOL-OS sweeps, or patch-posture checks per server.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard Windows Server Read

**When to use:** Triage lands on a server ("what roles/services does <device> run?"), "who's in local Administrators on <device> / across the fleet?", "any servers still on an end-of-life OS?", "when was <device> last patched?", or "what changed on this server?".

**Run it:** on one client — name the client and the server question (one server or the whole fleet).

## Prompt

```
Read per-server Windows state for CLIENT_NAME from the Liongard Windows inspector. Read-only — never start/stop services or change group membership; service control via RMM is a separate gated workflow.

1. Resolve the client's environment, then find the Windows Server inspectors (one per server) and confirm each ran recently — carry "as of <timestamp>" per server. Fleet sweeps iterate all Windows inspectors — state coverage ("14 of 16 documented servers have working inspectors"); a fleet table mixing ages must show as-of per row or qualify the whole table.
2. Read the values from each server's latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - Identity/EOL: OS caption + build per server — flag versions at or past end of support, labeled "verify against Microsoft lifecycle dates" rather than asserting from memory.
   - Roles: installed roles/features — the "what does this box do" answer (AD DS, DNS, DHCP, IIS, Hyper-V, file services).
   - Local admins: Administrators group members per server — flag unexpected user accounts, per-user counts across the fleet (one account admin on every server is a finding), and non-standard service accounts. Findings are "unrecognized — verify" review inputs, never accusations; some entries are legitimate service accounts.
   - Services: services in a stopped state whose start mode is Automatic — the classic silent-breakage list; also new/unrecognized services.
   - Patch level: latest installed update date/build — servers >60 days behind get flagged. Patch posture from Liongard approximates; the RMM/patch platform is authoritative for compliance claims — say which source answered.
3. "What changed?" → check what changed per server: new local admin, service adds/state changes, role changes ordered against the incident window (time-adjacency, bounded by inspector cadence). An undocumented local-admin addition is a flag even with no incident.
4. Output: per-server or fleet table for the asked angle, flags with severity (EOL OS, unexpected admins, stopped-auto services, stale patching), source + data age per server. Offer to leave a plain-text note. Degradation: servers without inspectors → documentation → ticket history → RMM.
```
