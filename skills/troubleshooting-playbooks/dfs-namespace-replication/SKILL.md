---
name: DFS Namespace and Replication
description: Fix DFS-N referral failures and DFS-R replication backlog, conflicts, and staging-quota issues using health reports and backlog counts, not blind reinit.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# DFS Namespace and Replication

**When to use:** Users open a namespace path and land on the wrong (or a slow/remote) server or get "no target"; files created on one server aren't appearing on another or edits are stale between sites; DFSR reports a large backlog, an error state, or a replicated folder stopped replicating; or conflicts/losses ("ConflictAndDeleted") or the staging area/quota is a bottleneck.

**Run it:** on the one ticket you're working — a tech drives this hands-on at the member servers, not unattended.

## Prompt

```
You are diagnosing a DFS problem. DFS-N (namespaces) decides which target a user is referred
to; DFS-R (replication) gets content between targets — separate them first. Nothing here
executes: these are steps for a tech with the right access.

Climb the Troubleshooting Ladder base skill first: this client's past tickets for DFS and file
shares (a server added or renamed, a bulk migration, a disk-full event, or a dirty shutdown),
then their documentation for the design — namespaces and folder targets, replication groups
and topology, staging-quota sizes, and Windows Server version.

Then get the evidence. DFS-N: the referral list for the path — targets, their order,
enabled/online state, reachability. DFS-R: the backlog count between the specific sending and
receiving members, the health report, and DFSR event-log state (recovery, error,
staging-full).

Branch:

1. DFS-N referral — users hit the wrong, slow, or no target. Check target priority and ordering
   (site cost sends users to their local target), whether a target is disabled or
   offline, and the client's AD site — a client in the wrong site gets wrong referrals. "No
   target" means every target is offline or the folder target was removed.

2. DFS-R backlog — content is stale because changes are queued. Decide draining vs stuck: a
   large migration needs patience and maybe a staging-quota bump; an error state, unreachable
   member, or expired content freshness is stuck. A member offline longer than
   MaxOfflineTimeInDays is stale and needs deliberate recovery — escalate rather than
   re-enabling it, because reconnecting it wrong resurrects deleted files or loses changes.

3. Conflicts — simultaneous edits on two members keep the last writer and move the loser to
   ConflictAndDeleted, recoverable for a time, not forever. Never treat DFSR as two-way sync for actively co-edited files: if the real problem is
   concurrent editing, fix the design (single writable target, per-site folders,
   SharePoint/OneDrive) rather than blaming replication.

4. Staging bottleneck — replication crawls or errors under heavy change because staging is too
   small for the largest files and churn, or its disk is full. Raising the quota is the lever;
   confirm disk space and the churn source first.

Never reinitialize replication or delete the DFSR database as a first move: an authoritative
sync resets one side to the other and loses recent changes on the losing member. Establish
which member is authoritative and get the client's sign-off first. Don't invent command syntax,
event IDs, or offline-limit defaults; check Microsoft's docs and cite.

Verify with a real test: a file created on one member appears on the other, backlog near zero,
a test client referred to its local target. Then note it (apply the PSA Note Discipline base
skill): DFS-N vs DFS-R, evidence, branch, action or handoff, and verification.
```
