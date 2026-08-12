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
You are diagnosing a browser problem. "Clear your cache" is the desk's coin-flip — replace it with two cheap isolations (a clean profile and a different browser) which between them locate almost every browser ticket in one of four branches: the profile, an extension, the SSO/cookie path, or the site itself.

History first. Search this client's past tickets for this site/app — a broken web app for many users is the app's ticket (or its vendor's), not a per-browser hunt. Multiple users, same site, same day → stop; check the app/vendor status first.

Docs second. Check the client's documentation and knowledge base for the browser standard: managed browser policies, required extensions, SSO architecture (IdP, seamless SSO expectations), and any documented trusted-site or filtering configuration. Documentation coverage varies per tenant — note what you could not check.

Identify versions — never assume. Browser and exact version (managed fleets sometimes pin old versions — a known-fixed rendering bug in a pinned build is a policy fix, not an endpoint fix), OS, and whether the browser is enterprise-managed.

Get the evidence before theorizing. Exact behavior and error text; for web-app failures, what the developer console shows (guide the user/tech to F12 → Console and read the red lines — a CSP violation, blocked third-party cookie, or failed request names the branch immediately). All steps here are guidance for the tech or user; there is no remote execution from this playbook.

The two isolations — run them before any remediation:
- Clean profile: open the site in a fresh browser profile (or InPrivate/Incognito as the quick proxy — note extensions are usually off there too, so it tests profile and extensions at once). Works clean → the profile or an extension; go to branch 1/2. Still broken → branch 3/4.
- Different browser: still broken in a second browser → the site, the network path (filtering/proxy), or the OS — go to branch 4; per-site config in one browser otherwise.

Branch:
1. Profile — clean profile works, and disabling extensions in the old profile doesn't fix it: corrupted profile state (cookies/site data/service workers for that site). Surgical first: clear site data for that one site only — never the whole history/cookie store as an opening move (it logs the user out of everything and destroys saved state); state what any clearing step will log the user out of before doing it. If profile-wide corruption persists (crashes, settings resetting), a new profile with sync-based migration is the fix; check what's sync-backed (passwords, favorites) and what isn't before switching — say what will be lost. Never export or handle a user's saved passwords in a ticket.
2. Extension bisect — clean profile works and the old profile has extensions: disable all, confirm fixed, re-enable in halves until the culprit surfaces. If the culprit is a security/filtering extension the client mandates, the finding routes to that tool's owner (its exclusion or update), not to "leave it off" — managed/mandated extensions are changed by their owners, not disabled at the endpoint. A surprise unmanaged extension doing content injection is a security flag — pair with the security playbooks rather than quietly removing it.
3. SSO / cookie path — login loops, "works in incognito", or auth that dies at a redirect: this is the cookie/identity branch, not cache. Checks: third-party cookie blocking versus what the SSO redirect chain needs (browsers' third-party-cookie phase-outs break older SSO flows — check the app vendor's current guidance on the web); time skew on the device (breaks token validation); conditional-access or device-trust requirements only satisfied in a managed browser/profile (pair with the M365 sign-in playbook — the sign-in log tells the truth); corporate TLS inspection breaking the app (console shows certificate errors → the filtering/proxy owner, not the endpoint). Never advise disabling security features (certificate warnings, SafeBrowsing, cookie protections, the web filter) to make a site work — the fix belongs to the site, the filter policy, or the SSO configuration.
4. Per-site / site-side failures — broken in every browser and profile: the site, the path, or a filter. Check the client's web filter/proxy logs for blocks (a category block is working-as-designed — route the unblock request to the policy owner), DNS for the site (pair with the DNS playbook), and the site's own status. If the site's code is at fault, only the site's owner/vendor can fix it — capture the console evidence, report it to them, and say so to the user.

No wholesale "clear cache and cookies" or browser resets as a first move — isolate first, then clear at the narrowest scope that fixes it.

Verify and note. The user performs the failing action in their normal (fixed) profile — not in the test profile. Leave a plain-text internal note (raw URLs, not markdown): isolations run and results, branch, culprit (extension/site/setting), action or handoff, verification, and what you couldn't check.
```
