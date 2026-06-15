---
name: media-content-workflows
description: "Use when handling lightweight media workflows: YouTube transcript extraction and repurposing, GIF search/download, song/AI-music prompting, HeartMuLa song generation, and audio feature/spectrogram analysis."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [media, YouTube, transcripts, GIFs, music, lyrics, audio-analysis, spectrograms]
    related_skills: []
---

# Media Content Workflows Umbrella

## Overview

Use this skill for class-level lightweight media tasks: fetching and transforming YouTube transcripts, searching/downloading GIFs, writing songs and AI-music prompts, generating songs with HeartMuLa, and analyzing audio with spectrogram/features tools.

## When to Use

- The user asks to summarize, thread, blog, or repurpose a YouTube video transcript.
- The user wants an appropriate reaction GIF or a downloaded GIF asset.
- The user asks for lyrics, song structure, Suno-style prompts, or HeartMuLa generation.
- The user wants audio features such as mel spectrograms, chroma, or MFCCs.

## Workflow Selection

| Need | Use | Verify |
|---|---|---|
| YouTube transcript to summary/thread/blog | transcript fetch script/API | confirm transcript language, timestamps, and output format |
| GIF search/download | Tenor/curl + jq workflow | verify URL/file and license/context fit |
| Songwriting / AI music prompt | lyric + tags craft workflow | include structure, genre, mood, instrumentation, vocal direction |
| HeartMuLa generation | HeartMuLa CLI/API | verify generated job/file URL/path |
| Audio analysis | Songsee CLI | verify output image/JSON and feature parameters |

## YouTube Transcript Workflow

Fetch the transcript, preserve source URL and language, then transform into the requested artifact. If transcript access fails, try alternate transcript libraries/services before summarizing from title alone; do not invent content.

## GIF Workflow

Search with concrete mood/action terms, inspect several candidates, download only the chosen asset when needed, and return the source URL/path.

## Songwriting and AI Music Workflow

Separate craft from generation: first create the lyric/structure/prompt, then call generation only if the user requested audio output. Include tags for genre, mood, tempo, instrumentation, and vocal style.

## HeartMuLa Workflow

Use when the user specifically wants HeartMuLa/Suno-like generation. Capture job IDs, generated media URLs/paths, and any provider errors.

## Audio Analysis Workflow

Use spectrogram/feature extraction for analysis or visualization. Record sample rate, window/hop sizes when relevant, and return generated images/data files.

## Support Files

Namespaced copied files live under `references/<workflow>/` with the former skill body preserved as `README.md`; for example `references/youtube-content/README.md`, `references/youtube-content/references/output-formats.md`, and `references/youtube-content/scripts/fetch_transcript.py`.

## Common Pitfalls

1. **Summarizing without a transcript.** Report transcript failure instead of hallucinating video content.
2. **Skipping file verification.** For downloads/generation, verify the media URL/path exists.
3. **Conflating prompts with final audio.** Ask/generate only when an actual audio artifact is requested.
4. **Ignoring platform fit.** GIFs and generated music need tone/context matching.

## Verification Checklist

- [ ] Source URL/query/asset path recorded.
- [ ] Transcript/download/generation/extraction actually succeeded or blocker reported.
- [ ] Output matches requested format.
- [ ] Media artifact path/URL is included when created.
