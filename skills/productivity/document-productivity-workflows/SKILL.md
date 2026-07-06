---
name: document-productivity-workflows
description: "Use when creating, editing, extracting, or explaining documents and knowledge artifacts: PDFs/OCR, slide decks, research papers, technical explainers, meeting-summary pipelines, and note/document deliverables."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [documents, pdf, powerpoint, ocr, writing, meetings, explainers]
    related_skills: []
---

# Document Productivity Workflows

## Overview

This umbrella covers document-centered work: extracting text from files, editing PDFs, generating or modifying slide decks, drafting research papers, producing technical explainer artifacts, and operating meeting-summary deliverables. Prefer one document workflow skill with labeled modes over separate one-off tool skills.

## When to Use

- User provides PDFs, scans, screenshots, Word/PowerPoint/Excel files, or asks for OCR/extraction.
- User asks to edit PDF text/metadata or create/modify a deck.
- User asks for a conference-style research paper, citation workflow, reviewer checklist, or LaTeX template.
- User asks to turn a technical website/spec/paper into diagrams, glossaries, cheat sheets, or plain-language explanations.
- User asks about Teams meeting summaries or replaying/inspecting a document generation pipeline.

## Mode Selection

| Mode | Former narrow skill(s) | Deliverable | Verification |
|---|---|---|---|
| OCR / document extraction | `ocr-and-documents` | Markdown/text/structured extraction | Confirm pages/text count and spot-check content. |
| PDF edit | `nano-pdf` | Modified PDF | Re-read/extract edited area and confirm metadata/text. |
| Slide deck | `powerpoint` | `.pptx`, HTML/PDF deck, speaker notes | Open/parse deck, count slides, validate assets. |
| Research paper | `research-paper-writing` | LaTeX/Markdown paper, outline, checklist | Compile or validate references/templates when possible. |
| Technical explainer | `technical-explainer-artifacts` | Diagram, glossary, mental model, cheat sheet | Confirm source claims are grounded in provided/extracted material. |
| Meeting pipeline | `teams-meeting-pipeline` | Summary status, replay, generated notes | Inspect job status/logs and verify output location. |

## Document Workflow

1. **Inventory inputs.** Identify file types, page/slide counts, and whether the user wants extraction, transformation, or generation.
2. **Pick the lowest-loss path.** Use native parsers for Office files, OCR only when text extraction fails, and source citations for research/explainers.
3. **Generate the deliverable.** Keep outputs in a named path and preserve source files.
4. **Round-trip verify.** Re-open, parse, compile, or extract the output to ensure it contains the requested changes.
5. **Report exact artifacts.** Include paths, counts, and limitations.

## Common Pitfalls

- Do not trust visual PDF edits without re-extracting or inspecting the changed area.
- Do not hallucinate citations or paper claims; tie them to sources or mark TODOs.
- Do not flatten large templates into always-visible instructions; keep conference/Office templates under `templates/` when restored from archive.
- Do not claim a meeting pipeline replay succeeded without checking status and output files.

## Verification Checklist

- [ ] Inputs inventoried and output path chosen.
- [ ] Mode selected from the table.
- [ ] Output generated or blocker reported.
- [ ] Output re-opened/parsed/compiled/extracted.
