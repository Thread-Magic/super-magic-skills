---
name: Hyper-V Clustering
description: Work Hyper-V failover cluster problems — quorum loss, CSV going redirected or offline, live-migration failures, node drain/pause not completing — from cluster and event evidence, never by failing VMs over blindly.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, Liongard, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Hyper-V Clustering

**When to use:** "The cluster is down" or a node is paused, down, or isolated; a CSV shows Redirected Access, No Access, or a volume dropped offline; live migration or quick migration fails or hangs and VMs won't move off a node; or draining/pausing a node for patching won't complete, or roles won't come online after a failover.

**Run it:** on the one ticket you're working — a tech with cluster-admin access drives this; not unattended.

## Prompt

```
A failover cluster fails in a few predictable seams: quorum math, Cluster Shared Volume access, the live-migration/network path, and storage under CSV. Read the cluster's own evidence (Failover Cluster Manager, cluster log, validation report) before anyone moves a role — because a blind failover during a storage blip can cascade the whole cluster.

Work it in this order:

1. Topology and version first. Check the client's documentation and knowledge base for the cluster design: node count, Windows Server version/build, witness type (disk / file-share / cloud), the shared-storage backend (SAN/iSCSI/S2D), CSV layout, and the migration network. Node count drives quorum behaviour, so establish it before reasoning about who has votes. If a Liongard Hyper-V/Windows inspector runs, read node/cluster state from its inspector data and note the dataprint age. Documentation and Liongard coverage varies per tenant — note what you couldn't check and any dataprint age.

2. History first. Search this client's past tickets for cluster work: a recent patch (clustering is sensitive to mixed build levels during CAU), a storage/firmware change, a networking change, or a prior identical event. Sudden onset after maintenance points at what changed, not at a spontaneous fault.

3. Get the cluster's evidence before acting. From Failover Cluster Manager and PowerShell (guidance for the tech): node/role/resource states (Get-ClusterNode, Get-ClusterGroup, Get-ClusterResource), the CSV states, current quorum config and vote assignment (Get-ClusterQuorum, node DynamicWeight), and the cluster log / System + FailoverClustering event logs around the incident. Read the actual failure reason — don't proceed on "it failed over".

4. Branch:
   - Quorum loss / cluster won't form — count votes: nodes plus witness must exceed half. A lost witness plus an even split, or too many nodes down, drops the cluster below quorum and it stops on purpose. Fix by restoring the missing votes (bring the witness/node back), not by force — Start-ClusterNode -FixQuorum (force quorum) is a last-resort recovery that can cause a split-brain/partition-in-time; use it only when you understand which partition has the authoritative data. Escalate when the witness is on infrastructure owned elsewhere or force-quorum is on the table — that's a data-integrity decision.
   - CSV redirected / offline — Redirected Access means IO is routing over the network to the coordinator node instead of direct — often a backup snapshot in progress, a storage-path loss on one node, or antivirus scanning the CSV. Check each node's path to the storage and the CSV coordinator; confirm the backup isn't mid-job before "fixing" a redirect that's expected. No Access/offline = a real storage-connectivity or reservation problem — check MPIO/iSCSI/HBA paths per node. Escalate when the fault is in the SAN/fabric — that's the storage owner, and pair with the storage vendor.
   - Live-migration failures — read the exact error: authentication/delegation (CredSSP/Kerberos constrained delegation misconfigured), a migration-network problem, insufficient memory/NUMA on the target, or version/CPU-compatibility mismatch between nodes. Live migration needs a healthy dedicated network and matching processor compatibility settings; a failed migration usually leaves the VM safely on the source — verify that before retrying.
   - Node drain / pause won't complete — a role won't move (anti-affinity, a resource that won't come online on any other node, or possible-owners misconfigured) or a VM has a pending state. Read which role is blocking the drain and why it won't start elsewhere. Don't force-stop a node mid-drain to "get patching moving" — that can hard-stop VMs; resolve the blocking role first.

Guardrails to hold throughout: no remote execution — all cluster PowerShell and Failover Cluster Manager steps are guidance for a tech with cluster-admin access; when the RMM integration is connected, open a node in the RMM (a deep link for the tech, not script execution) to hand the tech onto it, otherwise ask them to reach it manually. Never force quorum (-FixQuorum / -ForceQuorum) casually — it can create a split-brain and lose writes; use only with a clear understanding of which partition is authoritative, and escalate the decision. Don't fail over or restart nodes as a first move during a storage event — a blind failover while storage is flaky can cascade; stabilize storage first. CSV Redirected Access during a backup window is often normal — confirm no job is running before treating a redirect as a fault. Storage-fabric, SAN, and firmware faults are the storage owner's and the vendor's — package the evidence, don't improvise on the array. Do not invent event IDs, cmdlet syntax, or version behaviours — Hyper-V/clustering changes by Windows Server version; look it up on the web and cite.

Verify and note. Success is the cluster's own report: all nodes Up, roles Online on intended owners, CSVs in direct (not redirected) access, quorum healthy, and a clean test migration if migration was the fault. Run Cluster Validation for a config problem (report, not a fix). Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): version/build, witness/quorum state, the evidence, branch, action or handoff, verification.
```
