---
name: Alert Reset With Note
description: Reset a NinjaOne alert only after the condition is genuinely healthy, posting an explanation note first. Attended or embedded in a recovery Flow.
category: Devices & Infrastructure
tools: [list_ninjaone_alerts, get_ninjaone_device, reset_ninjaone_alert, add_ticket_note]
connectors: [NinjaOne]
scope: single
flow: yes
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Alert Reset With Note

**When to use:** "Clear/reset the alert on <device>, it's fine now" — or a stale alert whose condition has visibly recovered.

**Run it:** on one alert/device · or as a Flow triggered when a recovery/alert-clear event lands on the ticket.

## Prompt

```
Close out a recovered RMM alert the safe way: verify healthy, write it down, then reset — strictly in that order. This needs the RMM connected; if it is not enabled, say the alert queue is unavailable and stop.

1. Identify the exact alert — pull the device's active alerts from the RMM and pin down the device, alert type, and message. If several match the description, list them and confirm which one; never reset on a fuzzy match.
2. Allowlist check. Eligible for reset here: device-offline (device back online), disk-space (space recovered), stopped-service (service running again), performance/CPU/memory threshold (readings back in range). NEVER reset and always leave for a human: security/EDR, backup failures, RAID/SMART/hardware-health, anything on a domain controller or hypervisor, and any type you cannot map to this allowlist. The allowlist is a ceiling, not a suggestion.
3. Verify healthy NOW by looking up the device in the RMM. Resolve the client organization then the device without stopping to ask mid-lookup, and don't trust a class filter — confirm the device class in its details. Offline alert -> device online with fresh last-contact; disk -> free space above threshold; service -> running. Alert text saying "recovered" is not verification; read current state. If verification fails or is inconclusive (device unreachable, stale data), do nothing and say why.
4. Recurrence check: if this same alert fired and was reset 3+ times in 30 days, do not silently reset — flag it as a chronic condition needing a root-cause ticket, and only reset if the requester still wants it after seeing that.
5. Leave the explanation note FIRST (plain text, no markdown/emojis): which alert, which device, the verified healthy state, and why it is being reset. No note, no reset.
6. Then reset the alert in the RMM. Resetting never closes the ticket — closure is a separate human decision.
7. Confirm in your reply: alert cleared, note posted, recurrence status if relevant.

Unattended (Flow) mode: your entire reply is posted verbatim as the plain-text note. Gates, all required: type on the allowlist AND current state verifies healthy AND recurrence under 3-in-30-days. Any gate fails or data is stale/capped -> do nothing, output one plain-text line stating why. Never sweep more than the single alert the Flow handed you.
```
