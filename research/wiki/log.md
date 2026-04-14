# Wiki Log

A chronological record of events and knowledge accumulation.

## [2026-04-14] init | Research Wiki Initialized
- Created directory structure and core schema.
- Initialized index and log files.

## [2026-04-14] experiment | Experiment #1: Prompt Specification Header
- Outcome: REJECTED (Score 0.737 vs Baseline 0.781).
- Finding: Formal header structure diluted face identity focus.

## [2026-04-14] ingest | Nano Banana (Gemini 3)
- Source: DeepMind Release Notes.
- Value: Introduced "Logic-first" consistency paradigm. Established foundation for Cross-Model benchmarking.

## [2026-04-14] architectural-shift | Modular Generator Design
- Goal: Create a multi-model adapter pattern (FLUX.2 vs Nano Banana).

## [2026-04-14] ingest | FLUX.2 Research & Pivot
- Ingested FLUX.2 release summary.
- Pivot: Research focus shifted to native **Multi-Reference Conditioning**.
- Created overview, variants, and concept pages.

## [2026-04-14] experiment | Experiment #2: Reference Set Diversity
- Outcome: WIN (Score 0.804 vs Baseline 0.781).
- Finding: Diverse references (front/profile/silhouette) boost silhouette and continuity scores significantly.

## [2026-04-14] experiment | Experiment #3: Reference Strategy Weighting
- Outcome: WIN (Score 0.877 vs Baseline 0.804).
- Finding: Weighting a "Style Anchor" at 1.5x recovers aesthetic consistency while maintaining identity gains.

## [2026-04-14] experiment | Experiment #4: Minimum Viable Reference Set
- Outcome: REJECTED (Score 0.840 vs Baseline 0.877).
- Finding: 3 images (MVRS) fall below the 0.850 high-fidelity threshold. 4-5 images are required for this complexity level.

## [2026-04-14] experiment | Experiment #5: Reference Order Sensitivity
- Outcome: REJECTED (Score 0.868 vs Baseline 0.877).
- Finding: Primacy Bias confirmed. Placing the Style Anchor first results in more robust identity grounding.

## [2026-04-14] experiment | Experiment #6: LoRA vs. Multi-Reference Hybrid
- Outcome: WIN (Score 0.910 vs Baseline 0.877).
- Finding: Combining LoRA (0.6) with Multi-Reference conditioning breaks the 0.900 consistency threshold.
