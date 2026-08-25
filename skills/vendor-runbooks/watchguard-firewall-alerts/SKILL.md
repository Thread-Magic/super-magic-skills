---
name: WatchGuard Firewall Alerts
description: Triage WatchGuard events: Firebox offline in WatchGuard Cloud, AuthPoint MFA push and token trouble, and mobile VPN authentication failures on the desk.
category: Vendor Runbooks
tools: [search_tickets, search_clients, search_contacts, search_itglue, get_ninjaone_device_link, add_ticket_note, update_ticket]
connectors: [NinjaOne]
scope: single
flow: no
role: [Technician, Security & Compliance Owner]
outcome: [Risk & Compliance, Faster Resolution & Response]
---

# WatchGuard Firewall Alerts

**When to use:** A "Firebox offline / not connected to WatchGuard Cloud" alert lands; users can't complete AuthPoint MFA (push not arriving, token codes rejected); or mobile VPN (SSLVPN/IKEv2) authentication is failing for one user or many.

**Run it:** on the alert ticket.

## Prompt

```
Triage a WatchGuard event: Firebox appliances, AuthPoint MFA, and the mobile VPNs behind
them. Console checks, log review, AuthPoint changes and config edits are technician actions
you direct and record. Verify certificate and firmware facts in the console; never invent
detail.

1. Firebox offline → device-offline-runbook logic with the firewall twist: "offline" in
   WatchGuard Cloud means the management tunnel is down, not necessarily the site. Check
   other site alerts and user tickets first. Cloud management down
   while the site passes traffic is an ISP blip or the appliance's outbound path: low
   urgency, still investigate. Site down → network-outage-triage: power, ISP, then the
   appliance; an unreachable firewall is a full-site event. Never close on "it came back"
   without noting the gap window and checking prior tickets — a nightly flap is an
   ISP/DHCP/power problem ticket.

2. AuthPoint MFA — identity first. Verify the requester on a number on file before touching
   MFA state (same canon as duo-mfa-anomalies) — MFA "help" is a takeover vector; the
   channel it came from is not proof. Push not arriving → mobile side first (notifications,
   connectivity, app signed in); token codes rejected → device clock drift. Pushes the user
   didn't initiate → the password is burned: rotate now and have the technician review the
   auth logs; a push approved by mistake goes to compromised-account-containment.
   Re-enrollment on a new phone follows the verified-identity ladder — remove the old token
   first. No standing bypasses: anything issued is time-boxed and logged.

3. VPN auth failures — scope decides the branch. One user → credential state upstream
   (AuthPoint, RADIUS, the directory), client version, their network; walk
   vpn-troubleshooting. Many at once → the server-side chain (Firebox, authentication
   server, directory): check certificate expiry on the VPN portal, auth-server health and
   recent config changes. Mass failure right after a config or certificate change is that
   change until proven otherwise. Repeated failures for one account from unfamiliar sources,
   with no user at the keyboard, is credential stuffing — a security event
   (security-alert-response), never resolved by unlocking the account again.

4. Note what was checked in which console, the verdict and outcome — plain text, no
   markdown or emojis (apply the PSA Note Discipline base skill). Firewall config changes
   run under the client's change process, never as routine ticket work. Escalate hardware or firmware
   suspicion to WatchGuard support with a package: serial, firmware version, cloud status
   history, log excerpts, what was ruled out. For hands-on work, deep-link the tech to
   the device in the RMM.

Without console visibility, say the view is partial and name what the tech should pull. When
in doubt do nothing irreversible and escalate.
```
