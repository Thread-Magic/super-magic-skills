---
name: Hyper-V Clustering
description: Troubleshoot Hyper-V failover clusters — quorum loss, CSV redirected or offline, failed live migrations, stuck node drains — from cluster and event logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
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
A failover cluster fails in a few seams: quorum math, Cluster Shared Volume access, the
live-migration path, and the storage under CSV. Read the cluster's own evidence before
anyone moves a role.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: a recent
patch (clustering is sensitive to mixed build levels during CAU), a storage, firmware or
networking change. Documentation: node count (it drives quorum, so establish it
first), Windows Server build, witness type — disk, file share or cloud — the storage
backend, CSV layout, and the migration network. Liongard, where present, gives node and
cluster state, dated (Inspector Read Discipline base skill).
Evidence: node, role and resource states (Get-ClusterNode, Get-ClusterGroup,
Get-ClusterResource), CSV states, quorum and votes (Get-ClusterQuorum, DynamicWeight), the
cluster log, and System and FailoverClustering events.

1. Quorum loss or the cluster won't form — count votes: nodes plus witness must exceed half.
   A lost witness with an even split, or too many nodes down, drops it below quorum and it
   stops on purpose. Restore the missing votes rather than forcing. Start-ClusterNode
   -FixQuorum is a last resort that can cause split-brain: use it only when you know which
   partition holds the authoritative data, and escalate that decision.

2. CSV redirected or offline — Redirected Access means IO routes over the network to the
   coordinator node instead of direct: often a backup snapshot in progress, a storage-path
   loss on one node, or antivirus scanning the CSV. Confirm no backup job is running before
   treating a redirect as a fault. No Access or offline is a real connectivity or
   reservation problem — check MPIO, iSCSI and HBA paths per node. SAN and fabric faults
   are the storage owner's and the vendor's.

3. Live-migration failures — read the exact error: authentication or delegation (CredSSP or
   Kerberos constrained delegation), a migration-network problem, insufficient memory or
   NUMA on the target, or a processor-compatibility mismatch. A failed migration usually
   leaves the VM on the source — verify before retrying.

4. A drain or pause that won't complete — a role won't move: anti-affinity, a resource that
   won't come online elsewhere, misconfigured possible owners, or a VM pending. Read which
   role blocks it and why. Never force-stop a node mid-drain to get patching moving;
   that can hard-stop VMs.

Don't fail over or restart nodes during a storage event — stabilize storage first. Success is the cluster's own report: all nodes Up, roles Online on intended owners,
CSVs in direct access, quorum healthy, and a clean test migration if that was the fault.
Cluster Validation reports a config problem, it does not fix one. Note in plain text (PSA
Note Discipline base skill): build, quorum state, evidence, branch, action, verification.
```
