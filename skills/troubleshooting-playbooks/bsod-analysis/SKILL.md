---
name: BSOD Analysis
description: Triage Windows blue screens by stop code and faulting module, correlating recent patches, drivers, or hardware to split driver, storage, and RAM causes.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, get_ninjaone_device, get_ninjaone_device_activities, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, NinjaOne]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# BSOD Analysis

**When to use:** "<user>'s PC blue-screened" — once or repeatedly; random reboots that turn out to be crashes (machine restarts overnight); BSODs starting after a patch cycle, driver update, or new peripheral; or multiple machines at one client crashing the same way.

**Run it:** on the one device ticket you're working — a tech drives evidence collection hands-on, not unattended.

## Prompt

```
You are triaging a Windows blue screen. A BSOD hands you its own diagnosis: the stop code and
usually a faulting module.

Climb the Troubleshooting Ladder base skill first: this device's past tickets (a recurring crash
means you're reading prior work) and the same stop code across the client. Multiple machines,
same code, same window, is a shared cause — a patch, a deployed agent or driver — so treat it as
one incident and search the web for the code plus that update before working endpoints one by
one.

Get the code before theorizing: the exact stop code (name and hex) and any named
file or module, from the BSOD photo, Event Viewer's System log BugCheck event, or the minidump.
If the machine rebooted past it, the event log still has it. No stop code, no theory — refuse to
speculate until it is in hand.

Correlate with recent change. Where an RMM is connected, read the device's recent activity for
patches, installs and driver updates in the days before onset, plus OS build and model;
otherwise ask about Windows updates, new peripherals, new security agents, vendor drivers.
Onset-after-change is the strongest signal you get.

Decode the code against Microsoft's documentation on the web — codes mean specific things
(memory corruption, driver IRQL faults, storage or boot device, watchdog timeouts) and a named
module names its owner. Never recite a code's meaning from memory, and never apply generic "run
sfc" folklore before the code is understood.

Branch:

1. Driver-implicated — the code or module names a third-party driver, or onset follows a driver
   update. Roll back or update that driver per the vendor's current guidance. If the vendor's own
   current driver is the defect, only the vendor can fix it — the interim is last-known-good. GPU,
   network, storage-controller and security-agent drivers are the usual suspects.
2. Patch-correlated — a Windows update lands in the window. Look for a documented known issue and
   its remediation. Uninstalling the patch is an interim with a security cost: say so, and flag
   it for re-patching once fixed.
3. Memory or hardware — memory-corruption codes, or codes that vary between crashes. Run a
   memory diagnostic and reseat; pair with the hardware-diagnostics playbook. Varying codes are
   hardware until proven otherwise.
4. Storage or boot — storage-stack codes, inaccessible boot device. Check disk SMART health first
   and any storage driver change; onset after imaging or a storage-mode or firmware change points
   at configuration, not the disk.

One blue screen with no recurrence: document the code and monitor, rather than remediating a
single event. Verification is stability over an agreed window (no BugCheck events for N days),
not one clean boot. Then leave a plain-text internal note (apply the PSA Note Discipline base
skill): stop code, module, change correlation, branch, action, monitoring window.
```
