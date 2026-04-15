import os
import json
from typing import Dict, Any, List, Optional
from google import genai
from google.genai import types
from PIL import Image

class GoogleImageAdapter:
    """
    Adapter for Google Imagen models on Vertex AI.
    Re-targeted to the production-stable workhorse model.
    """
    
    def __init__(self, project_id: str, location: str, api_key: str):
        self.project_id = project_id
        self.location = location
        # If API KEY is provided, use Google AI mode
        if api_key:
            print("Initializing Imagen via Google AI (API Key mode)...")
            self.client = genai.Client(api_key=api_key)
        else:
            print(f"Initializing Imagen via Vertex AI (Project: {project_id})...")
            self.client = genai.Client(
                vertexai=True,
                project=project_id,
                location=location
            )
        # Use Imagen 4 (Premium fidelity for product research)
        self.model_id = "imagen-4.0-generate-001"

    def _prepare_style_references(self, references: List[Dict[str, Any]]) -> List[types.StyleReferenceImage]:
        """
        Converts local reference images into StyleReferenceImage objects.
        """
        ref_images = []
        for i, ref in enumerate(references):
            path = ref['path']
            if os.path.exists(path):
                img = Image.open(path)
                ref_images.append(types.StyleReferenceImage(
                    image=img,
                    reference_id=i + 1 # [1], [2], etc.
                ))
        return ref_images

    def generate(self, prompt: str, references: List[Dict[str, Any]], lora_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generates an image using Imagen 3.
        Uses Style Reference for consistency.
        """
        print(f"--- Imagen 3: Commencing Generation ({self.model_id}) ---")
        
        # 1. Prepare Style References
        style_refs = self._prepare_style_references(references)
        
        # 2. Configure Imagen Generation
        # Construct kwargs to avoid passing None to fields that forbid it
        config_args = {
            "number_of_images": 1,
            "aspect_ratio": "1:1",
        }
        
        if style_refs:
            config_args["style_reference_config"] = types.StyleReferenceConfig(
                style_reference_images=style_refs
            )
            
        config = types.GenerateImagesConfig(**config_args)
        
        # 3. Request Execution
        print(f"Submitting to Imagen 3 API with {len(style_refs)} style references...")
        try:
            response = self.client.models.generate_images(
                model=self.model_id,
                prompt=prompt,
                config=config
            )
            
            # 4. Extract and Save Result
            if response.generated_images:
                img_data = response.generated_images[0].image
                output_path = f"data/results/output_{os.urandom(4).hex()}.png"
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                img_data.save(output_path)
                
                return {
                    "image_url": os.path.abspath(output_path),
                    "scores": {} 
                }
            
        except Exception as e:
            print(f"Imagen Generation Failed: {e}")
            return {"image_url": f"error://{str(e)}", "scores": {}}

        return {"image_url": "error://no-image", "scores": {}}

    def get_name(self) -> str:
        return f"Imagen 3 ({self.model_id})"
