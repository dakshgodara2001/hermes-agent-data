---
name: github-workflows
description: "Use when working with GitHub repositories end-to-end: authentication, repo/remotes/releases, issues, pull requests, code review, CI checks, and repository inspection. Consolidates gh-first and curl/API fallback workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, gh-cli, git, PRs, issues, code-review, CI, repositories, releases]
    related_skills: [requesting-code-review, coding-agent-delegation]
---

# GitHub Workflows Umbrella

## Overview

Use this skill for class-level GitHub operations. It unifies authentication, repository management, issues, PR lifecycle, PR/code review, CI troubleshooting, releases, and codebase inspection. Prefer `gh` when authenticated; fall back to `git` + GitHub REST/GraphQL with `GITHUB_TOKEN` when needed.

## When to Use

- The user asks to inspect, clone, create, fork, push, release, or back up a GitHub repo.
- You need to create/triage/update issues or pull requests.
- You need to review a PR or diff, post comments, or manage CI failures.
- You need codebase statistics/language breakdowns before planning or reporting.

## Safety Defaults

- Never commit, push, merge, close, delete branches, or post public comments unless the user asked for that side effect.
- For website/UI work, preview locally and wait for approval if the user asked to see changes before pushing.
- Always inspect `git status --short --branch` before changing repo state.
- Do not expose tokens in logs; prefer `gh auth status` and environment variables.

## Auth and Context Detection

```bash
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  AUTH=gh
else
  AUTH=curl
fi
REMOTE_URL=$(git remote get-url origin 2>/dev/null || true)
OWNER_REPO=$(printf '%s' "$REMOTE_URL" | sed -E 's|.*github\.com[:/]||; s|\.git$||')
OWNER=${OWNER_REPO%%/*}
REPO=${OWNER_REPO#*/}
```

Authentication sources: `gh auth login/status`, `GITHUB_TOKEN`, `~/.hermes/.env`, SSH remotes, and credential helpers. Use least-privilege tokens and never print secrets.

## Repository Management

Use for clone/create/fork/remotes/releases/backups. Verify remotes and branches before writes:

```bash
git status --short --branch
git remote -v
gh repo view --json nameWithOwner,defaultBranchRef,isPrivate
```

Secret-safe backups and project pushes belong under this class: scan for `.env`, keys, build artifacts, and large files before pushing to a remote.

## Issues

Use issue templates for feature requests and bug reports when available. Include reproduction steps, expected/actual behavior, environment, labels, assignees, and links to related PRs. Prefer `gh issue create/edit/comment/list` with REST fallback.

## Pull Request Lifecycle

1. Start from updated base branch.
2. Create a scoped branch.
3. Make changes with file tools or a delegated coding agent.
4. Run verification.
5. Commit with Conventional Commits.
6. Push and create a PR.
7. Monitor CI and fix failures.
8. Merge only with explicit approval or established repo policy.

Useful commands:

```bash
git fetch origin
git checkout main && git pull origin main
git checkout -b feat/descriptive-name
git add <files> && git commit -m 'feat: concise summary'
git push -u origin HEAD
gh pr create --title 'feat: concise summary' --body-file /tmp/pr-body.md
gh pr checks --watch
gh pr merge --squash --delete-branch
```

## Preview-before-push Rule

When the user asks to preview local changes before syncing/pushing:

1. Create/keep a branch and make local edits.
2. Run build/tests.
3. Serve or export a local preview.
4. Report URL/path, changed files, and git status.
5. Stop before commit/push until approval.

## Code Review

For reviews, gather the exact diff (`gh pr diff`, `git diff base...head`, or REST diff), inspect affected files, and return findings with severity, path, line, evidence, and fix suggestion. Avoid nitpicks unless requested. If posting comments, use GitHub review APIs only after verifying paths/line positions.

## CI Troubleshooting Loop

```bash
gh pr checks
gh run list --branch $(git branch --show-current) --limit 5
gh run view <run-id> --log-failed
# fix -> test locally -> commit -> push -> watch checks
```

Repeat a bounded number of times and report blockers with the failed job/log excerpt.

## Codebase Inspection

Use pygount/cloc-like inspection when a high-level repo report is needed. Exclude vendored/build directories and report LOC by language, generated code ratio, and notable structure.

## Support Files

This umbrella may contain namespaced files copied from absorbed skills:

- `references/github-auth/*` — auth helpers and shell snippets.
- `references/github-code-review/*` — review output templates and REST review details.
- `references/github-pr-workflow/*` — CI troubleshooting and commit conventions.
- `references/github-repo-management/*` — API cheatsheets and secret-safe backup/push recipes.
- `templates/github-issues/*`, `templates/github-pr-workflow/*` — issue/PR body templates.
- `scripts/github-auth/*` — reusable auth environment helpers.

## Common Pitfalls

1. **Assuming `gh` is authenticated.** Check first and fall back explicitly.
2. **Using stale line positions for PR comments.** Re-fetch the diff immediately before inline reviews.
3. **Pushing secrets.** Scan before initial project pushes/backups.
4. **Merging without CI/user approval.** Wait for green checks and explicit scope.
5. **Preview bypass.** If the user asked to see UI changes before pushing, stop at preview.

## Verification Checklist

- [ ] `git status --short --branch` inspected.
- [ ] Auth method determined and secrets not printed.
- [ ] Target owner/repo/base/head confirmed.
- [ ] Templates/checklists used for issues/PRs/reviews as appropriate.
- [ ] CI or local verification run when code changes are involved.
- [ ] All public side effects were requested by the user.
