---
name: coding-agent-delegation
description: "Use when delegating software-development work to autonomous coding CLIs such as Claude Code, OpenAI Codex, or OpenCode. Covers choosing an agent, safe prompt construction, print vs interactive modes, tmux monitoring, worktrees, permissions, verification, and cleanup."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding-agents, delegation, claude-code, codex, opencode, tmux, worktrees, PR-review]
    related_skills: [hermes-agent, github-pr-workflow, requesting-code-review, subagent-driven-development]
---

# Coding Agent Delegation Umbrella

## Overview

Use this skill when Hermes should hand off coding work to an external autonomous coding CLI. It consolidates provider-specific operational knowledge for Claude Code, OpenAI Codex, and OpenCode into one class-level workflow: select the right agent, run it in the right mode, constrain permissions, monitor progress, verify real changes, and clean up sessions/worktrees.

## When to Use

- A coding task is large enough to benefit from a second agent or isolated autonomous worker.
- The user explicitly asks to use Claude Code, Codex, or OpenCode.
- You need a PR review, refactor, bug fix, test generation, or repository-wide code search by another CLI agent.
- You want an independent implementation/review pass but will verify the result yourself.

## When NOT to Use

- A single direct file edit or one test command is enough.
- The task needs the user to answer prompts during the child agent run.
- You cannot provide a bounded, self-contained prompt and working directory.
- The requested side effect is dangerous and scope is unclear.

## Agent Selection Matrix

| Agent | Best for | Default mode | Notes |
|---|---|---|---|
| Claude Code | Deep refactors, PR reviews, multi-file reasoning, slash-command workflows | `claude -p` print mode for one-shots; tmux interactive for iterative sessions | Use `--max-turns`, `--allowedTools`, `--output-format json`; tmux is best for TUI monitoring. |
| OpenAI Codex CLI | Focused implementation/review in repos where Codex is configured | non-interactive command where possible; PTY/tmux if interactive | Keep prompts explicit about verification commands and no unapproved pushes. |
| OpenCode | Alternative coding CLI for feature/PR review work | non-interactive first, interactive only when needed | Useful as an independent reviewer/implementer when installed. |

## Universal Delegation Workflow

1. **Gather context first.** Determine repo path, branch state, task scope, test commands, and forbidden side effects.
2. **Choose isolation.** Prefer a feature branch or worktree for implementation. For reviews, avoid writes or restrict tools.
3. **Write a bounded prompt.** Include objective, paths, constraints, verification commands, output format, and whether commits/pushes are allowed.
4. **Constrain permissions.** Use read-only modes for review and targeted write/bash permissions for implementation.
5. **Run with a turn/time budget.** Use max turns/budget flags when the CLI supports them.
6. **Monitor.** For TUI agents, run inside tmux and capture panes rather than losing state.
7. **Verify yourself.** Inspect diffs and run tests/lints in Hermes after the child reports success.
8. **Clean up.** Kill tmux sessions, note worktree paths, and do not leave hidden background agents running.

## Claude Code Quick Reference

Prefer print mode for one-shot tasks:

```bash
claude -p 'Review this diff for bugs and security issues. Return findings with file:line.' --max-turns 1
claude -p 'Fix the failing tests in src/auth. Run pytest tests/auth and summarize changes.' --allowedTools 'Read,Edit,Bash' --max-turns 10 --output-format json
```

Use tmux for interactive sessions:

```bash
tmux new-session -d -s claude-work -x 140 -y 40
tmux send-keys -t claude-work 'cd /path/to/repo && claude' Enter
sleep 5 && tmux capture-pane -t claude-work -p -S -40
```

Important Claude Code pitfalls:

- `--dangerously-skip-permissions` dialogs default to a safe exit in interactive mode; handle with Down then Enter only when explicitly intended.
- `--max-turns` is print-mode only.
- `--bare` is fastest but requires API-key style auth and skips CLAUDE.md/plugins/MCP unless explicitly supplied.
- Monitor context health in long sessions and compact/clear when the agent becomes context-heavy.

## Codex and OpenCode Quick Reference

Because flags vary by installed version, start by checking the CLI help/version and prefer the least-interactive invocation supported by that installation. If a command opens a TUI, wrap it in tmux so you can capture output and send follow-up input.

Prompt pattern:

```text
You are working in /path/to/repo on branch <branch>. Task: <specific task>.
Constraints: do not push, do not edit unrelated files, do not install global packages.
Verification: run <commands>. Report changed files, tests run, failures, and remaining risks.
```

## PR Review Pattern

For read-only reviews, pipe the exact diff or checkout the PR in a temporary worktree and tell the agent not to modify files. Require actionable findings with severity, path, line, reasoning, and suggested fix. Then independently validate any claimed issue before posting a review.

## Absorbed Package References

Provider-specific historical packages are preserved under `references/absorbed-packages/`:

- `references/absorbed-packages/claude-code/`
- `references/absorbed-packages/codex/`
- `references/absorbed-packages/opencode/`

## Common Pitfalls

1. **Trusting child-agent self-reports.** Always verify diffs, tests, and generated artifacts yourself.
2. **Unbounded prompts.** Missing max turns, budgets, or allowed tools can create runaway cost/time.
3. **Wrong working directory.** Always set or `cd` to the intended repo.
4. **Interactive prompts without tmux.** TUI agents are hard to monitor unless launched in tmux.
5. **Letting agents push/merge without approval.** State commit/push boundaries explicitly.
6. **Leaving sessions behind.** Kill or document tmux sessions/worktrees.

## Verification Checklist

- [ ] Agent CLI exists and auth/status is healthy, or failure is reported.
- [ ] Prompt includes repo path, task scope, constraints, verification, and output expectations.
- [ ] Permissions/tools are restricted to the task.
- [ ] Hermes independently inspected changes and ran relevant checks.
- [ ] Background sessions/worktrees are cleaned up or reported.
