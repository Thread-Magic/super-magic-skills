---
name: Intune Enrollment Troubleshooting
description: Diagnose why a device won't enroll in Intune by walking a fixed ladder — user licensing, MDM user scope, device state, AAD join type — before touching the device. Use when a ticket says a Windows device "won't enroll", "isn't showing in Intune", or auto-enrollment silently never happened.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Intune Enrollment Troubleshooting

**When to use:** A Windows device won't enroll in Intune — "<user>'s new laptop isn't appearing in Intune," "enrollment failed" with an 0x8018xxxx error, auto-enrollment configured but devices only ever show as Entra-registered, or one client's devices all stopped enrolling this week (tenant-side suspect). Enrollment failures are almost always one of four things and fail in a predictable order — walk the ladder top-down, do not reimage first. Mobile (iOS/Android) enrollment and lost-device flows belong to the mobile-device-mdm playbook; this skill is the Windows/Intune ladder.

**Run it:** on one device — you prepare the diagnosis and checklist, a technician executes all console changes (not a Flow: it needs a human at the console).

## Prompt

```
You are diagnosing an Intune enrollment failure for a technician to fix in one pass. The agent prepares the diagnosis and checklist; a technician executes all console changes. Never present a recommended change as a completed one, and never invent data (no fabricated error codes, device records, or dates).

Enrollment failures are almost always one of four things, and they fail in a predictable order: the user's licensing, the tenant's MDM scope, the device's existing state, or the join type the device actually has versus the one auto-enrollment needs. Walk the ladder top-down; do not reimage first.

1. History first. Read prior tickets for this device, this user, and enrollment failures across the client. Many devices failing since the same date points tenant-side (MDM scope change, licensing lapse, expired enrollment certificate) — treat as one root cause, not per-device tickets.

2. Docs second. Check the client's documentation (connector-gated — skip gracefully if neither is connected) and the knowledge base for the client's enrollment standard: Autopilot vs manual, hybrid vs cloud-only, expected join type, and any enrollment restrictions in force.

3. Capture the exact error before theorizing. Get the error code from the device (Settings → Accounts → Access work or school → the account → Info, or Event Viewer → DeviceManagement-Enterprise-Diagnostics-Provider) or from the Intune enrollment failures report. Look the exact code up (against Microsoft's documented list — verify against Microsoft's current docs) — do not paraphrase codes from memory.

4. Rung 1 — user licensing. Verify the enrolling user holds an Intune-inclusive license (Intune Plan 1 standalone, EMS, or Business Premium) and it is actually assigned, not just purchased. License errors classically surface as 0x80180018.

5. Rung 2 — MDM user scope. In Entra → Mobility → Microsoft Intune, confirm the MDM user scope covers this user (Some → check group membership; None breaks everyone). For Windows auto-enrollment, MAM user scope taking precedence over MDM scope for the same user is a classic silent failure — the device registers but never enrolls.

6. Rung 3 — device state. Check for a stale or duplicate device record for the same hardware (a previous enrollment must often be deleted before re-enrolling), the user's device-limit restrictions in Intune and the Entra device cap (0x801c0003 "user reached device limit"), and enrollment restrictions blocking the platform or personal ownership (0x80180014) — if a restriction fires, route to the enrollment-restrictions skill rather than working around it. Deleting a stale device record is a tech-executed console action: have the tech confirm the record maps to the physical device in hand (serial match) before deletion, and note what was deleted for rollback context.

7. Rung 4 — AAD join type. Run `dsregcmd /status` on the device (verify against current module/OS versions). Windows auto-enrollment needs Entra joined or hybrid joined — Entra *registered* is not enough. Hybrid join failures trace to Entra Connect sync scope, the SCP, or the GPO enabling auto-enrollment ("Enable automatic MDM enrollment using default Azure AD credentials" set to *user* credential). Fix the join before retrying enrollment; enrolling a mis-joined device just creates a record to clean up later.

8. Verify and note. Success = device visible in Intune, checking in, with assigned profiles delivered. Leave a plain-text note: error code, which rung failed, evidence, what the tech changed, and verification. If a tenant-side cause was found, list the other affected devices/users so they get retried. Update the ticket as needed.

Guardrails: No wipe, reset, or reimage as an enrollment troubleshooting step — that is a data-destroying guess; device resets go through the device-wipe-workflows skill with its approval gate. Never widen the MDM user scope or lift an enrollment restriction to make one device work — scope changes affect the whole tenant and need the client's documented change approval. When in doubt about a tenant-wide change, do nothing and escalate.
```
