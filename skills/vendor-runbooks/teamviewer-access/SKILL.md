---
name: TeamViewer Access
description: Troubleshoot TeamViewer remote access: host and agent health, unattended access, session connectivity, and the commercial-use-detected flag on handoff.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# TeamViewer Access

**When to use:** An unattended device won't connect in TeamViewer, or sessions drop/time out; sessions are being blocked, time-limited, or nagged — possibly the commercial-use flag; or a tech asks how to read TeamViewer host/assignment status or why a machine is unreachable.

**Run it:** on the access-problem ticket.

## Prompt

```
Troubleshoot a TeamViewer remote-access problem. There is no native integration, so this is
diagnose-and-hand-off: work the symptom from the ticket, host behavior and documentation, then
direct the technician into the TeamViewer console. On-endpoint work is a technician step you
direct and record. State is inferred from the ticket, documentation or Liongard — give the
source and its freshness, never present it as a live console read.

1. Classify the problem: host offline (unattended agent not connecting), session connectivity
   (host online, session fails or drops), authentication or assignment (device not assigned to
   the company account, allowlist or Conditional Access block), or a commercial-use restriction.
   Copy the exact symptom and any on-screen message. "Machine offline", "host offline" and
   "device unassigned" are three different fixes.

2. Check commercial use first when sessions are throttled, time-limited or show a commercial-use
   notice: the "commercial use detected/suspected" flag is a licensing state, not a network
   fault, and it masquerades as a connectivity problem. Confirm the account tier and the
   device's assignment; the fix is in the TeamViewer management console, not on the endpoint.

3. For host offline, run the reachability ladder per device-offline-runbook: endpoint online,
   TeamViewer service running, outbound to TeamViewer's network reachable (firewall, proxy,
   DNS), host version current, and the device assigned to the company account.

4. For session or authentication issues, check version compatibility, allowlist and blocklist,
   Conditional Access policy, and account or group permission scope. Check prior tickets for the
   same device or account, the client's documentation for assignment and policy, and a Liongard
   inspector if one covers the endpoint — note its last run and data age, or say it's absent.

5. Security check: unexpected sessions, unknown assigned devices, or logins from unfamiliar
   locations are a potential access compromise — work them per security-alert-response as a
   security incident, not a support ticket. TeamViewer credentials are a known attacker target.

6. Hand off: reinstalling or repairing the Host, fixing assignment or licensing, adjusting
   allowlist or Conditional Access, and any on-endpoint work are technician or account actions.
   Assignment, allowlist and Conditional Access changes are security decisions: narrowest scope,
   named approver, review date — never widen access to "make it work". Verify the requester's
   identity before any access change.

7. Note the classification (with the commercial-use outcome), ladder results, security check and
   handoff. Client-facing wording per defensive-writing-standard.

Without documentation the account, assignments and policy may be unknown — say so. When in doubt
do nothing irreversible and escalate.
```
