---
name: LastPass Migration
description: Run a LastPass migration-away: export, import to a new vault, rotate every secret, decommission the account, and handle the breach-history talk with facts.
category: Vendor Runbooks
tools: [search_tickets, search_contacts, search_itglue, search_hudu, search_knowledge_base, add_ticket_note, create_ticket, update_ticket]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# LastPass Migration

**When to use:** A client asks whether they should move off LastPass or references the LastPass breaches; a migration off LastPass to another password manager is being planned or executed; or post-incident credential-rotation planning is needed for a current or former LastPass tenant.

**Run it:** on the migration or advisory ticket.

## Prompt

```
A client is on LastPass, asking about the 2022 security incidents and wanting a plan. Run the
migration-away as a rotation-first project, and equip the desk to discuss the breach history
responsibly. Build on password-manager-rollout for the destination platform's vault structure and
emergency access. You have no console access — export, import, rotation, and decommission are
technician steps you direct and record. Never reproduce credential contents or invent data; when
in doubt do nothing irreversible and escalate.

1. Breach history, facts only. Verify every claim against LastPass's own disclosures before
   repeating it and link those notices rather than reconstructing them; never paraphrase from
   memory into specifics. What is publicly documented: LastPass reported security incidents in
   2022 in which an unauthorized party obtained a copy of customer vault data, some fields
   encrypted and some metadata such as URLs not. Do not invent victim counts or causal claims, do
   not speculate that this client was affected, and do not downplay it. To "were we affected," the
   scoped answer: vault data that existed in the affected window is potentially exposed, so rotate
   it.

2. Frame the decision, don't sell it. The rotation obligation is the fixed point: credentials held
   in LastPass during the incident window are rotate-until-proven-otherwise. Whether the client
   also changes platform is their call — route platform selection to the account manager or vCIO.

3. Run the migration as a rotation project, not a copy-paste:
   - Stand up the destination first (password-manager-rollout) before touching LastPass data.
   - Export from LastPass and import into the destination. The export file is plaintext credential
     material: never attach it to a ticket, hold it only transiently on a controlled machine, and
     delete it after import with evidence.
   - Rotate everything, in priority order: privileged and infrastructure, then shared accounts,
     then reused passwords, then the rest. Verify or add MFA on critical accounts while rotating.
     Migration without rotation is theater — every credential that lived in LastPass is
     compromised until rotated. Track rotation as the completion metric, never "items imported."

4. Decommission LastPass with evidence once import is verified and rotation under way: remove
   users and data, and record it. An abandoned but still-populated tenant is unrotated exposure.

5. In the internal note: posture communicated and links provided, destination structure, rotation
   progress by privilege tier, decommission evidence. Credentials never appear in tickets, notes,
   chat, or your output — locations, counts, and status only. Open a ticket per phase and rotation
   tier.

Without documentation access, the inventory rests on client interviews and the export itself — say
so, and rotate broadly.
```
