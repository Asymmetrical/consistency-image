from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class BaseGenerator(ABC):
    """
    Abstract Base Class for image generators in the Character Consistency Lab.
    Supports a modular adapter pattern for FLUX, Nano Banana, etc.
    """
    
    @abstractmethod
    def generate(self, prompt: str, references: List[Dict[str, Any]], lora_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Takes a prompt and references, returns standardized score/result metadata.
        Standardized Return: {
            "image_url": str,
            "scores": {
                "face_identity": float,
                "hairstyle": float,
                "silhouette": float,
                "world_continuity": float,
                "art_style_consistency": float
            }
        }
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Returns the model name."""
        pass
