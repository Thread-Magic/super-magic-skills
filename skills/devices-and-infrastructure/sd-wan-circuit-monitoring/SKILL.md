---
name: SD-WAN / Multi-Circuit Monitoring
description: Review a multi-circuit or SD-WAN site — confirm each circuit is up, failover works, and open the right ISP escalation when a link is down or degraded.
category: Devices & Infrastructure
tools: [liongard_launchpoint, liongard_metric, liongard_timeline, search_ninjaone_devices, search_itglue, web_search, create_ticket, add_ticket_note]
connectors: [Liongard, NinjaOne, IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Always-On Coverage]
---

# SD-WAN / Multi-Circuit Monitoring

**When to use:** "Is <site>'s backup circuit actually working?" / failover verification, one circuit at a multi-WAN site reported down or flapping, or a post-outage review of how failover behaved.

**Run it:** on one site's connectivity, on demand (not a Flow — it's a posture/failover check and escalation prep, not a per-ticket event).

## Prompt

```
For a site with more than one WAN link, confirm the state of each circuit, prove failover is real (not just configured), and drive a clean ISP escalation when a circuit is down or degraded. This skill reads state and prepares escalations; it does not fail traffic over, change SD-WAN policy, or contact the carrier itself.

1. Establish the site's circuit topology: how many circuits, primary vs secondary, carrier and account per circuit, and the SD-WAN/edge platform. Pull documented circuit inventory (IT Glue — cross-reference circuit-inventory) and the edge device from the RMM.
2. Read current state per circuit. Where Liongard runs, read the environment's posture filtered to the SD-WAN/firewall platform (e.g. Meraki, Fortinet, VeloCloud, Palo Alto) for the edge inspector — read per-uplink status and the recent uplink up/down transitions. Confirm the inspector last ran and state dataprint age; where none exists, degrade to RMM reachability + documentation and say the check is partial.
3. Verify failover, not just presence: confirm the secondary circuit is up AND is configured in the failover/SD-WAN policy AND has recent evidence of carrying (or being able to carry) traffic. A secondary that is "up" but not in the policy is a silent single-point-of-failure — flag it.
4. For a down/degraded circuit, assemble the ISP escalation package: carrier, account/circuit ID, site address and demarc, the observed symptom with timestamps (from the uplink transition history), and what's already been checked. Confirm the current carrier support contact/process from documentation or a web search — do not guess a support path.
5. Classify the site: Healthy (all circuits up, failover verified), Degraded (running on one circuit / failover unverified), or Down. State which circuit is carrying traffic now.
6. Output a status summary per circuit plus the failover verdict and, if needed, the ready-to-send ISP escalation package. Leave it as a plain-text note (no markdown/emojis) or open a ticket. For a broader single-circuit outage, hand off to isp-outage-tracking.

Guardrails: "circuit is up" is not "failover works" — do not report a site as resilient without confirming the secondary is in the failover policy and viable. Trust Liongard/RMM data only after confirming the inspector/agent last ran; report dataprint age; circuit transition timestamps come from the timeline/inspector, not assumption. Verify carrier support contacts/process from documentation or current sources before escalating — never invent an ISP ticket number, phone number, or portal.
```
