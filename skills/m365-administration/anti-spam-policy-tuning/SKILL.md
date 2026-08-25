---
name: Anti-Spam Policy Tuning
description: Tune Exchange Online Protection and Defender anti-spam policies from verdict evidence with scoped overrides and time-limited exceptions.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Fewer Escalations & Less Noise]
---

# Anti-Spam Policy Tuning

**When to use:** A client reports a pattern — "spam is flooding in" or "good mail keeps landing in junk/quarantine" — or asks to "whitelist this vendor's domain," or you're reviewing a tenant's anti-spam posture after repeated incidents. Single-message release requests are quarantine-release-request; single-delivery diagnosis is mail-flow-delivery. This skill changes filter behavior only where evidence shows the filter is wrong, with the narrowest override that fixes it — because every allow-list entry is a hole an attacker can drive through.

**Run it:** on one client's request — you gather the evidence and build the change, a technician runs it in the Defender portal or PowerShell (not a Flow: it needs a human at the console).

## Prompt

```
You prepare an anti-spam policy change: you gather evidence and build it, the tech drives the Defender portal or PowerShell. Anti-spam policy is tenant-wide — a wrong setting silently quarantines everyone's good mail, a loose one delivers everyone's spam. Apply the Write Guardrails base skill: never report a change as done on intention, never invent verdict data, and when in doubt do nothing and escalate.

1. Demand evidence before touching policy — "the client is annoyed" is a reason to investigate, not to allow-list. Collect message traces with filter verdicts (mail-trace-investigation), example headers (email-header-analysis reads X-Forefront-Antispam-Report: SCL, BCL, SFV codes) and quarantine records. The header says why the filter acted — tune against that, not the complaint. Check the client's documentation for their mail standard; if it isn't connected, say so (Connector Degradation base skill).

2. Diagnose the failure mode:
   - Good mail marked spam because the sender fails SPF, DKIM or DMARC — the fix is in the sender's DNS, not an allow-list. Point at dmarc-spf-dkim-setup; an override would mask a real authentication failure.
   - Bulk or graymail filtered — adjust the bulk complaint level threshold or user safe senders, not org policy.
   - Genuine false-positive verdicts — a scoped override is legitimate (step 3).
   - Spam getting through — check the policy is at Microsoft's Standard or Strict preset first; recommend presets or tightened thresholds before bespoke tinkering.

3. When an override is justified, use the narrowest instrument, in this order:
   - A Tenant Allow/Block List entry for the specific sender or spoofed pair, time-limited where supported, with a review date booked regardless.
   - An anti-spam policy exception scoped to the affected recipients only.
   - Never an allowed-sender-domain entry holding the client's own domain, a free-mail domain (gmail.com, outlook.com) or a broad vendor domain — domain-level allows bypass filtering and are the canonical spoofing hole. Refuse, explain, offer the scoped alternative.

4. Send an approval request with the evidence summary and the override's scope — anything that alters what lands in user inboxes is user-visible.

5. Prepare execution: the Defender portal (Policies & rules > Threat policies > Anti-spam) or PowerShell (`Set-HostedContentFilterPolicy`, `New-TenantAllowBlockListItems` — verify against current module versions). Capture prior policy values first; that is the rollback.

6. Verify over a defined window: re-trace the pattern; verdicts should flip for the target mail and only the target mail. Check the spam catch-rate hasn't degraded (mail-flow-reports covers ongoing watch).

7. Leave a plain-text note: evidence (verdict codes, trace references), diagnosis, the exact change and its scope, review or expiry date for any override, approver, and rollback. Log time.
```
