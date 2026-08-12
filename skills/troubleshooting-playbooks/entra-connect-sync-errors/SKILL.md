---
name: Entra Connect Sync Errors
description: Fix Entra Connect (Azure AD Connect) sync errors — export failures, duplicate attributes, quarantined objects, users missing in the cloud — no blind runs.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Entra Connect Sync Errors

**When to use:** New or changed on-prem users/groups aren't appearing or updating in Entra ID / M365; the portal shows provisioning errors (duplicate attribute, InvalidSoftMatch, AttributeValueMustBeUnique); sync-health alerts fire (export errors, a connector quarantined, password hash sync stopped); or after a migration/consolidation objects matched to the wrong cloud user or a server swap is planned.

**Run it:** on the one ticket you're working — a tech drives the sync console hands-on with the identity owner; not unattended.

## Prompt

```
Sync errors are precise — each carries an error type and the exact attribute in conflict. The rule: read the actual error from Synchronization Service Manager or the Entra portal's provisioning-errors view before proposing anything, and treat every scope or sync-rule change as a change with a preview, because the sync engine happily deletes at scale.

Work it in this order:

1. Version identification first. Check the client's documentation and knowledge base for the sync design: Entra Connect vs Cloud Sync (different products, different fixes), server name, staging server present?, the source anchor in use (ms-DS-ConsistencyGuid vs legacy objectGUID), OU/domain filtering scope, and any custom sync rules. Also check the installed version against Microsoft's minimum-supported list — retired builds silently stop syncing. Documentation coverage varies per tenant — note anything you could not check.

2. History first. Search this client's past tickets: recent AD cleanups, OU moves/renames, domain consolidations, server migrations, bulk user imports. Bulk on-prem changes immediately preceding the symptom usually are the story — especially pending deletions from an OU move out of scope.

3. Get the error before theorizing. Guide the tech to Synchronization Service Manager -> Operations (per-run, per-object errors) and the Entra admin center's provisioning error report. Capture verbatim: error type, attribute named, the conflicting object pair if given, and which step failed (import/sync/export). "Sync is broken" is not evidence — never invent it.

4. The cardinal rule — preview before any sync that follows a config change. If filtering, OUs, rules, or the server changed, run Start-ADSyncSyncCycle ONLY after checking pending exports (Get-ADSyncCSObject counts / the "staging" preview, or a full import+sync in a staging-mode server) and reading how many adds/updates/deletes are queued. A scope mistake plus a forced full sync = mass deletion in the tenant. If pending deletes exceed the deletion threshold, the engine stops on purpose (ExportDeletionThreshold) — do NOT disable the threshold to push through; that guard is the last line. Escalate to the identity owner with the pending-delete list.

5. Branch on the error family:
   - Duplicate attribute (AttributeValueMustBeUnique, ProxyAddresses/UPN conflicts) — two objects claim the same proxyAddress or UPN. Identify both objects (one is often a forgotten cloud-only user or a contact), decide with the client which keeps the value, fix on-prem (sync will overwrite cloud edits on synced objects). Duplicate-attribute resiliency may have quarantined just the attribute — clearing the conflict lets the next cycle heal it.
   - InvalidSoftMatch / wrong-object match — soft match (SMTP/UPN) joined an on-prem user to the wrong cloud object, or a hard-match conflict on the source anchor. Source-anchor caution: never edit ms-DS-ConsistencyGuid / immutableId by hand to force a match unless you can state exactly which object should own which cloud identity and why — a wrong hard-match rebinds someone's mailbox to someone else. Escalate to the identity owner with both objects' anchors documented.
   - Object not syncing at all (no error) — it's filtered: out-of-scope OU, cloudFiltered by a rule, or hit by the default "AdminSDHolder/CriticalSystemObjects" style exclusions. Trace with the sync rule preview against that one object rather than guessing; the preview names the rule that excluded it.
   - Connector/run-level failures (stopped-server-down, quarantine, password hash sync heartbeat lost) — service account lockout/expiry, TLS 1.2 enforcement after a hardening pass, permissions removed from the connector account, or the connector quarantined after repeated failures. Fix the cause, then let the scheduler run; forcing repeated Initial (full) syncs is not a repair and multiplies load.
   - Staging mode surprises — nothing exports and no errors: check whether the server is in staging mode (someone built a replacement and never cut over, or a cutover left two active). Exactly one active (non-staging) server per tenant; two active servers fight, zero export nothing. When swapping servers, the new one goes staging -> verify pending exports -> old to staging -> new to active, in that order. Never run two active (non-staging) sync servers against one tenant.

Guardrails to hold throughout: never run a full/initial sync — or any sync after a scope/rule/server change — without previewing pending exports first, and never disable the export deletion threshold to force one through. Never edit source anchors to force a match without documented justification and the identity owner's sign-off. Fix synced-object attributes on-prem, not in the cloud — cloud edits on synced objects are overwritten or refused. Deleting the Entra Connect server or uninstalling to "start fresh" converts every synced user to cloud-managed with consequences — that is a designed migration, not a troubleshooting step. All sync console/PowerShell work is guidance for the tech; you never execute it. Verify error meanings and supported-version status against Microsoft's current docs on the web — the product renames and rewires often; don't recite from memory.

Verify and note. Success = the affected objects clean in the next delta cycle (Operations shows no errors for them) and correct in the cloud, plus the portal's provisioning-error count back at baseline. Leave a plain-text internal note (no markdown, no emojis, raw URLs not markdown links): error verbatim, objects involved (sanitized), branch, on-prem fix applied or escalated, whether any sync cycle was run and what the preview showed, verification time.
```
