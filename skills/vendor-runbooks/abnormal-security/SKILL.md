---
name: Abnormal Security
description: Triage Abnormal Security email cases: read ATO and BEC behavioral signals, treat account takeover as an identity incident, finish auto-remediation gaps.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# Abnormal Security

**When to use:** An Abnormal case arrives — BEC / vendor fraud / invoice fraud, a phishing/malware verdict, or (most importantly) an Account Takeover case; a tech asks how to read Abnormal's behavioral signals or whether a case is an identity compromise; or an Abnormal auto-remediation moved messages and the desk must validate and follow through.

**Run it:** on the alert ticket.

## Prompt

```
Triage an Abnormal Security case. Abnormal is the behavioral email-security platform for
Microsoft 365 and Google Workspace: it flags business email compromise, vendor fraud and
account takeover by deviation from a learned baseline rather than by signature. Your job is
to map its case types onto the generic runbooks, which own the canon. You have no Abnormal
or tenant-admin console — remediation,
un-remediation and account containment are technician steps you direct and record. Never
invent detection detail.

1. Classify the case type first; it decides the runbook.
   - Account Takeover → an identity incident that happens to surface in email. Go straight to
     compromised-account-containment; the sign-in, mail-rule or send behavior Abnormal
     flagged is the symptom. Never close it as "email quarantined" — the sweep for
     persistence is the actual work.
   - BEC, vendor fraud or invoice fraud → vendor-fraud-bec-alert: verify any payment or
     banking-change request through an independent known channel, a phone number on file,
     never a reply to the suspect thread — attackers control it. These attacks are pure
     social engineering, so never downgrade a behavioral verdict because there's no malware.
   - Phishing or malware → phishing-triage or quarantine-release-request.

2. Parse the anatomy: affected identity (UPN), the behavioral signals Abnormal cited (unusual
   geo or device, atypical recipients, mailbox-rule creation, tone and urgency), the
   auto-remediation state (moved to junk or quarantine versus detected-only), and timestamps.
   Copy Abnormal's exact case language into the note. Route per security-alert-response by
   tenant; low routing confidence means flag for a human, not reassign.

3. On an ATO case, don't stop at the email symptom: run the full
   compromised-account-containment sweep — password, MFA methods, sessions, app passwords,
   delegated and OAuth access, mail rules. Message movement is not identity containment.

4. Verify auto-remediation by effect: confirm the messages Abnormal claims it moved did
   move — a claimed remediation that didn't apply is false comfort. Detected-only means
   treat it as live.

5. Scope it: check prior tickets for the same client and sender or domain over roughly 90
   days — vendor-fraud actors reuse infrastructure across a client's contacts.

6. Note the case type, the behavioral signals weighed, the verification outcome and the
   containment sweep results; classify per soc-classification-tree. Exclusions and
   VIP-impersonation exceptions are security decisions: narrowest scope, named approver,
   review date. Client-facing wording per defensive-writing-standard.

Without documentation the client's known-vendor and payment-approval process may be
unknown — lean harder on independent verification and say so. When in doubt do nothing
irreversible and escalate.
```
