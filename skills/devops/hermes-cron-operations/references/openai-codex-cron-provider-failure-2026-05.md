# OpenAI Codex cron provider failure — May 2026

## Situation

Multiple Hermes cron jobs showed `last_status: error` with:

```text
RuntimeError: 'NoneType' object is not iterable
```

Affected job classes:

- nightly GitHub sync
- morning market scanner cache job
- pre-market report delivery

## Key evidence pattern

`~/.hermes/cron/jobs.json` and each output file showed the same generic runtime error, but `~/.hermes/logs/agent.log` revealed the real boundary:

```text
API call failed (attempt 1/3) error_type=TypeError
provider=openai-codex
base_url=https://chatgpt.com/backend-api/codex
model=gpt-5.5
summary='NoneType' object is not iterable
```

The failure happened on the first agent API call, before the terminal command ran. `last_delivery_error` was `null`, so platform delivery was not the cause. Telegram reconnect warnings existed nearby, but were unrelated to the cron job execution failure.

## Useful verification commands

Run the underlying scripts directly to prove whether the script layer is healthy:

```bash
cd ~/.hermes/bin && python3 nse_stock_scanner.py --silent
cd ~/.hermes/bin && python3 premarket_pulse.py
bash ~/.hermes/bin/nightly-github-sync.sh
```

Check dependencies only as evidence, not as a permanent rule:

```bash
python3 - <<'PY'
for m in ['yfinance', 'pandas', 'requests', 'bs4']:
    try:
        __import__(m)
        print(m, 'OK')
    except Exception as e:
        print(m, 'ERR', repr(e))
PY
```

## Fix that generalized

For deterministic cron jobs that only run a command, create small wrappers under `~/.hermes/scripts/` and update jobs to script-only mode:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$HOME/.hermes/bin"
python3 nse_stock_scanner.py --silent
```

Then set:

- `script`: wrapper filename
- `no_agent`: `true`
- `deliver`: unchanged from the original job

This avoids requiring a model/provider round trip merely to execute a shell command.

## What to tell the user

Report the layer separation clearly:

- Cron scheduler fired.
- Agent/provider failed before tool execution.
- Scripts were manually verified.
- Jobs were converted to `no_agent` script mode.
- Old `last_status` may remain until the next scheduled/manual run for each job.
