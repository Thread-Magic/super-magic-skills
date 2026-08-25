---
name: App Protection Policies
description: Configure Intune MAM-without-enrollment app protection for BYOD to protect org data in managed apps without managing the personal device.
category: M365 Administration
tools: [search_tickets, search_knowledge_base, add_ticket_note, update_ticket, send_approval, schedule_ticket, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# App Protection Policies

**When to use:** A ticket asks to protect company email on personal phones where users refuse MDM, to set up a MAM policy, or to answer "if <user> leaves, can we remove company data from their personal phone?" or "what can the company actually see on my phone?" Also when a BYOD population is created by a personal-device enrollment block (see enrollment-restrictions). App protection (MAM-WE) draws a container around org data inside managed apps on a device the MSP does not manage — its adoption succeeds or fails on one honest sentence to users: "the company can see and wipe its data in work apps — not your photos, messages, or location." This skill configures the container and delivers that sentence.

**Run it:** on one client's request — you scope, design the policy, and write the comms, a technician runs it in the Intune console (not a Flow: it needs a human at the console).

## Prompt

```
Prepare an app-protection (MAM-WE) rollout. You scope, design the policy and write the comms
and rollback; the tech drives the Intune console. Verify current platform behavior against
vendor docs, not memory.

1. Scope and licensing. Confirm Intune licensing covers the target users and identify the BYOD
   population and platforms. Check the client's documentation and the knowledge base for their
   BYOD stance and any existing MAM policy to extend; note it if IT Glue or Hudu isn't
   connected (Connector Degradation base skill).

2. Be precise in every artifact. It protects org data inside policy-managed apps (Outlook,
   Teams, OneDrive, Office): PIN or biometric to open them, encryption, cut/copy/paste and
   save-as limits to unmanaged apps, selective wipe of org data only. It does not manage the
   device, see personal apps, photos, texts, browsing or location, patch the OS, protect apps
   outside the policy, or make a compromised device safe. Never describe MAM as "managing" or
   "securing the phone".

3. Design the policy: the managed-app set (start with the Microsoft core apps in use), data
   transfer (org data to policy-managed apps only; decide contact-sync and backup exceptions
   deliberately), access requirements (app PIN, biometric allowed), and conditional launch —
   minimum OS, jailbreak/root block, offline grace period, wipe-on conditions.

4. Enforce the gate or it's optional. Without a Conditional Access policy granting mail and app
   access only to protected apps, users on native mail clients bypass MAM entirely. Plan the
   "require app protection policy" grant alongside, with a report-only soak first, and state
   the effect: native and unsupported mail apps stop working, Outlook becomes the path. Label
   MAM without CA enforcement "optional protection" so the client chooses knowingly.

5. Comms: the app PIN prompt, work data staying in work apps, native mail stopping if CA
   enforces, and step 2's can/cannot list in plain words, accurate for the platforms in
   question.

6. Approval and pilot. Send an approval request to the client authority covering policy
   settings, the CA enforcement decision and its effects, comms, pilot group, and rollback
   (unassign the policy, relax the CA grant — both reversible without touching devices). No
   selective wipe without a destructive-action approval (Write Guardrails base skill). Pilot on
   real personal devices across platforms; verify the blocks and that daily flows survive
   before broadening.

7. Offboarding tie-in: a departing BYOD user gets a selective wipe of org data. Wire it into
   the client's offboarding checklist and record it in their documentation. Leave a plain-text
   note, no markdown or emojis (PSA Note Discipline base skill), with what, why, when and
   rollback.

When in doubt about privacy accuracy or CA enforcement scope, do nothing and escalate.
```
