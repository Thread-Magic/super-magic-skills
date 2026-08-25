---
name: SQL Server Performance
description: Diagnose SQL Server slowness: blocking, deadlocks, missing indexes, stale statistics, tempdb contention, and parameter sniffing via live wait stats.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# SQL Server Performance

**When to use:** "The database / <LOB app> got slow this morning" or intermittent hangs; reports, saved queries, or a specific screen time out, or deadlock-victim errors (error 1205); "blocking" complaints where one user's action freezes others; or tempdb full, log file growth, or CPU pegged on the SQL host.

**Run it:** on the one ticket you're working — a DBA/tech works it hands-on; not unattended.

## Prompt

```
"SQL is slow" is a symptom: find the bottleneck from wait statistics and the specific slow
query before anyone adds an index or restarts a service.

Climb the Troubleshooting Ladder base skill first: documentation for version and edition
(Express's 10 GB, 1 GB RAM, one-socket ceiling alone explains many "slow" cases); then
past tickets, since a month-end pattern or a recent app upgrade reframes everything. Scope
forks it: whole instance, one query, or one user blocking others. Then measure — blocking
chains from sys.dm_exec_requests and sys.dm_os_waiting_tasks, aggregate waits from
sys.dm_os_wait_stats, costly statements from sys.dm_exec_query_stats, and the actual
execution plan for a slow query, never the estimated.

1. Blocking and deadlocks — find the head of the chain, not a victim. One uncommitted
   transaction blocks everyone behind it, so the fix is that transaction, not killing
   sessions. For repeating deadlocks read the graph from extended events or system_health.
   Escalate when the head blocker or the deadlock sits in vendor code.

2. Missing indexes and stale statistics — large scans, or a big estimated-versus-actual
   row skew. UPDATE STATISTICS is low risk and often the fastest win; a new index is a
   schema change with write cost, frequently unsupported on a vendor database.
   Missing-index DMV hints are candidates, never a script to bulk-apply.

3. tempdb contention — PAGELATCH waits on tempdb allocation pages, or tempdb full. Check
   file count, sizing and autogrowth, and what is spilling: bad-plan sorts and hashes, or
   the version store from long transactions. Fixing the query beats resizing.

4. Parameter sniffing — fast for some inputs, slow for others; compare the cached plan
   with the actual. The honest fixes (OPTION RECOMPILE, plan guides, query changes) belong
   with the app owner or vendor, and a blanket DBCC FREEPROCCACHE is never a first move.

5. Resource pressure — SOS_SCHEDULER_YIELD, RESOURCE_SEMAPHORE or PAGEIOLATCH waits plus
   host metrics. Check Max Server Memory is set (unbounded starves the OS), the host isn't
   swapping, storage latency is sane, and no backup collides with the workday. Escalate
   host and storage sizing as infrastructure, not a query fix.

Vendor-database caution is the headline rule: on a line-of-business database, new indexes,
statistics changes, query edits or schema changes can break vendor support and the app.
Read freely; before any write get the vendor's blessing or the client's explicit
acceptance. Never run DBCC FREEPROCCACHE, kill sessions, shrink files or drop and create
indexes on production as a reflex — state the impact and get sign-off. Log growth belongs
to sql-backup-maintenance.

Note it (apply the PSA Note Discipline base skill): version and edition, scope, measured
bottleneck, branch, action or handoff, and verification by the same measurement that found
it.
```
