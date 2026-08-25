---
name: Scanner & Copier Fleet
description: Fix MFP and copier scan-to-folder failures after SMB or credential changes, address-book cleanup, firmware quirks, and panel errors on leased fleets.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Scanner & Copier Fleet

**When to use:** Scan-to-folder stopped working (often the whole office, often right after a password change or server work), the copier can't reach the share after a migration or security hardening, address-book entries are wrong/missing or need bulk changes, or there are panel error codes / firmware weirdness / "the copier company says it's a network problem".

**Run it:** on the one ticket you're working — a tech works the admin panel and lease-vendor handoff; not unattended.

## Prompt

```
Copiers hold a service-account password someone eventually rotates, speak SMB dialects
servers deprecate, and run firmware nobody updates until scanning breaks. For the print path
and scan-to-email, use the Printer Troubleshooting playbook instead.

Name the boundary early: hardware, consumables, jams and usually firmware are the lease
vendor's; network, credentials, shares and DNS are the desk's.

Climb the Troubleshooting Ladder base skill first: past tickets for this copier, since
scan-to-folder failures cluster after a password rotation, an SMB1 disablement or a server
migration; then the documented fleet profile — models and firmware, the scan service
account, destination share paths, the lease vendor's contract scope, panel access details.
Get the copier's own error (panel message, send log, or a code looked up for the exact
model), the scope — one destination, all, or all copiers — and the SMB dialect the server
accepts.

Branch:
1. Authentication — every destination dies at once after a credential change. The copier's
   embedded SMB service account was rotated or disabled in a cleanup: confirm its state,
   then update the stored credential in the panel. The durable fix is a documented
   least-privilege account policy won't silently expire; flag collisions to whoever owns
   identity. Scanning as individual users is a design change, not a fix: escalate.
2. SMB version — scans fail after server hardening or a migration, credentials good.
   Firmware capped at SMB1 leaves two honest options: a vendor firmware update (the lease
   vendor's job) or an intermediary path the client accepts. Never re-enable SMB1 as the fix
   — it reopens a known attack surface, and that is the security owner's call, in writing.
3. Destination path — one fails, others work: the share moved, was renamed, or its
   permissions changed. Verify the path exists and the scan account can write, then correct
   the copier's entry. Permission problems underneath go to the File Share Permissions
   playbook.
4. Address book — wrong, missing, or bulk changes. Small edits in the panel; for bulk, use
   the vendor's export/import procedure for the model and save the export to the client's
   documentation first. Directory sync is vendor-specific — the lease vendor rules on it.
5. Firmware quirks and panel errors — reboots, codes, vanished features. Match the code to
   the vendor's published meaning. One mapping to a hardware subsystem goes to the lease
   vendor with model and code; firmware updates on leased devices are theirs.

Never put credentials in a note; reference where they are stored. Touching hardware or
vendor firmware can void the contract. Verify with a real scan to the affected destination,
then note it (PSA Note Discipline base skill): model and firmware, code, branch, what
changed, who owns what's left, verification.
```
