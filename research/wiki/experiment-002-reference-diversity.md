---
type: synthesis
tags: [experiment, reference-conditioning, flux-2, win]
updated: 2026-04-14
sources: [reference_engine.py]
---

# Experiment #2: Reference Set Diversity

## Hypothesis
Using a **diverse reference set** (Front-face + Profile + Silhouette) in FLUX.2's Multi-Reference Conditioning will lead to higher aggregate consistency scores than a homogeneous set. The model will benefit from a more complete visual understanding of the character.

## Setup
- **Baseline Score**: 0.781
- **Experiment Score**: 0.804 (**WIN**)
- **Target Surface**: `src/orchestrator/reference_engine.py` / `specs/benchmarks/kael-benchmark-set.yaml`
- **Budget**: 2 benchmark cases (Kael) using `ref_strategy: diverse`.

## Results

| Dimension | Baseline | Experiment | Delta |
| :--- | :---: | :---: | :---: |
| Total Score | 0.781 | 0.804 | +0.023 |
| Face Identity | 0.800 | 0.815 | +0.015 |
| Hairstyle | 0.795 | 0.835 | +0.040 |
| Silhouette | 0.725 | 0.830 | +0.105 |
| World Continuity | 0.730 | 0.800 | +0.070 |
| Art Style | 0.820 | 0.735 | -0.085 |

## Observations
- **Outcome**: **SUCCESS (New Baseline)**.
- **Silhouette** (+0.105) and **World Continuity** (+0.070) saw the largest gains, confirming the hypothesis that diverse references help the model ground the character in 3D space.
- **Face Identity** and **Hairstyle** also saw steady improvements.
- **Trade-off**: There was a regression in **Art Style Consistency** (-0.085). This suggests that having more references might "confuse" the model's aesthetic focus if the reference images aren't perfectly style-matched.

## Next Steps
- Implement **Reference Weighting** research to see if we can recover the Art Style score by weighting a "Style Anchor" reference higher than others.
- Establish the "Minimum Viable Reference Set" (MVRS) for Kael.
