---
name: Mac Fleet Management
description: Review the Macs a client has under RMM management — agent health, macOS version and update posture, disk/encryption basics, and awareness of a separate MDM owning updates. Use when someone asks "how are the Macs looking", a Mac-specific rollout is planned, or a macOS ticket needs fleet context.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, get_ninjaone_device_activities, list_ninjaone_alerts, get_ninjaone_device_link, connectwise_rmm_search_devices, search_itglue, search_hudu, add_ticket_note, create_ticket]
connectors: [NinjaOne, ConnectWise RMM, IT Glue, Hudu]
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Time & Cost Savings (Capacity)]
---

# Mac Fleet Management

**When to use:** "How are <client>'s Macs doing?" / "Which Macs are behind on macOS updates?", planning a macOS major-version upgrade, or a Mac user's ticket needs fleet context.

**Run it:** across a client's Mac fleet, on demand (not a Flow — it's a posture review, not a per-ticket event).

## Prompt

```
One-pass posture review of a client's Mac population in the RMM: which Macs are checking in, what macOS versions they run, which are behind, and whether an MDM (Jamf, Mosyle, Kandji, Intune) — not the RMM — owns update policy. Requires an RMM; if none is enabled, fall back to documentation + ticket history and do not fabricate fleet data.

1. Resolve the client organization, then look up its devices in the RMM (whichever is connected) and filter to macOS devices. Verify the OS in each device's details rather than trusting class filters alone. If the listing may have capped, report "at least N Macs".
2. Agent health first: group by last-contact time. Macs silent >~7 days are the top finding — macOS permission prompts (Full Disk Access, background items) silently break agents after OS upgrades, so call that out as the likely cause for agents that went quiet right after an update.
3. Version posture: tabulate macOS versions across the fleet. Flag versions past Apple's support window (Apple publicly patches roughly the current and two previous major versions — verify against Apple's current documentation before asserting a specific cutoff) and Macs more than one minor release behind.
4. Per-Mac depth where warranted: read the device details for disk free space and pending updates; pull the device's alerts and recent activity for recent failures on the Macs that look unhealthy.
5. MDM overlap check: consult documentation (IT Glue / Hudu) for whether a Mac MDM manages this client. If an MDM owns updates/config, the RMM's job is monitoring only — do not report "RMM can't push updates" as a gap, and route update actions to the MDM owner.
6. Output: fleet summary (count, agent-health buckets, version spread), a ranked issue list (silent agents, unsupported versions, low disk), and per-issue handoff — a deep link into the device in the RMM for hands-on work, or the MDM console for policy work. Offer to open tickets per issue or leave a plain-text note (no markdown/emojis).

Guardrails: this integration cannot run scripts or push macOS updates — every remediation is a deep-link or MDM handoff, never an action you performed. Do not state Apple's exact support policy from memory as fact; frame it as the general pattern and recommend verifying against Apple's current security-release documentation. A Mac missing from the RMM is not necessarily unmanaged — it may be MDM-only by design; check documentation before flagging a coverage gap.
```
