import yaml
import json
import os
import sys
import datetime
import random
import argparse
from dotenv import load_dotenv

# Ensure the root directory is in sys.path so we can import 'src'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.orchestrator.prompt_engine import compile_prompt
from src.orchestrator.secret_manager import bootstrap_production_env
from src.orchestrator.reference_engine import get_reference_set
from src.generators.simulated_adapter import SimulatedAdapter
from src.generators.seeddream_adapter import SeedDreamAdapter
from src.orchestrator.vision_evaluator import VisionEvaluator

# Safety Safeguards for Real Mode
REAL_MODE_SAFEGUARD = 5
real_generation_count = 0

# Load environment variables (.env.local)
load_dotenv(".env.local")

def get_env_var(name: str, default: str = "") -> str:
    """Robustly fetch env vars, cleaning 'SET ' prefixes if present."""
    val = os.getenv(name)
    if val and val.startswith("SET "):
        return val.replace("SET ", "").split("=")[-1]
    return val or default

# Defaults
DEFAULT_CHAR_SPEC = "specs/characters/example-kael.yaml"
DEFAULT_BENCHMARK = "specs/benchmarks/kael-benchmark-set.yaml"
EVALUATOR_PATH = "specs/evaluators/default-character-v1.yaml"
BASELINE_PATH = "data/results/current_baseline.json"
LOG_PATH = "data/results/experiment_log.tsv"

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Character Consistency Lab: Experiment Runner")
    parser.add_argument("model", choices=["gemini", "seeddream", "flux"], help="Model to test")
    parser.add_argument("--mode", choices=["simulation", "real"], default="simulation", help="Execution mode")
    parser.add_argument("--budget", type=int, default=3, help="Max benchmarks to run")
    parser.add_argument("--spec", default=DEFAULT_CHAR_SPEC, help="Path to character or product spec")
    parser.add_argument("--bench", default=DEFAULT_BENCHMARK, help="Path to benchmark set")
    args = parser.parse_args()
    
    global real_generation_count
    
    # 1. Bootstrap Production Secrets if in Real Mode
    if args.mode == "real":
        print(f"--- Stage 2: REAL PIXEL ACTIVATION (Safeguard: {REAL_MODE_SAFEGUARD} images) ---")
        if not bootstrap_production_env():
            print("CRITICAL ERROR: Failed to bootstrap production environment. Aborting real-pixel experiment.")
            return

    # Configuration from .env.local (Freshly bootstrapped)
    project_id = get_env_var('GCP_PROJECT_ID', '894937596656')
    location = get_env_var('GCP_LOCATION', 'us-central1')
    google_api_key = get_env_var('GOOGLE_API_KEY')
    bytedance_api_key = get_env_var('BYTEDANCE_API_KEY')
    
    # Initialize Generator based on Selection
    if args.mode == "simulation":
        if args.model == "seeddream":
            generator = SeedDreamAdapter() # Defaults to sim if no key
        else:
            generator = SimulatedAdapter(args.model)
        evaluator = None
    else:
        # Real Mode
        if args.model == "seeddream":
            generator = SeedDreamAdapter(api_key=bytedance_api_key)
        else:
            from src.generators.google_image_adapter import GoogleImageAdapter
            generator = GoogleImageAdapter(project_id, location, google_api_key)
        
        # In real mode, we try to use the VisionEvaluator for objective parity scoring
        evaluator = None
        if google_api_key:
            evaluator = VisionEvaluator(project_id, location, google_api_key)
    
    # Load Benchmarks
    benchmarks = load_yaml(args.bench)
    results = []
    
    # Process Benchmarks
    max_benchmarks = min(args.budget, 10)
    
    # Weights for Scoring
    weights = {
        "face_identity": 0.35, "hairstyle": 0.15, "silhouette": 0.20,
        "world_continuity": 0.20, "art_style_consistency": 0.10
    }

    for i, bench in enumerate(benchmarks):
        if i >= max_benchmarks:
            break
            
        # Safeguard Check for Real Mode
        if args.mode == "real":
            real_generation_count += 1
            if real_generation_count > REAL_MODE_SAFEGUARD:
                print(f"--- SAFEGUARD TRIGGERED: Reached limit of {REAL_MODE_SAFEGUARD} generations. Stopping. ---")
                break
                
        print(f"\nRunning Benchmark: {bench['id']} ({args.mode.upper()})")
            
        # 1. Get Reference Set
        ref_data = get_reference_set(bench)
        ref_set = ref_data.get('references', []) if isinstance(ref_data, dict) else ref_data
            
        # 2. Compile Prompt with Identity Lock logic
        spec = load_yaml(args.spec)
        prompt = compile_prompt(spec, bench, references=ref_set)
        
        # 3. Generate
        gen_result = generator.generate(prompt, ref_set)
        image_url = gen_result['image_url']
        case_scores = gen_result.get('scores', {})
        
        # 4. Handle Scoring (Vision Evaluator handles Stage 2 pixels)
        if not case_scores and evaluator:
            case_scores = evaluator.evaluate(image_url, [r['path'] for r in ref_set], spec)
        
        # 5. Calculate Weighted Score
        if case_scores:
            weighted_score = sum(case_scores.get(k, 0.5) * weights[k] for k in weights if k in case_scores)
            case_scores['total'] = round(weighted_score, 3)
            case_scores['image_url'] = image_url
            print(f"[{args.model}] Result for {bench['id']}: {case_scores['total']} (Identity: {case_scores.get('face_identity')})")
            results.append(case_scores)

    if not results:
        return

    # Aggregate and Log
    avg_total = sum(r['total'] for r in results) / len(results)
    print(f"\n--- Final {args.model.upper()} Result: {round(avg_total, 3)} ---")
    
    # Log Result
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"{timestamp}\t{args.model}-{args.mode}\t{round(avg_total, 3)}\t{avg_total}\tDONE\n"
    with open(LOG_PATH, 'a') as f:
        f.write(log_entry)

if __name__ == "__main__":
    main()
