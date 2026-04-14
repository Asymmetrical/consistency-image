# Research Program: Character Consistency Optimization

This document serves as the primary instructions for the AI research agent. It defines the goal, the boundaries, and the protocol for systematic consistency improvement.

## 1. Primary Objective

**Maximize the Weighted Character Consistency Score.**

The score is a weighted average of:
- **Face Identity** (30%)
- **Hairstyle** (20%)
- **Silhouette** (20%)
- **World Continuity** (10%)
- **Art Style Consistency** (20%)

## 2. The Research Loop (Protocol)

Every research iteration must follow these five steps:

1.  **Hypothesis**: Propose a single change to the **Editable Surface**.
2.  **Execution**: Modify the target file(s) and run `python scripts/experiment_runner.py`.
3.  **Scoring**: The runner will output a composite score based on a **Fixed Budget** of benchmark cases.
4.  **Comparison**: Compare the new score against the `data/results/current_baseline.json`.
5.  **Decision**: 
    - If the score improves: **KEEP** the change (commit/save as new baseline).
    - If the score stays the same or drops: **REVERT** the change.

## 3. Editable Surface

The agent is allowed to modify the following files to test hypotheses:

- **Prompt Engine**: `src/orchestrator/prompt_engine.py` (How specs/references are Compiled).
- **Reference Strategy**: `specs/benchmarks/kael-benchmark-set.yaml` (Which images are used as references).
- **Evaluator Weights**: `specs/evaluators/default-character-v1.yaml` (Scoring priority).
- **Generation Parameters**: `specs/experiments/experiment.schema.yaml` (Steps, guidance, etc.).

## 4. Fixed Experiment Budget

To ensure comparability, all experiments must use:
- **Benchmark Set**: `specs/benchmarks/kael-benchmark-set.yaml`.
- **Sample Count**: 4 candidates per benchmark case.
- **Seed Policy**: Deterministic (fixed seeds per case).
- **Model**: FLUX.2 [dev] (preferred for research stability).

## 5. Constraints

- Never modify the **Benchmark Ground Truth** (`specs/benchmarks/kael-benchmark-set.yaml`)—except for the `references` list during a reference-optimization experiment.
- Never modify the **Character Specs** (`specs/characters/example-kael.yaml`) during a research run.
- Changes must be focused and incremental (one hypothesis at a time).

## 6. Current Focus Areas

- **Objective 2: Hybrid Orchestration**
    - Optimization of LoRA + Multi-Reference weights (Experiment #6 established 0.910 baseline).
    - Research the "Order Sensitivity" and "MVRS" efficiency ceilings.

- **Objective 3: Cross-Model Logic vs. Aesthetic**
    - Benchmark Nano Banana's (Gemini 3) structural reasoning against FLUX.2's visual fidelity.
    - Research "Dual-Model Pipelines" (Nano Banana for identity setup, FLUX for aesthetic finish).

- **Reference Orchestration**: Optimizing the selection and weighting of characters' reference images using FLUX.2's Multi-Reference Conditioning.
- **Prompt vs. Reference Balance**: Researching the tradeoff between detailed text descriptions and image-based conditioning.
- **Identity Retention**: Minimizing face drift across high-variance poses using a stable reference anchor.
