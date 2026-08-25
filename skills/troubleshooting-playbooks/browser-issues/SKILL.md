---
name: Browser Issues
description: Diagnose browser problems — one broken site, SSO loops, crashes, extension conflicts — using profile isolation and extension bisect, not clear-everything.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response]
---

# Browser Issues

**When to use:** One website misbehaves for a user (won't load, renders broken, buttons dead); sign-in loops on a web app ("keeps asking me to log in"); the browser crashes, eats memory, or shows a "managed by your organization" surprise; or "it works in <browser A> but not <browser B>".

**Run it:** on the one ticket you're working — a tech drives the isolations hands-on with the user, not unattended.

## Prompt

```
"Clear your cache" is the desk's coin-flip. Two cheap isolations place almost every browser
ticket in one of four branches: the profile, an extension, the SSO/cookie path, or the site.

Climb the Troubleshooting Ladder base skill first: past tickets for this site (many users,
same site, same day is the app's or vendor's ticket — check their status first), then the
documented standard: managed policies, required extensions, SSO architecture, filtering. Get
the exact browser version — managed fleets pin old builds, so a known-fixed rendering bug is
a policy fix, not an endpoint one — and whether it is managed. For a web app, read the
developer console (F12) red lines: a CSP violation, blocked third-party cookie or failed
request names the branch.

Both isolations first. A clean profile (or a private window, which usually disables
extensions too) tests both at once: clean sends you to branch 1 or 2, still broken to 3 or
4. Still broken in a second browser points at the site, the path or the OS — branch 4.

Branch:
1. Profile — a clean profile works and disabling extensions doesn't fix the old one:
   corrupted profile state (cookies, site data, service workers). Clear site data for that
   one site only, never the whole history or cookie store as an opening move, and say what
   any clearing logs the user out of first. For profile-wide corruption, a new profile with
   sync migration is the fix — name what isn't sync-backed and will be lost. Never handle
   saved passwords.
2. Extension bisect — disable all, confirm fixed, re-enable in halves until the culprit
   surfaces. A mandated security or filtering extension is changed by its owner (exclusion
   or update), never left off at the endpoint. An unmanaged extension injecting content is a
   security flag: pair with the security playbooks rather than removing it.
3. SSO and cookies — login loops, "works in incognito", auth dying at a redirect. Check
   third-party cookie blocking against what the SSO chain needs (phase-outs break older
   flows; read the vendor's guidance), device time skew, conditional-access or device-trust
   rules only met in a managed browser, and TLS inspection (console certificate errors point
   at the filtering owner). Never disable certificate warnings, SafeBrowsing, cookie
   protections or the web filter to make a site work; the fix belongs to the site, the
   filter policy or the SSO config.
4. Site-side — broken in every browser and profile. Check the filter or proxy logs for
   blocks (a category block works as designed: the unblock goes to the policy owner), DNS,
   and the site's status. If the site's code is at fault only its vendor can fix it: capture
   the console evidence and say so.

Verify with the user doing the failing action in their own profile, not the test one. Note
it (PSA Note Discipline base skill): isolations, branch, culprit, action, verification.
```
