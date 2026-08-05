import json
from ollama import chat


def extract_memory(user_input):

    prompt = f"""
    You are Vyom's Memory Intelligence Engine.

    Your job is to determine whether the user is:

    1. Trying to SAVE memory.
    2. Trying to RECALL memory.
    3. Not talking about memory.

    Return ONLY valid JSON.

    SAVE example:

    {{
    "action":"remember",
    "key":"favorite_color",
    "value":"blue"
    }}

    RECALL example:

    {{
    "action":"recall",
    "key":"favorite_color"
    }}

    NOT MEMORY:

    {{
    "action":"none"
    }}

    Normalize these automatically:

    DOB
    Birth date
    Birthday
    Date of birth
    Born on
    → date_of_birth

    Favourite colour
    Favorite colour
    Fav colour
    Fav color
    Colour
    Color
    → favorite_color

    Laptop
    Laptop name
    Computer
    PC
    → laptop

    College
    University
    Campus
    → college

    Never explain.
    Never add markdown.
    Return JSON only.

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