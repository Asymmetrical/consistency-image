"""
Prompt Engine - Defines how character specs and benchmark tasks are Compiled into prompts.
This file is a primary target for AI research and optimization.
"""

def compile_prompt(character_spec, benchmark_task):
    """
    Assembles a prompt for image generation.
    Updated for Imagen 3 consistency (Style Referencing).
    """
    
    # 1. Base identity anchors from YAML
    anchors = character_spec.get('identity_anchors', {})
    face = anchors.get('face_identity', {}).get('description', '')
    hair = anchors.get('hairstyle', {}).get('description', '')
    body = anchors.get('silhouette', {}).get('description', '')
    identity_description = f"{face}, {hair}, {body}"
    
    # 2. Scene task
    task_prompt = benchmark_task.get('task_prompt', '')
    
    # 3. Style and Constraints
    style = character_spec.get('style_family', 'cinematic photography')
    
    # 4. Final Assembly (The "Formula")
    # Hypothesis: Explicitly linking to [1]-[4] reference tags improves consistency in Imagen 3.
    full_prompt = (
        f"A professional photo of {character_spec.get('name', 'character')}. "
        f"Physical traits: {identity_description}. "
        f"Style: {style}. "
        f"Action/Scene: {task_prompt}. "
        f"Maintain strict consistency with the appearance and lighting shown in [1], [2], [3], and [4]."
    )
    
    return full_prompt.strip()

if __name__ == "__main__":
    # Quick test
    test_char = {'name': 'Kael', 'identity_anchors': {'face_identity': {'description': 'angular face'}}, 'style_family': 'cinematic'}
    test_task = {'task_prompt': 'standing in a forest'}
    print(f"Compiled Prompt: {compile_prompt(test_char, test_task)}")
