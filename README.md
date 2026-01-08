## ChatInject

![Main Figure](images/main_figure.png)

ChatInject is an indirect prompt-injection attack that exploits LLM agents' reliance on structured chat templates. By formatting malicious payloads to mimic native chat templates—and expanding to persuasion-driven multi-turn dialogues to prime the agent—ChatInject causes agents to accept and execute otherwise suspicious instructions.

## Quickstart

```bash
pip install agentdojo
```

> [!IMPORTANT]
> Note that the API of the package is still under development and might change in the future.

If you want to use the prompt injection detector, you need to install the `transformers` extra:

```bash
pip install "agentdojo[transformers]"
```

## Setup

### OpenRouter API Key

Before running the benchmark, you need to set up your OpenRouter API key:

```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
```

Alternatively, you can create a `.env` file in the project root with:
```
OPENROUTER_API_KEY=YOUR_API_KEY
```

To obtain an API key, visit [OpenRouter](https://openrouter.ai/) and create an account.

## Available Attack Methods

The following attack methods are available for testing with `qwen3-235b-a22b-2507`:

- **`injecagent`**: Default plain-text injection attack that concatenates an attention-grabbing prefix with the injection task as plain text
- **`injecagent_with_utility_system_multiturn_7`**: Default multi-turn attack that embeds persuasive multi-turn dialogue where each turn is formatted as plain text and concatenated into a single string
- **`chat_inject_qwen3`**: InjecPrompt + ChatInject variant that applies model-specific formatting where the attention-grabbing prefix is wrapped in system role tags and injection task is wrapped in user role tags using the target model's chat template
- **`chat_inject_qwen3_with_utility_authority_system_multiturn_7`**: Multi-turn + ChatInject attack that combines persuasive dialogue with template exploitation, where each turn in conversation is wrapped in corresponding role tags using the model-specific template

For other available models, check `src/agentdojo/models.py`. For other available attacks, check `src/agentdojo/attacks/baseline_attacks.py`.

## Running the benchmark

First, navigate to the src directory:
```bash
cd ./src
```

The benchmark can be run with the [benchmark](src/agentdojo/scripts/benchmark.py) script using `qwen3-235b-a22b-2507`. Documentation on how to use the script can be obtained with the `--help` flag.

### Examples for different attack methods:

**1. Default plain-text injection attack (injecagent):**
```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
python -m agentdojo.scripts.benchmark -s banking -s slack -s travel \
    --model "qwen/qwen3-235b-a22b-2507" \
    --defense instructional_prevention \
    --attack injecagent
```

**2. Multi-turn dialogue attack (injecagent_with_utility_system_multiturn_7):**
```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
python -m agentdojo.scripts.benchmark -s banking -s slack -s travel \
    --model "qwen/qwen3-235b-a22b-2507" \
    --defense instructional_prevention \
    --attack injecagent_with_utility_system_multiturn_7
```

**3. Model-specific formatting attack (chat_inject_qwen3):**
```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
python -m agentdojo.scripts.benchmark -s banking -s slack -s travel \
    --model "qwen/qwen3-235b-a22b-2507" \
    --defense instructional_prevention \
    --attack chat_inject_qwen3
```

**4. Multi-turn + template exploitation attack (chat_inject_qwen3_with_utility_authority_system_multiturn_7):**
```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
python -m agentdojo.scripts.benchmark -s banking -s slack -s travel \
    --model "qwen/qwen3-235b-a22b-2507" \
    --defense instructional_prevention \
    --attack chat_inject_qwen3_with_utility_authority_system_multiturn_7
```

---

## Acknowledgement

This project is based on the excellent work from the [AgentDojo](https://github.com/ethz-spylab/agentdojo) repository by ETH Zurich and Invariant Labs. We sincerely thank the original authors for their contributions and for making their code publicly available.
