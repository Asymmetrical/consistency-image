"""
Prompt Engine - Defines how character specs and benchmark tasks are Compiled into prompts.
This file is a primary target for AI research and optimization.
"""

def compile_prompt(character_spec, benchmark_task, references=None):
    """
    Assembles a prompt for image generation.
    Supports individual heroes and multi-subject parties.
    """
    # 1. Subject Invariants (Group vs Individual)
    if "members" in character_spec:
        # Multi-Subject Logic
        descriptions = []
        for m in character_spec['members']:
            desc = m.get('visual_anchors') or m.get('identity_anchors', {}).get('face_identity', {}).get('description', '')
            descriptions.append(f"{m['name']}: {desc}")
        identity_description = " | ".join(descriptions)
    else:
        # Single Subject Logic
        anchors = character_spec.get('identity_anchors', {})
        if not anchors and 'visual_anchors' in character_spec:
             identity_description = character_spec['visual_anchors']
        else:
            face = anchors.get('face_identity', {}).get('description', '')
            hair = anchors.get('hairstyle', {}).get('description', '')
            body = anchors.get('silhouette', {}).get('description', '')
            identity_description = f"{face}, {hair}, {body}"
    
    # 2. Scene task
    task_prompt = benchmark_task.get('task_prompt', '')
    
    # 3. Identify Lock Logic (Weighted Orchestration)
    identity_lock = ""
    if references:
        # Check for multi-anchor support (Slot 0-3)
        if len(references) > 1:
            identity_lock = " CRITICAL: Maintain strict identity lock for all subjects [1]-[4]. Mirror their specific geometries."
        else:
            sorted_refs = sorted(references, key=lambda x: x.get('weight', 1.0), reverse=True)
            top_ref = sorted_refs[0]
            if top_ref.get('weight', 1.0) > 1.0:
                identity_lock = f" CRITICAL: Precisely mirror the unique racial/facial geometry of reference [1]."
    
    # 4. Style and Assembly
    style = character_spec.get('style_family', 'cinematic photography')
    
    full_prompt = (
        f"A professional photo of {character_spec.get('name', 'character')}. "
        f"Subject Details: {identity_description}. "
        f"Style: {style}. "
        f"Action/Scene: {task_prompt}. "
        f"{identity_lock}"
    )
    
    return full_prompt.strip()

if __name__ == "__main__":
    # Quick test
    test_char = {'name': 'Kael', 'identity_anchors': {'face_identity': {'description': 'angular face'}}, 'style_family': 'cinematic'}
    test_task = {'task_prompt': 'standing in a forest'}
    print(f"Compiled Prompt: {compile_prompt(test_char, test_task)}")
