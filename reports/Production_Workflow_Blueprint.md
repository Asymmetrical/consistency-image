# Production Blueprint: AI Consistency Orchestration

This document outlines the proposed architecture for integrating the **Identity Lock** consistency strategy into the Virtuall production environment. It transitions our lab-based YAML files into a scalable, user-centric workflow.

## 1. The Unified Identity Registry (The Spec)
In the lab, we use YAML files (`kael.yaml`, `pizza.yaml`). In production, these become **Identity Profiles** stored in our database.

### How it works:
- **Registration**: When a creator character is created, the platform generates/captures the **Master Anchors** (the Ground Truth images).
- **Storage**: These anchors are stored in our production S3 bucket with permanent, internal URLs.
- **Invariants**: We store a list of "Visual Invariants" (e.g., "sharp jawline", "leopard-spotted crust") associated with the profile ID.

## 2. The Orchestration Middleware (The Bridge)
This is the "Logic Layer" that sits between the User UI and the GenAI APIs (SeedDream/Imagen/Flux).

### The "Intercept & Enrich" Workflow:
1. **User Prompt**: The user enters a simple natural language prompt:
   > *"Kael sitting in a cyberpunk library, neon lighting."*
2. **Identity Lookup**: The system detects the keyword **"Kael"** (or the user selects the Kael profile from a dropdown).
3. **Spec Retrieval**: The system pulls the **Kael Identity Profile** from the Registry.
4. **Hybrid Compilation**: Our `compile_prompt` logic automatically transforms the user's simple prompt into a high-consistency production prompt:
   > *"SUBJECT UNIFORM: Kael as seen in [1], sitting in a cyberpunk library, neon lighting, highly detailed face [1], identity lock active."*
5. **Reference Mapping**: The system automatically assigns the Kael Reference Anchor to **Slot-0** and weights it at 1.0 (Master).
6. **API Dispatch**: The enriched request is sent to the model provider (e.g., ByteDance).

## 3. UX Impact Analysis
The primary goal of this architecture is to provide **High-Fidelity Consistency** while **Lowering the Barrier to Entry.**

### UX Wins:
- **"One-Word Identity"**: Users don't need to be expert prompt engineers. They don't have to re-describe their character in every prompt. The platform "remembers" the character's geometry.
- **Trial-and-Error Reduction**: Consistency is "locked" from frame 1, reducing the number of regenerative credits wasted on "failed" faces.
- **Brand Control (The IKEA Benefit)**: For corporate clients, the Registry ensures that a product (like a pizza or a chair) **cannot deviate** from its legal/accurate appearance, regardless of what the user prompts as the background.

## 4. Logical Workflow Diagram

```mermaid
graph TD
    A[User UI] -- "Prompt: Kael in a library" --> B{Orchestration Middleware}
    B -- "Fetch Kael Profile" --> C[Identity Registry]
    C -- "Anchors + Invariants" --> B
    B -- "Enrich & Anchor" --> D[Hybrid Prompt Compiler]
    D -- "Final Request (Slot-0 + Ref [1])" --> E[GenAI API (SeedDream)]
    E -- "Consistent Pixel Result" --> A
```

## 5. Conclusion
By moving the consistency logic into a **Middleware Layer**, we decouple the "Who" (Character/Product) from the "Where" (Prompt/Environment). This allows Virtuall to offer a "Consistent Subject" feature that is model-agnostic and pro-grade, while keeping the UI clean and accessible for non-technical creators.
