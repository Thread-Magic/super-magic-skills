---
name: Purview DLP Policy
description: Scope, test, and roll out Microsoft Purview DLP policies with test-mode first, narrow scope, and evidence before enforce to protect PII and PHI.
category: M365 Administration
tools: [search_tickets, search_clients, search_knowledge_base, add_ticket_note, send_approval, log_time_entry, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Security & Compliance Owner, Technician]
outcome: [Risk & Compliance]
---

# Purview DLP Policy

**When to use:** A client asks to stop people emailing credit card numbers / SSNs / PHI outside the company, needs DLP for PCI/HIPAA/GDPR compliance, or wants to prevent sensitive files leaving via Teams/SharePoint/OneDrive. This skill creates/tunes the policy; for triaging DLP alerts that already fire, see security/dlp-alert-triage.

**Run it:** on one client's request — you prepare and verify, a technician drives the Purview portal (not a Flow: it needs a human at the console).

## Prompt

```
Roll out a Purview DLP policy in the only order that doesn't break a business. The tech
drives the Purview portal. Apply the Write Guardrails base skill — never invent data, and
when in doubt do nothing and escalate.

1. Pin down what "sensitive" means before touching Purview: which data types (credit card,
   SSN, bank account, health, a custom pattern), which locations (Exchange, SharePoint,
   OneDrive, Teams, endpoint), and what should happen (audit only, notify user, block with
   override, hard block). A vague "block sensitive data" request gets narrowed to concrete
   sensitive-info types, or the policy misses everything or blocks everything. Pull documented
   client compliance requirements (Connector Degradation base skill if their docs are off).

2. Scope narrowly. Prefer built-in sensitive-info types with a confidence level and instance
   count — "10+ credit-card matches, high confidence" — over broad keyword rules that
   false-positive on ordinary text and get disabled in anger. First rollout targets the
   affected users and locations, not the tenant.

3. Test mode first, always. Deploy in test/simulation mode, with or without policy tips, for
   a defined window. Enforcement is never enabled on a freshly
   created policy — the non-negotiable of DLP work.

4. Read the evidence, then decide. Sort the matches into real leaks and false positives — a
   template, a test string, an internal system that legitimately carries the pattern. Tune
   confidence and instance thresholds and add exceptions for legitimate flows BEFORE
   enforcing. Heavy legitimate traffic that would be blocked is a finding to take back to the
   client, not a reason to push through.

5. Approval to enforce. Test to enforce is user-visible and can block real work: get client
   sign-off carrying the test-mode match summary, the exact action (block versus
   block-with-override) and the scope. Prefer block-with-override with a business
   justification where risk tolerance allows — a hard block with no escape generates
   emergency tickets, so reserve it for where compliance demands it.

6. Prepare execution (verify against the current portal): Purview compliance portal > Data
   loss prevention > Policies, created in test mode, then edited to turn enforcement on.
   Endpoint DLP also needs devices onboarded to Purview — flag that dependency before
   promising endpoint coverage.

7. Verify: after enforce, a controlled matching message or file is handled as intended and
   legitimate traffic is not blocked; check the DLP alert and activity view. Note it (PSA
   Note Discipline base skill: plain text, no markdown or emojis) — data types and locations,
   scope, test-mode findings, action, exceptions, approver, date, and rollback (return to
   test mode or disable; capture the prior state first). Log time. Ongoing alerts go to
   security/dlp-alert-triage.
```
