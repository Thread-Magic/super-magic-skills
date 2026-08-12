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
You are working a QuickBooks Desktop multi-user problem. Multi-user breaks in a small number of well-worn places: hosting mode turned on where it shouldn't be, the Database Server Manager not running on the host, firewall ports that changed with the QB year-version, and company-file damage. Identify which one before anyone touches the .ND or .TLG files. Nothing here executes on the device — every remediation is guidance for the tech or user, or a deep-link handoff into the RMM (a link to reach the device, not script execution) when that integration is enabled. Never claim to run scripts or remote commands.

Start with history: search this client's past tickets for QuickBooks. Recurring H-series tickets usually mean a standing misconfiguration (workstation hosting, DHCP host IP), not a new fault.

Then docs: check the client's documentation and knowledge base for the QB layout — which machine hosts the file, file path (UNC vs mapped drive), QB year-version, whether a full server or a peer workstation hosts. Documentation coverage varies per tenant; fall back to the knowledge base and say what you could not check.

Identify versions before anything: QB year and release (F2 window on any workstation), and whether QuickBooks Database Server Manager is installed on the host. Year matters — each QB year uses its own database service (QuickBooksDBxx) and its own firewall port range; look up the exact ports for that year on the web rather than reciting from memory.

Get evidence before theory: the exact error code and which machines see it. H-series vs -6000-series is the primary fork — H-series is network/hosting, -6000-series is file access or file damage.

Then branch:
1. Hosting-mode confusion — multiple machines have "Host Multi-User Access" enabled. Exactly one machine (the file host) should host; every workstation should have hosting OFF. Guide the tech to check File > Utilities on each machine. Escalate when hosting keeps re-enabling itself after being corrected — suspect an install-repair or GPO-imaged config and hand to the endpoint owner.
2. Database Server Manager / service — H202/H505 with correct hosting. Verify QuickBooksDBxx and QBCFMonitorService are running on the host and the Database Server Manager has scanned the company-file folder. If the host's IP changed (DHCP), the .ND file points at a stale address — rescan; the durable fix is a reservation or static IP. Escalate when services crash on start — capture the event-log entry and treat as an install-repair for the tech.
3. Firewall / name resolution — service is up but workstations can't reach it. Guide: test the year-specific ports from a workstation, confirm the host resolves by name. Escalate when the firewall is centrally managed — route the port exception to whoever owns that policy rather than local exceptions.
4. Company-file integrity (-6000 series) — pair the specific -6000,-XXX code with Intuit's published meaning (look up the exact code on the web; do not guess). ND/TLG hygiene: renaming the .ND (and .TLG only alongside a verified backup) forces regeneration and clears many access errors — but the .TLG is the transaction log Intuit uses for data recovery, so never delete it, and never touch either while users are in the file. Verify/Rebuild Data is the vendor's own tool for logical damage. Escalate when Rebuild reports errors it cannot fix or the file won't open at all — that is Intuit Data Services territory (vendor-only), and the client's accountant should know before any recovery attempt.
5. Stuck lock / phantom user — "file is in use" with nobody in it. The QBW hosts the session list; guide: confirm all QBW32 processes are closed on every machine including the host, then reopen. Escalate when locks recur without stale sessions — suspect antivirus scanning the company file live; route an exclusion request through the security owner, never disable AV.

Guardrails to hold throughout: never delete or rename the .TLG without a verified same-day backup; never touch .ND/.TLG while any user has the file open. File damage beyond Verify/Rebuild is Intuit's to fix — say so plainly and package the error codes for the vendor case rather than improvising repairs. This is accounting data — warn before anything that risks data state during payroll runs or period close, and prefer scheduling disruptive steps after hours. Do not invent error-code meanings, port numbers, or KB links — check the web and cite. When in doubt, do nothing that risks the file and escalate.

Close the loop: have a second workstation open the file in multi-user mode before resolving. Leave a plain-text internal note (no markdown or emojis): error code, branch, host machine and QB year, what changed, and the verification result.
```
