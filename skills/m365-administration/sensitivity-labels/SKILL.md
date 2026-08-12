---
name: Sensitivity Labels
description: Roll out Microsoft Purview sensitivity labels with a small taxonomy, auto-labeling in simulation, and encryption consequences understood upfront.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# Sensitivity Labels

**When to use:** A client asks to "set up Confidential / Internal / Public document labels," needs data classification for a compliance requirement, wants to "auto-label anything containing card numbers / PHI as Confidential," or wants to "encrypt documents marked Confidential." NOT for the DLP side (blocking sensitive data in transit) — that is purview-dlp-policy; labels classify and can encrypt, DLP prevents movement. This skill treats the rollout as governed, not a big-bang taxonomy: a handful of clear labels, publishing to a pilot before the org, and — above all — treating label encryption as the irreversible, access-breaking decision it is.

**Run it:** on one client's request — you prepare and verify, a technician executes in the Purview portal (not a Flow: it needs a human at the console).

## Prompt

```
You are rolling out Microsoft Purview sensitivity labels as a governed, piloted change. You prepare and verify; the technician executes in the Purview portal. Never invent data — verify the portal surface against current docs.

1. Design a SMALL taxonomy first. Three to five labels people can actually choose correctly beats a fifteen-label tree nobody understands (a common pattern: Public / Internal / Confidential / Highly Confidential). Define each label's meaning in plain client language before building anything — an ambiguous label is applied wrongly and trusted falsely. A misunderstood label is worse than none.

2. Decide per label what it DOES: visual marking only (header/footer/watermark), and/or encryption, and/or container settings (Teams/site/group privacy), and/or endpoint/DLP tie-ins. Keep the first rollout to marking for most labels; reserve encryption for the top tier and treat it as a separate, heavier decision (step 4). Check the client's documented classification standard in the client's documentation if connected; degrade gracefully to plain design if not.

3. Publish to a PILOT, not the tenant. Attach labels to a label policy scoped to a small pilot group first, set whether a default label and mandatory labeling apply, and let people use it before org-wide publish. Mandatory labeling changes everyone's save/send flow — introduce it only after the pilot proves the taxonomy.

4. Encryption is the dangerous part — spell out the consequences before enabling it on any label:
   - Encrypted files carry their protection everywhere; access is enforced by the label's permissions, not the file's location. Wrong permissions = users locked out of their own documents.
   - External sharing of encrypted files requires the recipient to authenticate and be granted rights — it can silently break partner/client workflows.
   - Some services, co-authoring scenarios, and third-party tools handle encrypted files poorly — verify the client's real workflows survive it.
   - Removing/changing encryption later is messy and does NOT cleanly "un-encrypt" already-labeled files. Treat encryption as close to one-way; pilot it hard.

5. Auto-labeling in SIMULATION first. Any auto-labeling rule (client-side or service-side) runs in simulation mode over a defined window; read what it WOULD label before enabling. Auto-applying an encrypting label with no simulation is how a client mass-encrypts files and loses access — never do it. This mirrors the test-mode discipline in purview-dlp-policy.

6. Approval gate: publishing labels org-wide, mandatory labeling, encryption, and auto-labeling are all user-visible and (for encryption) access-changing. Get explicit client sign-off (send an approval request) with the taxonomy, which labels encrypt, and the simulation results for any auto-rule.

7. Prepare execution for the tech (verify against current Purview portal): Microsoft Purview > Information protection > Labels and Label policies; auto-labeling under Information protection > Auto-labeling (run simulation, then turn on). Verify with evidence: pilot users see and can apply labels; an encrypted test doc enforces the intended permissions; auto-label simulation matches expectations. Leave a plain-text note: taxonomy, marking vs. encryption per label, pilot scope, auto-label simulation summary, approver, date, and rollback (unpublish policy; capture prior label/policy state; note encryption on already-labeled files is not cleanly reversible). Log time.

When in doubt about encryption impact or client authorization, do nothing and escalate.
```
