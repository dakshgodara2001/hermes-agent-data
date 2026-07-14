# Voice Transcription Recovery

Use this when a messaging platform reports that a user voice note could not be transcribed.

## Goal

Recover the transcript from the cached audio file before asking the user to resend, and report the actual cause plus any durable setup fix.

## Recovery Steps

1. Find the cached audio and failure reason in gateway logs.
   - Search for terms like `transcrib`, `voice`, `stt`, `whisper`, `audio`.
   - Telegram voice notes are commonly cached under `~/.hermes/audio_cache/` as `.ogg`/Opus.
2. Verify the file exists and identify its codec/container.
3. Ensure a decoder is available for non-WAV inputs.
   - Preferred durable setup: install `ffmpeg` and ensure the gateway process has it on `PATH`.
   - User-space fallback when system install is blocked:
     ```bash
     python3 -m pip install --user imageio-ffmpeg
     python3 - <<'PY'
     import imageio_ffmpeg
     print(imageio_ffmpeg.get_ffmpeg_exe())
     PY
     ```
     Symlink or prepend that binary location as `ffmpeg` on PATH for the retry.
4. Transcribe the cached file with the available local STT/Whisper path.
   - Example retry shape:
     ```bash
     mkdir -p ~/.hermes/audio_cache/bin ~/.hermes/audio_cache/transcribed
     ln -sf /path/to/imageio_ffmpeg/binaries/ffmpeg-* ~/.hermes/audio_cache/bin/ffmpeg
     PATH="$HOME/.hermes/audio_cache/bin:$PATH" \
       python3 -m whisper ~/.hermes/audio_cache/audio_xxx.ogg \
       --model tiny --language en \
       --output_dir ~/.hermes/audio_cache/transcribed --output_format txt
     ```
5. Return the transcript and mention whether the gateway needs a restart/config/path repair for future voice notes.

## Pitfalls

- Do not summarize or guess the audio content if transcription failed.
- Do not store one-off transcript content in memory or skills.
- Treat missing `ffmpeg` as a setup fix, not as a permanent claim that voice transcription is broken.
- If the user asks for the original request to be handled after recovery, continue from the recovered transcript rather than asking them to retype it.
