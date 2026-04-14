import os
import fal_client
from typing import Dict, Any, List, Optional
from .base import BaseGenerator

class FluxAdapter(BaseGenerator):
    """
    Adapter for FLUX.2 models via fal.ai.
    Uses real API calls and automated vision evaluation.
    """
    
    def generate(self, prompt: str, references: List[Dict[str, Any]], lora_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generates an image using FLUX.2 on fal.ai.
        """
        print(f"--- fal.ai: Commencing Real Generation ---")
        
        # 1. Prepare References (Upload local files to fal URLs)
        image_urls = []
        for ref in references:
            path = ref['path']
            if os.path.exists(path):
                print(f"Uploading {path} to fal storage...")
                url = fal_client.upload_file(path)
                image_urls.append(url)
            else:
                print(f"Warning: Reference path {path} not found.")

        # 2. Configure fal.ai Call
        # We use the 'flux-2/edit' or similar endpoint for multi-reference
        model_id = "fal-ai/flux-2/edit" 
        
        arguments = {
            "prompt": prompt,
            "image_urls": image_urls[:4], # fal supports up to 4
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
        }
        
        # Handle LoRA weight if present
        if lora_metadata:
            # Note: Specific fal endpoints handle LoRAs differently. 
            # This is a generic placeholder for the 'loras' schema.
            arguments["loras"] = [{
                "path": lora_metadata['id'],
                "scale": lora_metadata['weight']
            }]

        # 3. Request Execution
        print(f"Submitting to {model_id}...")
        result = fal_client.subscribe(model_id, arguments=arguments, with_logs=True)
        
        return {
            "image_url": result['images'][0]['url'],
            "scores": {} # Scores will be populated by the VisionEvaluator later
        }

    def get_name(self) -> str:
        return "FLUX.2 (fal.ai)"
