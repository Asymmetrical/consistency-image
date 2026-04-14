import yaml
import json
import os
import sys
import datetime
import random

# Ensure the root directory is in sys.path so we can import 'src'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.orchestrator.prompt_engine import compile_prompt
from src.orchestrator.reference_engine import get_reference_set
from src.generators.flux_adapter import FluxAdapter
from src.generators.nano_banana_adapter import NanoBananaAdapter

# Paths
CHAR_SPEC_PATH = "specs/characters/example-kael.yaml"
BENCHMARK_PATH = "specs/benchmarks/kael-benchmark-set.yaml"
EVALUATOR_PATH = "specs/evaluators/default-character-v1.yaml"
BASELINE_PATH = "data/results/current_baseline.json"
LOG_PATH = "data/results/experiment_log.tsv"

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def get_generator(model_id: str):
    """Factory to return the selected generator adapter."""
    if model_id == "nano-banana":
        return NanoBananaAdapter()
    return FluxAdapter() # Default to FLUX

def run_experiment(model_id: str = "flux2"):
    """
    Main loop to run a character consistency experiment.
    Uses the modular Generator Architecture.
    """
    print(f"--- Character Consistency Lab: Experiment Runner ---")
    print(f"Using Model: {model_id}")
    
    # Load Benchmark Spec
    with open("specs/benchmarks/kael-benchmark-set.yaml", "r") as f:
        benchmarks = yaml.safe_load(f)
    
    # Get Current Generator
    generator = get_generator(model_id)
    
    # Evaluation Logic: Define weights for the dimensions
    weights = {
        "face_identity": 0.35,
        "hairstyle": 0.15,
        "silhouette": 0.20,
        "world_continuity": 0.20,
        "art_style_consistency": 0.10
    }
    
    results = []
    
    for bench in benchmarks:
        print(f"\nRunning Benchmark: {bench['id']}")
        
        # 1. Compile Prompt via Prompt Engine
        # We need to load the specific character spec for this benchmark
        char_spec = load_yaml(f"specs/characters/example-kael.yaml") # Hardcoded for now per benchmark
        prompt = compile_prompt(char_spec, bench)
        print(f"Generated Prompt: {prompt}")
        
        # 2. Get Reference Set via Reference Engine
        ref_data = get_reference_set(bench)
        
        # Handle different return types (list for simple, dict for lora_hybrid)
        if isinstance(ref_data, dict):
            ref_set = ref_data.get('references', [])
            lora_info = ref_data.get('lora', None)
        else:
            ref_set = ref_data
            lora_info = None
            
        print(f"References ({len(ref_set)}): {[r['path'] for r in ref_set]}")
        if lora_info:
            print(f"LoRA Active: {lora_info['id']} (Weight: {lora_info['weight']})")
        
        # 3. Generate Image and Scores via Modular Adapter
        gen_result = generator.generate(prompt, ref_set, lora_info)
        case_scores = gen_result['scores']
        
        # 4. Calculate Weighted Score for this case (Evaluation Layer)
        weighted_score = sum(case_scores[k] * weights[k] for k in weights)
        case_scores['total'] = round(weighted_score, 3)
        
        print(f"Scores: {case_scores}")
        results.append(case_scores)

    # 3. Aggregate Results
    avg_scores = {k: round(sum(r[k] for r in results) / len(results), 3) for k in weights}
    total_avg_score = round(sum(avg_scores[k] * weights[k] for k in weights), 3)
    
    print(f"\n--- Final Result ---")
    print(f"Total Weighted Score: {total_avg_score}")
    print(f"Dimensions: {avg_scores}")
    
    # 4. Compare with Baseline
    with open(BASELINE_PATH, 'r') as f:
        baseline = json.load(f)
    
    is_win = total_avg_score > baseline['total_score']
    print(f"Baseline Score: {baseline['total_score']}")
    print(f"Outcome: {'WIN (Improvement Found!)' if is_win else 'REJECTED (No Improvement)'}")

    # 5. Log Result
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"{timestamp}\texp-{random.randint(100,999)}\t{total_avg_score}\t{avg_scores['face_identity']}\t{avg_scores['hairstyle']}\t{avg_scores['silhouette']}\t{avg_scores['world_continuity']}\t{avg_scores['art_style_consistency']}\t{'WIN' if is_win else 'FAIL'}\tStubbed Run\n"
    
    with open(LOG_PATH, 'a') as f:
        f.write(log_entry)
        
    # 6. If Win, update baseline
    if is_win:
        new_baseline = {
            "experiment_id": f"exp-{random.randint(100,999)}",
            "total_score": total_avg_score,
            "dimensions": avg_scores,
            "timestamp": timestamp,
            "commit_hash": "stub"
        }
        with open(BASELINE_PATH, 'w') as f:
            json.dump(new_baseline, f, indent=2)
        print("Updated data/results/current_baseline.json")

if __name__ == "__main__":
    # Allow model selection via command line: python scripts/experiment_runner.py nano-banana
    m_id = sys.argv[1] if len(sys.argv) > 1 else "flux2"
    run_experiment(m_id)
