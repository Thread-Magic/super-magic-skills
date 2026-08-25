---
name: ThreatLocker Allowlisting
description: Work ThreatLocker approval and elevation requests: triage daily allowlisting safely, keep Learning vs Secured mode straight, protect zero-trust posture.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# ThreatLocker Allowlisting

**When to use:** A ThreatLocker approval request (blocked application/script needing allowlisting) lands — the routine, high-volume case; an Elevation Control (run-as-admin) or Storage Control (USB/network-share access) request arrives; or a client is being onboarded and the Learning-vs-Secured mode transition needs handling.

**Run it:** on the approval-request ticket.

## Prompt

```
Run the ThreatLocker default-deny runbook. A blocked application is the product working; the
risk is approving too fast. Approvals and policy changes are console actions: you triage,
recommend a scoped decision, record it, never self-approve.

1. Identify what was blocked: application or file, hash, publisher and certificate, the path
   it ran from, the parent process, the user, the endpoint.

2. Weigh legitimacy before approving: publisher or certificate valid and expected; path
   normal (Program Files) rather than user-writable (temp, AppData); a legitimate parent
   process rather than Office or a browser spawning an unknown binary; an expected update of
   allowed software rather than something new. Correlate with a change the user made and
   prior tickets for the same app.

3. Approve at the narrowest scope: verified publisher or certificate over hash, hash over
   full path, full path over folder or wildcard. Scope to the client or policy group that
   needs it, not globally unless it is fleet-wide trusted. A path or folder allow in a
   user-writable location is a hole. When legitimacy cannot be established — unsigned, odd
   origin, unknown-reputation binary launched by a document or script — do NOT approve to
   clear the ticket. Investigate (edr-detection-runbook, or phishing-triage
   if a document or link is upstream) and leave it denied.

4. Learning versus Secured mode. Learning builds the baseline by observing what runs and is
   NOT protecting; Secured enforces default-deny. Onboarding runs Learning first, then Secured
   after review. A client "protected by ThreatLocker" but left in Learning is not
   enforcing — flag it. A spike of requests right after go-live is expected;
   never "fix" it by loosening broadly.

5. Elevation Control (admin rights for one app, not the user) takes the same
   legitimacy bar plus a privilege lens: scope elevation to the specific application, prefer
   time-limited or one-time, and never grant standing elevation for convenience. Elevating
   an unknown binary is a red flag. Storage Control (USB, removable media, network shares)
   follows the client's removable-media policy per usb-removable-media-policy: scope to the
   specific device or share and user, time-box temporary access, and route policy-loosening
   to the client's authorized approver, never the requester.

6. Note the decision: what was blocked, the legitimacy evidence, the rule scope chosen and
   why, and the approver where a policy was loosened. Plain text, no markdown or emojis
   (apply the PSA Note Discipline base skill). Recurring legitimate blocks get a scoped
   baseline policy, not repeated one-off approvals; client-facing wording follows
   defensive-writing-standard.

Without documentation the client's software baseline is unknown — lean to
investigate-don't-approve and say so. When in doubt, leave it denied and escalate.
```
