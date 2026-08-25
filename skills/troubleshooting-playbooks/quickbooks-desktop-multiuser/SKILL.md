---
name: QuickBooks Desktop Multi-User
description: Fix QuickBooks Desktop multi-user errors: H202/H505 hosting, -6000 series company file, stuck locks, via hosting mode and Database Server Manager checks.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# QuickBooks Desktop Multi-User

**When to use:** H202/H505 errors switching to multi-user mode, a -6000,-XXX error opening the company file, "someone else has the file open" / a stuck single-user lock, or one workstation can open the file but others can't (often after an update).

**Run it:** on the one ticket you're working — a tech works it with the user; not unattended.

## Prompt

```
You are working a QuickBooks Desktop multi-user problem. Identify the cause before anyone
touches the .ND or .TLG files. You execute nothing: every step is guidance for the tech or
user.

Climb the Troubleshooting Ladder base skill first: this client's past QuickBooks tickets
(recurring H-series tickets mean a standing misconfiguration, not a new fault), then their
documentation: which machine hosts the file, the path, and the year-version. Confirm
Database Server Manager is installed on the host, and get the year and release from the F2
window: each year uses its own database service and firewall port range, so look that year's
ports up.

H-series versus -6000 is the fork: network or hosting, versus file access or damage.

1. Hosting-mode confusion — more than one machine has Host Multi-User Access enabled. Only
   the file host should host. Check File > Utilities on each. If hosting keeps re-enabling
   itself, suspect an install repair or imaged config; hand it to the endpoint owner.

2. Database Server Manager — H202/H505 with hosting correct. Verify QuickBooksDBxx and
   QBCFMonitorService are running on the host and that Database Server Manager has scanned
   the company-file folder. If the host's IP changed under DHCP the .ND points at a stale
   address: rescan, and make a reservation the durable fix. Services crashing on start are
   an install repair.

3. Firewall or name resolution — the service is up but workstations can't reach it. Test
   that year's ports from a workstation and confirm the host resolves by name. A centrally
   managed firewall means routing the exception to its owner.

4. File integrity (-6000 series) — pair the -6000,-XXX code with Intuit's published meaning;
   look it up, don't guess. Renaming the .ND forces regeneration and clears many access
   errors. The .TLG is the transaction log Intuit uses for data recovery: never delete it,
   rename it only alongside a verified same-day backup, and never touch either file while a
   user has the file open. Verify/Rebuild Data is the vendor's tool for logical damage; if
   it can't fix the file, that is Intuit Data Services territory, and the client's
   accountant should know first.

5. Stuck lock or phantom user — "file is in use" with nobody in it. Confirm all QuickBooks
   processes are closed on every machine including the host, then reopen. Recurring locks
   without stale sessions suggest antivirus scanning the file live: route an exclusion
   through the security owner, never disable AV.

This is accounting data: warn before anything that risks the file during a payroll run or
period close, and schedule disruptive steps after hours. Don't invent error-code meanings or
port numbers.

Verify by opening the file in multi-user mode from a second workstation, then note it (apply
the PSA Note Discipline base skill): error code, branch, host, QB year, and verification.
```
