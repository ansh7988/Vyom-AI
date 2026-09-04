from ollama import chat
def classify(user_input):

    prompt = f"""
You are Vyom's intent classifier.

Return ONLY ONE WORD.
Possible intents:
CHAT
COMMAND
SEARCH
MEMORY

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
    return response["message"]["content"].strip().upper()



