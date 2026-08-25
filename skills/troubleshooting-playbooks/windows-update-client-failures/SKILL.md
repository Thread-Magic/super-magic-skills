---
name: Windows Update Client Failures
description: Diagnose Windows Update client failures: 0x8024xxxx and 0x800Fxxxx errors, update loops and rollbacks, and stuck scans across WU, WSUS, and Intune sources.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Windows Update Client Failures

**When to use:** One machine (or a handful) erroring on updates with an 0x8024xxxx / 0x800Fxxxx / 0xC1900xxx code; an update that installs, reboots, then rolls back ("We couldn't complete the updates"); "checking for updates" hanging, or a machine compliant in one console but stale in another; or RMM patch reports flagging a device repeatedly failing the same KB.

**Run it:** on the one device ticket you're working — a tech works it hands-on; not unattended.

## Prompt

```
Two questions decide most of these tickets: where does this machine think updates come
from, and what is the exact error code. A components reset without both destroys the
evidence.

Climb the Troubleshooting Ladder base skill first: past tickets for this KB and client
(the same KB failing across many machines is a known-bad update or infrastructure —
check the vendor's known-issues page and switch to wsus-patching-infrastructure), then
the documented patch design: WSUS, Intune rings, RMM patching, dual-scan or
co-management.

Then find the update source — never assume. Faster than Get-WindowsUpdateLog:
HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate (WUServer set means WSUS),
dsregcmd /status for Intune enrolment, and the "managed by your organization" banner in
Settings. Source confusion is a first-class root cause — a decommissioned WSUS pointer
never updates and never errors loudly, and a machine holding both WSUS policy and Intune
rings scans the wrong source. Fix the pointing per the documented design, confirmed with
the client's patch owner, before any repair.

Then take the exact code from update history or CBS and decode by family. 0x8024xxxx
(update agent) is usually transport — can't reach the source, WSUS content missing,
proxy or TLS interception; test reachability to the source you found. 0x800F0831 /
0x800F09xx / 0x800F081F (servicing/CBS) is store corruption or a missing servicing
payload — go to the ladder. 0x80070070 family is disk full; check free space first,
feature updates need tens of GB. 0xC1900xxx (feature update/setup) is driver or app
compatibility — read SetupDiag.

Component-store repair ladder, in order:
a. DISM /Online /Cleanup-Image /ScanHealth then /RestoreHealth. On WSUS-managed machines
   RestoreHealth may need /Source or the "repair from Windows Update" policy allowed —
   0x800f081f there is usually source, not corruption.
b. sfc /scannow AFTER DISM — SFC repairs from the store DISM just fixed; first, it would
   repair from a corrupt store.
c. Retry. Only then rename SoftwareDistribution and Catroot2, once: it destroys update
   history and re-downloads everything, so it is never step one.
d. Still failing: an in-place upgrade repair (keeps apps and files).

Rollback loops: name the failing component with SetupDiag (feature updates) or the CBS
log around the reboot (cumulative). Usual causes are a filter driver — AV or backup
agent — or a bad third-party driver. Pausing the specific update while a vendor issue is
confirmed is legitimate; disabling updates wholesale or setting indefinite deferrals to
close a ticket is not — record a re-review date.

Success is the failing KB showing Installed and the client's compliance console
reflecting it after a check-in cycle. Note it (apply the PSA Note Discipline base
skill): update source, verbatim code, ladder steps and results, action, verification.
```
