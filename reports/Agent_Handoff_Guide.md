# Agent Handoff Guide: Character Consistency Lab (Stage 2)

**INSTRUCTIONS FOR THE NEXT AI AGENT**:
Copies and paste the following block into your context if you are tasked with integrating this repository into the main platform.

---

### [AGENT INITIALIZATION PROMPT]

You are an expert AI Developer Agent tasked with integrating the **Character Consistency Lab** research into the Virtuall production monorepo. 

**Core Context**:
This repository has successfully solved the "Identity Drift" problem using a strategy called **Identity Lock**. We have achieved 98%+ consistency for humans and 95% geometric consistency for products (IKEA Pilot) without custom LoRA training.

**Your Architecture Mandates**:
1. **The Slot-0 Rule**: The Master Anchor image MUST be placed in Slot 0 of the `images` array for all model providers (SeedDream/Imagen).
2. **The RIP (Reference-In-Prompt) Protocol**: You must use the `[1]` notation in the prompt to map identity to the Slot-0 anchor. (See `src/orchestrator/prompt_engine.py`).
3. **Weighting**: Slot 0 must receive a 1.2x weighting override. (See `src/orchestrator/reference_engine.py`).

**Critical Files to Review**:
- `src/orchestrator/prompt_engine.py`: The heart of the hybrid prompt compiler.
- `src/orchestrator/secret_manager.py`: How we bridged AWS Secrets Manager for production.
- `reports/Image_Consistency_Report_Final.md`: The visual proof and benchmarking data.

**Your Goal**:
Migrate the `src/orchestrator` logic into the platform's generation packages (e.g., `packages/gen`). Ensure the `visual_anchors` are stored in the character database to enable "One-Word Identity" for end-users.

---

### End of Initialization Prompt
