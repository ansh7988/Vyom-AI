import json
from ollama import chat


SYSTEM_PROMPT = """
You are Vyom's Memory Intelligence Engine.

Your ONLY job is to determine whether the user is:

1. Remembering a long-term fact.
2. Recalling a long-term fact.
3. Not talking about memory.

Return ONLY valid JSON.

Remember example:

{
    "intent":"remember",
    "entity":{
        "type":"favorite_color",
        "value":"blue",
        "confidence":1.0
    }
}

Recall example:

{
    "intent":"recall",
    "entity":{
        "type":"favorite_color",
        "confidence":1.0
    }
}

Not memory:

{
    "intent":"none"
}

Rules:

- Understand meaning.
- Never rely on keywords.
- Normalize entity names to snake_case.
- Infer the entity naturally.
- Return ONLY JSON.
"""


def extract_memory(user_input):

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
            "intent": "none"
        }
    