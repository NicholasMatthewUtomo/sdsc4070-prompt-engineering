# Context Engineering with Gemini

## Overview

This repository contains a small experiment that demonstrates structured prompt engineering across three techniques and uses the Gemini/Google GenAI client (`main.py`) to generate responses. The repo includes:

- `main.py`: script that loads JSON prompts, calls the Gemini API, and writes outputs.
- `prompt_generator.py`: creates the 15 structured JSON prompt files under `prompt/`.
- `prompt/`: organized JSON configurations for three techniques (`base`, `role_cot`, `role_few_shot`).
- `output/`: generated Markdown logs (15 files) confirming model outputs for each prompt technique.

## Project Structure

- **Main script**: [main.py](main.py) — Connects to the Gemini API and saves results.
- **Prompt generator**: [prompt_generator.py](prompt_generator.py) — Generates prompt JSON files into `prompt/`.
- **Prompts**: [prompt](prompt) — Contains `base/`, `role_cot/`, and `role_few_shot/` subfolders with 5 JSON files each.
- **Outputs**: [output](output) — Contains `base/`, `role_cot/`, and `role_few_shot/` subfolders with result Markdown logs.

## Quick Start

1. Ensure you have Python 3.9+ installed.
2. Install the Google GenAI client (or the appropriate SDK used in `main.py`):

```bash
pip install google-genai
```

3. (Optional) Regenerate prompts if you want to change them:

```bash
python prompt_generator.py
```

4. Configure API credentials:

- `main.py` currently reads an API key inline. Replace the `api_key` value in [main.py](main.py) with your own key, or modify `main.py` to read from an environment variable for safety.

5. Run the main script to call the Gemini API and write outputs:

```bash
python main.py
```

Outputs will be written into the `output/` subfolders as Markdown files (e.g., `output/role_cot/ex1_bubble_sort_result.md`).

## Notes & Troubleshooting

- Network access and valid API credentials are required to call the Gemini API.
- If you hit rate limits, `main.py` already includes a small `time.sleep(1)` between calls — increase if needed.
