# Project Architecture: Five Layers of Consistency

The Character Consistency Lab is organized into five functional layers that work together to create a repeatable research loop.

## 1. Character Spec Layer

The heart of the spec-driven approach. It defines exactly what must persist for a character and assigns priorities to different identity anchors.

- **Files**: `specs/characters/*.yaml`
- **Purpose**: Formalize identity (face, hair, silhouette) and constraints.

## 2. Benchmark Layer

A library of repeatable test cases (tasks) that challenge the generation system.

- **Files**: `specs/benchmarks/*.yaml`
- **Purpose**: Provide a fixed ground for testing; define what varies (pose, lighting) vs. what stays invariant.

## 3. Generation Layer

The execution engine that interacts with the FLUX model.

- **Files**: `src/generators/`, `scripts/run_benchmark.py`
- **Purpose**: Modular adapter to run generation workflows with specific configs.

## 4. Evaluation Layer

The scoring engine that measures outputs against the Character Spec.

- **Files**: `src/evaluators/`, `specs/evaluators/*.yaml`
- **Purpose**: Provide objective scores and identify failure modes (e.g., "face drift", "style collapse").

## 5. Experiment Layer

The orchestration layer that runs comparison tests.

- **Files**: `experiments/`, `specs/experiments/*.yaml`, `scripts/run_experiment.py`
- **Purpose**: Run repeatable experiments to test hypotheses (e.g., "does reference conditioning improve face identity?").

---

## Data Flow

1.  **Orchestrator** loads an **Experiment Config**.
2.  The config points to a **Benchmark Set** and a **Character Spec**.
3.  **Generator** runs the benchmark tasks, saving outputs to a results directory.
4.  **Evaluator** scores the outputs based on the **Evaluation Profile**.
5.  **Reporter** builds a comparison report from the scores and outputs.
