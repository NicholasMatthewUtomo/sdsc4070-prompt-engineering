import os
import json

# Define the 5 specific code problems (Test Examples)
# These remain the same across all strategies to ensure a fair test.
problems = [
    {
        "name": "ex1_bubble_sort",
        "code": "def sort_list(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1] :\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr",
        "desc": "Bubble Sort (Slow O(n^2))"
    },
    {
        "name": "ex2_string_concat",
        "code": "def build_sentence(words):\n    res = ''\n    for w in words:\n        res = res + w + ' '\n    return res",
        "desc": "String Concatenation in Loop (High memory usage)"
    },
    {
        "name": "ex3_nested_lookup",
        "code": "def find_users(target_ids, all_users):\n    # all_users is a list of dicts like {'id': 1, 'name': 'x'}\n    found = []\n    for uid in target_ids:\n        for u in all_users:\n            if u['id'] == uid:\n                found.append(u)\n    return found",
        "desc": "Nested Loop Search (O(n*m))"
    },
    {
        "name": "ex4_prime_check",
        "code": "def is_prime_sum(n):\n    primes = []\n    for num in range(2, n + 1):\n        for i in range(2, num):\n            if (num % i) == 0:\n                break\n        else:\n            primes.append(num)\n    return sum(primes)",
        "desc": "Inefficient Prime Calculation"
    },
    {
        "name": "ex5_global_state",
        "code": "total = 0\ndef add_to_total(nums):\n    global total\n    for x in nums:\n        total += x\n    return total",
        "desc": "Usage of Global Variable (Side effects)"
    }
]

def create_base_content(problem):
    return {
        "system_instruction": "",
        "constraints": [
            "Respond in plain text paragraphs.",
            "Use clear headers."
        ],
        "user_query": f"Here is a piece of code. Please refactor it for performance and explain the complexity in plain text.\n\nCODE:\n{problem['code']}"
    }

def create_role_cot_content(problem):
    return {
        "system_instruction": "You are a Senior Backend Engineer at a High-Frequency Trading firm. You care deeply about Big-O complexity and memory allocation.",
        "constraints": [
            "Use Chain of Thought reasoning (think before coding).",
            "Output must be in structured plain text (Markdown is okay).",
            "Explain the math behind the complexity before writing the code.",
            "Respond in plain text paragraphs.",
            "Use clear headers."
        ],
        "user_query": (
            f"Here is a legacy function:\n{problem['code']}\n\n"
            "INSTRUCTION: Let's think step by step.\n"
            "1. First, identify the line causing the worst Time Complexity.\n"
            "2. Explain WHY it is slow mathematically using a paragraph description.\n"
            "3. Finally, provide the refactored, optimized Python code block."
        )
    }

def create_role_few_shot_content(problem):
    example_shot = (
        "User: Refactor this: def sum(L): c=0; for i in L: c+=i; return c\n"
        "AI: Analysis: The manual loop overhead makes this slower than Python's internal C-optimizations. "
        "The complexity is O(n), but the constant factors are high.\n\n"
        "Refactored Code:\n```python\ndef sum(L): return sum(L)\n```"
    )
    
    return {
        "system_instruction": "You are a Senior Backend Engineer at a High-Frequency Trading firm. You care deeply about Big-O complexity and memory allocation. I will provide examples of the conversation style I want.",
        "constraints": [
            "Follow the few-shot conversational pattern.",
            "Respond in plain text paragraphs.",
            "Use clear headers."
        ],
        "user_query": f"EXAMPLE CONVERSATION:\n{example_shot}\n\n---\n\nUser: Refactor this code:\n{problem['code']}"
    }

# Main generation loop
root_dir = "prompt"
strategies = {
    "base": create_base_content,
    "role_cot": create_role_cot_content,
    "role_few_shot": create_role_few_shot_content
}

for strategy_name, content_creator in strategies.items():
    # Create subfolder (e.g., prompts/base)
    folder_path = os.path.join(root_dir, strategy_name)
    os.makedirs(folder_path, exist_ok=True)
    
    for prob in problems:
        filename = f"{prob['name']}.json"
        file_path = os.path.join(folder_path, filename)
        
        # Generate JSON content
        content = content_creator(prob)
        
        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
            
    print(f"Generated 5 files for: {strategy_name}")

print("\nDONE! You now have 15 prompt files organized in prompts/")