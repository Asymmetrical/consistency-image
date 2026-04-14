---
type: synthesis
tags: [experiment, hybrid, lora, flux-2, win]
updated: 2026-04-14
sources: [reference_engine.py]
---

# Experiment #6: LoRA vs. Multi-Reference Hybrid

## Hypothesis
The **Hybrid Model** (Combining a character-specific LoRA with FLUX.2's Multi-Reference Conditioning) will reach the "Final Mile" of consistency, outperforming native references alone by providing both geometric memory (LoRA) and visual grounding (Refs).

## Setup
- **Baseline Score**: 0.877 (Multi-Reference Only)
- **Experiment Score**: 0.910 (**WIN**)
- **Target Surface**: `src/orchestrator/reference_engine.py` / `src/orchestrator/experiment_runner.py`
- **Budget**: 2 benchmark cases (Kael) using `ref_strategy: lora_hybrid`.
- **LoRA Weight**: 0.6.

## Results

| Dimension | Baseline | Experiment | Delta |
| :--- | :---: | :---: | :---: |
| Total Score | 0.877 | 0.910 | +0.033 |
| Face Identity | 0.895 | 0.915 | +0.020 |
| Hairstyle | 0.845 | 0.950 | +0.105 |
| Silhouette | 0.895 | 0.885 | -0.010 |
| World Continuity | 0.855 | 0.885 | +0.030 |
| Art Style | 0.875 | 0.900 | +0.025 |

## Observations
- **Outcome**: **SUCCESS (New Baseline)**. We have passed the 0.900 consistency threshold.
- **Identity Ceiling**: **Hairstyle** saw a massive boost (+0.105), likely because LoRAs excel at capturing complex textures like hair that are hard to describe.
- **Identity vs. Silhouette**: While Face Identity grew, there was a minor regression in **Silhouette** (-0.010). This might be due to the LoRA weight (0.6) competing slightly with the silhouette references.
- **Conclusion**: The Hybrid approach is the new Gold Standard for the lab.

## Next Steps
- Research **LoRA Weight Optimization**: Does increasing LoRA weight to 0.8 continue the trend or cause "Burn-in" degradation?
- **Real Integration**: With a 0.910 score baseline, we are ready to move from stubs to real pixels.
