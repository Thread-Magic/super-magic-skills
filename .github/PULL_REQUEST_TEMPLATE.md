<!--
Adding or updating a skill? Thanks! Fill in the summary and run the checklist below.
New to this? Read CONTRIBUTING.md (4 steps) and copy TEMPLATE.md to start.
Not sure about the exact format? SKILL-FORMATTING-AGENT.md is the full spec.
-->

## What this adds or changes

<!-- One or two lines: the skill(s) added/updated and the workflow they solve. -->

## Checklist

- [ ] One folder per skill at `skills/<category>/<slug>/SKILL.md`, kebab-case slug under an existing category
- [ ] Started from [`TEMPLATE.md`](../blob/main/TEMPLATE.md) — frontmatter has `name`, `description` (the *trigger*), `category`, `tools`, `connectors`, `scope`, `flow`, `role`, `outcome`
- [ ] Every tool in `tools:` exists in [`research/tool-catalog.md`](../blob/main/research/tool-catalog.md), and **no tool names appear in the prompt** (write natural English — "change the status", not `update_ticket`)
- [ ] `connectors:` lists any integration the prompt needs, and the prompt **degrades gracefully** when it's absent (`[]` if native-only)
- [ ] `role:` and `outcome:` use only the fixed values in [`research/taxonomy.md`](../blob/main/research/taxonomy.md)
- [ ] Guardrails are **inline in the prompt** (confidence gate before writes, "show me before you send/close", "when in doubt, do nothing", result-cap honesty, never invent data)
- [ ] **No private data** — no client/partner names, people, hostnames, credentials, ticket IDs, or environment-specific board/status names (use placeholders)
- [ ] Ran `python3 tools/gen_catalog.py` to refresh the README catalog
- [ ] Tested the prompt in Super Magic against a real tenant

<!-- On merge to main, the docs site (docs.getthread.com/skill-library) picks this up automatically. -->
