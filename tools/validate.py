#!/usr/bin/env python3
"""Validate every skills/<category>/<slug>/SKILL.md against the library format.

Run from the repo root:

    python3 tools/validate.py            # check every skill
    python3 tools/validate.py skills/security/phishing-triage/SKILL.md   # check some

Exit 0 when clean, 2 when anything fails.

The hard rule this exists for: **a prompt block may not exceed 3,000 characters.**
Super Magic caps skill instructions and Flow agent prompts at 3,000; an over-limit
skill still runs but can no longer be saved, so a longer skill here is a skill a
partner cannot actually use. Authors should aim for ~2,900 to leave editing room.

Everything else here restores checks the repo lost when the internal research/ tree
and tools/gen_catalog.py were removed in 778823d. The allowed-value lists below come
from that commit -- recover the originals with:

    git show 778823d^:research/tool-catalog.md
    git show 778823d^:SKILL-FORMATTING-AGENT.md

Why these checks and not others: every failure mode below is **silent** on the docs
site. A role that isn't in the fixed list doesn't error, it just drops the skill out
of that filter; a multi-line YAML list parses as empty; a dead cross-reference slug
sends a reader nowhere. None of it surfaces until someone notices a gap.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROMPT_MAX = 3000

FRONTMATTER_KEYS = [
    "name", "description", "category", "tools",
    "connectors", "scope", "flow", "role", "outcome",
]
LIST_KEYS = {"tools", "connectors", "role", "outcome"}

ROLES = {
    "Technician", "Dispatcher", "Service & Ops Manager", "CSM / Account Manager",
    "Security & Compliance Owner", "Sales & Business Development",
    "MSP Owner / Leadership",
}
# "Staff Enablement" is real: CONTRIBUTING.md documents it (skills whose value is making
# your OWN people faster -- training, coaching, ramp). It postdates the 778823d snapshot
# these lists were seeded from, so the inlined set was missing it while six shipped skills
# already used it.
OUTCOMES = {
    "Faster Resolution & Response", "Fewer Escalations & Less Noise",
    "Time & Cost Savings (Capacity)", "Always-On Coverage", "Risk & Compliance",
    "Retention & Growth (CSAT/Expansion)", "Staff Enablement",
}
# "Runbooks" is real: the runbook tool family is in-app AND needs the partner to have
# built a runbook library, so tool-catalog.md graded it connector-grade. CONTRIBUTING
# dropped it by accident when the lists were inlined.
CONNECTORS = {
    "NinjaOne", "Liongard", "IT Glue", "Hudu", "TimeZest", "Notion", "Linear",
    "ConnectWise RMM", "ImmyBot", "Microsoft 365", "Runbooks",
}
SCOPES = {"single", "global", "both"}
FLOWS = {"yes", "no"}

# From research/tool-catalog.md. Member-MCP families (Notion, Linear) were listed with
# a trailing "..." there, so those are matched by prefix in tool_is_known().
TOOLS = {
    # native reads
    "search_tickets", "search_clients", "search_contacts", "search_members",
    "search_knowledge_base", "search_thread_docs", "web_search", "list_boards",
    "list_ticket_statuses", "list_ticket_priorities", "list_recap_templates",
    # native writes
    "add_ticket_note", "update_ticket", "create_ticket", "assign_contact",
    "log_time_entry", "merge_ticket", "schedule_ticket", "list_schedule_entries",
    "update_schedule_entry",
    "send_approval", "run_assistive_ai",
    # in-app SuperAgent only
    "view_openDraft", "view_save", "view_list", "view_duplicate", "view_getCurrent",
    "view_listFilterAttributes", "view_searchFilterValues",
    "load_skill", "create_skill", "update_skill", "list_skills", "run_skill_on_ticket",
    "create_recap", "get_next_thread", "send_client_email",
    # runbooks (connector-grade)
    "list_ticket_runbooks", "recommend_runbooks", "search_runbooks",
    "get_runbook_form_link", "open_runbook_form",
    # admin: flows & intents
    "list_flows", "get_flow", "create_flow", "update_flow", "activate_flow",
    "list_flow_actions", "list_flow_filter_attributes",
    "list_flow_filter_attribute_values",
    "list_intents", "get_intent", "create_intent", "update_intent",
    "create_variation", "update_variation", "set_variation_arguments",
    "set_variation_replies",
    # TimeZest
    "create_timezest_scheduling_request", "get_timezest_scheduling_requests",
    "list_timezest_appointment_types", "list_timezest_resources",
    # NinjaOne
    "list_ninjaone_organizations", "search_ninjaone_devices", "get_ninjaone_device",
    "get_ninjaone_device_activities", "get_ninjaone_device_link",
    "list_ninjaone_alerts", "reset_ninjaone_alert", "list_ninjaone_windows_services",
    "control_ninjaone_windows_service", "reboot_ninjaone_device",
    "set_ninjaone_device_maintenance", "set_ninjaone_device_approval",
    # Liongard
    "liongard_environment", "liongard_launchpoint", "liongard_alert",
    "liongard_detection", "liongard_metric", "liongard_events", "liongard_timeline",
    "liongard_device", "liongard_identity", "liongard_domain",
    "liongard_cyber_risk_dashboard", "liongard_report", "liongard_agents",
    "liongard_query",
    # docs connectors
    "search_itglue", "search_hudu",
    # ImmyBot
    "search_immybot_computers", "list_immybot_tenants", "get_immybot_computer",
    "list_immybot_maintenance_sessions",
    # Linear (member MCP)
    "list_issues", "get_issue", "create_issue", "update_issue", "create_comment",
    "list_projects", "list_cycles", "list_teams", "list_issue_labels",
}
TOOL_PREFIXES = ("notion-", "connectwise_rmm_")

# Tool names must never appear in a prompt -- Super Magic is native-English, so an
# author writes "change the status", not update_ticket. Only flag the unambiguous
# ones: several catalog entries (list_teams, get_issue) are ordinary English as well.
TOOL_NAMES_BANNED_IN_PROMPT = sorted(
    t for t in TOOLS if "_" in t and not t.startswith("liongard_")
)

# skills/localized/* carry translated preamble headings, so the English labels below
# are absent by design. Checked for structure, not for those two strings.
LOCALIZED = "localized"


def parse_list(raw: str) -> list[str]:
    """Parse an inline-flow list. Multi-line YAML block lists parse as empty upstream,
    which is exactly the silent failure we want to catch, so don't be lenient here."""
    raw = raw.strip()
    if not (raw.startswith("[") and raw.endswith("]")):
        return None
    inner = raw[1:-1].strip()
    if not inner:
        return []
    out, cur, quote, depth = [], "", None, 0
    for ch in inner:
        if quote:
            if ch == quote:
                quote = None
            else:
                cur += ch
        elif ch in "\"'":
            quote = ch
        elif ch == "(":
            depth += 1
            cur += ch
        elif ch == ")":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def tool_is_known(tool: str) -> bool:
    return tool in TOOLS or tool.startswith(TOOL_PREFIXES)


def split_skill(text: str):
    """-> (frontmatter_text, body). Returns (None, None) if the fences are missing."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    return m.group(1), text[m.end():]


def check(path: Path, all_slugs: set[str], all_categories: set[str],
          slug_categories: dict[str, str]) -> list[str]:
    errs = []
    text = path.read_text(encoding="utf-8")
    category, slug = path.parent.parent.name, path.parent.name

    fm_text, body = split_skill(text)
    if fm_text is None:
        return ["missing or malformed --- frontmatter block"]

    # Only top-level unindented keys, matching the docs-site parser.
    fm = {}
    for line in fm_text.splitlines():
        if line[:1].isspace() or not line.strip() or line.lstrip().startswith("#"):
            continue
        k, sep, v = line.partition(":")
        if sep:
            fm[k.strip()] = v.split("#")[0].strip() if k.strip() in LIST_KEYS else v.strip()

    for key in FRONTMATTER_KEYS:
        if key not in fm:
            errs.append(f"frontmatter missing `{key}:`")
    if errs:
        return errs

    if not fm["name"]:
        errs.append("`name:` is empty")
    if not fm["description"]:
        errs.append("`description:` is empty")
    if fm["scope"] not in SCOPES:
        errs.append(f"scope: {fm['scope']!r} -- must be one of {sorted(SCOPES)}")
    if fm["flow"] not in FLOWS:
        errs.append(f"flow: {fm['flow']!r} -- must be yes or no")

    # The directory is the page identity on the docs site; category: is cosmetic, so a
    # mismatch is invisible there and misleading here.
    expect = category.replace("-and-", " & ").replace("-", " ").title()
    expect = expect.replace(" & ", " & ")
    if fm["category"].lower().replace(" & ", " and ").replace(" ", "-") != category:
        errs.append(
            f"category: {fm['category']!r} does not match its directory {category!r} "
            f"(expected something that slugifies to {category!r}, e.g. {expect!r})"
        )

    for key, allowed in (("role", ROLES), ("outcome", OUTCOMES),
                         ("connectors", CONNECTORS), ("tools", None)):
        vals = parse_list(fm[key])
        if vals is None:
            errs.append(
                f"{key}: must be an inline flow list like [A, B] -- a multi-line "
                f"YAML block list parses as empty on the docs site"
            )
            continue
        if key == "tools":
            for t in vals:
                if not tool_is_known(t):
                    errs.append(f"tools: {t!r} is not a real Super Magic tool")
            continue
        if key in ("role", "outcome"):
            if not vals:
                errs.append(f"{key}: must name 1-2 values")
            elif len(vals) > 2:
                errs.append(f"{key}: {len(vals)} values -- the format allows at most 2")
        for v in vals:
            if key == "connectors" and v.startswith("Zapier"):
                # "Zapier: <App>" names the app a skill actually drives. Bare "Zapier"
                # is reserved for the app-agnostic case -- zapier-action-discovery
                # sweeps every app, so pinning it to one would be a lie.
                if v != "Zapier" and not re.fullmatch(r"Zapier: .+", v):
                    errs.append(
                        f"connectors: {v!r} -- a Zapier entry is written "
                        f'"Zapier: <App>" and must be quoted (the colon breaks the list)'
                    )
                continue
            if v not in allowed:
                errs.append(f"{key}: {v!r} is not in the fixed list (see CONTRIBUTING.md)")

    # --- body ---------------------------------------------------------------
    h1 = re.search(r"^# (.+)$", body, re.M)
    if not h1:
        errs.append("body has no `# Title` heading")
    elif h1.group(1).strip() != fm["name"]:
        errs.append(f"H1 {h1.group(1).strip()!r} does not match name: {fm['name']!r}")

    if category != LOCALIZED:
        if "**When to use:**" not in body:
            errs.append("body is missing the `**When to use:**` line")
        if "**Run it:**" not in body:
            errs.append("body is missing the `**Run it:**` line")

    if "## Prompt" not in body:
        errs.append("body is missing the `## Prompt` heading")

    fences = re.findall(r"^```\n(.*?)\n```$", body, re.S | re.M)
    if len(fences) != 1:
        errs.append(f"expected exactly one ``` prompt block, found {len(fences)}")
        return errs

    prompt = fences[0]
    if len(prompt) > PROMPT_MAX:
        errs.append(
            f"prompt block is {len(prompt):,} characters -- the limit is "
            f"{PROMPT_MAX:,}. Super Magic will refuse to save it. Tighten the prose "
            f"or compose with a base skill (see CONTRIBUTING.md -> Base skills)."
        )

    for tool in TOOL_NAMES_BANNED_IN_PROMPT:
        if re.search(rf"\b{re.escape(tool)}\b", prompt):
            errs.append(
                f"prompt names the internal tool {tool!r} -- write plain English "
                f'instead ("change the status", "leave a note")'
            )

    # Cross-references matter -- a renamed skill silently strands every prompt that
    # pointed at it, and base skills make that load-bearing. Only the path-qualified
    # form is checked: a bare slug is indistinguishable from ordinary hyphenated
    # English ("end-of-day", "token-based-auth"), so checking those is all false
    # positives. Write a reference as `<category>/<slug>` to get it verified.
    # Limitation worth knowing: a path pointing at a slug that exists nowhere cannot be
    # told apart from prose that happens to use a slash ("security/multi-user forces
    # high"), so only a wrong *category* is reported -- the case that actually breaks
    # when a skill is moved between folders.
    for cat, ref in re.findall(r"\b([a-z0-9-]+)/([a-z0-9]+(?:-[a-z0-9]+)+)\b", prompt):
        if cat in all_categories and ref in all_slugs and slug_categories[ref] != cat:
            errs.append(
                f"prompt references {cat}/{ref}, but {ref!r} lives in "
                f"{slug_categories[ref]}/"
            )

    return errs


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    if argv:
        paths = [Path(a).resolve() for a in argv]
    else:
        paths = sorted((root / "skills").glob("*/*/SKILL.md"))

    all_slugs = {p.parent.name for p in (root / "skills").glob("*/*/SKILL.md")}
    all_categories = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    slug_categories = {p.parent.name: p.parent.parent.name
                       for p in (root / "skills").glob("*/*/SKILL.md")}

    failed = 0
    for p in paths:
        errs = check(p, all_slugs, all_categories, slug_categories)
        if errs:
            failed += 1
            rel = p.relative_to(root) if p.is_relative_to(root) else p
            print(f"\n{rel}")
            for e in errs:
                print(f"  - {e}")

    print(f"\n{len(paths)} skills checked, {failed} with problems.")
    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
