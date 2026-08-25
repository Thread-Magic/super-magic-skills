<!--
Adding or updating a skill? Thanks! Fill in the summary and run the checklist below.
New to this? Read CONTRIBUTING.md (4 steps) and copy TEMPLATE.md to start.
-->

## What this adds or changes

<!-- One or two lines: the skill(s) added/updated and the workflow they solve. -->

## Checklist

- [ ] One folder per skill at `skills/<category>/<slug>/SKILL.md`, kebab-case slug under an existing category
- [ ] Started from [`TEMPLATE.md`](../blob/main/TEMPLATE.md) — frontmatter has `name`, `description` (the *trigger*), `category`, `tools`, `connectors`, `scope`, `flow`, `role`, `outcome`
- [ ] `tools:` are real Super Magic tools, and **no tool names appear in the prompt** (write natural English — "change the status", not `update_ticket`)
- [ ] `connectors:` lists any integration the prompt needs, and the prompt **degrades gracefully** when it's absent (`[]` if native-only)
- [ ] `role:` and `outcome:` use only the fixed values listed in [`CONTRIBUTING.md`](../blob/main/CONTRIBUTING.md)
- [ ] The **prompt block is under 3,000 characters** — Super Magic won't save a longer skill. `python3 tools/validate.py` checks this (and everything else here that a machine can check)
- [ ] Guardrails are **inline in the prompt** (confidence gate before writes, "show me before you send/close", "when in doubt, do nothing", result-cap honesty, never invent data)
- [ ] **No private data** — no client/partner names, people, hostnames, credentials, ticket IDs, or environment-specific board/status names (use placeholders)
- [ ] Tested the prompt in Super Magic against a real tenant
- [ ] `python3 tools/validate.py` passes

<!-- On merge to main, the docs site (docs.getthread.com/skill-library) picks this up automatically. -->
