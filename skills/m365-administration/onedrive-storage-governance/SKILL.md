---
name: OneDrive Storage Governance
description: Set OneDrive policy deliberately — storage quotas, retention on leaver accounts, sync scope (which devices/domains can sync), and external-sharing posture. Use when a client asks about OneDrive limits, "what happens to files when someone leaves," blocking personal-device sync, or tightening OneDrive sharing.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# OneDrive Storage Governance

**When to use:** A client asks about their OneDrive storage limit or raising it, where a departed employee's OneDrive files go, stopping people syncing company files to personal PCs, or locking down OneDrive external sharing — the four tenant-level settings that decide whether OneDrive is a controlled store or a quiet data-exfil path. NOT for a single leaver's file handover on one ticket (that's an offboarding task), and NOT for SharePoint site sharing — that is sharepoint-site-provisioning.

**Run it:** on one client's request — you prepare and verify, a technician drives the admin center or PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You govern OneDrive for Business at the tenant level: quotas, what happens to a leaver's files, which devices are allowed to sync, and how open sharing is. You prepare and verify; the tech drives the admin center or PowerShell. Never invent data.

1. Quota: report the current default (and per-user overrides) and the tenant license ceiling before changing anything — quota is capped by license, so "just give them more" has a hard limit. Raise the default only with a reason; unbounded quota hides the real problem (people storing what belongs in SharePoint/Teams). Recommend per-user overrides for genuine outliers rather than lifting the default for everyone. (Check the client's documentation for documented client OneDrive standards — skip gracefully if not connected.)

2. Retention on leaver accounts: confirm the tenant's OneDrive retention setting — how long a deleted user's OneDrive is kept before permanent deletion, and who is auto-granted access (the manager, by default, if configured). This is the setting that decides whether offboarding can still recover a leaver's files next month. If it's short or unset, recommend a retention policy (tie into retention-policy-requests) so files aren't lost the moment an account is removed. Never rely on the default silently.

3. Sync scope: restrict the OneDrive sync client to domain-joined / managed devices and to allowed domains, and block sync on personal machines where the client wants that — this is the control that stops company files landing on unmanaged home PCs. Note it takes effect on new sync sessions; already-synced files on a device aren't clawed back by the setting (that's an Intune/wipe conversation — device-wipe-workflows).

4. External-sharing posture: set OneDrive's sharing level (it can be equal to or more restrictive than SharePoint's, never more open). Default links to "specific people," set link expiration, and disable anonymous "Anyone" links unless there's an approved need. Review whether "Anyone" is on today and flag it.

5. Approval: quota changes, retention, sync restrictions, and sharing all affect users tenant-wide. Send an approval request with each setting's before/after value stated.

6. Prepare execution for the tech (verify against current SharePoint/OneDrive admin center / PowerShell, current module versions): OneDrive admin settings, or `Set-SPOTenant` (sync-scope, sharing) and `Set-SPOSite` for per-user overrides; retention via the Purview/compliance portal.

7. Verify with evidence: quota reflects the change; a test share behaves at the set level; sync from a non-allowed device is blocked; retention shows applied. Document what/why/when/rollback — leave a plain-text note: each setting's before/after, retention window and auto-access target, sync-scope rule, sharing level, approver, date, and rollback (restore prior values captured before the change). Log time.

Guardrails: Quota is license-capped; state the ceiling before promising more, and prefer per-user overrides to lifting the org default. Never leave leaver-file retention to chance — confirm the window and auto-access target; that setting is what makes future recovery possible. Sync-scope restrictions apply going forward; they do not retrieve files already on a device — that's a wipe/Intune action, not this setting. OneDrive sharing can't exceed the SharePoint/tenant ceiling; anonymous links are an approved exception with expiry, not a default. Capture every prior value before changing it; that is the rollback. When in doubt, do nothing and escalate.
```
