---
name: creative-media-production
description: "Use when creating animated, generative, interactive, or model-driven media: ASCII art/video, p5.js sketches, Manim animations, TouchDesigner scenes, ComfyUI workflows, and audio/image/video generation pipelines."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [creative, media, animation, generative-art, video, audio]
    related_skills: [creative-visual-artifacts]
---

# Creative Media Production

## Overview

This umbrella covers media workflows where timing, rendering, generative code, model execution, or external creative runtimes matter. The goal is a working media artifact backed by real execution: rendered frames/video/audio, a runnable sketch, a ComfyUI workflow run, or a verified scene/control script.

## When to Use

- ASCII text art, terminal posters, image-to-ASCII, and ASCII video/GIF conversion.
- p5.js sketches, WebGL experiments, generative art, interactive browser demos, and frame exports.
- Manim CE animations for math, algorithms, diagrams, and paper explainers.
- TouchDesigner/twozero MCP scene control, operator graphs, realtime visuals, audio-reactive visuals, projection mapping, MIDI/OSC patterns.
- ComfyUI install/setup, workflow execution, template validation, model/node dependency repair, image/video/audio generation.
- AudioCraft/MusicGen/AudioGen-style text-to-music or text-to-sound workflows when available.

For static diagrams, HTML mockups, visual design systems, and infographics, use `creative-visual-artifacts` instead.

## Mode Selection

| Mode | Former narrow skill(s) | Primary deliverable | Minimum verification |
|---|---|---|---|
| ASCII art | `ascii-art` | Terminal/text art, banners, image-to-ASCII output | Show rendered output or write text file. |
| ASCII video | `ascii-video` | MP4/GIF or frame sequence | Confirm output file exists and has nonzero duration/size. |
| p5.js | `p5js` | HTML/JS sketch, optional exported frames/video | Serve/open or run export script; check console/build errors. |
| Manim | `manim-video` | Python scene + rendered video | Run Manim render at preview/low quality before final if possible. |
| TouchDesigner | `touchdesigner-mcp` | Live TD network/scene changes or reusable script | Query created operators/parameters and capture screenshot/status. |
| ComfyUI | `comfyui` | Workflow JSON plus generated image/video/audio | Health check server, validate workflow graph, confirm output file. |
| Audio generation | `audiocraft-audio-generation` | WAV/MP3 or generation script | Confirm sample rate/duration and playable file. |

## Production Loop

1. **Pick the runtime.** Identify the engine/toolchain and check whether it is installed/running. If not, install in a venv/project-local location or state the blocker.
2. **Create a small tracer output first.** Render a low-resolution frame, short clip, or minimal sketch before spending time on final quality.
3. **Iterate visually/audibly.** Inspect output with vision/video/audio metadata tools where available; adjust composition, timing, labels, and readability.
4. **Render final artifact.** Save files under a clear output directory and avoid overwriting user work without confirmation.
5. **Verify and report.** Include exact paths, durations/sizes, command outputs, and any runtime limitations.

## Common Pitfalls

- Do not treat media generation as complete until an actual artifact exists.
- Do not assume GPU/model availability; check and provide CPU/lightweight fallbacks where possible.
- Do not bury reusable runtime setup in prose. If resurrecting detailed archived material, place setup scripts under `scripts/` and long API notes under `references/`.
- For long renders, use background processes with completion notifications and inspect logs before reporting success.

## Verification Checklist

- [ ] Runtime/toolchain checked.
- [ ] Tracer output rendered or blocker reported.
- [ ] Final file(s) created with paths.
- [ ] Output size/duration/parseability verified.
