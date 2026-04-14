import os
import json
import logging
from typing import Dict, Any, List
from google import genai
from google.genai import types
from PIL import Image
import requests
from io import BytesIO

class VisionEvaluator:
    """
    Automated Scorer using Gemini 1.5 Pro on Vertex AI.
    """
    
    def __init__(self, project_id: str, location: str, api_key: str):
        if api_key:
            print("Judge: Initializing via Google AI (API Key mode)...")
            self.client = genai.Client(api_key=api_key)
        else:
            print(f"Judge: Initializing via Vertex AI (Project: {project_id})...")
            self.client = genai.Client(
                vertexai=True,
                project=project_id,
                location=location
            )
        self.model_id = 'gemini-1.5-pro'
        self.logger = logging.getLogger(__name__)

    def _load_bytes(self, image_source: str) -> bytes:
        """Loads image bytes from a local path or URL."""
        if image_source.startswith(('http://', 'https://')):
            response = requests.get(image_source)
            return response.content
        with open(image_source, "rb") as f:
            return f.read()

    def evaluate(self, generated_image_path: str, reference_paths: List[str], character_spec: Dict[str, Any]) -> Dict[str, Any]:
        """
        Performs a vision-based comparison via Vertex AI.
        """
        print(f"--- AI Vision Judge (Vertex AI): Commencing Evaluation ---")
        
        # 1. Prepare Multimodal Parts
        gen_bytes = self._load_bytes(generated_image_path)
        gen_part = types.Part.from_bytes(data=gen_bytes, mime_type="image/png")
        
        ref_parts = []
        for p in reference_paths:
            ref_bytes = self._load_bytes(p)
            mime = "image/png" if p.endswith(".png") else "image/jpeg"
            ref_parts.append(types.Part.from_bytes(data=ref_bytes, mime_type=mime))
        
        # 2. Construct Prompt
        prompt = f"""
        You are a Character Consistency Judge. Compare the GENERATED image against the REFERENCE images.
        
        CHARACTER SPEC:
        {json.dumps(character_spec, indent=2)}
        
        SCORING RUBRIC (0.0 to 1.0):
        - face_identity
        - hairstyle
        - silhouette
        - world_continuity
        - art_style_consistency
        
        RETURN ONLY A RAW JSON OBJECT with these 5 keys and a 'reasoning' brief for each.
        """
        
        # 3. Call Vertex AI
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt), gen_part] + ref_parts)]
            )
            
            # Extract JSON from response text
            text = response.text.strip().replace('```json', '').replace('```', '')
            scores = json.loads(text)
            return scores
        except Exception as e:
            self.logger.error(f"Vision Evaluation Failed: {e}")
            return {"face_identity": 0.5, "reasoning": f"Error: {str(e)}"}
