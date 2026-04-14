---
type: synthesis
tags: [experiment, reference-conditioning, flux-2, rejected, order-sensitivity]
updated: 2026-04-14
sources: [reference_engine.py]
---

# Experiment #5: Reference Order Sensitivity

## Hypothesis
FLUX.2 exhibits a **Primacy Bias**, giving higher implicit attention to the first image in the Multi-Reference sequence. Moving the prioritized "Style Anchor" from the 1st position to the **last** position will result in a measurable drop in consistency.

## Setup
- **Baseline Score**: 0.877 (Style Anchor at Index 0)
- **Experiment Score**: 0.868 (**REJECTED**)
- **Target Surface**: `src/orchestrator/reference_engine.py`
- **Budget**: 2 benchmark cases (Kael) using `ref_strategy: inverted`.

## Results

| Dimension | Baseline | Experiment | Delta |
| :--- | :---: | :---: | :---: |
| Total Score | 0.877 | 0.868 | -0.009 |
| Face Identity | 0.895 | 0.870 | -0.025 |
| Hairstyle | 0.845 | 0.815 | -0.030 |
| Silhouette | 0.895 | 0.850 | -0.045 |
| World Continuity | 0.855 | 0.865 | +0.010 |
| Art Style | 0.875 | 0.935 | +0.060 |

## Observations
- **Outcome**: **REJECTED**. The inversion resulted in a slight drop in the aggregate score.
- **Primacy Effect**: The -0.025 drop in Face Identity and -0.045 drop in Silhouette support the hypothesis that the model resolves identity more robustly when the primary anchor is presented first.
- **Aesthetic Shift**: Interestingly, **Art Style Consistency** saw a gain (+0.060) in the inverted run. This could mean that "Recency" (the last image) might have a stronger shadow on the style/filter layer, while the "First" image grounds the geometry.

## Conclusion
- Keep the **Style Anchor at Index 0** as per the winning Experiment #3.
- The benefit to identity grounding outweighs the slight aesthetic gain from inversion.

## Next Steps
- Revert to **Weighted Strategy** (Index 0 Anchor).
- Propose **Experiment #6: Hybrid Conditioning** (Mixing LoRA + Multi-Reference).
