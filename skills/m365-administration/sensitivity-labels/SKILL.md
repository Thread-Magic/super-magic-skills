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
You roll out Purview sensitivity labels as a governed, piloted change: you prepare and verify, the tech executes in the portal. Apply the Write Guardrails base skill — never invent data, and when in doubt about encryption impact or authorization, do nothing and escalate. Verify the portal against current docs.

1. Design a small taxonomy first: three to five labels people can choose correctly beat a fifteen-label tree nobody understands — Public / Internal / Confidential / Highly Confidential is typical. Define each label in plain client language first — an ambiguous label is applied wrongly and trusted falsely.

2. Decide per label what it does: visual marking, encryption, container settings (Teams, site, group privacy), DLP tie-ins. Keep the first rollout to marking for most labels; reserve encryption for the top tier (step 4). Check the client's documented classification standard; if that integration isn't connected, say so (Connector Degradation base skill).

3. Publish to a pilot, not the tenant: scope the policy to a small group and decide whether a default label and mandatory labeling apply. Mandatory labeling changes everyone's save and send flow — introduce it only after the pilot proves the taxonomy.

4. Encryption is the dangerous part — spell out the consequences before enabling it on any label:
   - Protection travels with the file; access follows the label's permissions, not the file's location — wrong permissions lock users out of their own documents.
   - Sharing an encrypted file externally requires the recipient to authenticate and hold rights; it silently breaks partner workflows.
   - Some services, co-authoring and third-party tools handle encrypted files poorly — verify the client's real workflows survive it.
   - Removing or changing encryption later does not cleanly un-encrypt already-labeled files. Treat it as one-way and pilot it hard.

5. Run auto-labeling in simulation first, over a defined window, and read what it would label before enabling it. Auto-applying an encrypting label with no simulation is how a client mass-encrypts files and loses access — never do it. Then get client sign-off before going wider — org-wide publish, mandatory labeling, encryption and auto-labeling are all user-visible, and encryption is access-changing. Send an approval request with the taxonomy, which labels encrypt, and the simulation results.

6. Prepare execution in the Purview portal: Information protection > Labels, Label policies, and Auto-labeling (simulate, then turn on). Verify: pilot users can apply labels and an encrypted test document enforces the intended permissions. Leave a plain-text note: taxonomy, marking vs. encryption per label, pilot scope, simulation summary, approver, date and rollback — unpublish the policy, prior label and policy state captured; encryption on already-labeled files is not cleanly reversible. Log time.
```
