# Project Vision: Character Consistency Lab

## Purpose

The **Character Consistency Lab** is built to solve the "Reality Gap" in AI-generated character consistency. Instead of relying on prompt engineering "vibes," this project implements a research framework to **define, measure, compare, and improve** recurring character consistency across generations.

The goal is to move from "accidental consistency" to "systematic consistency" for game and concept-art characters within the FLUX ecosystem.

## What "Consistency" Means Here

Consistency is not a single nebulous quality. In this lab, it is decomposed into five measurable dimensions:

1.  **Face Identity**: The core facial features, structure, and recognition.
2.  **Hairstyle**: The shape, color, and texture of the character's hair.
3.  **Body Shape / Silhouette**: The physical proportions and the distinctive outline of the character.
4.  **World / Background Continuity**: The environmental context and atmospheric coherence.
5.  **Art Style Consistency**: The specific rendering, line work, and aesthetic signature.

## Why Recurring Characters?

Recurring characters serve as the perfect benchmark for consistency. If a system can maintain a character across wildly different poses, lighting, and environments while preserving their identity, it has solved the core problem of visual persistence.

## Spec-Driven, Not Vibe-Driven

Most current workflows rely on finding the "right prompt" by trial and error. This lab treats consistency as a spec-matching problem:
- We **define** what must persist (Character Spec).
- We **test** the definition against a fixed set of challenges (Benchmarks).
- We **score** the results objectively (Evaluation).
- We **iterate** based on data (Experiments).

## Phase 1 Focus: Research

Phase 1 is strictly about building the "consistency lab" infrastructure:
* benchmark cases
* experiment configs
* generated outputs
* evaluator scores
* comparison reports
* reusable research logic

We are not building a product yet; we are building the tool that makes the product possible.
