---
name: Safe Attachments and Links Policy
description: Tune Defender for Office 365 Safe Attachments and Safe Links policies from evidence — dynamic delivery, detonation action, URL rewriting/scanning, and scoped exceptions — without breaking legitimate mail flow. Use when a client reports attachment delivery delays, blocked links, or asks to strengthen (or loosen) Defender for O365 protection.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# Safe Attachments and Links Policy

**When to use:** A client reports attachments taking forever to arrive / email with a PDF delayed, a legitimate link being blocked or rewritten badly, asks to strengthen attachment and link protection, or wants to whitelist a vendor's URL/file in Defender. This skill tunes the policy; for alerts that have already fired from these policies, see vendor-runbooks/defender-m365-alerts.

**Run it:** on one client's request — you prepare and verify, a technician drives the Defender portal or PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You adjust Defender for Office 365 Safe Attachments and Safe Links policy against verdict evidence, favoring the tightest change that fixes the problem. Loose exceptions here are the holes that let a malicious attachment or URL through, so every override is scoped and justified. You prepare and verify; the tech drives the Defender portal or PowerShell. Never invent data.

1. Confirm licensing and current baseline first. Safe Attachments/Links require Defender for Office 365 (Plan 1/2, or the M365 Business Premium equivalent) — verify it's licensed before promising features. Read the current policy and whether the tenant is on Microsoft's Standard/Strict preset; recommend the preset baseline before bespoke rules. (Read the ticket for context; check the client's documentation for documented client Defender standards — skip gracefully if not connected.)

2. Diagnose from evidence, not the complaint:
   - Attachment delays → Safe Attachments detonation adds latency. Check whether Dynamic Delivery is on (delivers the body immediately, attaches the file once scanned) vs. a blocking action; enabling Dynamic Delivery usually fixes "slow attachments" without weakening protection.
   - A blocked/mangled link → inspect the Safe Links verdict and URL. A true malicious verdict stays blocked; a false positive gets a scoped Tenant Allow/Block List URL entry, not a broad domain allow.
   - "Strengthen protection" → confirm Safe Attachments action (Block), Safe Links scanning of email + Teams + Office apps, "click protection" settings, and that internal-sender scanning is on.

3. Scope every exception narrowly. A specific URL or file hash via the Tenant Allow/Block List, time-limited where supported, beats a wildcard domain allow — domain-level allows in Safe Links/Attachments are a bypass an attacker will find. Never disable Safe Attachments/Links wholesale to "fix" one message.

4. Approval: changes that alter delivery behavior or add allow entries are user- and security-relevant. Get client sign-off (send an approval request) with the verdict evidence, the exact change, and the scope of any exception.

5. Prepare execution for the tech (verify against current Defender portal, current module versions): Microsoft Defender portal > Policies & rules > Threat policies > Safe Attachments / Safe Links, or `Set-SafeAttachmentPolicy` / `Set-SafeLinksPolicy` / `New-TenantAllowBlockListItems`. Preset policies are edited via the preset security policies page.

6. Verify with evidence over a window: the affected pattern behaves as intended (attachment arrives promptly with Dynamic Delivery; the false-positive URL resolves; malicious verdicts still block) and protection isn't silently weakened. Document what/why/when/rollback — leave a plain-text note: verdict evidence, diagnosis, exact change and scope, review/expiry date for any allow entry, approver, date, and rollback (remove entry / restore prior policy values captured before the change). Log time.

Guardrails: Verify Defender for O365 licensing before promising Safe Attachments/Links behavior. No policy change without verdict/trace evidence; "it feels slow/blocked" is a reason to investigate, not to weaken. Scoped URL/file allow entries with a review date — never wildcard domain allows, and never disable the policy wholesale for one message. Prefer Dynamic Delivery to fix attachment latency over turning detonation off. Delivery/allow changes need client approval; capture prior policy values as rollback. When in doubt, do nothing and escalate.
```
