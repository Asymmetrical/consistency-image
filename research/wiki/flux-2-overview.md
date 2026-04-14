---
type: entity
tags: [model, flux-2, black-forest-labs]
updated: 2026-04-14
sources: [flux-2-research-summary.md]
---

# FLUX.2 Overview

**FLUX.2** is the second generation of image generation and editing models from Black Forest Labs, released in November 2025. It represents a paradigm shift in character consistency and compositional control.

## Key Advancements over FLUX.1

| Feature | FLUX.1 | FLUX.2 |
| :--- | :--- | :--- |
| **Model Size** | 12B Parameters | 32B Parameters ([max]/[dev]) |
| **Language Model** | T5-XXL | Mistral-3 24B |
| **Consistency** | Prompt / LoRA based | [Multi-Reference Conditioning](multi-reference-conditioning.md) |
| **Distillation** | [Schnell] (4-step) | [Klein] (9B & 4B variants) |
| **Text Rendering** | Strong | State-of-the-Art |

## The Consistency Lab Strategy

With the arrival of FLUX.2, the objective of the Character Consistency Lab expands beyond traditional prompt engineering:

1.  **Reference Set Optimization**: Finding the ideal set of 5-10 images that provide the most stable "identity anchor" for the model.
2.  **Reference Weighting**: Tuning the influence of each reference in the conditioning set.
3.  **Cross-Model Benchmarking**: Comparing how different [variants](flux-2-variants.md) (e.g., [dev] vs [klein]) handle identity drift during generation.

## Related Pages
- [Multi-Reference Conditioning](multi-reference-conditioning.md)
- [FLUX.2 Variants](flux-2-variants.md)
