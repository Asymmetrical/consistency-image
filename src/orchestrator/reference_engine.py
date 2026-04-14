"""
Reference Engine - Manages selection and weighting of reference images for FLUX.2.
This is an editable surface for researching reference-conditioning strategies.
"""

def get_reference_set(benchmark_case):
    """
    Returns a list of references based on the benchmark case strategy.
    Format: list of dicts with 'path' and 'weight'.
    """
    
    # Strategy extraction (can be defined in the benchmark YAML)
    strategy = benchmark_case.get('ref_strategy', 'default')
    
    # Base reference list from the benchmark case
    base_refs = benchmark_case.get('references', [])
    char_id = benchmark_case.get('character_id', 'unknown')
    
    # Hypothesis Loop: Logic for different reference strategies
    if strategy == 'diverse':
        # Hypothesis: Diverse angles lead to better 3D identity consistency
        return [{"path": p, "weight": 1.0} for p in base_refs]
    
    if strategy == 'weighted':
        # Hypothesis: Weighting a "Style Anchor" higher (1.5) preserves aesthetics
        # while other references (1.0) provide the identity grounding.
        return [{"path": p, "weight": 1.5 if i == 0 else 1.0} for i, p in enumerate(base_refs)]
    
    if strategy == 'compact':
        # Hypothesis: MVRS (Minimum Viable Reference Set)
        # Use only first 3 refs (Front, Profile, Silhouette) with weighting.
        compact_refs = base_refs[:3]
        return [{"path": p, "weight": 1.5 if i == 0 else 1.0} for i, p in enumerate(compact_refs)]
    
    if strategy == 'inverted':
        # Hypothesis: Primacy Bias Test
        # Same as 'weighted' but the list is reversed (Style Anchor at the end).
        weighted_refs = [{"path": p, "weight": 1.5 if i == 0 else 1.0} for i, p in enumerate(base_refs)]
        return weighted_refs[::-1]
    
    if strategy == 'lora_hybrid':
        # Hypothesis: Dual-Anchor (LoRA + Refs)
        # Use Weighted strategy (1.5x anchor) but signal that a LoRA is active.
        weighted_refs = [{"path": p, "weight": 1.5 if i == 0 else 1.0} for i, p in enumerate(base_refs)]
        return {
            "references": weighted_refs,
            "lora": {"id": char_id, "weight": 0.6}
        }
    # Default strategy: equal weighting
    return [{"path": p, "weight": 1.0} for p in base_refs]

if __name__ == "__main__":
    test_case = {'ref_strategy': 'diverse', 'references': ['ref1.png', 'ref2.png']}
    print(f"Reference Set: {get_reference_set(test_case)}")
