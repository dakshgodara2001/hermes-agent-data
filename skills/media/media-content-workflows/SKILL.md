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
- The user sends or references a voice note/audio file that needs transcription, especially when platform auto-transcription failed.
- The user wants audio features such as mel spectrograms, chroma, or MFCCs.

## Workflow Selection

| Need | Use | Verify |
|---|---|---|
| YouTube transcript to summary/thread/blog | transcript fetch script/API | confirm transcript language, timestamps, and output format |
| GIF search/download | Tenor/curl + jq workflow | verify URL/file and license/context fit |
| Songwriting / AI music prompt | lyric + tags craft workflow | include structure, genre, mood, instrumentation, vocal direction |
| HeartMuLa generation | HeartMuLa CLI/API | verify generated job/file URL/path |
| Voice note/audio transcription | cached audio file + ffmpeg/Whisper or configured STT | verify transcript text, source file, and whether gateway STT needs config/path repair |
| Audio analysis | Songsee CLI | verify output image/JSON and feature parameters |

## YouTube Transcript Workflow

Fetch the transcript, preserve source URL and language, then transform into the requested artifact. If transcript access fails, try alternate transcript libraries/services before summarizing from title alone; do not invent content.

## GIF Workflow

Search with concrete mood/action terms, inspect several candidates, download only the chosen asset when needed, and return the source URL/path.

## Songwriting and AI Music Workflow

Separate craft from generation: first create the lyric/structure/prompt, then call generation only if the user requested audio output. Include tags for genre, mood, tempo, instrumentation, and vocal style.

## HeartMuLa Workflow

Use when the user specifically wants HeartMuLa/Suno-like generation. Capture job IDs, generated media URLs/paths, and any provider errors.

## Voice Note / Audio Transcription Recovery

When a platform message says a voice note could not be transcribed, inspect platform/gateway logs for the cached audio path and exact failure. Do not ask the user to repeat themselves until you have tried the cached file if it is accessible. For Telegram, cached voice notes are often `.ogg`/Opus files under `~/.hermes/audio_cache/`; local transcription generally needs `ffmpeg` available on the gateway PATH before Whisper/STT can decode non-WAV audio. If system package installation is blocked, a practical repair path is to install a user-space ffmpeg provider (for example `python3 -m pip install --user imageio-ffmpeg`), expose its binary on PATH for the retry, and run Whisper/STT against the cached file. After successful recovery, return both the cause and the transcript, and separately note any durable gateway setup fix needed.

See `references/voice-transcription-recovery.md` for a concise recovery recipe.

## Audio Analysis Workflow

Use spectrogram/feature extraction for analysis or visualization. Record sample rate, window/hop sizes when relevant, and return generated images/data files.

## Support Files

Namespaced copied files live under `references/<workflow>/` with the former skill body preserved as `README.md`; for example `references/youtube-content/README.md`, `references/youtube-content/references/output-formats.md`, and `references/youtube-content/scripts/fetch_transcript.py`.

## Common Pitfalls

1. **Summarizing without a transcript.** Report transcript failure instead of hallucinating video/audio content.
2. **Giving up on failed voice auto-transcription too early.** Check logs/cache and retry the cached audio file before asking the user to resend.
3. **Skipping file verification.** For downloads/generation/transcription, verify the media URL/path exists and that output was produced.
4. **Conflating prompts with final audio.** Ask/generate only when an actual audio artifact is requested.
5. **Ignoring platform fit.** GIFs and generated music need tone/context matching.

## Verification Checklist

- [ ] Source URL/query/asset path recorded.
- [ ] Transcript/download/generation/extraction actually succeeded or blocker reported.
- [ ] Output matches requested format.
- [ ] Media artifact path/URL is included when created.
