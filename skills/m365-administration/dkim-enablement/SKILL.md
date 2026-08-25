---
name: DKIM Enablement
description: Enable DKIM signing for a custom domain in Exchange Online: publish selector CNAMEs, activate signing, verify records, and plan key rotation.
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
You are enabling or rotating DKIM for a custom domain in Exchange Online. You prepare and
verify; the tech runs the portal or PowerShell and the DNS owner publishes the records.
Never report signing as enabled on intention.

1. Confirm the domain is a verified accepted domain, and find who controls its DNS — the
   long pole; the Exchange side is two clicks. Documented ownership is in the client's
   documentation; continue without it if that integration is off (Connector Degradation
   base skill).

2. Take the CNAME targets from THIS tenant, never a template or another client — they embed
   the tenant's own onmicrosoft domain, so copied values fail silently. Have the tech run
   (verify against current module versions):
   Get-DkimSigningConfig -Identity <domain> | Format-List Selector1CNAME, Selector2CNAME
   creating the config first with New-DkimSigningConfig if none exists. Publish:
   - selector1._domainkey.<domain> CNAME → the Selector1CNAME value
   - selector2._domainkey.<domain> CNAME → the Selector2CNAME value

3. The DNS owner publishes both: rotation depends on the second selector existing, so one
   working selector today blocks rotation tomorrow. Verify externally with
   nslookup -type=cname selector1._domainkey.<domain>. Never enable signing before both
   selector CNAMEs resolve externally — Exchange would sign with a selector the world cannot
   look up, so every signature fails validation and the domain's mail reputation takes the
   hit.

4. Enable signing — Defender portal, Email authentication settings > DKIM, or
   Set-DkimSigningConfig -Identity <domain> -Enabled $true. This restamps all outbound mail
   from the domain, so send an approval request to the client contact with the change window.

5. Verify with evidence: send a test to an external mailbox the tech controls and read the
   headers for dkim=pass with d=<domain> and s=selector1 or 2. Where DMARC is in play,
   confirm d= matches the From domain. Paste the authentication-results header into the
   ticket.

6. Rotation, for hygiene or suspected key exposure: Rotate-DkimSigningConfig
   -Identity <domain>. Exchange flips to the other selector while the DNS CNAMEs stay put,
   so no DNS change is needed — that indirection is the point. Record the rotation date and
   recommend an annual cadence. The default onmicrosoft.com domain signs automatically;
   custom domains are the work.

7. Leave a plain-text note (PSA Note Discipline base skill): domain, both CNAMEs published,
   enable or rotation date, the header evidence, who approved, and rollback —
   Set-DkimSigningConfig -Enabled $false drops back to default onmicrosoft signing, leaving
   SPF and DMARC posture intact but possibly changing alignment. Log time.

Diagnosing SPF, DKIM or DMARC failures on mail in flight belongs to dmarc-spf-dkim-setup.
When in doubt, do nothing and escalate.
```
