---
name: Auvik Network Monitoring
description: Triage Auvik network alerts: separate device-down, interface-down, and config-change events, and use the topology map to spot cascades early.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, add_ticket_note, update_ticket]
connectors: []
scope: single
flow: yes
role: [Technician]
outcome: [Fewer Escalations & Less Noise, Faster Resolution & Response]
---

# Auvik Network Monitoring

**When to use:** An Auvik alert lands (device down/unreachable, interface down/errors, or a configuration change); a "the network is down at <site>" report needs structured triage against the topology; or Auvik alert volume is high and someone asks which alerts are noise / what to retune.

**Run it:** on the alert ticket · or as a Flow (triggered when a matching Auvik alert ticket is created).

## Prompt

```
Triage an Auvik network-monitoring alert. Console, polling, collector and config actions are
technician steps you direct and record. Verify feature names against Auvik's documentation;
never invent detail.

1. Classify the family first:
   - Device down / unreachable — Auvik can't poll it. Separate truly down from unreachable
     by Auvik: lost path, changed SNMP credentials or community, or a dead collector.
     Confirm the site's collector is healthy before trusting a wave of "down" alerts — a
     dead collector fakes a site-wide outage.
   - Interface down or errors. An access-port flap on an endpoint is minor; an uplink or
     trunk down between switches is a cascade source — read which interface on which device.
   - Configuration change — the config backup/diff caught an edit: planned and authorized,
     or unexpected?

2. Use topology before chasing symptoms: open the device on the map and check its upstream
   parent. If a parent switch, router or firewall is down, the alerts behind it are children
   of one root cause — work the parent, not each leaf. Name the root device and the cascade,
   and merge symptom tickets into the root.

3. Respond by family. Device down with a healthy collector and parent → the device itself:
   power, site, recent change, maintenance window. Parent is the site edge or ISP → possible
   circuit outage; correlate other site devices and check for an ISP advisory. Uplink or
   trunk down → potential network partition. Interface errors climbing → cabling,
   duplex or optics: degradation, not a clean down. Config change → check prior tickets and
   the client's change policy; an unexpected change on network gear is an outage risk and a
   possible security event, never assumed benign.

4. Check recurrence over 30-90 days for the same device, interface or site: a link that
   flaps nightly is a chronic problem ticket, never a repeated one-off close.

5. Repeated self-clearing or benign alerts from one device, interface or site — flapping
   access ports, an accepted degraded link, a retired device still polled — go to
   alert-noise-assessment for a quantified retune: threshold, dedup window, or auto-close of
   self-healing pairs. Recommend the retune; never suppress or disable monitoring silently,
   and prefer a threshold change to removing a check that could catch a real failure.

6. Note the family, root vs symptom, verdict, recurrence and, for config changes,
   authorized or not; set the priority. Plain text, no markdown or emojis (apply
   the PSA Note Discipline base skill). As a Flow, apply the classification and note
   directly and flag any config or security judgment for a human.

Without documentation the topology intent and change policy may be unknown — say so and
name what the tech should confirm on the map. When in doubt do nothing irreversible and
escalate.
```
