---
name: Liongard M365 Tenant Read
description: Answer tenant-level Microsoft 365 questions via the Liongard M365 inspector: license assignment, mailbox stats, admin roles, secure score, sharing.
category: Liongard Inspectors
tools: [liongard_launchpoint, liongard_metric, liongard_identity, liongard_detection, liongard_timeline, liongard_query]
connectors: [Liongard]
scope: single
flow: no
role: [Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Liongard M365 Tenant Read

**When to use:** "How many global admins are in <client>'s M365 tenant / who holds admin roles?", license counts and unassigned SKUs, mailboxes near quota or with forwarding set, external-sharing and secure-score-input questions — any M365 tenant fact where reading is enough.

**Run it:** on one client — name the client and the M365 tenant question.

## Prompt

```
Answer a tenant-level Microsoft 365 question for CLIENT_NAME from the Liongard Microsoft 365 inspector. Read-only — any change this motivates routes to a technician or an m365-administration skill.

1. Find the Microsoft 365 inspector for this client and confirm it ran recently; capture the last-run time — every answer carries "as of <timestamp>." A failed or ancient run means the answer is stale: say so and offer a technician-side refresh before anyone acts.
2. Read the values from its latest dataprint, verifying every field angle against the live dataprint (schemas vary by inspector version — an empty result from a wrong angle looks identical to a true zero):
   - Identity-shaped (admins, MFA, stale accounts) → use the reconciled identity view for the cross-system picture, then read tenant-specific detail. Admin-role work hands off to a security audit for judgment; this supplies the raw reads.
   - License-shaped → subscribed-SKU and per-user assignment sections: total vs. consumed per SKU, unassigned count, licensed-but-disabled accounts (money leaking). (Angles to verify: SKU total vs. consumed; disabled accounts still holding licenses.)
   - Mailbox-shaped → mailbox statistics: size vs. quota, item counts, forwarding addresses, litigation hold. A forwarding address outside the client's domains is a security lead, not a stat — flag it.
   - Settings-shaped (sharing, legacy auth, password policy) → tenant/SharePoint/OneDrive sharing and auth-policy sections.
   - Open-ended ("what looks off?") → ask in plain language, then verify anything actionable with a targeted read.
3. "Did this change?" → check what changed for admin-role grants, license count changes, and sharing-setting flips, with timestamps.
4. Surface admin-role and external-forwarding findings even when unasked, flagged. Never present the data as live — M365 changes minute-to-minute; state the capture age. If an angle returns nothing, confirm the section exists before reporting "none."
5. Output: the direct answer first, then evidence rows, the data as-of timestamp, and which fields were read. Leave a plain-text note on the ticket on request. Degradation: no M365 inspector → ticket history and documentation, labeled "not instrumented — attestation only."
```
