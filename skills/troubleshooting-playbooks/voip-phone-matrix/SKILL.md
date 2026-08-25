---
name: VoIP Phone Matrix
description: Diagnose VoIP problems: inbound calls failing, ring group misbehavior, one-way audio, dead phones, provisioning fails, by splitting phone vs site vs trunk.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# VoIP Phone Matrix

**When to use:** "Callers can't reach us" / inbound dies while outbound works (or vice versa); the ring group isn't ringing a user or calls route to the wrong place; one-way, choppy, or dropping audio; or a phone shows no registration or a new/replacement phone won't provision.

**Run it:** on the one ticket you're working — a tech works it and routes config/carrier changes to their owners; not unattended.

## Prompt

```
Voice tickets collapse once you know which layer is sick: handset, LAN path, platform
config, or trunk/carrier. Split on scope first, and treat one-way audio as what it usually
is: NAT or firewall, not the phone.

Climb the Troubleshooting Ladder base skill first: past phone tickets (voice breaks with
network changes, so a firewall or ISP ticket in the same window is likely the cause), then
the documented environment: platform or PBX vendor, trunk and carrier, phone models and
firmware, VLAN/QoS design, SIP ALG and firewall settings.

Scope split first: one phone is device, one group routing, a whole site trunk or network.
Inbound-only points at the carrier/DID layer, outbound-only at trunk auth or dial plans.
Then evidence: a call log or SIP trace for one failed call (time, caller, callee), the
phone's registration state, and MOS/jitter/loss where exposed.

Branch:
a. Inbound — do the platform logs show the call arriving? Silence means carrier or DID
   routing, which only they can fix: open the case. If it arrives, follow the inbound route,
   IVR and hours rules to where it dies; misfiring after-hours or holiday schedules, and
   their timezone, are the usual answer.
b. Ring groups — a member not ringing: registration state, DND and forwarding flags,
   simultaneous versus sequential strategy and timeouts, and whether the deskphone or app is
   the registered client. Check against documented intent; config often does exactly what it
   was wrongly told.
c. Trunk — site-wide failure. Registration or peering state, the carrier's status page,
   recent firewall or ISP work. A new public IP breaks IP-authenticated trunks, so check
   that first after ISP changes. A trunk down at the carrier is theirs alone: capture
   evidence and the case number.
d. Provisioning — a new or replacement phone is dead. Is its MAC registered in provisioning;
   can it reach the provisioning server (VLAN placement, phone DHCP options, filtered
   outbound); is firmware too old for current provisioning or TLS (check the vendor's
   minimum).
e. One-way audio — signaling works, RTP flows one way: NAT/firewall asymmetry until proven
   otherwise. SIP ALG on consumer and branch routers is the number-one culprit; then RTP
   port ranges, keep-alives and NAT settings per the platform's published firewall guide,
   pulled from the web, not recited. Choppy or robotic audio is jitter and loss: QoS,
   saturated uplink, Wi-Fi softphones; measure, don't guess. Firewall changes go to the
   network owner, never "just to test"; a path inside the ISP is their case.

Verify by placing the failing call type end to end, holding two-way audio a minute. Any
change touching trunks or outbound routing gets the post-change emergency-calling test (933)
— flag it explicitly. Note it (PSA Note Discipline base skill): scope split, branch,
evidence, fix or handoff with case numbers, verification.
```
