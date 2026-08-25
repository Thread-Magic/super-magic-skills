---
name: Outlook Client Issues
description: Diagnose Outlook desktop crashes, hangs, broken search, password prompts, and crash-on-send using profile, data-file, and add-in isolation branches.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Outlook Client Issues

**When to use:** Outlook crashes, hangs on load, or freezes on specific actions; "Outlook keeps asking for my password" (after M365 sign-in is ruled healthy); search returns nothing / mail missing in Outlook but visible in web; or a crash/hang on send, especially with certain content or one recipient.

**Run it:** on the one ticket you're working — a tech works the isolation steps with the user; not unattended.

## Prompt

```
You are diagnosing an Outlook desktop problem. Isolate before you remediate, and gate the two
big hammers — OST rebuild and profile recreation — behind explicit criteria.

Climb the Troubleshooting Ladder base skill first: this user's past tickets and the same symptom
across the client (many users after a patch cycle is an Office build regression — verify it on
the web before touching machines), then the client's documentation for the Office standard:
channel and build policy, required add-ins, shared-mailbox patterns. Establish the exact Outlook
build and update channel, the OS version, and new versus classic Outlook.

Then two cheap isolation splits, in order. Outlook on the web: reproducing there means mailbox
or service-side, so stop treating the client. Then safe mode: if the problem vanishes it is an
add-in or view corruption, not the profile. For crashes, read the Application event log first —
the faulting module names the culprit half the time.

Branch:

1. Add-ins — safe mode is clean. Disable all COM add-ins and re-enable in halves until the
   culprit is found. If it is a required business add-in, look for an update and be honest when
   only the add-in vendor can fix it; the interim is running without it, with the client's
   sign-off.

2. OST and cached data — search broken, mail on the web but not the desktop, sync errors, "data
   file cannot be accessed". Rebuild only on OST corruption evidenced in the event log,
   persistent sync errors after a send/receive reset, or vendor guidance for that error. Deleting
   the OST re-syncs mailbox data but destroys unsent drafts and local-only PST-side data: check
   for local PSTs and unsent items first, and say so. Large mailboxes take hours to re-sync — set
   that expectation.

3. Profile — repeated password prompts with healthy sign-in logs, a profile that won't load, or
   autodiscover errors. Build a new profile alongside the old; never delete the old one first.
   Recreate only when the new one works where the old fails. Both failing identically means it is
   not the profile — go back to isolation.

4. Crash on send — name the pattern first. One recipient is a corrupt autocomplete entry: clear
   that single entry, not the whole cache. One message is a corrupt draft or attachment. Every
   send is an add-in in the send pipeline, branch 1. Only with a signature is the signature
   template, image, or signature tool. The pattern names the fix.

When the defect is a Microsoft build regression or an add-in bug, say plainly that the vendor
must fix it and give the documented workaround only — verified against current vendor
documentation on the web, never asserted from memory.

Verify by reproducing the original failing action. Then leave a plain-text internal note (apply
the PSA Note Discipline base skill): build, isolation results, branch, faulting module if any,
action, verification.
```
