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
Sync errors are precise: each names an error type and the conflicting attribute. Read the
actual error first, and treat every scope or rule change as a change.

Climb the Troubleshooting Ladder base skill first: documentation for the sync design —
Entra Connect or Cloud Sync (different products, different fixes), the source anchor
(ms-DS-ConsistencyGuid or objectGUID), OU and domain filtering, custom rules — and the
installed version against Microsoft's supported list; retired builds stop syncing
silently. History: AD cleanups, OU moves, consolidations and bulk imports just before the
symptom are usually the story. Then take the error verbatim from Synchronization Service
Manager's Operations tab or the provisioning-error report: type, attribute, conflicting
pair, failing step.

Preview before any sync that follows a config change: read the queued adds, updates and
deletes first, because a scope mistake plus a forced full sync is mass deletion. When
pending deletes exceed the export deletion threshold the engine stops on purpose; never
disable it — escalate to the identity owner with the pending-delete list.

1. Duplicate attribute (AttributeValueMustBeUnique, proxyAddresses or UPN conflicts) — two
   objects claim the same value, often a forgotten cloud-only user or contact. The client
   decides which keeps it; fix it on-prem and the next cycle heals it.

2. InvalidSoftMatch or wrong-object match — a soft match joined the user to the wrong
   cloud object, or a hard match conflicts on the anchor. Never edit ms-DS-ConsistencyGuid
   or immutableId by hand to force a match: a wrong hard match rebinds someone's mailbox
   to someone else. Escalate to the identity owner with both anchors.

3. Object not syncing, no error — it is filtered: out-of-scope OU, cloudFiltered by a
   rule, or a default exclusion. The sync rule preview against that object names the rule.

4. Connector or run-level failure — stopped-server-down, quarantine, lost
   password-hash-sync heartbeat. Look for service account lockout or expiry, TLS 1.2
   enforcement after hardening, or lost connector permissions. Fix the cause; repeated
   forced full syncs are not a repair.

5. Staging surprises — nothing exports and no errors means staging mode. Exactly one
   active server per tenant, so two fight and zero export nothing; swapping goes
   new-to-staging, verify exports, old to staging, new to active.

Fix synced-object attributes on-prem, never in the cloud; cloud edits are overwritten.
Uninstalling the server to "start fresh" converts every synced user to cloud-managed — a
designed migration, not a troubleshooting step.

Success is the affected objects clean in the next delta cycle and the error count back at
baseline. Note it (apply the PSA Note Discipline base skill): error verbatim, objects,
branch, fix or escalation, whether a cycle ran and what the preview showed.
```
