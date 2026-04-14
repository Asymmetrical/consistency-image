# Nano Banana (Gemini 3) Research Summary

**Source Title**: Gemini 3: The Next Generation of Multimodal Reasoning and Generation
**Released**: December 2025
**Developer**: Google DeepMind
**Internal Designation**: "Nano Banana"

## Summary
Nano Banana is the creative image generation capability native to the Gemini 3 model family. Unlike many "vision-first" models (like FLUX), Nano Banana is "logic-first," prioritizing structural consistency, instruction adherence, and reasoning.

## Key Technical Features

### Gemini 3 Reasoning Engine (Thinking Mode)
- Supports a "Thinking" phase where the model generates a latent reasoning chain before rendering pixels.
- Capable of following complex, multi-part character specs without drifting.
- Superior text rendering and infographic layout capabilities.

### Integrated Reference Handling
- Uses a "Semantic Reference" system where images are treated as logical tokens.
- Supports conversational image editing (e.g., "Change Kael's coat to green while keeping his face identical").

### Models
- **gemini-3-pro-image-preview** (Nano Banana Pro): High-fidelity, reasoning-heavy.
- **gemini-3.1-flash-image-preview** (Nano Banana 2): Faster, optimized for volume.

## Implications for Character Consistency
Nano Banana shifts the consistency challenge from "Image Conditioning Weights" to "Logical Spec Adherence." It relies more on the model's ability to "understand" the character spec than on the specific pixel weights of the references.
