---
name: RD Gateway Issues
description: Fix Remote Desktop Gateway and RD Web Access problems: external RDP failures, certificate errors, CAP/RAP policy mismatches, and MFA integration failures.
category: Troubleshooting Playbooks
tools: [search_tickets, search_knowledge_base, search_itglue, search_hudu, add_ticket_note, web_search]
connectors: [IT Glue, Hudu]
scope: single
flow: no
role: [Technician]
outcome: [Faster Resolution & Response, Risk & Compliance]
---

# RD Gateway Issues

**When to use:** External users can't connect through RD Gateway / RD Web or connections drop at the gateway, certificate warnings appear connecting, some users/resources connect while others don't (authorization suspicion), or RD Web sign-in / the MFA prompt in front of the gateway fails.

**Run it:** on the one ticket you're working — a tech works the gateway hands-on; not unattended.

## Prompt

```
RD Gateway tunnels RDP over HTTPS so internal desktops are reachable without exposing raw
RDP, and fails at four gates: the certificate, the Connection Authorization Policy (who may
connect), the Resource Authorization Policy (what they may reach), and any MFA layer in
front.

Climb the Troubleshooting Ladder base skill first: past RDS tickets — a certificate renewal
(sudden onset on a date is a cert until proven otherwise), a CAP/RAP or group change, an MFA
rollout, a firewall change on 443 — then the documented deployment: roles in play (Gateway,
Web Access, Broker, Session Hosts), the external FQDN and its certificate (issuer, expiry,
SAN), the CAP/RAP design, the MFA layer.

Evidence: the exact client message or code: certificate-trust, "not authorized to connect"
and can't-reach-the-gateway are three different problems — plus the Operational log under
Microsoft-Windows-TerminalServices-Gateway, which records the CAP and RAP evaluated per
connection and why one was denied.

Branch:
1. Certificate — trust or name errors, or failures right after a renewal; the most common
   gateway break. It must be valid, trusted by clients (public CA or trusted internal
   chain), match the external FQDN in its SAN, and be bound in RD Gateway Manager and across
   every RDS role — a renewed certificate has a new thumbprint and often was never
   re-applied to all. Treat it as a change (see the certificate-renewal and PKI playbooks).
2. CAP — "not authorized to connect to this gateway": the user isn't in a group the CAP
   allows, its device or authentication requirements aren't met (smart card, a specific
   method), or CAP ordering denies them. The log names the CAP evaluated; fix the membership
   or condition.
3. RAP — reaches the gateway but not the target host: the RAP doesn't grant that user group
   access to that resource group or computer — classically a new session host never added to
   the RAP group. Read the RAP the log evaluated and add the resource.
4. MFA — sign-in fails at the MFA step, or the gateway rejects the connection after it. With
   the NPS extension for Entra MFA or a RADIUS 2FA the gateway defers to a central NPS or
   RADIUS server, so an extension error, a shared-secret or timeout problem, an unregistered
   user or a Conditional Access interaction all block it. Read those logs and pair with the
   RADIUS/NPS playbook. Never disable MFA to get someone in.

Never work around this by exposing RDP (3389) to the internet — the exposure the gateway
exists to prevent. Never create allow-all CAP or RAP policies. Shared secrets are
credentials: name the RADIUS client in a note, never the secret.

Verify with a real external user reaching their resource through the gateway past MFA, no
warnings. Note it (PSA Note Discipline base skill): client error, the CAP and RAP evaluated,
certificate state, MFA path, branch, action, verification.
```
