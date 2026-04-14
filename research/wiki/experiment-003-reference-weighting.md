---
type: synthesis
tags: [experiment, reference-conditioning, flux-2, win, weighting]
updated: 2026-04-14
sources: [reference_engine.py]
---

# Experiment #3: Reference Strategy Weighting

## Hypothesis
Assigning a higher weight (**1.5x**) to a designated "Style Anchor" image (the first reference) in a Multi-Reference set will stabilize the **Art Style Consistency** score without significantly degrading the **Face Identity** or **Silhouette** scores gained from diversity.

## Setup
- **Baseline Score**: 0.804
- **Experiment Score**: 0.877 (**WIN**)
- **Target Surface**: `src/orchestrator/reference_engine.py`
- **Budget**: 2 benchmark cases (Kael) using `ref_strategy: weighted`.

## Results

| Dimension | Baseline | Experiment | Delta |
| :--- | :---: | :---: | :---: |
| Total Score | 0.804 | 0.877 | +0.073 |
| Face Identity | 0.815 | 0.895 | +0.080 |
| Hairstyle | 0.835 | 0.845 | +0.010 |
| Silhouette | 0.830 | 0.895 | +0.065 |
| World Continuity | 0.800 | 0.855 | +0.055 |
| Art Style | 0.735 | 0.875 | +0.140 |

## Observations
- **Outcome**: **SUCCESS (New Baseline)**.
- **Art Style Consistency** saw a massive recovery (+0.140), validating the "Style Anchor" hypothesis. 
- Interestingly, **Face Identity** (+0.080) and **Silhouette** (+0.065) also saw further improvements, suggesting that a clear primary reference helps the model resolve ambiguities even when using a diverse set.
- **Conclusion**: Balanced weighting (prioritizing one high-quality anchor) is superior to equal-weighting for multi-reference character consistency in FLUX.2.

## Next Steps
- Research the impact of **Reference Order** (e.g., does the model give implicit preference to the first vs. last image?).
- Test the "Minimum Viable Reference Set" (MVRS) with the weighted strategy to find the efficiency ceiling.
