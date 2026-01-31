# smolagent-training-model
This project demonstrates a reliable, executable pattern for using the smolagents library to support party planning tasks.
Instead of relying on free-form code generation, the project separates:

- Deterministic execution (Python tools)
- Natural-language narration (LLM)

This approach avoids common agent runtime errors while still benefiting from large language models.

## What this Project Does

- Calculates total preparation time for a party
- Determines the exact finish time based on the current clock
- Optionally generates a polite, in-character explanation using an LLM (“Alfred the butler”)
- Demonstrates how to define and validate @tool functions in smolagents

## Architecture Overview
- `parse_tasks` – returns predefined preparation tasks
- `calculate_party_time` – sums task durations
- `calculate_finish_time` – computes the finish time
- `suggest_menu` – suggests a menu based on occasion

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Damienb123/training-model.git
    cd training-model
    ```

2. Install the required dependencies:
    ```sh
    pip install smolagents transformers torch
    ```

## Example Output
```
Party will be ready at 00:39
Good evening, sir. All preparations will be completed precisely on schedule...
```

## Why This Approach 
Many agent examples rely on language models to generate and execute code, which can lead to:
- Parsing errors
- Runtime failures
- Non-deterministic behavior

This project demonstrates a production-oriented alternative:
- Python handles logic
- LLMs handle language
- Tools are explicit and testable

## Usage

Run the [training-model.py](http://_vscodecontentref_/0) script to see the agent in action:
```sh
python training-model.py
```

## Acknowledgements
This project uses the smolagents library, which leverages models from Hugging Face to create intelligent agents.
