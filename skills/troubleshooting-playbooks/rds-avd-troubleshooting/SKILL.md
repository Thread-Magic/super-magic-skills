---
name: RDS / AVD Troubleshooting
description: Diagnose Remote Desktop Services and Azure Virtual Desktop session issues: connect failures, profile hangs, licensing, black screens, missing printers.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu, Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# RDS / AVD Troubleshooting

**When to use:** A user can't connect to the remote desktop / AVD (error, hang, or immediate disconnect), everyone is disconnected from one host or the whole farm, "No Remote Desktop license servers available" appears, or a session is stuck at "Please wait for the user profile service", black screens, or missing printers/drives in-session.

**Run it:** on the one ticket you're working — a tech works the console hands-on; not unattended.

## Prompt

```
A session-host stack fails in layers — broker or gateway, host assignment, license check,
session creation, profile load, redirections — and one "can't connect" screenshot fits all
six. Place the failure on that ladder first.

Climb the Troubleshooting Ladder base skill first, with these specifics. Establish the
stack: on-prem RDS, AVD host pools, or Windows 365. If Citrix fronts these hosts use
citrix-basics — fixing the Microsoft layer under a Citrix problem wastes the outage.
Documentation: hosts, broker and gateway, profile technology, license server and CAL type; Liongard, where present, gives host and certificate state, dated
(Inspector Read Discipline base skill). For AVD check Azure service health first. Evidence:
the client error, TerminalServices operational logs on the host, AVD agent and stack logs,
FSLogix logs for a profile hang — event IDs verbatim.

1. Can't reach the broker or gateway — nobody connects, timing out before any credential
   prompt. On-prem: the gateway service, certificate expiry (a farm-wide failure on a date
   means check certificate dates first), DNS for the farm name. AVD: hosts unavailable or
   the agent unhealthy.

2. Licensing — the error names licensing, or it is roughly 120 days after a new deployment,
   which is why it worked unlicensed until now. Check the licensing diagnoser: license server reachable, CALs installed, mode right (per-user
   versus per-device mismatch is common). Never clear the client-side GracePeriod registry
   key — a dodge that returns in 120 days. The fix is real CALs in the right mode.

3. One host sick — only its users affected. Check memory, disk, a pending update reboot. Do
   not sign users out to test: set drain mode, let it empty, then investigate. The same
   failure across hosts is an image or GPO problem, not a host.

4. Profile hangs and temporary profiles hand off to roaming-profiles-fslogix. A black
   screen with the profile fine is shell or GPO loopback processing or a stuck appx
   registration — measure how long logon takes, not just whether it completes.

5. Redirections missing in-session — printers, drives, clipboard. Policy or plumbing? Check
   whether GPO or host-pool RDP properties allow it, since disabled redirections are common
   security posture, and whether printing goes via Easy Print or a print-server driver. One
   user means their device, everyone means policy — see printer-troubleshooting.

Never reboot a session host or sign out connected users as a diagnostic step — drain first;
every session is someone's workday. Never change farm-wide RDP or GPO settings for one user.
For AVD platform failures, only Microsoft can act — say so. Success is a fresh session with
profile and redirections, confirmed by the user in-session. Note in plain text (PSA
Note Discipline base skill): stack, rung, event IDs verbatim, action or handoff,
verification.
```
