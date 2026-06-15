---
name: llm-fine-tuning-operations
description: "Use when fine-tuning or post-training LLMs: choose Axolotl, TRL, or Unsloth; prepare datasets; configure LoRA/QLoRA, SFT, DPO, PPO, GRPO, reward models; run smoke tests; track hardware/memory constraints; and package trained adapters/models."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [LLM, fine-tuning, post-training, Axolotl, TRL, Unsloth, LoRA, QLoRA, DPO, GRPO, RLHF]
    related_skills: [huggingface-hub, ml-evaluation-experiment-tracking, llm-inference-operations]
---

# LLM Fine-Tuning Operations Umbrella

## Overview

Use this skill for class-level LLM fine-tuning and post-training work. It consolidates framework-specific packages for Axolotl, Hugging Face TRL, and Unsloth into one workflow: choose the right trainer, prepare datasets, configure memory-efficient training, run small smoke jobs, evaluate outputs, and preserve reproducibility.

## When to Use

- The user wants to fine-tune an LLM with SFT, LoRA, QLoRA, DPO, PPO, GRPO, RLHF, reward modeling, or preference alignment.
- The task involves selecting between Axolotl YAML configs, TRL Python trainers/CLI, and Unsloth accelerated LoRA training.
- You need to debug training OOMs, dataset formatting, chat templates, multi-GPU/FSDP/DeepSpeed, or adapter packaging.
- You need to hand off trained adapters/models to Hugging Face Hub, local inference, or evaluation.

## Framework Selection Matrix

| Need | Prefer | Why |
|---|---|---|
| Production YAML-driven supervised/preference fine-tuning | Axolotl | Rich config surface, LoRA/QLoRA, FSDP/DeepSpeed, many model families |
| RLHF/preference/post-training algorithms | TRL | SFTTrainer, DPOTrainer, PPO/GRPO, reward modeling and alignment methods |
| Fast memory-efficient LoRA/QLoRA on supported models | Unsloth | 2-5x speedups and lower VRAM for common Llama/Mistral/Gemma/Qwen paths |
| Publishing/downloading datasets/models | Hugging Face Hub | Pair with `huggingface-hub` skill |
| Comparing tuned models | lm-eval/custom evals/W&B | Pair with `ml-evaluation-experiment-tracking` |

## Universal Workflow

1. Define the objective: instruction following, domain adaptation, preference alignment, reward model, or online RL.
2. Inspect hardware and memory budget before choosing model size, quantization, sequence length, and batch size.
3. Validate dataset schema and chat template on 2-5 examples before launching training.
4. Start with a tiny smoke run (`max_steps`/small split) that saves an adapter/checkpoint.
5. Scale gradually: batch size, gradient accumulation, packing, FSDP/DeepSpeed, context parallelism.
6. Evaluate with held-out examples and benchmark/eval tooling before declaring success.
7. Save reproducibility metadata: base model revision, dataset revision, config, seed, hardware, command, metrics, and output path.

## Axolotl Notes

Use Axolotl when the user wants YAML-first training, broad model support, and production-oriented LoRA/QLoRA/SFT/preference training. Keep config files explicit. Common levers include FSDP/DeepSpeed, `context_parallel_size`, dataset format adapters, packed sequences, and compressed checkpoint saving.

Detailed pre-consolidation material lives in `references/axolotl/README.md` and its nested `references/` files.

## TRL Notes

Use TRL for post-training algorithms and Python-first control. Select method by data shape:

- SFT: prompt-completion or chat examples.
- DPO/IPO/cDPO/RPO: chosen/rejected preference pairs.
- RewardTrainer: outcome/process reward modeling.
- PPO/GRPO/RLOO/OnlineDPO: online RL or reward-function optimization.

Production-ready GRPO examples and method guides are under `references/trl-fine-tuning/`.

## Unsloth Notes

Use Unsloth when speed/VRAM are the bottleneck and the target model/method is supported. Verify compatibility before promising support; fall back to Axolotl or vanilla TRL/Transformers when model architecture or training objective is outside Unsloth's supported path.

Detailed pre-consolidation material lives in `references/unsloth/README.md` and its nested `references/` files.

## Common Pitfalls

1. **Skipping the smoke run.** Full fine-tunes waste hours if dataset formatting or chat templates are wrong.
2. **Confusing SFT and preference data.** Method choice follows data shape; do not force DPO/GRPO onto plain completions.
3. **Ignoring reference model memory.** DPO/PPO-style methods may need extra model copies or careful adapter/reference handling.
4. **Unpinned base/dataset revisions.** Reproducibility requires exact model, dataset, code, and seed metadata.
5. **Treating lower training loss as deployment success.** Evaluate qualitative examples and benchmarks before publishing.

## Verification Checklist

- [ ] Objective, method, model, and framework chosen with reason.
- [ ] Hardware/VRAM and sequence length/batch assumptions recorded.
- [ ] Dataset schema and chat template verified on examples.
- [ ] Tiny smoke run completed or blocker reported.
- [ ] Output checkpoint/adapter path verified.
- [ ] Evaluation plan/results and reproducibility metadata captured.
