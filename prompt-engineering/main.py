import json
import os
import time
from google import genai
from google.genai import types

# --- CONFIGURATION ---
ROOT_PROMPT_DIR = "prompt"
ROOT_OUTPUT_DIR = "output"

# 1. Initialize Client
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# 2. API Configuration
config = types.GenerateContentConfig(
    temperature=0.2, 
    max_output_tokens=2048,
)

# 3. Logic to load and parse the Input JSON prompt files
def load_complex_prompt(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # We construct the final string prompt from the structured JSON data
    full_prompt = ""
    
    # Always include Role/System Instruction if available
    if "system_instruction" in data:
        full_prompt += f"ROLE: {data['system_instruction']}\n\n"
        
    if "constraints" in data:
        constraints = data['constraints']
        # Handle if constraints are list or string
        if isinstance(constraints, list):
            constraints = "\n".join([f"- {c}" for c in constraints])
        full_prompt += f"CONSTRAINTS:\n{constraints}\n\n"
        
    if "user_query" in data:
        full_prompt += f"TASK/QUERY:\n{data['user_query']}"

    return full_prompt

# --- MAIN EXECUTION LOOP ---

# Get list of strategy folders (e.g., base, role_cot, few_shot)
strategies = [d for d in os.listdir(ROOT_PROMPT_DIR) if os.path.isdir(os.path.join(ROOT_PROMPT_DIR, d))]

if not strategies:
    print(f"No folders found in '{ROOT_PROMPT_DIR}'. Did you run the setup script?")

for strategy in strategies:
    print(f"\nEntering Strategy Folder: {strategy.upper()}")
    
    # Setup Input/Output paths
    strategy_input_dir = os.path.join(ROOT_PROMPT_DIR, strategy)
    strategy_output_dir = os.path.join(ROOT_OUTPUT_DIR, strategy)
    os.makedirs(strategy_output_dir, exist_ok=True)
    
    # Get all .json files in this folder
    test_files = [f for f in os.listdir(strategy_input_dir) if f.endswith(".json")]
    
    for i, test_file in enumerate(test_files):
        prompt_path = os.path.join(strategy_input_dir, test_file)
        
        # Load prompt
        try:
            formatted_prompt = load_complex_prompt(prompt_path)
        except Exception as e:
            print(f"  Skipping {test_file} due to read error: {e}")
            continue

        print(f"  > Processing ({i+1}/{len(test_files)}): {test_file} ...", end="", flush=True)

        try:
            # Generate
            response = client.models.generate_content(
                model="gemini-3-flash-preview", # Use standard flash model
                config=config,
                contents=[{"role": "user", "parts": [{"text": formatted_prompt}]}]
            )

            # Save Output
            # We save as .md (Markdown) because Code CoT usually contains ```python blocks
            base_name = os.path.splitext(test_file)[0]
            output_filename = f"{base_name}_result.md"
            output_path = os.path.join(strategy_output_dir, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(response.text)
                
            print(f"Saved to {output_path}")
            
            # Tiny sleep to avoid hitting rapid rate limits (optional)
            time.sleep(1)

        except Exception as e:
            print(f"API Error: {e}")

print(f"\nAll done! Check the '{ROOT_OUTPUT_DIR}' folder.")