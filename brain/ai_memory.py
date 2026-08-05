import json
from ollama import chat


def extract_memory(user_input):

    prompt = f"""
You are Vyom's memory manager.

Analyze the user's sentence.

If the user is telling you something about themselves,
return JSON like:

{{
    "action":"remember",
    "key":"favorite_color",
    "value":"blue"
}}

If the user is asking something already stored,
return:

{{
    "action":"recall",
    "key":"favorite_color"
}}

Rules:
- Return ONLY valid JSON.
- Use snake_case keys.
- Normalize similar meanings.
Examples:
DOB, birth date, birthday -> date_of_birth
fav color, favourite colour -> favorite_color
laptop name, computer name -> laptop
college, university -> college

User:
{user_input}
"""

    response = chat(
        model="qwen3.5:4b",
        think=False,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(response["message"]["content"])