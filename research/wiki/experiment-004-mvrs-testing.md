---
type: synthesis
tags: [experiment, reference-conditioning, flux-2, rejected, efficiency]
updated: 2026-04-14
sources: [reference_engine.py]
---

# Experiment #4: Minimum Viable Reference Set (MVRS)

## Hypothesis
Using only **3 reference images** (Front, Profile, Silhouette) with the **Weighted Strategy** (1.5x on Style Anchor) can maintain a Total Consistency Score **> 0.850**.

## Setup
- **Baseline Score**: 0.877 (5-image set)
- **Experiment Score**: 0.840 (**REJECTED**)
- **Target Surface**: `src/orchestrator/reference_engine.py`
- **Budget**: 2 benchmark cases (Kael) using `ref_strategy: compact`.

## Results

| Dimension | Baseline | Experiment | Delta |
| :--- | :---: | :---: | :---: |
| Total Score | 0.877 | 0.840 | -0.037 |
| Face Identity | 0.895 | 0.840 | -0.055 |
| Hairstyle | 0.845 | 0.795 | -0.050 |
| Silhouette | 0.895 | 0.840 | -0.055 |
| World Continuity | 0.855 | 0.875 | +0.020 |
| Art Style | 0.875 | 0.865 | -0.010 |

## Observations
- **Outcome**: **REJECTED**. The model failed to maintain the >0.850 threshold.
- The -0.055 drop in **Face Identity** and **Silhouette** suggests that 3 images do not provide enough "spatial grounding" for the model to maintain the high-fidelity baseline set in Experiment #3.
- **Inference**: The "Efficiency Ceiling" for Kael appears to be higher than 3 images. 4-5 images are likely the sweet spot for this complexity Level.
- **Winner**: Experiment #3 (5-image Weighted set) remains the lab's current gold standard.

## Next Steps
- Revert to the **Weighted Strategy** (5 references).
- Proposed Experiment #5: **Reference Order Sensitivity** (does moving the Style Anchor to the end of the list change anything?).
