from agentdojo.strenum import StrEnum
class ModelsEnum(StrEnum):
    """Currently supported models."""
    OPENAI_GPT_4O_20240806 = "gpt-4o-2024-08-06"
    """gpt-4o-2024-08-06"""
    OPENAI_GPT_4O_MINI_20240718 = "gpt-4o-mini-2024-07-18"
    """gpt-4o-mini-2024-07-18"""
    OPENAI_GPT_4_0125_PREVIEW = "gpt-4-0125-preview"
    """GPT-4 Turbo Preview 0125"""
    OPENAI_GPT_4_TURBO_2024_04_09 = "gpt-4-turbo-2024-04-09"
    """GPT-4 Turbo"""
    CLAUDE_3_OPUS_20240229 = "claude-3-opus-20240229"
    """Claude 3 Opus"""
    CLAUDE_3_SONNET_20240229 = "claude-3-sonnet-20240229"
    """Claude 3 Sonnet"""
    CLAUDE_3_5_SONNET_20240620 = "claude-3-5-sonnet-20240620"
    """Claude 3.5 Sonnet"""
    CLAUDE_3_5_SONNET_20241022 = "claude-3-5-sonnet-20241022"
    """Claude 3.5 Sonnet October"""
    CLAUDE_3_7_SONNET_20250219 = "claude-3-7-sonnet-20250219"
    """Claude 3.7 Sonnet"""
    CLAUDE_3_7_SONNET_20250219_THINKING_16000 = "claude-3-7-sonnet-20250219-thinking-16000"
    """Claude 3.7 Sonnet"""
    CLAUDE_3_HAIKU_20240307 = "claude-3-haiku-20240307"
    """Claude 3 Haiku"""
    COMMAND_R_PLUS = "command-r-plus"
    """Command R Plus"""
    COMMAND_R = "command-r"
    """Command R"""
    MISTRALAI_MIXTRAL_8X7B_INSTRUCT_V0_1 = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    """MistralAI Mixtral 8x7B Instruct v0.1"""
    LLAMA_3 = "meta-llama/Llama-3-70b-chat-hf"
    """Llama 3"""
    GEMINI_1_5_PRO_002 = "gemini-1.5-pro-002"
    """Gemini 1.5 Pro 002"""
    GEMINI_1_5_PRO_001 = "gemini-1.5-pro-001"
    """Gemini 1.5 Pro 001"""
    GEMINI_1_5_FLASH_002 = "gemini-1.5-flash-002"
    """Gemini 1.5 Flash 002"""
    GEMINI_1_5_FLASH_001 = "gemini-1.5-flash-001"
    """Gemini 1.5 Flash 001"""
    GEMINI_2_0_FLASH_EXP = "gemini-2.0-flash-exp"
    """Gemini 2.0 Flash Exp"""
    GEMINI_2_0_FLASH_001 = "gemini-2.0-flash-001"
    """Gemini 2.0 Flash 001"""
    GEMINI_2_5_FLASH_PREVIEW_04_17 = "gemini-2.5-flash-preview-04-17"
    """Gemini 2.5 Flash Preview 04/17"""
    GEMINI_2_5_PRO_PREVIEW_05_06 = "gemini-2.5-pro-preview-05-06"
    """Gemini 2.5 Pro Preview 05/06"""
    LOCAL = "local"
    """Local model"""
    VLLM_PARSED = "vllm_parsed"
    """VLLM parsed model"""
    OPENROUTER_GPT_OSS_120B = "openai/gpt-oss-120b"
    """openai/gpt-oss-120b"""
    OPENAI_GPT_5_NANO = "gpt-5-nano-2025-08-07"
    """gpt-5-nano-2025-08-07"""
    OPENROUTER_DEEPSEEK_V3_1 = "deepseek/deepseek-chat-v3.1"
    """deepseek/deepseek-chat-v3.1"""
    OPENROUTER_QWEN3_235B_A22B_INSTRUCT_2507 = "qwen/qwen3-235b-a22b-2507"
    """qwen/qwen3-235b-a22b-2507"""
    OPENROUTER_CLAUDE_3_7_SONNET_20250219 = "anthropic/claude-3.7-sonnet"
    """anthropic/claude-3.7-sonnet"""
    OPENROUTER_LLAMA_4_MAVERICK = "meta-llama/llama-4-maverick"
    """meta-llama/llama-4-maverick"""
    OPENROUTER_GEMINI_2_5_PRO = "google/gemini-2.5-pro"
    """google/gemini-2.5-pro"""
    OPENROUTER_GROK_2_1212 = "x-ai/grok-2-1212"
    """x-ai/grok-2-1212"""
    OPENROUTER_GLM_4_5 = "z-ai/glm-4.5"
    """z-ai/glm-4.5"""
    OPENROUTER_KIMI_K2_0905 = "moonshotai/kimi-k2-0905"
    """moonshotai/kimi-k2-0905"""
    OPENROUTER_GROK3_MINI = "x-ai/grok-3-mini"
    """x-ai/grok-3-mini"""
    OPENAI_GPT_5_MINI = "gpt-5-mini-2025-08-07"
    """gpt-5-mini-2025-08-07"""
    OPENAI_GPT_5 = "gpt-5-2025-08-07"
    """gpt-5-2025-08-07"""
    OPENROUTER_MISTRAL_LARGE_2411 = "mistralai/mistral-large-2411"
    """mistralai/mistral-large-2411"""
    OPENROUTER_MISTRAL_MEDIUM_3_1 = "mistralai/mistral-medium-3.1"
    """mistralai/mistral-medium-3.1"""
    OPENAI_GPT_4O_20241120 = "gpt-4o-2024-11-20"
    """gpt-4o-2024-11-20"""
    OPENROUTER_GROK3 = "x-ai/grok-3"
    """x-ai/grok-3"""

MODEL_PROVIDERS = {
    ModelsEnum.OPENROUTER_MISTRAL_MEDIUM_3_1: "openrouter",
    ModelsEnum.OPENROUTER_MISTRAL_LARGE_2411: "openrouter",
    ModelsEnum.OPENROUTER_GROK3_MINI: "openrouter",
    ModelsEnum.OPENROUTER_GROK3: "openrouter",
    ModelsEnum.OPENROUTER_KIMI_K2_0905: "openrouter",
    ModelsEnum.OPENROUTER_GLM_4_5: "openrouter",
    ModelsEnum.OPENROUTER_GROK_2_1212: "openrouter",
    ModelsEnum.OPENROUTER_GEMINI_2_5_PRO: "openrouter",
    ModelsEnum.OPENROUTER_LLAMA_4_MAVERICK: "openrouter",
    ModelsEnum.OPENROUTER_CLAUDE_3_7_SONNET_20250219: "openrouter",
    ModelsEnum.OPENROUTER_QWEN3_235B_A22B_INSTRUCT_2507: "openrouter",
    ModelsEnum.OPENROUTER_DEEPSEEK_V3_1: "openrouter",
    ModelsEnum.OPENROUTER_GPT_OSS_120B: "openrouter",
    ModelsEnum.OPENAI_GPT_5: "openai",
    ModelsEnum.OPENAI_GPT_5_MINI: "openai",
    ModelsEnum.OPENAI_GPT_5_NANO: "openai",
    ModelsEnum.OPENAI_GPT_4O_20241120: "openai",
    ModelsEnum.OPENAI_GPT_4O_20240806: "openai",
    ModelsEnum.OPENAI_GPT_4O_MINI_20240718: "openai",
    ModelsEnum.OPENAI_GPT_4_0125_PREVIEW: "openai",
    ModelsEnum.OPENAI_GPT_4_TURBO_2024_04_09: "openai",
    ModelsEnum.CLAUDE_3_OPUS_20240229: "anthropic",
    ModelsEnum.CLAUDE_3_SONNET_20240229: "anthropic",
    ModelsEnum.CLAUDE_3_5_SONNET_20240620: "anthropic",
    ModelsEnum.CLAUDE_3_5_SONNET_20241022: "anthropic",
    ModelsEnum.CLAUDE_3_7_SONNET_20250219: "anthropic",
    ModelsEnum.CLAUDE_3_7_SONNET_20250219_THINKING_16000: "anthropic",
    ModelsEnum.CLAUDE_3_HAIKU_20240307: "anthropic",
    ModelsEnum.COMMAND_R_PLUS: "cohere",
    ModelsEnum.COMMAND_R: "cohere",
    ModelsEnum.MISTRALAI_MIXTRAL_8X7B_INSTRUCT_V0_1: "together",
    ModelsEnum.LLAMA_3: "together-prompting",
    ModelsEnum.GEMINI_1_5_PRO_001: "google",
    ModelsEnum.GEMINI_1_5_PRO_002: "google",
    ModelsEnum.GEMINI_1_5_FLASH_001: "google",
    ModelsEnum.GEMINI_1_5_FLASH_002: "google",
    ModelsEnum.GEMINI_2_0_FLASH_EXP: "google",
    ModelsEnum.GEMINI_2_0_FLASH_001: "google",
    ModelsEnum.GEMINI_2_5_FLASH_PREVIEW_04_17: "google",
    ModelsEnum.GEMINI_2_5_PRO_PREVIEW_05_06: "google",
    ModelsEnum.LOCAL: "local",
    ModelsEnum.VLLM_PARSED: "vllm_parsed",
}
MODEL_NAMES = {
    "x-ai/grok-3": "x-ai/grok-3",
    "gpt-4o-2024-11-20": "gpt-4o-2024-11-20",
    "mistralai/mistral-medium-3.1": "mistralai/mistral-medium-3.1",
    "mistralai/mistral-large-2411": "mistralai/mistral-large-2411",
    "gpt-5-2025-08-07": "gpt-5-2025-08-07",
    "gpt-5-mini-2025-08-07": "gpt-5-mini-2025-08-07",
    "x-ai/grok-3-mini": "x-ai/grok-3-mini",
    "moonshotai/kimi-k2-0905": "moonshotai/kimi-k2-0905",
    "z-ai/glm-4.5": "z-ai/glm-4.5",
    "x-ai/grok-2-1212": "x-ai/grok-2-1212",
    "google/gemini-2.5-pro": "google/gemini-2.5-pro",
    "meta-llama/llama-4-maverick": "meta-llama/llama-4-maverick",
    "anthropic/claude-3.7-sonnet": "anthropic/claude-3.7-sonnet",
    "qwen/qwen3-235b-a22b-2507": "qwen/qwen3-235b-a22b-2507",
    "deepseek/deepseek-chat-v3.1": "deepseek/deepseek-chat-v3.1",
    "gpt-5-nano-2025-08-07": "gpt-5-nano-2025-08-07",
    "openai/gpt-oss-120b": "openai/gpt-oss-120b",
    "gpt-4o-2024-08-06": "gpt-4o-2024-08-06",
    "gpt-4o-mini-2024-07-18": "gpt-4o-mini-2024-07-18",
    "gpt-3.5-turbo-0125": "GPT-3.5",
    "gpt-4-turbo-2024-04-09": "GPT-4",
    "gpt-4-0125-preview": "GPT-4",
    "claude-3-opus-20240229": "Claude",
    "claude-3-sonnet-20240229": "Claude",
    "claude-3-5-sonnet-20240620": "Claude",
    "claude-3-5-sonnet-20241022": "Claude",
    "claude-3-7-sonnet-20250219": "Claude",
    "claude-3-7-sonnet-20250219-thinking-16000": "Claude",
    "claude-3-haiku-20240307": "Claude",
    "command-r-plus": "Command R+",
    "command-r": "Command R",
    "mistralai/Mixtral-8x7B-Instruct-v0.1": "Mixtral",
    "meta-llama/Llama-3-70b-chat-hf": "AI assistant",
    "gemini-1.5-pro-002": "AI model developed by Google",
    "gemini-1.5-pro-001": "AI model developed by Google",
    "gemini-1.5-flash-002": "AI model developed by Google",
    "gemini-1.5-flash-001": "AI model developed by Google",
    "gemini-2.0-flash-exp": "AI model developed by Google",
    "gemini-2.0-flash-001": "AI model developed by Google",
    "gemini-2.5-flash-preview-04-17": "AI model developed by Google",
    "gemini-2.5-pro-preview-05-06": "AI model developed by Google",
    "local": "Local model",
    "vllm_parsed": "Local model"
}
