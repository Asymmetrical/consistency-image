import yaml
import json
import os
import sys
import datetime
import random
from dotenv import load_dotenv

# Ensure the root directory is in sys.path so we can import 'src'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.orchestrator.prompt_engine import compile_prompt
from src.orchestrator.reference_engine import get_reference_set
from src.generators.simulated_adapter import SimulatedAdapter
from src.generators.seeddream_adapter import SeedDreamAdapter
from src.orchestrator.vision_evaluator import VisionEvaluator

# Load environment variables (.env.local)
load_dotenv(".env.local")

def get_env_var(name: str, default: str = "") -> str:
    """Robustly fetch env vars, cleaning 'SET ' prefixes if present."""
    val = os.getenv(name)
    if val and val.startswith("SET "):
        return val.replace("SET ", "").split("=")[-1]
    return val or default

# Paths
CHAR_SPEC_PATH = "specs/characters/example-kael.yaml"
BENCHMARK_PATH = "specs/benchmarks/kael-benchmark-set.yaml"
EVALUATOR_PATH = "specs/evaluators/default-character-v1.yaml"
BASELINE_PATH = "data/results/current_baseline.json"
LOG_PATH = "data/results/experiment_log.tsv"

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def run_experiment(mode: str = "simulation", model: str = "gemini"):
    """
    Main loop for Character Consistency Lab.
    Supports 'gemini' (Logic Focus) and 'seeddream' (Identity Focus) modes.
    """
    print(f"--- Character Consistency Lab: {model.upper()} ({mode.upper()}) ---")
    
    # Configuration from .env.local
    project_id = get_env_var('GCP_PROJECT_ID', '894937596656')
    location = get_env_var('GCP_LOCATION', 'us-central1')
    google_api_key = get_env_var('GOOGLE_API_KEY')
    bytedance_api_key = get_env_var('BYTEDANCE_API_KEY')
    
    # Safety Catch
    max_budget = 5 if mode == "simulation" else 1 
    
    # Initialize Generator based on Selection
    if mode == "simulation":
        if model == "seeddream":
            generator = SeedDreamAdapter() # Defaults to sim if no key
        else:
            generator = SimulatedAdapter()
    else:
        # Real Mode
        if model == "seeddream":
            generator = SeedDreamAdapter(api_key=bytedance_api_key)
        else:
            from src.generators.google_image_adapter import GoogleImageAdapter
            generator = GoogleImageAdapter(project_id, location, google_api_key)
        
    evaluator = None 
    if mode != "simulation" and google_api_key:
        evaluator = VisionEvaluator(project_id, location, google_api_key)
    
    # Load Benchmarks
    benchmarks = load_yaml(BENCHMARK_PATH)
    
    # Weights for Scoring
    weights = {
        "face_identity": 0.35, "hairstyle": 0.15, "silhouette": 0.20,
        "world_continuity": 0.20, "art_style_consistency": 0.10
    }
    
    results = []
    
    for i, bench in enumerate(benchmarks):
        if i >= max_budget:
            break
            
        print(f"\nRunning Benchmark: {bench['id']}")
        char_spec = load_yaml(CHAR_SPEC_PATH)
        prompt = compile_prompt(char_spec, bench)
        
        # 1. Get Reference Set
        ref_data = get_reference_set(bench)
        ref_set = ref_data.get('references', []) if isinstance(ref_data, dict) else ref_data
            
        # 2. Generate
        gen_result = generator.generate(prompt, ref_set)
        image_url = gen_result['image_url']
        case_scores = gen_result.get('scores', {})
        
        # 3. Handle Local evaluation logic (if in Real mode or scoring requested)
        if not case_scores and evaluator:
            case_scores = evaluator.evaluate(image_url, [r['path'] for r in ref_set], char_spec)
        
        # Calculate Weighted Score
        weighted_score = sum(case_scores.get(k, 0.5) * weights[k] for k in weights)
        case_scores['total'] = round(weighted_score, 3)
        case_scores['image_url'] = image_url
        
        print(f"[{model}] Result for {bench['id']}: {case_scores['total']} (Identity: {case_scores.get('face_identity')})")
        results.append(case_scores)

    if not results:
        return

    # Aggregate and Log
    avg_total = sum(r['total'] for r in results) / len(results)
    
    print(f"\n--- Final {model.upper()} Result: {round(avg_total, 3)} ---")
    
    # Log Result
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"{timestamp}\t{model}-sim\t{round(avg_total, 3)}\t{avg_total}\tDONE\tSeedDream Integrated\n"
    
    with open(LOG_PATH, 'a') as f:
        f.write(log_entry)

if __name__ == "__main__":
    # We can now specify the model to test
    import sys
    target_model = sys.argv[1] if len(sys.argv) > 1 else "gemini"
    run_experiment(mode="simulation", model=target_model)
