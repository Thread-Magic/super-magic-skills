---
name: Session Token Theft Response
description: Respond to stolen session cookies or tokens after MFA-passed account abuse: revoke sessions and tokens system-wide, not just the user's password.
category: Security
tools: [search_tickets, search_contacts, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Session Token Theft Response

**When to use:** Malicious or anomalous activity on an account where sign-in logs show MFA succeeded and no password change explains it; a user's session appears active from an unfamiliar IP/device while the user is elsewhere; or post-phishing where the lure harvested a session (adversary-in-the-middle / token-replay), not just credentials.

**Run it:** on one ticket (a suspected stolen-session case).

## Prompt

```
The tell is a paradox: confirmed malicious activity on an account whose MFA was satisfied
and whose password nobody reset recently. That is a stolen session token or cookie — an
attacker replaying the user's already-authenticated session, sailing past MFA because the
session already cleared it. The fix a password reset alone will not deliver: kill the
sessions. You drive and document; the client's admin performs the tenant-side revocation.
Work it in order:

1. Recognize the pattern before acting: MFA-satisfied sign-in + malicious activity + no
   plausible password compromise = session/token theft until proven otherwise. Capture the
   anomalous session's IP, device, and timestamps.
2. Revoke first, and revoke the right thing: invalidate all active sessions AND refresh
   tokens for the account — this is what evicts the attacker. A password reset alone does
   NOT kill an already-issued session; the stolen cookie stays valid until the session is
   explicitly revoked.
3. Then rotate the password too — the harvest that produced the token may have taken the
   credential as well — and re-verify MFA (remove any attacker-registered method).
4. Look for persistence the attacker planted during the live session: inbox rules and
   forwarding (inbox-rule-alert-runbook for the full sweep), OAuth app consents
   (oauth-consent-grant-abuse), delegates/send-as. Token theft buys a window; attackers use
   it to plant durable access.
5. Trace the source: if this came from a phishing message, run email-header-analysis and
   treat other recipients as potentially hit by the same token-stealing lure. If fraud was
   sent from the account, branch to business-email-compromise-recovery.
6. Assess blast radius and run the account-takeover-runbook sweep for anything the session
   touched.
7. Document the decision, not just the action: the MFA-passed-yet-malicious evidence, exactly
   what was revoked (sessions + tokens) and when, what persistence was found, and the
   root-cause hypothesis. Classify per soc-classification-tree.

Guardrails — always:
- The core rule: revoke sessions and tokens, not just the password. If your remediation is
  only a password reset, the attacker is still in.
- Session/token revocation is a tenant-side action owned by the client's admin — recommend,
  drive, and document; never hold credentials or flip the setting yourself.
- MFA passing does NOT clear the account — replayed sessions are pre-authenticated. Do not
  treat "MFA succeeded" as evidence of legitimacy here.
- Always check for planted persistence — a revoked session with a live forwarding rule or
  OAuth grant is not remediated.
- Defensive writing: "an unauthorized session was detected and revoked," not "you were
  hacked"; do not assert data was accessed without log evidence. Plain text only. When in
  doubt, revoke and re-verify.
```
