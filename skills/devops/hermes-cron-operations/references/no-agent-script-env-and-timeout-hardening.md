# no_agent script environment and timeout hardening

Use this reference when a Hermes cron job is `no_agent: true` and fails inside a wrapper script or times out before producing useful output.

## Pattern 1: Cron Python/path mismatch

Symptom:

```text
ModuleNotFoundError: No module named '<package>'
```

The same script may work manually while cron fails because the wrapper uses generic `python3`, and cron resolves a different interpreter than the interactive shell.

Fix pattern:

1. Probe likely interpreters manually:

```bash
for p in /usr/local/bin/python3 /usr/bin/python3 "$HOME/.hermes/hermes-agent/venv/bin/python"; do
  [ -x "$p" ] || continue
  echo "--- $p"
  "$p" - <<'PY'
import sys
print(sys.executable)
try:
    import yfinance  # replace with the failing package
    print('package OK')
except Exception as e:
    print(type(e).__name__ + ': ' + str(e))
PY
done
```

2. Update the cron wrapper to call the interpreter that actually has the dependencies, e.g.:

```bash
cd "$HOME/.hermes/bin"
/usr/local/bin/python3 premarket_pulse.py
```

3. Run the wrapper directly, not just the inner script, before declaring fixed.

## Pattern 2: Git/SSH cron job timeout

Symptom:

```text
Script timed out after 120s: ~/.hermes/scripts/<job>.sh
```

For GitHub sync jobs, cron may hang on `git pull`, `git push`, SSH auth prompts, or network stalls.

Hardening pattern inside the underlying script:

```bash
TIMEOUT="/usr/local/bin/timeout"
[ -x "$TIMEOUT" ] || TIMEOUT="timeout"
export GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=15 -o ServerAliveInterval=10 -o ServerAliveCountMax=2"
unset SSH_ASKPASS GIT_ASKPASS

"$TIMEOUT" 60s git pull --rebase origin main 2>/dev/null || true
# ... sync files ...
"$TIMEOUT" 60s git push origin main
```

For large local backup copies, prefer incremental sync over delete-and-copy:

```bash
rsync -a --delete --exclude '.curator_backups/' "$HERMES_DIR/skills/" skills/
rsync -a --delete "$HERMES_DIR/memories/" memories/
```

## Verification checklist

- Inspect the job definition and confirm it is script-only/no-agent if deterministic.
- Read the wrapper and underlying script.
- Reproduce with the wrapper path exactly as cron calls it.
- If Git is involved, verify non-interactive remote access with BatchMode before/after hardening.
- Measure runtime with `/usr/bin/time -p` and ensure it is well under the cron timeout.
- Trigger the cron job if safe; otherwise explain why manual wrapper execution is the verification boundary.
