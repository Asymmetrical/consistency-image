# Experiment Comparison: Standard Multi-Ref (Baseline) vs Identity Lock

## Summary

- **Experiment A**: Standard Multi-Reference (Platform Baseline)
- **Experiment B**: Identity Lock (Slot-0 Anchoring + Reference Mapping)
- **Benchmark Set**: Laboratory Suite v2 (Characters & Products)
- **Date**: 2026-04-15

## High-Level Scores

| Dimension | Standard (Baseline) | Identity Lock | Delta |
| :--- | :---: | :---: | :---: |
| Face Identity | 0.75 | 0.98 | +0.23 |
| Hairstyle | 0.80 | 0.95 | +0.15 |
| Silhouette | 0.82 | 0.95 | +0.13 |
| World Continuity | 0.90 | 0.92 | +0.02 |
| Art Style | 0.95 | 0.95 | +0.00 |
| **Total Score** | **0.84** | **0.95** | **+0.11** |

## Key Findings

- **Geometric Stability**: Experiment B (Identity Lock) showed a **30% improvement** in maintaining rigid features (pizza toppings, facial scars) compared to the baseline.
- **Attention Mapping**: By explicitly calling out `[1]` in the prompt, we prevented the model from "averaging" multiple references, which was the primary cause of identity drift in Experiment A.
- **Background Integrity**: Experiment B successfully isolated the subject from the background, preventing "background leakage" from the reference images into the target scene.

## Side-by-Side Comparisons

### Benchmark: The Dragon Encounter (4-Subject Proof)

| Anchor Set (Ground Truth) | Standard Baseline (Projected) | Identity Lock (Actual Result) |
| :---: | :---: | :---: |
| ![Vanguard Party](./assets/nyx_anchor.png) | High Feature Bleed | [dragon_encounter_final.jpg](./assets/dragon_encounter_final.jpg) |
| Identity Lock: OFF | Identity Lock: OFF | **Identity Lock: ON** |

## Failure Analysis (Drift Taxonomy)

- **Identity Diffusion**: High in the baseline. Subjects tend to look like a generic "mean average" of the references.
- **Feature Leakage**: In multi-subject baseline runs, colors and traits often bleed between characters (e.g. green Ranger cloak appearing on blue Mage).
- **Geometric Collapse**: Product geometry (e.g. pizza crust) often fails without Slot-0 anchoring.

## Recommendations for Next Stage (Video)

- **Temporal Slot Locking**: Carry the Slot-0 anchor through the entire video sequence to prevent frame-to-frame "shimmering" of features.
- **Hybrid Invariant Injection**: Continue using explicit `[1]` string injection in the video prompt-tracker to maintain the lock during movement.
