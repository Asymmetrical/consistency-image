---
type: synthesis
tags: [experiment, prompt-engineering, failed]
updated: 2026-04-14
sources: [prompt_engine.py]
---

# Experiment #1: Prompt Specification Header

## Hypothesis
Structuring the prompt with a formal specification (`FIXED CHARACTER SPECIFICATION: Face: ... Hair: ...`) and explicit headers (`ART STYLE:`, `SCENE/TASK:`) would improve consistency scores by clearly separating character identity from scene specifics.

## Setup
- **Baseline Score**: 0.781
- **Experiment Score**: 0.737
- **Target Surface**: `src/orchestrator/prompt_engine.py`
- **Budget**: 2 benchmark cases (Kael)

## Results

| Dimension | Baseline | Experiment | Delta |
| :--- | :---: | :---: | :---: |
| Total Score | 0.781 | 0.737 | -0.044 |
| Face Identity | 0.800 | 0.610 | -0.190 |
| Hairstyle | 0.795 | 0.755 | -0.040 |
| Silhouette | 0.725 | 0.850 | +0.125 |
| World Continuity | 0.730 | 0.650 | -0.080 |
| Art Style | 0.820 | 0.840 | +0.020 |

## Observations
- **Outcome**: **REJECTED**.
- While **Silhouette** (+0.125) and **Art Style** (+0.020) saw improvements, there was a significant drop in **Face Identity** (-0.190).
- **Inference**: The rigid "Specification" structure might have made the prompt too long or diluted the attention on the face by giving equal real-estate to the blocky header text. 

## Next Steps
- Revert to the simpler string-concatenation baseline.
- Next experiment should try **weighting identity anchors** (e.g., using parentheses like `(angular face:1.3)`) instead of restructuring the entire prompt into headers.
