# Hermes Agent Data

Automated nightly backup of Hermes agent configuration and data.

**Last synced:** 2026-07-20 14:02 IST

## Contents

| Directory/File | Description |
|---|---|
| `skills/` | All custom skills and procedures |
| `cron/` | Scheduled cron job definitions |
| `memories/` | Persistent agent memories |
| `config.yaml.redacted` | Config with secrets stripped |
| `SOUL.md` | Agent personality definition |

> ⚠️ Secrets, API keys, tokens, and auth files are **never** committed.

## Auto-sync

This repo is updated nightly at midnight Central Time via a Hermes cron job.
