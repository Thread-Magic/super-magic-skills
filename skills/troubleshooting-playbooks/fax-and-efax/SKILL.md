---
name: Fax & eFax
description: Work fax tickets — dead analog lines, ATA fax page corruption, eFax cloud portals not sending or receiving — across the line, ATA, and portal matrix.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# Fax & eFax

**When to use:** Faxes aren't sending or being received on a physical fax machine; faxes partially transmit, arrive garbled, or fail only on long documents (classic ATA symptoms); an eFax portal / fax-to-email stopped working or inbound faxes stopped arriving; or a healthcare or legal client reports fax failure (treat as workflow-critical, not legacy).

**Run it:** on the one ticket you're working — a tech drives this with on-site staff and the carrier/vendor; not unattended.

## Prompt

```
Fax is compliance-anchored in healthcare, legal and finance, and fails at one of three
layers: the line (analog or its VoIP replacement), the ATA bridging the machine onto VoIP,
or the eFax service that replaced it. Identify the layer first. For healthcare clients, ask
what the fax carries and whether an interim path exists; the workflow may need a bridge
before the fix.

Climb the Troubleshooting Ladder base skill first: past fax tickets, then the documented
architecture, the carrier or eFax vendor, the numbers and where they terminate, ATA
make/model/firmware. POTS is being retired widely, so a "line" that used to work may not be
analog any more; check too for a phone-system replacement or eFax vendor change.

Evidence: failing direction, error code or transmission report, total versus partial failure
(mid-page, long documents), one failed fax — number, time, page count.

Branch:
- Analog line — total failure on a POTS machine. Plug a handset into the wall jack: dial
  tone or not is the fork. No dial tone is a carrier ticket (line fault, or a quiet POTS
  retirement) — nobody on the desk fixes copper. Dial tone but no fax is the machine or its
  settings: test against a known-good number.
- ATA / fax over VoIP — partial pages, garbled output, long-document failures: fax on a
  compressed voice path. Check the ATA's fax handling per its documentation — T.38 relay
  versus G.711 pass-through, and ECM on the machine; a mismatch with what the carrier's
  platform supports is the usual cause. Stepping baud down to 9600 is a legitimate
  stabiliser. If settings match vendor guidance and it still fails, only the carrier can
  confirm T.38 end to end: hand over the failed-call examples.
- eFax service — check the vendor's status page, then the boring causes: inbound
  notifications in spam or quarantine, a changed password breaking portal login, a sender
  not on the authorized list, attachments outside the vendor's format or size limits. A
  failing platform or a misrouted ported number is a vendor case with fax IDs and
  timestamps.
- Receive-only — sends fine, nothing arrives: a recent port, carrier migration or forwarding
  change can silently route inbound faxes elsewhere. Send from a known source and trace
  where it lands; wrong routing is the carrier's.

Never read, transcribe or attach fax content to a ticket: for healthcare and legal clients
it is regulated. Reference metadata (time, page count, destination) only. Don't promise
reliability on a voice-optimized path: healthcare-grade fax means T.38 end to end or a cloud
eFax service — a recommendation, not an action taken.

Verify with a test fax in the failing direction, evidenced by a transmission confirmation or
portal record; for compliance-sensitive clients, name that artifact. Note it (PSA Note
Discipline base skill): architecture, direction, branch, evidence, vendor case,
verification.
```
