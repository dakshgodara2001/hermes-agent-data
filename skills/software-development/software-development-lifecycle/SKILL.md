---
name: software-development-lifecycle
description: "Use when planning, debugging, testing, reviewing, simplifying, or safely evolving software. Consolidates lifecycle workflows such as spikes, TDD, systematic debugging, debugger attachment, code review, cleanup, and project refreshes."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [software-development, debugging, testing, review, refactor, lifecycle]
    related_skills: []
---

# Software Development Lifecycle

## Overview

This umbrella covers the class-level discipline for changing software safely: exploratory spikes, test-first development, root-cause debugging, language/runtime debugger attachment, review before commit, simplification, and incremental project refreshes. Use one labeled subsection instead of loading a separate micro-skill for each phase.

## When to Use

- The user asks to fix a bug, diagnose failures, attach a debugger, or explain root cause.
- The user asks to implement a feature with tests or asks for TDD.
- The user asks for code review, security/quality checks, cleanup, simplification, or refactoring.
- The user asks for a throwaway experiment/spike to validate feasibility.
- The user asks to maintain a specific website/app while preserving existing style and Git safety.

## Mode Selection

| Mode | Former narrow skill(s) | Trigger | Core behavior |
|---|---|---|---|
| Systematic debugging | `systematic-debugging` | Failing tests, production bugs, confusing behavior | Reproduce, localize, identify root cause, add regression test, then fix. |
| Python debugger | `python-debugpy` | Need Python REPL/DAP/pdb inspection | Start with minimal repro, use pdb/debugpy only after static inspection and tests identify the area. |
| Node inspector | `node-inspect-debugger` | Need Node.js `--inspect` / Chrome DevTools Protocol | Attach to the correct process, set breakpoints, inspect state, then verify with tests. |
| TDD | `test-driven-development` | New behavior or bug fix where tests are feasible | RED-GREEN-REFACTOR; prove test fails before implementation when practical. |
| Spike | `spike` | Unknown feasibility or API behavior | Build a disposable tracer; preserve only findings and reusable commands. |
| Code review | `requesting-code-review` | Pre-commit/pre-PR review | Inspect diff, security, tests, edge cases; auto-fix safe issues. |
| Simplify code | `simplify-code` | Recent changes feel overcomplicated | Compare behavior, remove abstraction, keep tests green, avoid semantic drift. |
| Project refresh | `portfolio-website-refresh` | Incremental website/product polish | Preserve approved visual identity, preview locally, use Git checkpoints. |

## Standard Safe-Change Loop

1. **Orient.** Inspect repository structure, current branch, dirty state, and relevant files. Do not assume context from memory.
2. **Establish evidence.** Reproduce the issue, failing test, current behavior, or visual baseline.
3. **Choose the mode.** Use the table above and say which discipline governs the work.
4. **Make the smallest useful change.** Prefer narrow diffs; keep experiments isolated if in spike mode.
5. **Verify with real commands.** Run tests, linters, builds, browser previews, or debugger checks as appropriate.
6. **Review the diff.** Ensure every modified file is intentional and no secrets/generated junk are included.

## Debugging Completion Criteria

A debugging task is not complete until:

- The failure is reproduced or a clear blocker is documented.
- A root cause is named in terms of code/data/control flow, not symptoms.
- The fix is exercised by a regression test or an equivalent verification command.
- The final report includes the failing and passing evidence.

## Review / Refactor Completion Criteria

- Tests/builds relevant to the changed area ran successfully or blockers are explicit.
- The diff is smaller or clearer without changing intended behavior.
- Any security-sensitive paths, config, credentials, or external calls were inspected.

## Common Pitfalls

- Do not jump to edits before reproducing or reading the relevant code.
- Do not use a debugger as a substitute for a hypothesis; use it to test one.
- Do not keep spike code unless the user asked to ship it.
- Do not claim verification from imagined output; include actual command results.

## Verification Checklist

- [ ] Repository state inspected before edits.
- [ ] Correct lifecycle mode selected.
- [ ] Evidence gathered before and after the change.
- [ ] Diff reviewed and summarized.
