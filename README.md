# Character Consistency Lab

> [!NOTE]
> Character Consistency Lab is a spec-driven R&D repository for improving recurring game and concept-art character consistency in the FLUX ecosystem.

The repo focuses on defining character identity anchors, building repeatable benchmark suites, evaluating generation quality across consistency dimensions, and comparing experiments over time.

Phase 1 is research-only: benchmarks, scores, experiment configs, and reports. Later phases may extend into orchestration, moodboard-guided generation, and product integration.

## The AutoResearch Operating Model

This repo is built around a disciplined research loop inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

1.  **Human-in-the-loop**: The human defines the research agenda in [research_program.md](file:///d:/Experiments/consistency/research_program.md).
2.  **Autonomous Iteration**: The AI research agent proposes hypotheses and modifies the **Editable Surface** (e.g., `src/orchestrator/prompt_engine.py`).
3.  **Fixed-Budget Evaluation**: Every experiment runs a fixed set of benchmarks via `scripts/experiment_runner.py` to ensure scores are comparable.
4.  **Keep-or-Revert**: Only changes that improve the **Total Weighted Score** compared to the `current_baseline.json` are committed.

## Getting Started

1.  **Review the Playbook**: Read [research_program.md](file:///d:/Experiments/consistency/research_program.md) to understand the current goals and rules.
2.  **Define Characters & Benchmarks**: Add specs in `specs/characters/` and `specs/benchmarks/`.
3.  **Run an Experiment**: Execute the research loop:
    ```bash
    python scripts/experiment_runner.py
    ```
4.  **Optimize the Prompt Engine**: Edit `src/orchestrator/prompt_engine.py` to test different prompt compilation strategies.
5.  **Track Progress**: Monitor the `data/results/current_baseline.json` and `data/results/experiment_log.tsv`.

## Project Structure

- `research/`: Persistent knowledge base following the [LLM Wiki pattern](file:///d:/Experiments/consistency/research/WIKI_SCHEMA.md).
    - `raw/`: Immutable source documents.
    - `wiki/`: Interlinked markdown pages maintained by Antigravity.
- `docs/`: Vision, Architecture, Roadmap, and Glossary.
- `specs/`: Structured definitions (YAML) for characters, benchmarks, evaluators, and experiments.
- `data/`: Raw data, including character references and benchmark results.
- `src/`: Core logic for generation orchestration, evaluation, and reporting.
- `scripts/`: Python scripts for running the lab workflows.
- `experiments/`: Record of experiment runs, including configs and outputs.
- `reports/`: Human-readable summaries and cross-experiment comparisons.

## Core Thesis

Character consistency can be improved systematically by combining structured specs, benchmark suites, evaluator logic, and repeatable experiment loops on top of FLUX-based generation.
