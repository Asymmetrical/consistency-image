Excellent. Here is a strong **v1 repo spec** and an initial **skill set** for a spec-driven R&D repo focused on **consistent recurring game / concept-art characters** in the **FLUX ecosystem**, with **research outputs only** for phase 1.

## Repo purpose

Build a research framework that can **define, measure, compare, and improve recurring character consistency** across generations.

The repo does **not** start as a product or generation service.
It starts as a **consistency lab** that produces:

* benchmark cases
* experiment configs
* generated outputs
* evaluator scores
* comparison reports
* reusable research logic

## Core phase-1 problem statement

Given one or more reference images of a recurring game or concept-art character, generate new images that preserve:

* face identity
* hairstyle
* body shape / silhouette
* world / background continuity
* art style consistency

while allowing controlled variation in pose, composition, and scene specifics.

## Phase-1 non-goals

Do not try to solve these yet:

* full product UI
* multi-tenant backend
* API platform
* moodboard-heavy workflows
* full commercial orchestration
* training a new base model
* perfect automation without human review

## Repo thesis

The repo should prove this:

**Character consistency can be improved systematically by combining structured specs, benchmark suites, evaluator logic, and repeatable experiment loops on top of FLUX-based generation.**

---

# 1. V1 system concept

The repo should be built around five layers.

## A. Character spec layer

Defines what must persist for a character.

Example:

* face identity: high importance
* hairstyle: high importance
* silhouette: medium-high importance
* world continuity: medium importance
* style consistency: high importance

This is the heart of the spec-driven approach.

## B. Benchmark layer

A library of repeatable test cases.

Example benchmark task:

* references: 3 images of the same character
* target prompt: “standing in a ruined temple with torchlight”
* expected invariants: face, hair, silhouette, style
* allowed variation: pose, camera angle, lighting nuance

## C. Generation layer

Wrappers around FLUX workflows.

For v1, keep this simple and modular:

* one generation adapter
* one config format
* one run interface
* one result directory format

## D. Evaluation layer

Scores outputs against the character spec.

This is what lets you say whether things improved.

## E. Experiment layer

Runs repeatable experiments and compares variants.

This is where AutoResearch-style loops can later plug in.

---

# 2. Recommended repo name

`character-consistency-lab`

Other strong options:

* `flux-consistency-lab`
* `character-rnd`
* `consistency-os`

Best practical choice: **character-consistency-lab**

---

# 3. Suggested repo layout

```text
character-consistency-lab/
  README.md
  docs/
    vision.md
    architecture.md
    roadmap.md
    glossary.md

  specs/
    characters/
    benchmarks/
    experiments/
    evaluators/

  data/
    characters/
    benchmarks/
    results/

  src/
    generators/
    evaluators/
    orchestrator/
    reporting/
    utils/

  scripts/
    run_benchmark.py
    run_experiment.py
    score_results.py
    compare_experiments.py
    build_report.py

  experiments/
    exp-001-baseline/
    exp-002-reference-conditioning/
    exp-003-style-locking/

  reports/
    summaries/
    comparisons/

  notebooks/
    exploratory/

  tests/
```

---

# 4. Core spec files

These are the most important pieces to create first.

## `specs/characters/character.schema.yaml`

Defines a recurring character.

Example shape:

```yaml
id: kael-ranger-01
name: Kael
domain: game-character
style_family: dark-fantasy concept art

identity_anchors:
  face_identity:
    priority: 1.0
    description: angular face, narrow nose, calm stern eyes
  hairstyle:
    priority: 0.95
    description: shoulder-length dark hair, tied loosely back
  silhouette:
    priority: 0.85
    description: lean athletic build, long coat outline
  world_continuity:
    priority: 0.7
    description: ruined ancient world, cold desaturated atmosphere
  art_style_consistency:
    priority: 0.9
    description: painterly high-end concept art, realistic proportions

locked_attributes:
  - facial structure
  - hair shape
  - body proportions
  - signature costume outline

soft_attributes:
  - pose
  - scene composition
  - lighting angle

negative_constraints:
  - cartoon proportions
  - sci-fi armor
  - modern clothing
  - anime facial simplification
```

## `specs/benchmarks/benchmark.schema.yaml`

Defines a benchmark case.

```yaml
id: bench-kael-temple-torchlight
character_id: kael-ranger-01
references:
  - data/characters/kael/ref_01.png
  - data/characters/kael/ref_02.png
task_prompt: "Kael standing in a ruined temple lit by torchlight"
expected_invariants:
  - face_identity
  - hairstyle
  - silhouette
  - art_style_consistency
allowed_variations:
  - pose
  - framing
  - lighting nuance
evaluation_profile: default-character-v1
```

## `specs/evaluators/default-character-v1.yaml`

Defines the scoring weights.

```yaml
name: default-character-v1

weights:
  face_identity: 0.30
  hairstyle: 0.20
  silhouette: 0.20
  world_continuity: 0.10
  art_style_consistency: 0.20

pass_thresholds:
  face_identity: 0.80
  hairstyle: 0.75
  silhouette: 0.72
  art_style_consistency: 0.78

report:
  include_failure_modes: true
  include_ranked_outputs: true
```

## `specs/experiments/experiment.schema.yaml`

Defines a single experiment.

```yaml
id: exp-001-baseline
generator: flux-dev-baseline
benchmark_set:
  - bench-kael-temple-torchlight
  - bench-kael-forest-watch
samples_per_case: 4

generation_settings:
  steps: 30
  guidance: 3.5
  seed_mode: fixed-per-case

evaluation_profile: default-character-v1

goal:
  primary: maximize_total_score
  secondary:
    - improve_face_identity
    - reduce_style_drift
```

---

# 5. First docs to write

## `docs/vision.md`

Should answer:

* what this repo is for
* what “consistency” means here
* why recurring characters are the first wedge
* why this is spec-driven, not vibe-driven

## `docs/architecture.md`

Should explain:

* character spec
* benchmark
* generator adapter
* evaluator
* experiment runner
* report builder

## `docs/roadmap.md`

Should define stages:

### Stage 1

Spec + benchmark foundation

### Stage 2

Baseline FLUX experiment framework

### Stage 3

Evaluator improvements

### Stage 4

Experiment comparison workflow

### Stage 5

AutoResearch-compatible loops

### Stage 6

Moodboard extension

---

# 6. The first repo “skills”

Given your direction, I would define **repo skills** first as reusable research capabilities. Later, some of these can become packaged ChatGPT Skills.

## Skill 1: Character Spec Author

Purpose:
turn a character concept plus references into a structured character spec.

Input:

* character references
* written character description
* target style family
* locked vs soft attributes

Output:

* `character.schema.yaml`
* short natural-language summary
* negative constraints list

What it should do:

* extract persistent identity anchors
* separate must-stay-fixed from may-vary
* write precise descriptors
* avoid vague style language

## Skill 2: Benchmark Builder

Purpose:
create benchmark tasks that test recurring character consistency.

Input:

* character spec
* reference set
* scene/task ideas

Output:

* benchmark YAML cases
* benchmark set manifest

What it should do:

* vary scene and pose
* keep invariants explicit
* cover easy, medium, hard cases
* avoid duplicate benchmark types

## Skill 3: FLUX Experiment Config Author

Purpose:
produce experiment configs for repeatable FLUX-based tests.

Input:

* benchmark set
* generation strategy
* evaluation profile

Output:

* experiment config YAML
* experiment hypothesis notes

What it should do:

* define baseline settings
* define comparison settings
* keep runs reproducible
* separate experiment intent from execution

## Skill 4: Consistency Evaluator Designer

Purpose:
define scoring logic and weights for recurring character consistency.

Input:

* desired consistency priorities
* example outputs
* observed failure patterns

Output:

* evaluator profile YAML
* scoring rubric
* failure mode taxonomy

What it should do:

* weight face/hair/silhouette/style/world separately
* define minimum acceptable thresholds
* define report structure
* document tradeoffs clearly

## Skill 5: Experiment Runner / Reporter

Purpose:
run a benchmark set and summarize what changed.

Input:

* experiment config
* result folders
* evaluator profile

Output:

* ranked result summary
* per-benchmark scores
* failure analysis
* experiment comparison report

What it should do:

* compare against baseline
* highlight failure clusters
* identify where improvement happened
* flag regressions clearly

## Skill 6: Drift Taxonomist

Purpose:
label and categorize consistency failures.

Input:

* generated outputs
* benchmark expectations
* evaluator scores

Output:

* drift labels such as:

  * face drift
  * hair drift
  * silhouette collapse
  * world mismatch
  * style drift

This is very useful because it gives you a language for research progress.

## Skill 7: Moodboard Extension Author

Later, not now.

Purpose:
extend the character system with style-anchor objects.

This should be stage 2+, not stage 1.

---

# 7. Which of these should later become real packaged Skills

These three are the strongest future candidates:

### `character-spec-author`

Best for turning concepts into reusable character specs.

### `benchmark-builder`

Best for generating structured test suites.

### `consistency-reporter`

Best for summarizing outputs and research progress.

These are good skill candidates because they encode repeatable workflow logic, not one-off code.

---

# 8. AutoResearch fit

AutoResearch should not be the first layer.
It should enter after the repo has:

* character specs
* benchmark sets
* evaluator profiles
* experiment configs
* repeatable result reports

Then it can optimize things like:

* prompt assembly
* generation settings
* reranking logic
* evaluator weights
* retry strategies

So the repo should be **AutoResearch-ready**, not AutoResearch-dependent on day one.

---

# 9. First milestones

## Milestone 1

Create the spec system.

Deliverables:

* character schema
* benchmark schema
* evaluator schema
* experiment schema

## Milestone 2

Create one example character.

Deliverables:

* one character spec
* 10–20 benchmark cases
* one evaluator profile

## Milestone 3

Create baseline reporting.

Deliverables:

* experiment folder format
* score summary format
* comparison report template

## Milestone 4

Prepare AutoResearch integration.

Deliverables:

* clear objective functions
* stable experiment entrypoints
* machine-readable score outputs

---

# 10. Recommended first files to actually create

Start with these:

```text
docs/vision.md
docs/architecture.md

specs/characters/character.schema.yaml
specs/benchmarks/benchmark.schema.yaml
specs/evaluators/default-character-v1.yaml
specs/experiments/experiment.schema.yaml

specs/characters/example-kael.yaml
specs/benchmarks/kael-benchmark-set.yaml

reports/comparison-template.md
README.md
```

---

# 11. A crisp README opening

You can use this almost as-is:

> Character Consistency Lab is a spec-driven R&D repository for improving recurring game and concept-art character consistency in the FLUX ecosystem.
>
> The repo focuses on defining character identity anchors, building repeatable benchmark suites, evaluating generation quality across consistency dimensions, and comparing experiments over time.
>
> Phase 1 is research-only: benchmarks, scores, experiment configs, and reports. Later phases may extend into orchestration, moodboard-guided generation, and product integration.

---

# 12. My recommendation for how to begin this week

Day 1:
write the schemas and docs.

Day 2:
create one example character spec and one benchmark set.

Day 3:
define the first evaluator rubric and failure taxonomy.

Day 4:
define experiment folder conventions and reporting format.

Day 5:
run the first baseline experiment manually and document the results.

That will give you a real spec-driven backbone very quickly.

I can next turn this into a **full repo starter pack** with ready-to-paste markdown and YAML files.
