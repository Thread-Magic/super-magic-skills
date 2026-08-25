---
name: Mac Support
description: The Windows tech's ladder for Mac tickets — keychain prompts, MDM enrollment, TCC app permissions, FileVault — mapping macOS causes vs Windows reflexes.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Mac Support

**When to use:** A Mac user gets endless password prompts after a password change ("keychain" anything), a Mac won't enroll in (or fell out of) MDM / profiles aren't applying, an app can't see the screen/camera/mic/files it needs (screen shares show black, mics "don't work"), or FileVault login/recovery issues — or any Mac ticket where the tech says "these steps are for Windows."

**Run it:** on the one ticket you're working — a tech works the Mac hands-on with the user; not unattended.

## Prompt

```
Mac tickets stall on Windows-native desks because nobody knows where macOS keeps the same
problem. Four issues cover most: keychain, MDM enrollment, TCC, FileVault.

Climb the Troubleshooting Ladder base skill first: past Mac tickets at this client, then the
documented standard — MDM product, supervised via Apple Business Manager or user-enrolled,
identity integration, and where FileVault keys are escrowed (say so if unknown). Get the
exact macOS and app versions: permissions and MDM behavior change materially between
releases, so verify steps against the running version on the web, never invent a menu path,
and translate Windows steps into their real macOS equivalent.

Branch:
a. Keychain — a password changed elsewhere and the Mac now prompts for the old one, or apps
   re-ask endlessly: the login keychain is still encrypted with it. If the user remembers
   it, update the login keychain to match. If not, a new login keychain discards every saved
   password and certificate in the old one — list what's in there (Wi-Fi, mail, app
   credentials) and get explicit acknowledgment of the loss first. Never delete keychain
   files by hand.
b. MDM enrollment — won't enroll, or profiles stopped applying. Check: is the serial
   assigned in Apple Business Manager to the right MDM server; does it show in the MDM
   console (a stale or duplicate record blocks re-enrollment — remove it per the MDM's
   process); can it reach Apple's enrollment endpoints (filtered networks break this).
   Re-enrolling a supervised device usually needs an erase, which destroys data: gate it
   behind explicit acknowledgment and a confirmed backup. Expired tokens and server
   mismatches are the MDM admin's.
c. Permissions (TCC) — an app can't use camera, mic, screen recording or files after an
   update or on a new machine; a remote-support tool showing black is classic. Enable that
   permission for the app in System Settings under Privacy & Security, then quit and
   relaunch it. A greyed-out or resetting toggle is MDM-managed via a PPPC profile: fix it
   in the MDM, don't fight the endpoint.
d. FileVault — stuck at disk unlock, or recovery needed. Check the documented escrow
   (MDM-escrowed recovery key, or the client's key record) before attempting anything. A
   password changed elsewhere may not reach the unlock screen until the local password syncs
   — known behavior; confirm current guidance. With no escrowed key and no working password,
   say plainly recovery is closed: erase and restore from backup. Recovery keys never go in
   notes or email, and no fleet-wide escrow is a client-level risk finding: raise it.

Verify by re-testing the failing action: screen share visible, no prompt storm across a
reboot, profile applied. Note it (PSA Note Discipline base skill): macOS version, branch,
cause, action, what was discarded and must be re-entered, verification.
```
