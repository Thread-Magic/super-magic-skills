---
name: PaperCut / PrinterLogic
description: Diagnose PaperCut and PrinterLogic print-management issues: release stations, driver deployment failures, and quota/account problems from platform logs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# PaperCut / PrinterLogic

**When to use:** Held/secure-release jobs won't release at a release station or via the app/card reader; a printer won't deploy to workstations (PrinterLogic self-service / PaperCut Print Deploy) or the wrong driver installs; users blocked by quota/balance, wrong account charged, or accounting not recording jobs; or the management client/agent isn't connecting to the server / the print provider went offline. A pure spooler, driver, or hardware fault with no management layer involved belongs to printer-troubleshooting.

**Run it:** on the one ticket you're working — a tech works the platform console hands-on; not unattended.

## Prompt

```
You are diagnosing a print-management platform — PaperCut, PrinterLogic or similar. Work
from the platform's own logs and deployment state, not the raw spooler. A fault with no
management layer involved belongs to printer-troubleshooting.

Climb the Troubleshooting Ladder base skill first, with these specifics. History: a platform
upgrade, a print-server or driver change, a card-reader change, or a Windows print-spooler
security update — those repeatedly broke third-party deployment, so check patch dates.
Documentation: platform and version, the deployment model (on-prem PaperCut with secondary
print servers; PrinterLogic SaaS or on-prem with its agent), the workstation client, release
hardware, and identity mapping. Evidence: the platform's logs (PaperCut's
App Log and print-provider log; PrinterLogic's admin portal and client logs), the job's
status there, agent check-in, and the deployment assignment. Confirm the spooler itself is
healthy — nothing releases through a dead spooler.

1. Release station / secure release — a held job never releases. Check the job reached the
   server and is held rather than failing at submit, and that the station, app or card
   reader is online, mapped to the right printer, and authenticating the user. A dead reader
   is a hardware and vendor path, not a queue fault.

2. Deployment / driver push — a printer won't deploy or installs a broken driver. Confirm
   the client agent is connected, the printer is assigned to that user, group or OU, and the
   driver package is valid for the OS. Type-3 versus Type-4 drivers and point-and-print
   policy changes frequently underlie "won't install". After a Windows print-security update
   the fix is the vendor's compatible client version — never roll back the patch.

3. Quota / accounting — a user is blocked or the wrong account is charged. Read the quota
   rules and the job's charged account. Wrong-account charging is usually identity mapping
   (a shared workstation, a generic login) or a cost-center rule. Balances are the client's
   money: confirm with the account owner first, and never zero quota to unblock someone.

4. Provider or agent offline — nothing works for a site or everyone. The print provider
   service or the PrinterLogic agent lost its connection, a secondary print server is down,
   or a firewall or certificate change broke the client-server channel. Check it first; it
   masquerades as many separate failures.

Restarting the spooler or print-provider service disrupts everyone printing — flag it and
prefer off-hours. Card-reader mappings tie to people: refer to users by placeholder, keep
identity mappings out of PSA notes. Success is end to end: release a real job, deploy to a
test user, or confirm the correct account charged. Note in plain text (PSA Note Discipline
base skill): platform and version, layer, log evidence, branch, action, verification.
```
