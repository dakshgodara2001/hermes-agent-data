---
name: kanban-operations
description: "Use when operating Hermes Kanban multi-agent workflows: orchestrator decomposition, worker lifecycle and handoffs, dependency graphs, recovery, goal-mode cards, and optional Codex lanes inside Kanban workers."
version: 1.0.0
platforms: [linux, macos, windows]
environments: [kanban]
metadata:
  hermes:
    tags: [kanban, multi-agent, orchestration, workers, codex, worktrees, recovery]
    related_skills: [coding-agent-delegation, hermes-agent]
---

# Hermes Kanban Operations Umbrella

## Overview

Use this skill for class-level Hermes Kanban work. It combines the orchestrator role, worker lifecycle, task graph design, dependency handling, completion/block handoffs, stuck-worker recovery, goal-mode cards, and optional Codex implementation lanes into one discoverable package.

## When to Use

- You are an orchestrator routing work across Hermes profiles.
- You are a Kanban worker that needs deeper lifecycle, handoff, or retry guidance.
- A user asks to decompose work into Kanban cards, inspect/repair a board, or recover stuck workers.
- A Kanban worker wants to use Codex as an isolated implementation lane while Hermes retains board ownership.

## Role Model

| Role | Responsibility | Do not do |
|---|---|---|
| Orchestrator | discover profiles, decompose, create dependency graph, summarize queued work | implement concrete subtasks yourself |
| Worker | orient with task state, work in assigned workspace, heartbeat, block/complete with structured handoff | call `clarify`, invent task IDs, mutate outside workspace |
| Codex lane | optional untrusted implementation helper inside a worker-run worktree | own Kanban lifecycle or replace Hermes verification |

## Orchestrator Workflow

1. Discover available profiles (`hermes profile list` or ask the user).
2. Extract independent lanes and true dependencies.
3. Create parent cards before children and pass `parents=[...]` at creation time.
4. Fan out independent lanes; fan in synthesis/review cards.
5. If no existing profile fits, ask the user instead of inventing an assignee.
6. Report queued cards, owners, and dependency order.

## Worker Workflow

1. `kanban_show` first; stop if task is blocked/archived/reassigned.
2. Respect `$HERMES_KANBAN_WORKSPACE` (`scratch`, `dir:<path>`, or `worktree`).
3. Read comments/runs to avoid repeating failed retry paths.
4. Work in bounded chunks and heartbeat only for meaningful long tasks.
5. For human decisions, add a context comment and `kanban_block(reason=...)` instead of `clarify`.
6. Use structured `kanban_complete(summary=..., metadata=...)`; for code needing review, block with `review-required:` and put details in comments.

## Dependency and Recovery Rules

- Use `parents=[...]` during creation for real gates; do not rely on prose such as "wait for T1".
- Capture successful `kanban_create` return values before listing `created_cards`; never invent `t_<hex>` IDs.
- Reclaim/reassign stuck workers through dashboard or `hermes kanban reclaim/reassign`.
- Goal-mode cards are for long acceptance-driven tasks; write explicit acceptance criteria and use budgets.

## Optional Codex Lane Inside Kanban

A Hermes worker may spawn Codex only as an isolated input lane. Required rules:

- Use a clean worktree/branch tied to the task ID.
- Prompt Codex with scope, ownership boundaries, prohibited actions, tests, and safety invariants.
- Monitor the process and kill if it requests secrets, drifts, or exceeds budget.
- Hermes reviews diffs, runs canonical tests, accepts/rejects/partially accepts changes, and writes `kanban_complete`/`kanban_block`.
- Include `metadata.codex_lane` with used/mode/worktree/branch/result/tests/artifacts.

## Absorbed Package References

Detailed pre-consolidation packages are preserved under `references/absorbed-packages/`:

- `references/absorbed-packages/kanban-orchestrator/`
- `references/absorbed-packages/kanban-worker/`
- `references/absorbed-packages/kanban-codex-lane/`

## Common Pitfalls

1. **Inventing assignees.** Unknown profiles silently sit in `ready` forever.
2. **Over-linking or under-linking.** Link only true data dependencies; keep independent work parallel.
3. **Completing instead of blocking for review.** Code-changing worker tasks usually need `review-required:` unless trivially terminal.
4. **Using `clarify` in headless workers.** Block the card instead.
5. **Trusting Codex self-report.** Codex output is untrusted until Hermes reviews and tests it.
6. **Losing package detail.** Keep absorbed package directories intact because they include templates and exact examples.

## Verification Checklist

- [ ] Existing profiles discovered before routing.
- [ ] Dependency graph uses `parents=[...]` for gates.
- [ ] Worker checked task state and workspace before acting.
- [ ] Handoffs include useful metadata, not vague prose.
- [ ] Human decisions use comments + block reasons.
- [ ] Codex lanes, when used, are isolated and independently verified.
