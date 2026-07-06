---
name: service-api-integrations
description: "Use when operating external service APIs and CLIs from Hermes: Google Workspace, Airtable, Notion, email, maps/geocoding, social/group messaging, smart-home endpoints, and other CRUD/search/action integrations."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [api, integrations, cli, productivity, external-services]
    related_skills: []
---

# Service API Integrations

## Overview

This umbrella covers task-oriented use of external services through APIs or CLIs. The shared class is: discover credentials and target resources, perform a bounded read/write action, verify with a follow-up read, and report stable handles instead of assuming success.

## When to Use

- User asks to read, create, update, delete, search, or export records/pages/messages/events through a service API.
- User asks for Google Workspace, Airtable, Notion, email/IMAP-SMTP, maps/routes/timezones, X/Twitter, Yuanbao groups, Hue lights, or similar service operations.
- User asks to configure or troubleshoot a CLI/API integration.

## Mode Selection

| Mode | Former narrow skill(s) | Typical actions | Verification |
|---|---|---|---|
| Workspace suite | `google-workspace` | Gmail, Calendar, Drive, Docs, Sheets | Re-read created/updated item; report URL/id. |
| Database/table API | `airtable`, `notion` | CRUD, filters, upserts, markdown/database pages | Fetch record/page after write. |
| Email | `himalaya` | Search, compose, send via IMAP/SMTP CLI | Confirm message id/mailbox/sent state. |
| Maps/geodata | `maps` | Geocode, POIs, routes, timezones | Include source endpoint and coordinates/distance. |
| Social/group APIs | `xurl`, `yuanbao` | Post/search/DM/group mention/member lookup | Report post/message/user ids or API status. |
| Smart home | `openhue` | Lights, rooms, scenes, bridge info | Read device state after command. |

## Integration Workflow

1. **Discover the target.** Resolve workspace/base/page/channel/device identifiers before writing.
2. **Check auth/config.** Verify required env vars, config files, or CLI login state. Do not expose tokens.
3. **Dry read before write.** Fetch current state when modifying existing resources.
4. **Perform the smallest scoped action.** Avoid broad deletes or fan-out without explicit user instruction.
5. **Verify by reading back.** Return IDs, URLs, timestamps, or state snapshots.

## Safety Rules

- Ask before destructive multi-record deletes or public posts when scope is ambiguous.
- Never invent API responses; report actual HTTP/CLI status and error text.
- Prefer service-specific tools when available; otherwise use documented curl/CLI commands.
- Keep provider-specific quirks in `references/` rather than splitting a new micro-skill for each service.

## Verification Checklist

- [ ] Target resource identified.
- [ ] Auth/config checked without leaking secrets.
- [ ] Action executed with bounded scope.
- [ ] Follow-up read verified outcome.
