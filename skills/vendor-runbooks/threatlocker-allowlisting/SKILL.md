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
You are running the ThreatLocker default-deny (zero-trust) runbook. Unlike detection products, ThreatLocker's daily driver is approval-request triage — an application was blocked because it isn't on the allowlist, and a human must decide whether it should be. This skill is the discipline for making that decision safely, plus Learning-vs-Secured mode, Elevation Control, and Storage Control. The block is the product working as designed; the risk is approving too fast. Verify feature names and console layout against ThreatLocker's current documentation. Approvals and policy changes are technician/admin actions in the ThreatLocker console; you triage, recommend a scoped decision, and record it — you do not silently self-approve.

1. Approval-request triage — the core workload, and a security decision every time (not a rubber stamp):
   - Identify what was actually blocked: the exact application/file, its hash, publisher/certificate, the path it ran from, the process that launched it (parent), the user, and the endpoint/client. ThreatLocker's request carries this — record it.
   - Legitimacy checks before approving: is the publisher/certificate valid and expected? Is the path normal (Program Files) or suspicious (temp, AppData, user-writable)? Did a legitimate process launch it, or something like Office/a browser spawning an unknown binary? Is this an expected update of already-allowed software, or something new? Correlate with any change the user actually made ("I installed X") and with prior tickets for the same app across clients.
   - Approve at the narrowest scope that works: prefer a rule matched on the verified publisher/certificate over a hash, a hash over a full-path, and a full-path over a folder/wildcard. Scope to the client (or specific policy group) that needs it, not globally, unless it's genuinely a fleet-wide trusted app. A path/folder allow in a user-writable location is a hole — avoid it.
   - When legitimacy can't be established (unsigned, unusual origin, unknown-reputation binary launched by a document or script), do NOT approve to make the ticket go away — this is exactly the block zero-trust exists for. Investigate as a potential threat (edr-detection-runbook / phishing-triage if a document/link is upstream); when in doubt, leave it denied and escalate.

2. Learning vs Secured mode — keep them straight: Learning mode builds the baseline allowlist by observing what runs (permissive — it is NOT protecting yet); Secured mode enforces default-deny. Onboarding runs Learning first, then transitions to Secured after review of the learned baseline. A client "protected by ThreatLocker" but left in Learning mode is not actually enforcing — flag any such gap. During Secured mode, a spike of approval requests right after go-live is expected, not a malfunction — don't "fix" it by loosening broadly.

3. Elevation Control requests (run application as admin without giving the user admin rights): same legitimacy bar as app approval, plus the privilege lens — scope elevation to the specific application, prefer time-limited/one-time where the need is temporary, and never grant standing elevation to satisfy convenience. A request to elevate an unknown binary is a red flag, not a routine approval.

4. Storage Control requests (USB/removable media, network-share access): treat per the client's removable-media/data policy (usb-removable-media-policy) — scope to the specific device/share and user, time-box where temporary, and route policy-loosening to the client's authorized approver, not the requesting user.

5. In the internal note, document the decision, not just the action: what was blocked, the legitimacy evidence weighed, the rule scope chosen and why, and the approver where a policy was loosened. Recurring legitimate blocks (a common app repeatedly tripping) → propose a properly-scoped baseline policy rather than repeated one-off approvals. Client-facing wording per defensive-writing-standard.

Degradation: without documentation access, the client's expected software baseline is unknown, so lean toward investigate-don't-approve and say so. When in doubt, leave it denied and escalate.
```
