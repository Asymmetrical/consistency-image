---
type: entity
tags: [model-variants, flux-2, black-forest-labs]
updated: 2026-04-14
sources: [flux-2-research-summary.md]
---

# FLUX.2 Variants

The [FLUX.2](flux-2-overview.md) family consists of several models tailored for different deployment environments and quality requirements.

## 1. FLUX.2 [max]
- **Target**: Maximum quality / Professional production.
- **Size**: 32B+ Parameters.
- **Features**: Highest semantic adherence, real-time web grounding, best-in-class text rendering.

## 2. FLUX.2 [pro]
- **Target**: Enterprise-grade API usage.
- **Size**: Optimized for scalability and throughput.
- **Availability**: Via BFL API and partners (Replicate, fal.ai).

## 3. FLUX.2 [dev]
- **Target**: Open-weight research and community modification.
- **Size**: 32B Parameters.
- **Importance**: The "Base Layer" for fine-tuning, LoRA research, and experimentation within the Consistency Lab.

## 4. FLUX.2 [flex]
- **Target**: Developer control.
- **Features**: Exposed sampling parameters, guidance scales, and latent flow injection points.

## 5. FLUX.2 [klein]
- **Target**: Local execution / Fast iteration.
- **Size**: Two variants: 9B and 4B.
- **Performance**: Capable of sub-second generation on consumer GPUs.
- **Role in Lab**: Ideal for rapid hypothesis testing (Drafting) before doing high-fidelity runs on [dev] or [max].

---

## Model Selection for Experimentation

For the Character Consistency Lab, we will primarily target:
- **[dev]** for development and local research workflows.
- **[max]** for final high-fidelity benchmarking and report generation.
- **[klein]** for fast-budget experiment loops where total score trends are more important than absolute image quality.
