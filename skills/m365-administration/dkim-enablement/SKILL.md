---
name: DKIM Enablement
description: Enable DKIM signing for a custom domain in Exchange Online — publish the two selector CNAMEs, flip signing on, verify, and plan key rotation. Use when a ticket asks to "set up DKIM," a deliverability or DMARC project needs signing enabled, or keys need rotating.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance]
---

# DKIM Enablement

**When to use:** Get a domain's outbound mail cryptographically signed — "enable DKIM for <client-domain>," a DMARC rollout that needs DKIM alignment, "rotate the DKIM keys" (scheduled hygiene or post-incident), or deliverability complaints where headers show dkim=none for the domain. The two CNAME records get published correctly, signing is enabled only after DNS resolves, and rotation is treated as routine hygiene rather than an emergency. Diagnosis and the wider SPF/DMARC picture live in dmarc-spf-dkim-setup — this skill is the Exchange Online execution half.

**Run it:** on one domain — you prepare and verify, a technician runs the admin portal or PowerShell and the DNS owner publishes the records (not a Flow: it needs a human at the console).

## Prompt

```
You are enabling (or rotating) DKIM for a custom domain in Exchange Online. You prepare and verify; the technician runs the admin portal or PowerShell and the DNS owner publishes records. Never report signing as enabled on intention — never invent data.

1. Confirm the domain is a verified accepted domain in the tenant, and find who controls its DNS (check the client's documentation for documented DNS ownership; skip gracefully if not connected) — the CNAMEs are the long pole; the Exchange side is two clicks.

2. Get the exact CNAME targets from THIS tenant, not from a template. Have the tech pull them (PowerShell labeled: verify against current module versions):
   Get-DkimSigningConfig -Identity <domain> | Format-List Selector1CNAME, Selector2CNAME
   (or create the config first with New-DkimSigningConfig if none exists). The records to publish are always:
   - selector1._domainkey.<domain> CNAME → the Selector1CNAME value
   - selector2._domainkey.<domain> CNAME → the Selector2CNAME value
   The targets embed the tenant's initial onmicrosoft domain — this is why copy-pasting from another client's setup silently fails. CNAME targets come from THIS tenant's DkimSigningConfig; never reuse another tenant's values.

3. Have the DNS owner publish both CNAMEs. Both — rotation depends on the second selector existing; one selector "working" today blocks rotation tomorrow. Verify resolution externally (nslookup -type=cname selector1._domainkey.<domain>) before enabling; enabling before DNS resolves is the classic "DKIM broke our mail reputation" self-inflicted wound (Exchange signs with a selector the world can't look up, so signatures fail validation). Never enable signing before both selector CNAMEs externally resolve.

4. Enable signing: Defender portal (Email authentication settings > DKIM) or Set-DkimSigningConfig -Identity <domain> -Enabled $true. This changes how all outbound mail from the domain is stamped — low risk when DNS is right, but tell the client the change window anyway (send an approval request / inform the client contact for a domain-wide mail-stamping change).

5. Verify via evidence: send a test to an external mailbox the tech controls and read the headers — dkim=pass with d=<domain> and s=selector1 (or 2). If DMARC is in play, confirm alignment (the d= domain matches the From domain). Paste the authentication-results header into the ticket.

6. Rotation: for scheduled hygiene or after suspected key exposure, run Rotate-DkimSigningConfig -Identity <domain>. Rotation is seamless because Exchange flips to the other selector while DNS CNAMEs stay put — no DNS change needed, which is the point of the CNAME indirection. Note the rotation date; recommend an annual cadence in the client's documentation. The default onmicrosoft.com domain is signed automatically — don't burn time "fixing" it; custom domains are the work.

7. Document what/why/when/rollback in a plain-text note: domain, both CNAME records published (names and targets), enable/rotation date, verification header evidence, approver/client contact informed, and rollback (Set-DkimSigningConfig -Enabled $false — mail then falls back to the default onmicrosoft signing; SPF and DMARC posture unaffected but alignment may change). Log time.

Diagnosis of failing SPF/DKIM/DMARC on mail already in flight belongs to dmarc-spf-dkim-setup — keep this skill to enablement and rotation. When in doubt, do nothing and escalate.
```
