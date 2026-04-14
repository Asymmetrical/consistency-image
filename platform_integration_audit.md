# Technical Audit: AI Generation Pipeline & Consistency Lab
**Status**: Simulation Mode (Digital Twin)
**Target**: Real-Pixel Production Integration

## Executive Summary
The Character Consistency Lab has successfully implemented a modular adapter architecture capable of running **Gemini 3 Pro** and **SeedDream (ByteDance)**. However, the transition to live production pixels is currently blocked by several platform-level constraints.

---

## 1. Gemini / Vertex AI Blockers
Our attempts to utilize the Google Cloud / Vertex AI stack for consistent image generation encountered the following failures:

### A. Quota Exhaustion (`429 RESOURCE_EXHAUSTED`)
*   **Model**: `gemini-3-pro-image-preview`
*   **Observations**: Every generation attempt returned a hard block.
*   **Technical Detail**: The current GCP project quota for `generativelanguage.googleapis.com/generate_content_requests` is set to **0** for preview models.
*   **Action for Platform Team**: Increase the "Image Generation" quota for the current Project ID and ensure the `preview` model access is whitelisted.

### B. Response Modality Mismatch (`400 Bad Request`)
*   **Model**: `gemini-2.0-flash`
*   **Observation**: When requesting image output via the standard API key, the model returned: `Model does not support the requested response modalities: image`.
*   **Conflict**: There is a mismatch between the advertised capabilities of the SDK and the active model permissions.

### C. SDK / Pydantic Validation Error
*   **Library**: `google-genai` (v1.73.0)
*   **Issue**: The SDK's `GenerateImagesConfig` model currently throws an `extra_forbidden` error for `style_reference_config`.
*   **Impact**: We cannot currently use "Style Referencing" (the primary consistency mechanism) via the standard Python SDK without manual dictionary overrides or an SDK update.

---

## 2. SeedDream (ByteDance) Blockers
While our adapter is fully implemented to mirror the platform code, it is currently "Dark" due to a lack of credentials.

### A. Credential Requirement
*   **Issue**: No `BYTEDANCE_API_KEY` exists in the research environment.
*   **Impact**: We are forced to simulate SeedDream's "Subject Locking" performance rather than measuring it live.
*   **Action for Platform Team**: Provide a development-scoped key for the ByteDance Volcano Engine (v3 API).

---

## 3. Recommended Platform Actions
To unlock Real-Pixel research, we recommend the following prioritization:

1.  **GCP Quota Fix**: Primary priority. Link a billing account to the research project to unlock non-zero limits for Gemini 3 Pro.
2.  **Credential Sync**: Mirror the ByteDance credentials from the production monorepo into the `consistency-image` research environment.
3.  **SDK Alignment**: Standardize on a specific `google-genai` version across the mono-repo and the lab to prevent Pydantic validation drift.

---

## 4. Current State: The Digital Twin
Until these blocks are cleared, the lab is operating in **Simulation Mode**. 
- **Benefit**: Orchestration logic (weighting, prompt engineering) is still being perfected.
- **Risk**: We are drifting away from "Real World" aesthetic drift patterns that only live tokens can reveal.
