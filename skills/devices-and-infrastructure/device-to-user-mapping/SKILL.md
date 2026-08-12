---
name: Device-to-User Mapping
description: Answer "who uses this device" or "what device does this user have" by combining RMM last-logged-on data with contact records, ticket history, and documentation. Use whenever a ticket names a person but not a machine, or a machine but not a person.
category: Devices & Infrastructure
tools: [search_ninjaone_devices, get_ninjaone_device, search_contacts, search_tickets, search_itglue, add_ticket_note]
connectors: [NinjaOne, IT Glue]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Device-to-User Mapping

**When to use:** "What PC does <user> use?" before remoting in, "who uses <device>?" when an alert fires, or an offboarding/refresh needs a person's device list.

**Run it:** on one user or one device, on demand (not a Flow — it's a lookup a tech reaches for mid-ticket).

## Prompt

```
Resolve the person<->machine link in either direction using every signal available, and report the answer with its confidence. This needs the RMM connected for the live-logon signal; degrade to contacts + docs + ticket history if absent and say the live signal is missing.

1. Determine direction: user->device or device->user.
2. User->device: look up the person (client, full name, aliases/usernames). Then pull the client's devices from the RMM and match on last-logged-on user against likely usernames (first.last, flast, etc. — state which convention matched). Cross-check documented asset assignments (IT Glue) and ticket history for tickets naming the user's machine. A user can map to multiple devices (desktop + laptop + kiosk) — return all with last-contact recency.
3. Device->user: resolve the device (organization first; rank candidates by org match then last-contact; verify class in the details — don't trust a class filter). Read the last-logged-on user from the device details, resolve that username back to a contact, corroborate with documentation and recent tickets.
4. Weigh signals and assign confidence:
   - High: the RMM last-logged-on matches a documented assignment, or matches consistently across recent history.
   - Medium: the RMM shows the user but documentation is silent or stale.
   - Low: signals conflict, the device is shared (multiple recent users, kiosk naming), or the last logon is weeks old.
5. Flag special cases instead of forcing an answer: shared devices (last-logged-on is whoever touched it last), service accounts as last logon, terminal servers (many users, no owner), recently reimaged machines (mapping reset).
6. Output: the mapping with confidence and evidence per signal, conflicts called out, and — when docs disagree with reality — an offer to note the discrepancy for documentation cleanup (plain text, no markdown/emojis).

Guardrails: last-logged-on user is a hint, not ownership — never present it as the assigned user without corroboration, and never on shared/multi-user devices. Do not contact or act against a person on a low-confidence mapping; say the confidence and what would raise it. Username-to-contact matching is heuristic — show the matched pattern so a human can sanity-check. Result-cap honesty when device/ticket searches may be truncated.
```
