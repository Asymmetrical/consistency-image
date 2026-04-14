---
type: concept
tags: [consistency, reference-conditioning, flux-2]
updated: 2026-04-14
sources: [flux-2-research-summary.md]
---

# Multi-Reference Conditioning

**Multi-Reference Conditioning** is the core consistency mechanism introduced in [FLUX.2](flux-2-overview.md). It allows for the input of multiple image samples to ground the generation process in a set of specific visual invariants.

## How it Works

Instead of the model relying solely on a text prompt (which is subject to semantic interpretation drift), Multi-Reference Conditioning injects visual data directly into the latent space during the flow-matching process.

- **Capacity**: Up to 10 images.
- **Data Privacy**: The references stay local to the inference pass and do not require weights-tuning (unlike LoRAs).
- **Control**: Users can specify weights for each image, allowing for "balanced" identity (e.g., using 3 front-facing faces, 2 profiles, and 3 outfit references).

## Advantages for Character Consistency

1.  **Instant Consistency**: No need to spend hours training a LoRA for a new character.
2.  **Identity + Variation**: The model can maintain the "Must-Stay-Fixed" features (identity) while still being flexible on "May-Vary" features (pose, lighting).
3.  **Cross-Model Stability**: Standardize a reference set and use it across different FLUX.2 [variants](flux-2-variants.md).

## Implementation in the Lab

For our [Research Program](../../research_program.md), this feature becomes a new primary **Editable Surface**. 

### Research Hypotheses:
- Does the order of references in the conditioning set affect identity stability?
- What is the "Minimum Viable Reference Set" (MVRS)? (e.g., is 3 images enough tracking for 90% face identity score?)
- How does reference weight interaction affect background continuity?
