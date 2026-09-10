---
name: Create KBA from Resolved Ticket
description: Run inside a resolved ticket to turn its notes into a formatted knowledge base article, ready to paste into your documentation platform.
category: Documentation
tools: [search_tickets]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity), Fewer Escalations & Less Noise]
---

# Create KBA from Resolved Ticket

**When to use:** A tech runs it from the slash command inside a resolved ticket that has detailed work notes, and wants a publish-ready article back in chat to paste into IT Boost, IT Glue, Hudu or a wiki. Use when the ticket has documented troubleshooting and fix steps worth keeping. For a looser draft that also checks the knowledge base for an existing article first, use `documentation/kb-article-draft` instead; this one always drafts new, in a fixed house format, with documentation metadata attached.

**Run it:** on one ticket.

## Prompt

```
Turn this resolved ticket into a knowledge base article, ready to copy and paste into
a documentation platform. Output the article in chat only. Never leave a note, a
reply, or any other write on the ticket.

1. Read the whole ticket: every message, internal note, and resolution note.
2. Use ONLY what the ticket documents. Never invent a step, cause, or command. Where
   something is missing, insert [NEEDS DETAIL: what is missing] inline and continue.
3. Generalize. Replace client, contact, and user names, hostnames, asset tags, IPs,
   and phone numbers with [Client], [User], [Hostname], [IP]. Keep verbatim: product
   names, versions, exact error text, file paths, process and service names, registry
   keys, commands, UI labels.
4. Output this structure every time, same headings, same order:

# [Platform]: "[exact error text]" Error
*Knowledge base article*

**Created:** today's date | **Version:** 1.0 | **Content owner:** [Content Owner]

**Revision history**
| Version | Date | Author | Change |
| 1.0 | today's date | [Content Owner] | Created from resolved ticket |

## Summary
Two paragraphs. First: what the user sees and when. Second: one sentence of cause,
one sentence of fix.

## Symptom
Bullets of observable behavior. Bold the exact error text.

## Cause
Prose on the mechanism, not a restatement of the symptom. Multiple causes become
bullets with the likely one flagged. Say what the ticket ruled out.

## Resolution
One intro line naming which option to prefer and any access, credentials, or tools
needed first, then numbered imperative steps. Use "### Option 1:" and "### Option 2:"
when the ticket shows more than one valid path, each restarting at 1. Disruptive
fixes go last, labeled fallback only.

## Verification
Numbered steps proving the fix worked, with the exact success output if the ticket
recorded one.

## Key Points
Five bullets. Bold the single most important fact. Include what a tech is most likely
to get wrong.

## Tags
Exactly 10, comma separated, lowercase except product names and filenames.

5. Title: use the error format above only when the ticket has exact error text,
   otherwise a plain descriptive title.
6. Leave [Content Owner] as a placeholder for the author to fill in. Never name the
   technician from the ticket.
7. Close with one line: "Gaps to fill:" and the list, or "Gaps to fill: none".

Rules: no em dashes, no jargon, never "solid" or "great". Bold UI paths and clickable
labels: **Tools > Task Manager**. Steps are imperative, written for a tech mid-ticket.
Drop dead-end troubleshooting the ticket shows did not fix, unless it was a needed
diagnostic step. Do not recap ticket history. Output the article and nothing before it.
```
