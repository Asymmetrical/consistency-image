"""
Prompt Engine - Defines how character specs and benchmark tasks are Compiled into prompts.
This file is a primary target for AI research and optimization.
"""

def compile_prompt(character_spec, benchmark_task):
    """
    Combines a character spec and a benchmark task into a high-fidelity FLUX prompt.
    """
    
    # 1. Base identity anchors
    anchors = character_spec.get('identity_anchors', {})
    identity_description = f"{anchors.get('face_identity', {}).get('description', '')}, {anchors.get('hairstyle', {}).get('description', '')}, {anchors.get('silhouette', {}).get('description', '')}"
    
    # 2. Scene task
    task_prompt = benchmark_task.get('task_prompt', '')
    
    # 3. Style and Constraints
    style = character_spec.get('style_family', '')
    negative = ", ".join(character_spec.get('negative_constraints', []))
    
    # 4. Final Assembly (The "Formula")
    # Current hypothesis: [Identity Description] + [Style] + [Task Prompt]
    full_prompt = f"{identity_description}. Art style: {style}. Scene: {task_prompt}. NO: {negative}"
    
    return full_prompt.strip()

if __name__ == "__main__":
    # Quick test
    test_char = {'identity_anchors': {'face_identity': {'description': 'angular face'}}, 'style_family': 'art'}
    test_task = {'task_prompt': 'standing in rain'}
    print(f"Compiled Prompt: {compile_prompt(test_char, test_task)}")
