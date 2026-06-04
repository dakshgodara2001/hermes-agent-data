---
name: apple-macos-automation
description: "Use when automating Apple/macOS user apps and device workflows: Notes, Reminders, iMessage/SMS, Find My, and background desktop control. Chooses the right CLI, handles macOS-only prerequisites, and verifies privacy permissions."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [Apple, macOS, Notes, Reminders, iMessage, FindMy, automation, desktop-control]
    related_skills: [obsidian]
---

# Apple/macOS Automation Umbrella

## Overview

Use this skill for class-level Apple ecosystem work on macOS: creating/searching Apple Notes, managing Reminders, sending/reading iMessage/SMS, locating Apple devices/AirTags through Find My, and driving the macOS desktop without stealing the user's active cursor/focus. All workflows are macOS-only and usually require app-specific privacy permissions.

## When to Use

- The user asks to interact with an Apple app or service from Hermes.
- The task must sync to the user's Apple devices via iCloud.
- A GUI-only macOS app needs background screenshots, mouse, keyboard, scroll, or drag operations.
- The user asks for SMS/iMessage communication, Apple Notes, Reminders, or Find My location data.

## When NOT to Use

- Agent-internal durable facts: use the `memory` tool.
- Markdown-native personal knowledge management: use Obsidian if the user asks for vault work.
- Non-macOS machines: these commands require macOS apps and Automation permissions.

## Tool Selection Matrix

| Need | Use | Typical commands / checks |
|---|---|---|
| Apple Notes | `memo` | `memo notes`, `memo notes -s "query"`, `memo notes -a "Title"`, `memo notes -e` |
| Apple Reminders | `remindctl` | list/add/complete reminders; verify Reminders.app privacy prompts |
| iMessage/SMS | `imsg` | list/read/send chats; confirm recipient/channel before sending |
| Find My | FindMy.app automation CLI | query devices/items; report timestamps and uncertainty |
| Background desktop control | macOS computer-use helper | screenshot, click, type, scroll, drag while preserving the user's foreground input |

## Apple Notes (`memo`)

Prerequisites: `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo`, Notes.app, and Automation access when prompted.

Quick commands:

```bash
memo notes
memo notes -f "Folder Name"
memo notes -s "query"
memo notes -a "Note Title"
memo notes -e
memo notes -d
memo notes -m
memo notes -ex
```

Limitations: notes containing images/attachments may not be editable; interactive prompts require a PTY.

## Apple Reminders (`remindctl`)

Use for synced personal tasks and reminder lists. Prefer explicit list/date parsing and read back the created reminder or list state after adding/completing items. If the user asks for a private agent TODO instead, use Hermes' `todo` tool rather than Reminders.app.

## iMessage/SMS (`imsg`)

Use for Messages.app conversations. Before sending to a specific person, identify the target chat/contact if available and avoid guessing ambiguous recipients. For media or group chats, verify CLI support and report if Messages.app permissions block access.

## Find My

Use when the user asks where a device, AirTag, or shared item is. Report:

- device/item name,
- latitude/longitude or human-readable location if available,
- location timestamp / freshness,
- battery or online state when exposed,
- uncertainty when data is stale or unavailable.

## Background macOS Computer Use

Use screenshot-driven operations for GUI tasks that do not expose a reliable CLI. Keep actions minimal, verify each visible state change, and avoid interacting with sensitive apps unless the user asked for that exact app/task.

## Absorbed Package References

The detailed pre-consolidation packages are preserved under `references/absorbed-packages/` for recovery and session-specific command detail:

- `references/absorbed-packages/apple-notes/`
- `references/absorbed-packages/apple-reminders/`
- `references/absorbed-packages/findmy/`
- `references/absorbed-packages/imessage/`
- `references/absorbed-packages/macos-computer-use/`

## Common Pitfalls

1. **Forgetting macOS privacy permissions.** Notes, Reminders, Messages, Find My, and Accessibility/Screen Recording may require System Settings grants.
2. **Using Apple apps for agent-private memory.** Use Hermes `memory` for internal future context and `todo` for session tasks.
3. **Assuming a location is live.** Find My data can be stale; include timestamps.
4. **Guessing recipients.** For iMessage/SMS, disambiguate contacts/chats before sending if the target is not explicit.
5. **Stealing user focus.** Prefer background computer-control workflows and verify with screenshots.

## Verification Checklist

- [ ] Confirm this is running on macOS.
- [ ] Check the required CLI exists or report the install command.
- [ ] Trigger/verify needed Automation, Accessibility, Screen Recording, or app permissions.
- [ ] Read back resulting app state after create/edit/send/complete actions.
- [ ] For communications and device locations, include target, timestamp, and confidence.
