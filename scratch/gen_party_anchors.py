import os
import requests
import json
from src.generators.seeddream_adapter import SeedDreamAdapter
from src.orchestrator.secret_manager import bootstrap_production_env

def generate_party():
    # 1. Setup Environment
    bootstrap_production_env()
    api_key = os.getenv('BYTEDANCE_API_KEY')
    if not api_key:
        raise Exception("BYTEDANCE_API_KEY not found in environment")
        
    adapter = SeedDreamAdapter(api_key)
    os.makedirs('data/characters/party', exist_ok=True)
    
    characters = [
        {
            "name": "elara",
            "prompt": "MASTER ANCHOR: Regal woman with glowing silver hair, ornate blue silk robes, silver staff with a pulsing sapphire, studio lighting, white background"
        },
        {
            "name": "thorn",
            "prompt": "MASTER ANCHOR: Massive man in battle-worn black plate armor, scarred jawline, holding a tower shield and a broadsword, studio lighting, white background"
        },
        {
            "name": "nyx",
            "prompt": "MASTER ANCHOR: Slender athletic woman in dark grey hooded leather, dual daggers on hips, green eyes visible under hood, studio lighting, white background"
        }
    ]
    
    for char in characters:
        print(f"--- Generating {char['name'].upper()} ---")
        try:
            result = adapter.generate(char['prompt'], [])
            url = result['image_url']
            
            # Download
            response = requests.get(url)
            save_path = f"data/characters/party/{char['name']}_anchor.png"
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Success: {char['name']} saved to {save_path}")
            print(f"URL: {url}")
        except Exception as e:
            print(f"Error generating {char['name']}: {e}")

if __name__ == "__main__":
    generate_party()
