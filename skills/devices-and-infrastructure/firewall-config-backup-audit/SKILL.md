---
name: Firewall Config Backup Audit
description: Verify that every firewall's current configuration is actually backed up and recent — via Liongard change history or the vendor's own backup state — and flag any device whose config backup is missing or stale. Use for "are our firewall configs backed up", before a firmware change, or a config-backup posture review.
category: Devices & Infrastructure
tools: [liongard_launchpoint, liongard_timeline, liongard_detection, liongard_metric, search_itglue, create_ticket, add_ticket_note]
connectors: [Liongard, IT Glue]
scope: global
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Firewall Config Backup Audit

**When to use:** "Are all our firewall configs backed up?", before a firewall firmware upgrade or rule change (rollback point), or a config-backup posture review.

**Run it:** across a client's firewalls, on demand (not a Flow — it's a posture audit, not a per-ticket event).

## Prompt

```
Answer one question with evidence: for each firewall, is the current running config captured somewhere restorable, and how fresh is it? Surface every gap before it becomes a rebuild-from-scratch incident. Best run with Liongard; if absent, degrade to documentation + vendor-backup evidence and say the audit is partial.

1. Enumerate firewalls in scope. Where Liongard runs, read the environment's posture filtered to firewall platforms (e.g. Palo Alto, Fortinet, SonicWall, Meraki, WatchGuard, Cisco ASA) to list each device's inspector and last successful run. Cross-reference the documented firewall inventory (IT Glue) so a firewall that exists but has no inspector is caught as a blind spot, not silently omitted.
2. For each firewall, determine config-backup state from the best signal:
   - Liongard as the read plane: its change timeline and detections show whether the inspector is capturing config changes and when it last did (a captured, dated config-change history is evidence the config is being read and versioned); read the last-config-capture timestamp or firmware/config fields where exposed.
   - Vendor-native backup (cloud-managed controller export, appliance auto-backup, or a documented scheduled export) where that is the client's mechanism — confirm from documentation which mechanism is authoritative per device.
3. Classify each firewall: Backed up & fresh (current config within cadence), Stale (backup older than cadence — state how old), or No backup / unverifiable (no inspector, inspector not running, or no vendor-backup evidence). Always state the age of the most recent captured config and the dataprint age of the Liongard source.
4. For every gap, note likely cause (inspector absent/failing, vendor backup not configured, credentials expired) and the remediation owner — do not present a gap as fixed.
5. Output an audit table: firewall, site, source of truth, last config capture (with age), status, specific gap/remediation. Flag Stale and No-backup rows first. Leave a plain-text note (no markdown/emojis) or open a ticket to track remediation.

Guardrails: distinguish "the inspector ran" from "the config is backed up" — confirm the client's actual restore mechanism from documentation before calling a firewall protected. Trust Liongard data only after confirming the inspector last ran successfully; always report dataprint/last-capture age. A firewall with no inspector and no vendor-backup evidence is "unverifiable", never assumed fine. This skill reads and reports only — it does not create, trigger, or configure any backup. Never expose firewall credentials, config contents, or environment identifiers.
```
