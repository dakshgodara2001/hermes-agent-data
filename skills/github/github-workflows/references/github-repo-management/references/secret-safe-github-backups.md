# Secret-Safe GitHub Backups

Use this pattern when the user wants a scheduled GitHub backup/sync of agent data, dotfiles, skills, cron jobs, or configuration while excluding secrets.

## Core Rules

Never commit:

- `.env`
- auth files (`auth.json`, OAuth token stores, keyrings)
- API keys, tokens, passwords, credentials
- local databases unless explicitly requested
- session logs that may contain sensitive prompts or tool outputs
- media/cache/output directories unless explicitly requested

Prefer a **private repository** for personal agent backups.

## Pattern

1. Create or reuse a private GitHub repo.
2. Maintain a local sync working tree separate from the source directory.
3. Copy only selected safe directories/files into the working tree.
4. Write a strong `.gitignore` in the sync repo.
5. Redact config files before committing.
6. Commit only if staged changes exist.
7. Schedule via cron/job runner.
8. Deliver a brief success/failure report.

## Example Sync Contents for Hermes Agent Data

Safe-ish to sync after review:

- `skills/`
- cron job definitions, not outputs
- memories, if the user explicitly wants them backed up
- redacted config
- agent personality files

Avoid:

- `.env`
- `auth.json`, `auth.lock`
- `state.db*`
- `sessions/`
- `logs/`
- `pairing/`
- `audio_cache/`, `image_cache/`
- generated outputs containing secrets or private data

## Redacting Config

For YAML-like config files, a simple defensive redaction pass can replace values for lines containing words like:

- token
- key
- secret
- password
- api_key
- auth
- credential

This is not a substitute for excluding true secret files entirely; it is a second layer.

## Scheduling Note

Be explicit about time zones. If the user's requested timezone differs from system timezone, convert the schedule and state both forms back to the user.

Example: midnight Central Time during CDT is 05:00 UTC.
