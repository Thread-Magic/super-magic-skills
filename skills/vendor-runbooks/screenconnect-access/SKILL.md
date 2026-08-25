---
name: ScreenConnect Access
description: Troubleshoot ScreenConnect / ConnectWise Control access: unattended-agent health, session connectivity, and console handoff for the technician on duty.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# ScreenConnect Access

**When to use:** An unattended device won't appear online in ScreenConnect or drops session repeatedly; a tech can't launch or complete a remote session (client won't install, session times out, host/guest mismatch); or a tech asks how to read ScreenConnect agent health or why a machine is unreachable.

**Run it:** on the access-problem ticket.

## Prompt

```
Troubleshoot a ScreenConnect (ConnectWise Control) remote-access problem. There is no native
Super Magic integration, so this is a diagnostic-and-handoff skill: work the symptom from the
ticket, agent behavior and documentation, then direct the technician into the ScreenConnect
console. You never run commands, scripts or Backstage sessions on an endpoint — on-endpoint
work is a technician step you direct and record.

1. Classify the problem: unattended-agent-offline (the Access agent isn't checking in),
   session-connectivity (agent online, session fails), or client-install (the guest or host
   client won't deploy). Copy the exact symptom and any error wording.

2. For agent-offline, climb the reachability ladder per device-offline-runbook: is the
   endpoint itself online (other monitoring), is the ScreenConnect service running, is
   outbound to the relay or server reachable (firewall, proxy, DNS), is the agent version
   current. Separate "the whole machine is down" from "only the ScreenConnect agent is down" —
   different tickets, and reinstalling the agent on a powered-off machine helps no one.

3. For session-connectivity, check relay and port reachability, host-versus-guest client
   version compatibility, session-group and permission scope, and — on a self-hosted instance
   — whether the server itself is healthy. For client-install, check OS and permission
   blockers and endpoint-protection interference.

4. Use the context you do have: prior tickets for the same device or instance for recurrence,
   the client's documentation for the instance URL, version and access policy, and a Liongard
   inspector covering the endpoint for corroborating state (verify its last run, note the age,
   degrade if absent). Give the source and its freshness; never present inferred state as a
   live console read.

5. Run the security check; do not skip it. Unexpected sessions, unknown access agents, or an
   alert about the instance itself are potential compromise of an actively exploited product.
   Treat that as a security incident per security-alert-response, not a connectivity ticket,
   and involve the security path.

6. Hand off for action: reinstalling or repairing the Access agent, changing session or
   permission config, patching the instance, and any on-endpoint work are technician actions.
   Never widen session permissions or access scope to make something work — access scope is a
   security decision with the narrowest scope, a named approver and a review date. Write the
   handoff with the classified cause and the steps.

7. Note the classification, the ladder results, the security-check outcome and the handoff.
   Client-facing wording per defensive-writing-standard.

Without documentation the instance URL, version and access policy may be unknown — say so.
When in doubt do nothing irreversible and escalate.
```
