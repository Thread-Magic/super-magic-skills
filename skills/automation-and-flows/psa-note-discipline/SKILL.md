---
name: PSA Note Discipline
description: Base skill defining how a note or reply is written when it may sync to a PSA — plain text, internal vs client-visible, and what never goes in a permanent record.
category: Automation & Flows
tools: [add_ticket_note]
connectors: []
scope: both
flow: yes
role: [Technician, Service & Ops Manager]
outcome: [Faster Resolution & Response]
---

# PSA Note Discipline

**When to use:** Writing or reviewing any skill that leaves a note, updates a ticket, or drafts a reply on a desk whose tickets sync to ConnectWise, Autotask, or HaloPSA — which is most of them. Also when a skill's notes are arriving in the PSA as literal asterisks and broken links.

**Run it:** on one ticket · across a set · or as a Flow — it's a base contract you fold into any skill that writes.

## Prompt

```
A note is a permanent record. It outlives the ticket, gets read by someone who wasn't
there, and on most desks it syncs into the PSA. Write every note to that standard.

1. Plain text, always. A note that may reach a PSA carries no markdown, no emojis, and
   no markdown links — PSAs render none of it, so `**urgent**` arrives as literal
   asterisks and a linked word arrives with the URL missing entirely. Write raw URLs in
   full. Use blank lines and plain "1." numbering for structure, not headers or bullets
   with special characters. A Thread-only note may render markdown, but if you cannot
   confirm the destination, assume it syncs.

2. Internal or client-visible — decide before you write, never after. An internal note
   carries the diagnosis, what you ruled out, the raw error, and what to try next. A
   client-visible note carries what happened, what it means for them, and what happens
   next. Never let internal reasoning, vendor blame, or a colleague's name-and-shame
   land in a client-visible note. When in doubt, write it internal.

3. What a note must contain. What you found, what you did, how you verified it, and
   what's next. A note that says "looked into it" is not a record. Quote errors and
   codes verbatim — they are what makes the ticket searchable next time.

4. What never goes in. Credentials, API keys, tokens, full account numbers, MFA codes,
   or the contents of a password reset. If you found one, say a credential was found and
   where, never what it was. No speculation stated as fact, and no invented ticket
   numbers, links, versions, or documentation — a value you could not verify does not
   appear in a permanent record.

5. Length matches the stakes. A routine action is one or two lines. A diagnosis someone
   will re-read in six months earns the detail. Padding a note to look thorough makes it
   less useful, not more.

6. Timestamps and attribution. Say when something was verified, not just that it was.
   "Confirmed printing at 14:20 after the spooler restart" beats "confirmed working" —
   the reader needs to know how stale your evidence is.

If the note is the entire output of an unattended Flow run, apply the Unattended Output
Discipline base skill too: the reply IS the note, with no narration around it.
```
