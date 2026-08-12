---
name: Flow Backup Export
description: Dump every flow definition to a JSON or markdown snapshot for archive and diffing — a read-only point-in-time backup of the desk's automation, no restore.
category: Automation & Flows
tools: [list_flows, get_flow]
connectors: []
scope: global
flow: no
role: [Service & Ops Manager]
outcome: [Risk & Compliance]
---

# Flow Backup Export

**When to use:** "Back up all our flows" / "snapshot the flow definitions so I can diff them later" / "export every flow to JSON / markdown for the archive" / before a big automation cleanup, or to establish a known-good baseline.

**Run it:** across all of the desk's flows — manually on demand (Flows can't schedule an export, so there's no Flow trigger for this one).

## Prompt

```
Capture a full point-in-time snapshot of every flow's definition to archive or diff.
Member-invoked only; no unattended variant (Flows can't schedule an export).

1. List every flow, then open each one to pull the full definition:
   trigger, filter conditions, actions, notification targets, and enabled/disabled state.
   Capture faithfully — the dump must reflect exactly what each flow definition contains;
   never summarize away fields that matter for a diff, and never fabricate a flow or field.

2. Serialize the collection into the requested format:
   - JSON — the faithful machine-readable dump, best for diffing two snapshots.
   - Markdown — a human-readable one-section-per-flow rendering, best for review/archiving.

3. Stamp the snapshot with the capture date/time and the flow count at the top, so a later
   diff knows what it's comparing.

4. Deliver the file/content and state clearly: this is a point-in-time snapshot that EXPORTS
   definitions but CANNOT re-import or restore them — it's for archive and diff, not
   recovery. Don't imply a snapshot can be "loaded back". Re-running produces a fresh one.

Don't include secrets — if a flow definition surfaces credential-like values, note their
presence rather than dumping them in plain text into an archive.
```
