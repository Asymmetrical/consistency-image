---
type: entity
tags: [model, generation, logic-first, gemini-3]
updated: 2026-04-14
sources: [nano-banana-research-summary.md]
---

# Nano Banana (Gemini 3 Pro)

**Nano Banana** is the logic-first image generation model developed by Google DeepMind as part of the Gemini 3 family.

## Conceptual Core: Logic-First Consistency
While models like FLUX.2 focus on "Aesthetic Conditioning" (pixel-level similarity), Nano Banana utilizes a **Reasoning Engine** to maintain consistency.

### Key Capabilities
- **Thinking Mode**: The model generates a reasoning trace before outputting the image, allowing it to "check" its work against the character spec.
- **Instruction Adherence**: Extreme reliability in following complex negative prompts and spatial instructions.
- **Native Editing**: Supports multi-turn editing where the character's identity is locked by the model's internal understanding, not just reference pixel weights.

## Usage in the Lab
In the **Character Consistency Lab**, Nano Banana serves as our benchmark for **Reasoning-Based Identity Retention**. We compare its "Logical Stability" against FLUX.2's "Pixel Stability."

## See Also
- [Gemini 3 Reasoning Engine](gemini-3-reasoning-engine.md)
- [FLUX.2 Comparison](index.md)
