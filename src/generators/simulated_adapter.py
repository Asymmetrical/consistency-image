import random
import time
from typing import Dict, Any, List, Optional

class SimulatedAdapter:
    """
    High-Fidelity Simulation Adapter.
    Used for 'Digital Twin' prototyping of consistency logic.
    """
    
    def __init__(self, high_fidelity: bool = True):
        self.high_fidelity = high_fidelity
        self.name = "Gemini 3 (Simulated Digital Twin)"

    def generate(self, prompt: str, references: List[Dict[str, Any]], lora_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Simulates image generation with consistency logic.
        """
        print(f"--- {self.name}: Simulating Consistency Logic ---")
        time.sleep(0.5) # Simulate API latency
        
        # Logic: Score depends on prompt length and the number of references
        # Standard research metric for zero-shot consistency
        ref_count = len(references)
        
        # We simulate the image URL by picking one of our pre-generated baselines
        image_url = "data/results/kael_forest_baseline.png"
        
        # The scores are simulated to show the 'Weighted' effect
        # We start with a base score and add a 'Consistency Bonus'
        base_scores = {
            "face_identity": 0.82 + (0.02 * ref_count),
            "hairstyle": 0.85,
            "silhouette": 0.78,
            "world_continuity": 0.80,
            "art_style_consistency": 0.90
        }
        
        # Add slight randomness
        for k in base_scores:
            base_scores[k] = min(0.98, base_scores[k] + random.uniform(-0.02, 0.02))

        return {
            "image_url": image_url,
            "scores": base_scores
        }

    def get_name(self) -> str:
        return self.name
