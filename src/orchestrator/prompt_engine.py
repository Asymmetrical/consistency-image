"""
Prompt Engine - Defines how character specs and benchmark tasks are Compiled into prompts.
This file is a primary target for AI research and optimization.
"""

def compile_prompt(character_spec, benchmark_task, references=None):
    """
    Assembles a prompt for image generation.
    Updated for Identity Locking: Detects high-weight 'Anchor' references.
    """
    
    # 1. Base identity anchors from YAML
    anchors = character_spec.get('identity_anchors', {})
    face = anchors.get('face_identity', {}).get('description', '')
    hair = anchors.get('hairstyle', {}).get('description', '')
    body = anchors.get('silhouette', {}).get('description', '')
    identity_description = f"{face}, {hair}, {body}"
    
    # 2. Scene task
    task_prompt = benchmark_task.get('task_prompt', '')
    
    # 3. Identify Lock Logic (Weighted Orchestration)
    identity_lock = ""
    if references:
        # Sort to find the highest weight 'Anchor'
        sorted_refs = sorted(references, key=lambda x: x.get('weight', 1.0), reverse=True)
        top_ref = sorted_refs[0]
        if top_ref.get('weight', 1.0) > 1.0:
            # We explicitly tell the model that [1] is the source of truth for features.
            identity_lock = f" CRITICAL: Precisely mirror the unique facial geometry and gaze of reference [1]."
    
    # 4. Style and Assembly
    style = character_spec.get('style_family', 'cinematic photography')
    
    full_prompt = (
        f"A professional photo of {character_spec.get('name', 'character')}. "
        f"Physical traits: {identity_description}. "
        f"Style: {style}. "
        f"Action/Scene: {task_prompt}. "
        f"{identity_lock} Use references [1]-[4] for overall consistency."
    )
    
    return full_prompt.strip()

if __name__ == "__main__":
    # Quick test
    test_char = {'name': 'Kael', 'identity_anchors': {'face_identity': {'description': 'angular face'}}, 'style_family': 'cinematic'}
    test_task = {'task_prompt': 'standing in a forest'}
    print(f"Compiled Prompt: {compile_prompt(test_char, test_task)}")
