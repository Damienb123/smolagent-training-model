# Smolagent Training Model

> A tool-based AI agent built with smolagents that separates deterministic Python execution from LLM-based language generation.


# Project Overview

This project demonstrates how to design **tool-based AI agents** using the `smolagents` framework.  
Instead of relying on language models to generate executable code, the system separates:

- Deterministic logic (Python tools)
- Natural language explanations (LLMs)

This improves **reliability, reproducibility, and debugging** when building AI agents.


# Features

- Calculates total preparation time for party tasks
- Determines finish time based on the current clock
- Generates polite explanations using an LLM
- Demonstrates `@tool` integration with smolagents
- Shows a hybrid architecture combining Python logic with LLM narration

# Tools / Components

| Component | Purpose |
|--------|--------|
| `suggest_menu()` | Suggests menu based on occasion |
| `parse_tasks()` | Returns predefined preparation tasks |
| `calculate_party_time()` | Computes total preparation time |
| `calculate_finish_time()` | Determines final completion time |


# Technologies Used

- Python
- smolagents
- Hugging Face Transformers
- PyTorch
- Tool-based AI agents

# Installation

Clone the repository:

```bash
git clone https://github.com/Damienb123/smolagent-training-model.git
cd smolagent-training-model

```

Install dependencies:
```bash
pip install smolagents transformers torch
```

# Key Design Decisions
Instead of allowing the LLM to generate executable code dynamically, this project uses deterministic Python tools. This approach:

- prevents runtime errors
- ensures predictable results
- makes the system easier to test

The language model is only responsible for natural-language explanations.

# What I learned
This project helped me explore:

- Tool-based AI agent architectures
- Integrating deterministic functions with LLM workflows
- Building more reliable AI systems by separating logic and language generation
