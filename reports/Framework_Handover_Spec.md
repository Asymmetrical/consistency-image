# Technical Specification: AI Consistency Orchestration (Stage 2)

**Version**: 1.0  
**Target**: Platform Integration (Virtuall Monorepo)  
**Subject**: Identity Lock Orchestration Layer  

## 1. System Overview
The **Consistency Orchestrator** is a middleware layer designed to provide model-agnostic character and product stability. It decouples **Identity** (Geometric Invariants) from **Context** (User Prompts).

### Core Components:
- **`src.orchestrator.prompt_engine`**: Compiles Hybrid Prompts using Slot-0 Anchoring.
- **`src.orchestrator.reference_engine`**: Manages positional weighting and strategy selection (Diverse vs. Weighted).
- **`src.orchestrator.secret_manager`**: AWS Boto3 bridge for production secret retrieval.
- **`src.orchestrator.s3_manager`**: Ingestion layer for cloud-hosted reference links.

## 2. The Identity Lock Protocol (The API)
Any agent integrating this logic must strictly follow the **RIP (Reference-In-Prompt)** standard:

1. **Positional Slotting**: The "Master Anchor" (Ground Truth) MUST reside in **Slot 0** of the generation payload.
2. **Hybrid Mapping**: The prompt must explicitly reference Slot 0 using the `[1]` string notation at high-intensity points (e.g. *"The face [1] must precisely mirror [1]"*).
3. **Weighting**: Slot 0 should be assigned a weight of **1.2x to 1.5x** relative to other references.

## 3. Data Schemas

### Character/Product Profile (YAML/JSON)
```yaml
id: <UUID>
name: <String>
visual_anchors: <Description of geometric invariants>
identity_anchors:
  face_identity: { description: <String> }
  # ...
style_family: <String>
```

### Reference Object
```json
{
  "path": "s3://<bucket>/<key>",
  "weight": 1.2
}
```

## 4. Integration Strategy
The recommended integration path for the `virtuall-monorepo` is:
1. **Model Adapter level**: Inject the `prompt_engine` logic into `packages/gen/src/engines/`.
2. **Middleware level**: Intercept `GenerateImagesConfig` to enrich the `prompt` and `images` arrays before they hit the cloud providers.
3. **Registry level**: Store the `visual_anchors` in the character metadata database.

## 5. Critical Invariants
- **NEVER** let the prompt drift into describing the character's geometry manually; always use the `[1]` anchor mapping.
- **NEVER** send references without Slot-0 prioritization if consistency is requested.
