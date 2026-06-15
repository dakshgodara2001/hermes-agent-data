---
name: hermes-cron-operations
description: "Operate and troubleshoot Hermes scheduled cron jobs: inspect failures, separate scheduler/provider/script/delivery faults, convert simple shell jobs to script-only mode, and verify runs."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, cron, scheduler, troubleshooting, automation]
---

# Hermes Cron Operations

Use this skill when a user asks why Hermes cron jobs are failing, wants scheduled jobs audited, or needs a reliable scheduled automation built from shell scripts.

## Core diagnostic workflow

1. **List jobs first**
   - Use the cron job manager to inspect every job's `last_status`, `last_error`, `last_delivery_error`, schedule, delivery target, script, and `no_agent` setting.
   - Do not assume a missing delivered message means the job failed; delivery can fail independently from execution.

2. **Read the saved cron output**
   - Check `~/.hermes/cron/output/<job_id>/...md` for the user-facing failure summary.
   - Check `~/.hermes/cron/jobs.json` for persisted `last_error` and current job definition.

3. **Check runtime logs for the real failure boundary**
   - `~/.hermes/logs/agent.log` usually shows whether the job failed before the agent ran, during an LLM provider call, inside a tool call, or during delivery.
   - `last_delivery_error: null` plus an agent/provider exception means delivery was not the cause.
   - Telegram/network warnings near the same time are not proof of cron failure unless the job status shows a delivery error.

4. **Determine which layer failed**
   - **Scheduler layer:** job did not fire; check gateway/cron ticker status and next run.
   - **Agent/provider layer:** logs show API/client/model error before any tool execution.
   - **Script/tool layer:** terminal/tool output contains non-zero exit or traceback from the script.
   - **Delivery layer:** job ran successfully but `last_delivery_error` is set or platform send fails.

5. **Run the underlying command directly**
   - If the job prompt wraps a shell command, run that command outside the cron agent to confirm whether the script itself works.
   - Verify real artifacts: cache files, output text, pushed commits, or other expected side effects.

## Durable fix pattern for simple shell-based jobs

If a cron job's only purpose is to run a deterministic command or script, prefer script-only cron mode instead of asking an LLM agent to interpret a prompt and call `terminal`.

1. Create a wrapper under `~/.hermes/scripts/`:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$HOME/.hermes/bin"
python3 some_job.py
```

2. Make it executable:

```bash
chmod +x ~/.hermes/scripts/some_job.sh
```

3. Update the cron job:

- `script`: wrapper filename, relative to `~/.hermes/scripts/`
- `no_agent`: `true`
- `deliver`: keep existing delivery semantics

This removes provider/model/API fragility from deterministic automations. Empty stdout in `no_agent` mode is silent; non-empty stdout is delivered verbatim; non-zero exit sends an error alert.

## Verification checklist

Before telling the user a cron issue is fixed:

- Confirm gateway cron ticker is running.
- Confirm the job definition now shows the intended `script` and `no_agent` values.
- Run the exact wrapper path cron calls, not only the inner command.
- Run at least one affected script manually or trigger the job if safe.
- Verify the expected artifact/output exists, not just that a command returned zero.
- For timeout failures, measure runtime with `/usr/bin/time -p` and confirm it is comfortably under the cron timeout.
- Explain which layer failed and which layer the fix bypassed or repaired.

## Script-only cron hardening patterns

- If a `no_agent` wrapper uses generic commands like `python3`, `node`, `git`, or `ssh`, check which binary cron will resolve and whether that environment has required dependencies. Prefer explicit absolute paths in wrappers when dependency location matters.
- For Python `ModuleNotFoundError` in cron, probe likely interpreters (`/usr/local/bin/python3`, `/usr/bin/python3`, Hermes venv Python) and pin the wrapper to the interpreter that imports the required package successfully. This captures the fix pattern without assuming today's package/path will stay true.
- For recurring Python cron families, prefer a dedicated venv under `~/.hermes/venvs/<name>` and call its interpreter explicitly from the `~/.hermes/scripts/` wrapper. If `uv venv` creates a venv without `pip`, install packages with `uv pip install --python "$HOME/.hermes/venvs/<name>/bin/python" ...`. See `references/no-agent-python-venv-pinning.md`.
- For GitHub or SSH sync jobs, prevent silent hangs: use `GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=15 -o ServerAliveInterval=10 -o ServerAliveCountMax=2'`, unset askpass variables, and wrap `git clone/pull/push` in a bounded `timeout`.
- For local backup syncs, prefer `rsync -a --delete` over `rm -rf && cp -r` so recurring jobs are incremental and less likely to hit scheduler timeouts; exclude bulky transient backup directories when they are not part of the intended durable backup.

## Pitfalls

- Do not conflate platform connectivity logs with cron execution failure. A Telegram reconnect warning is not the same as a cron job failure.
- Do not keep LLM-agent cron jobs for simple command execution unless reasoning is truly needed.
- Do not record environment-specific missing dependency failures as durable rules. Capture only the diagnostic/fix pattern.
- A manual run of the inner command is not enough for cron wrapper bugs; execute the same wrapper path configured on the job.
- If a protected bundled skill like `hermes-agent` has the general docs but lacks this operational playbook, create/update an editable umbrella skill instead of patching the protected skill.

## References

- `references/openai-codex-cron-provider-failure-2026-05.md` — example investigation where all jobs failed before script execution due to an agent/provider API error and were converted to `no_agent` script jobs.
- `references/no-agent-script-env-and-timeout-hardening.md` — concrete patterns for Python interpreter mismatches in script-only cron jobs and Git/SSH timeout hardening for GitHub sync jobs.
