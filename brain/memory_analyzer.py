import json
from ollama import chat


SYSTEM_PROMPT = """
You are Vyom's Memory Analyzer.

Your only job is to understand whether the user's message contains
memory information.

Return ONLY valid JSON.

Possible intents:

1. remember
The user is telling Vyom a long-term fact.

Example:
"My birthday is 8 June 2007"

↓
{
    "intent":"remember",

    "entity":{
        "type":"date_of_birth",
        "value":"8 June 2007",
        "confidence":1.0
    }
}
--------------------------------------------------

2. recall

The user is asking Vyom to recall a stored fact.

Example:

"When was I born?"

↓

{
    "intent":"recall",
    "entity":{
        "type":"date_of_birth",
        "confidence":1.0
    }
}

--------------------------------------------------

3. none

The message is not related to memory.

↓

{
    "intent":"none"
}

Rules:

- Understand meaning.
- Do NOT rely on keywords.
- Infer entity names naturally.
- Entity names must be snake_case.
- Never explain.
- Never use markdown.
- Return JSON only.
"""



def understand_memory(user_input):

    response = chat(
        model="qwen3.5:4b",
        think=False,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    try:
        return json.loads(response["message"]["content"])

    except Exception:
        return {
            "intent": "none",
            "entity": None
        }