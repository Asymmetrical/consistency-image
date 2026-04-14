# FLUX.2 Research Summary

**Source Title**: FLUX.2: The Next Generation of Image Generation and Editing
**Released**: November 25, 2025
**Developer**: Black Forest Labs
**URL**: https://bfl.ai/blog/flux-2-release

## Summary
FLUX.2 is a family of state-of-the-art image generation models that succeeds FLUX.1. It introduces significant architectural and feature improvements, most notably a native solution for character consistency through Multi-Reference Conditioning.

## Key Technical Features

### Multi-Reference Conditioning
- Allows up to 10 reference images (PNG/JPG) as input.
- Enables the model to maintain character identity, clothing, style, and specific product details without LoRA training.
- Users can weight individual references to balance identity vs. variation.

### Architecture
- **Vision-Language Model**: Mistral-3 24B (replaces the 12B original).
- **Transformer**: Rectified Flow Transformer with 32B parameters.
- **Improved Spatial Understanding**: Better handling of physical properties and complex compositional logic.

### Models
- **FLUX.2 [max]**: Highest quality, 32B+, strong prompt following.
- **FLUX.2 [pro]**: Production grade via API.
- **FLUX.2 [dev]**: Open-weights research model (32B).
- **FLUX.2 [flex]**: Developer-controlled parameters.
- **FLUX.2 [klein]**: Size-distilled (9B & 4B) for rapid local generation.

## Implications for Character Consistency
FLUX.2 moves the "state of the art" from manual prompt engineering and per-character LoRAs to native reference orchestration. The "Stable Anchor" is no longer just a text description; it is a multi-dimensional reference set.
