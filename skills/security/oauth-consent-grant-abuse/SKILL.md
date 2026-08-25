---
name: OAuth Consent Grant Abuse
description: Remove a malicious or over-privileged OAuth consent grant from a client tenant: identify the grant, revoke it, and tighten tenant consent policy.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# OAuth Consent Grant Abuse

**When to use:** An alert fires for a newly consented enterprise app, a risky OAuth grant, or an unfamiliar app with mail/file permissions; a user reports approving an app "to view a document" that then behaved oddly; or persistence hunting during a takeover/BEC recovery surfaces an attacker-added app consent.

**Run it:** on one ticket (a suspicious OAuth grant).

## Prompt

```
Consent phishing skips the password entirely: the user is tricked into granting a rogue app
OAuth permissions (read mail, send mail, read files), and the app now holds durable access
via a refresh token — no password to reset, MFA never challenged again. Find the grant,
revoke it, close the consent path. You drive and document; the client's admin executes tenant
changes. In order:

1. Identify the grant: which app, which account(s) consented, what permissions (delegated vs
   application/tenant-wide), and when. Application-level and admin-consented grants are the
   most dangerous and outrank single-user grants — they persist beyond any one account's
   cleanup.
2. Judge legitimacy before revoking: is this a known business app the client uses, or an
   unfamiliar or lookalike app requesting broad mail/file scopes? Broad "read/send
   mail" or "read all files" on an unknown app is malicious until proven otherwise. Check
   publisher verification and the consent timestamp against any sign-in anomaly. A wrongful
   revoke breaks a real integration — but broad scopes on an unverified publisher outvote
   convenience.
3. Revoke on the malicious verdict: direct the client's admin to remove the app's grant and
   service principal and revoke its issued tokens tenant-side, which kills the refresh token
   giving the app standing access. A password reset and session revocation do NOT touch an
   OAuth grant; the app keeps access until the grant itself is revoked.
4. Assess what the app could reach during its access window: mailbox contents, files,
   directory data. Preserve the grant definition and app audit logs before removal. If mail
   was accessible and fraud may have flowed, branch to business-email-compromise-recovery.
5. Close the vector tenant-wide: recommend the client restrict user consent — require admin
   approval for third-party apps, or limit consent to verified publishers and low-risk scopes
   — and enable an admin-consent request workflow. Flag it as the priority remediation, owned
   by the client's admin.
6. If the grant accompanied a takeover, check for co-planted persistence: inbox rules,
   forwarding, delegates.
7. Document the decision, not just the action: the app, its scopes, the legitimacy reasoning,
   what was revoked and when, the access-window assessment, and the consent-policy
   recommendation with its owner. Classify per soc-classification-tree.

Revoking grants and changing tenant consent policy are the client admin's actions — recommend
and drive them, never modify tenant app registrations or consent settings yourself. Write
defensively: "an unauthorized application grant was detected and removed", not "your tenant
was breached", and never assert data exfiltration without log evidence. Notes are plain text,
no markdown (apply the PSA Note Discipline base skill). When in doubt, escalate and restrict
consent.
```
