---
name: ml-evaluation-experiment-tracking
description: "Use when evaluating ML/LLM models and tracking experiments: lm-eval-harness benchmarks, custom/API evaluations, distributed evals, Weights & Biases logging, sweeps, artifacts, and dashboards."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [evaluation, benchmarks, lm-eval-harness, W&B, experiment-tracking, sweeps, artifacts]
    related_skills: [llm-inference-operations, huggingface-hub]
---

# ML Evaluation and Experiment Tracking Umbrella

## Overview

Use this skill for class-level evaluation and experiment observability: running lm-eval-harness benchmarks, evaluating local or API-served LLMs, defining custom tasks, scaling/distributing evaluation, and logging metrics/artifacts/sweeps in Weights & Biases.

## When to Use

- The user wants benchmark scores such as MMLU, GSM8K, HellaSwag, ARC, HumanEval-like tasks, or custom evals.
- You need to evaluate an OpenAI-compatible model endpoint or local inference server.
- You need to compare models/runs and preserve metrics/config/artifacts.
- The user asks for W&B dashboards, sweeps, model registry, or artifact lineage.

## Workflow

1. Define the evaluation question, dataset/task, model endpoint, and metric.
2. Confirm licensing/data sensitivity before uploading to third-party tracking.
3. Run a tiny smoke evaluation first.
4. Run the full benchmark with pinned model, prompt template, seeds, and generation params.
5. Log run config, code version, metrics, outputs, and artifacts.
6. Summarize statistically meaningful results and limitations.

## lm-eval-harness Notes

Use for standardized LLM benchmarks and custom tasks. Keep exact task names, model args, batch size, few-shot count, device, and commit/version in the report. For API endpoints, capture base URL/model name and rate-limit behavior.

## W&B Notes

Use W&B for experiment tracking, sweeps, model artifacts, tables, and dashboards. Avoid logging secrets or private datasets unless the project/account policy allows it. Prefer explicit project/entity names and record offline-mode state if network is unavailable.

## Support Files

Namespaced files from absorbed skills live under `references/lm-evaluation-harness/` and `references/weights-and-biases/`; the former skill bodies are preserved as `README.md` and their original support files remain below each directory.

## Common Pitfalls

1. **Full benchmark before smoke test.** Always validate one tiny run first.
2. **Unpinned generation settings.** Temperature, max tokens, few-shot count, and prompts affect scores.
3. **Uploading sensitive examples.** Check data policy before W&B tables/artifacts.
4. **Comparing non-equivalent runs.** Normalize model version, prompt, hardware, batch size, and eval commit.
5. **Reporting only headline scores.** Include confidence/variance and known limitations.

## Verification Checklist

- [ ] Task/dataset/model/generation settings recorded.
- [ ] Smoke evaluation completed.
- [ ] Full run completed or blocker reported.
- [ ] Metrics/artifacts logged or saved locally.
- [ ] Results include caveats and reproducibility details.
