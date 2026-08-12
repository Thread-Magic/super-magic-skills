---
name: Liongard Hyper-V Read
description: Interrogate a client's Hyper-V hosts via Liongard: host and VM inventory, checkpoint sprawl, replica health, and VM placement and power state.
category: Liongard Inspectors
tools: [liongard_environment, liongard_launchpoint, liongard_metric, liongard_query, liongard_detection, liongard_timeline]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Liongard Hyper-V Read

**When to use:** "What VMs run on <client>'s Hyper-V host(s)?", "any old checkpoints?" (the top silent disk-eater), "is their Hyper-V replication healthy?", a host disk-space incident, or "what changed on the host?".

**Run it:** on one client — name the client and the Hyper-V question.

## Prompt

```
Read Hyper-V estate state for CLIENT_NAME from the Liongard inspector. Read-only — never delete checkpoints, alter replication, or move VMs.

1. Resolve the client's environment, then find the Hyper-V inspector — if none, check for a Windows Server inspector on the known host, whose data may carry the Hyper-V role. Confirm it ran recently — carry "as of <timestamp>." Clusters: one inspector per node is common — enumerate nodes before summing VMs (clustered VMs appear on their current owner); state which nodes you covered.
2. Read the values from the latest dataprint for the angle you need, verifying every field angle against the live dataprint (schemas vary by inspector version):
   - VM inventory: name, state, host, storage path — the placement map; VHDX paths on the system volume are a flag on their own.
   - Checkpoints: VMs with checkpoints + age — flag >72h old and any deep chains; backup products create transient checkpoints, so a young checkpoint during the backup window is normal — when unsure, say "review — may be backup-managed." Checkpoint deletion merges disks and needs free space + IO headroom — flag that when recommending cleanup on a stressed host.
   - Replication: replica-enabled VMs with health state — anything not "Normal" is a finding; also flag VMs the client believes are replicated but show no replica config. "Normal" in a day-old data read is not "healthy right now" — on DR-critical questions recommend a live check.
   - Host: OS version + Hyper-V role — feed EOL-OS concerns to the Windows Server read.
3. "What changed?" → check what changed: VM adds/removals, checkpoint creation, replication-state transitions ordered against the incident window (time-adjacency, not proven cause).
4. Output: inventory table, checkpoint findings, replication-health table, flags with severity, source + data age. Offer to leave a plain-text note. Degradation: no inspector covers the host → documentation → ticket history.
```
