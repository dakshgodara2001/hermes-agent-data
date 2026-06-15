# no_agent Python cron: pin a dedicated venv

When a deterministic `no_agent=True` cron script fails with Python import errors, fix the cron execution environment rather than routing the job back through an LLM.

## Pattern

1. Inspect the saved cron output under `~/.hermes/cron/output/<job_id>/...md` and confirm the failure is inside the script, not delivery.
2. Create a dedicated venv for that cron family under `~/.hermes/venvs/<name>`:

```bash
mkdir -p "$HOME/.hermes/venvs"
uv venv "$HOME/.hermes/venvs/<name>" --python 3.11
```

3. If the venv has no `pip` module, install dependencies with `uv pip install --python` instead of `python -m pip`:

```bash
uv pip install --python "$HOME/.hermes/venvs/<name>/bin/python" yfinance pandas numpy ta requests
```

4. Patch the wrapper in `~/.hermes/scripts/` to call the venv interpreter explicitly:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$HOME/.hermes/bin"
"$HOME/.hermes/venvs/<name>/bin/python" script.py
```

5. Verify by running the exact wrapper path, not just the inner Python file:

```bash
bash "$HOME/.hermes/scripts/<wrapper>.sh"
```

6. If the cron job's `deliver` target would spam the user, trigger only silent/local jobs via `cronjob(action='run')`; for delivering jobs, manual wrapper success is enough unless the user explicitly wants a live delivery test.

## Why this matters

Cron inherits the gateway/scheduler environment, which may not match the shell or the assistant's active Python. A pinned venv makes deterministic no-agent jobs reproducible and avoids brittle reliance on `/usr/local/bin/python3`, `python3`, or a Hermes runtime venv that intentionally lacks `pip`.
