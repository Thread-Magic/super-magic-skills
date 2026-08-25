---
name: Teams Call Quality
description: Fix Microsoft Teams call quality: choppy audio, robotic voice, frozen video, and drops via CQD-style device, machine, and network path layer isolation.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Teams Call Quality

**When to use:** "My Teams calls are choppy/robotic/echoing" or video freezes for one user; a whole office reports bad Teams calls (especially at certain times of day); drops/reconnects mid-meeting or "your network is causing poor quality" banners; or complaints only on calls with specific others (direction matters). Teams sign-in/crash/feature problems belong to teams-issues instead.

**Run it:** on the one ticket you're working — a tech runs the isolation tests hands-on; not unattended.

## Prompt

```
Call quality is a path problem: headset, machine, Wi-Fi or LAN, firewall or ISP,
Microsoft. Place the impairment on that path with evidence before recommending anything.

Climb the Troubleshooting Ladder base skill first: one user points at their device or home
network, one site at that LAN, Wi-Fi or ISP, everyone everywhere at Microsoft service
health — reference the incident and stop. "Choppy" hides four faults: do they sound bad to
others (uplink) or others to them (downlink)? Echo comes from whoever does not hear it;
robotic voice is loss, talk-over is latency, freeze-then-catch-up is jitter.

Get numbers first. In-call statistics need no CQD, and the Teams admin center's per-user
call history gives per-leg loss, RTT and jitter and names the degraded leg. Sustained loss
over 1–2%, RTT over 200–300 ms, or jitter over 30 ms is audible. Say when per-leg data was
unavailable.

1. Headset and device — one user, others hear them badly, stats clean. The most skipped
   branch, and half of all "network issues": Bluetooth headsets drop to handsfree codecs,
   hubs and docks starve audio, the wrong device is selected. Test the built-in mic and
   speaker on the same call type; clean built-in means the headset, dongle or driver.

2. Machine — stats fine, audio still bad, fans roaring. CPU starvation degrades encode
   first: check utilization during a call for AV scans, tab sprawl or 4K backgrounds.

3. Wired versus Wi-Fi — the decisive test. Same machine and call pattern on Ethernet:
   clean on wire and bad on Wi-Fi is wireless (mid-call AP roaming, congested 2.4 GHz,
   weak signal) — hand to wifi-network-troubleshooting. Bad on both is upstream. It also
   separates a home user's Wi-Fi from their ISP; advise, don't manage — it's theirs.

4. Site network path — many users, or a wired user still bad. Is media forced through a
   full-tunnel VPN when split-tunnel is Microsoft's guidance? That is a design flaw to
   raise, not a per-user fix. Is a proxy or inspection device chewing UDP — media needs
   UDP 3478-3481 to Microsoft's published ranges, and TCP fallback degrades badly. Never
   ask for inspection off wholesale — the ask is Microsoft's documented media-endpoint
   bypass, routed to the security owner. Then peak saturation, then QoS, which helps only
   where the gear enforces DSCP end to end. Design changes go to the network owner.

5. The far end — bad only with one external party is their path, and per-leg analytics
   names the degraded side. Offer the evidence rather than churning the local network;
   beyond the client's edge, document and report to the ISP.

Success is a test call with clean per-leg stats plus the user's confirmation over days —
one good call proves nothing. Note it (apply the PSA Note Discipline base skill): symptom
and direction, stats found, isolation results, branch, action or routing.
```
