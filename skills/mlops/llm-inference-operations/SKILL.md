---
name: llm-inference-operations
description: "Use when running, serving, optimizing, quantizing, or modifying local/open LLM inference stacks: llama.cpp, vLLM, OpenAI-compatible servers, GGUF/quantization, and refusal-abliteration workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [LLM, inference, serving, llama.cpp, vLLM, GGUF, quantization, OpenAI-compatible, abliteration]
    related_skills: [huggingface-hub, evaluating-llms-harness]
---

# LLM Inference Operations Umbrella

## Overview

Use this skill for class-level local/open LLM inference operations: downloading models, selecting llama.cpp vs vLLM, serving an OpenAI-compatible endpoint, quantizing/converting weights, benchmarking throughput, troubleshooting GPU/Metal/CUDA issues, and applying specialized model surgery such as refusal-abliteration.

## When to Use

- The user wants to run a GGUF or Hugging Face LLM locally.
- The task requires serving an OpenAI-compatible API endpoint.
- You need throughput-focused deployment with vLLM or lightweight local inference with llama.cpp.
- You need quantization, KV cache tuning, batching, GPU memory fitting, or server debugging.
- The user asks about OBLITERATUS-style diff-in-means refusal vector analysis/abliteration.

## Engine Selection Matrix

| Need | Prefer | Why |
|---|---|---|
| CPU/macOS/Metal local chat, GGUF models | llama.cpp | Simple build, broad quantization support, low overhead |
| High-throughput API serving on CUDA GPUs | vLLM | Paged attention, batching, OpenAI-compatible serving |
| Model conversion/quantization to GGUF | llama.cpp tooling | Standard path for local quantized models |
| Behavioral vector surgery/refusal ablation | OBLITERATUS workflow | Specialized analysis + modification pipeline |

## Universal Workflow

1. Identify hardware (`uname`, GPU, RAM/VRAM), model format, license, and target context length.
2. Select engine and quantization based on memory budget.
3. Download/convert model safely, preferring Hugging Face tooling and checksums where available.
4. Start with a minimal smoke test before server deployment.
5. Serve with explicit host/port and model name.
6. Verify with a real completion request and inspect logs.
7. Tune batch size, context, GPU layers, tensor parallelism, or quantization only after baseline works.

## llama.cpp Notes

Use for GGUF local inference and lightweight servers. Typical concerns: build flags for Metal/CUDA/CPU, `--n-gpu-layers`, context length, batch size, GGUF quantization selection, server endpoint compatibility, and prompt/chat-template mismatches.

## vLLM Notes

Use for high-throughput OpenAI-compatible serving. Typical concerns: CUDA/driver/PyTorch compatibility, tensor/pipeline parallel settings, `--max-model-len`, GPU memory utilization, KV cache, tokenizer/chat-template selection, and long-context/quantized model support limits.

## OBLITERATUS Notes

Use only for explicit model-surgery/research tasks. Preserve original checkpoints, document vectors/datasets/layers, and evaluate for regressions. Treat output models as experimental and verify behavior with both target refusal probes and normal capability checks.

## Support Files

Namespaced reference files from absorbed engine-specific skills live under `references/llama-cpp/`, `references/vllm/`, and `references/obliteratus/`. The former skill bodies are preserved as `README.md`; original support subdirectories (for example `references/obliteratus/templates/*.yaml`) are re-homed under each engine's reference directory.

## Common Pitfalls

1. **Choosing vLLM on unsupported hardware.** vLLM is primarily CUDA/server-oriented; llama.cpp is often better on macOS/CPU.
2. **Ignoring chat templates.** Wrong templates cause poor outputs even when the server works.
3. **Overcommitting context/VRAM.** Reduce model size, quantization, context, or parallel settings.
4. **Treating server start as verification.** Always send a real API request.
5. **Overwriting original weights in model surgery.** Preserve inputs and record configuration.

## Verification Checklist

- [ ] Hardware and model format identified.
- [ ] Engine selected with reason.
- [ ] Model download/conversion completed or blocker reported.
- [ ] Local smoke prompt and/or OpenAI-compatible request succeeded.
- [ ] Logs checked for warnings/errors.
- [ ] Tuning/model-surgery results validated with explicit tests.
