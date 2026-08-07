from ollama import chat
from brain.router import detect_intent 
from brain.personality import get_personality
from brain.conversation import Conversation
from brain.state import VyomState
from classifier import classify
from brain.decision import DecisionEngine
from brain.memory_manager import MemoryManager
from brain.short_memory import ShortMemory
from brain.ai_memory import extract_memory

conversation = Conversation()
state = VyomState()
decision = DecisionEngine()
memory = MemoryManager()
short_memory = ShortMemory()


print("=" * 45)
print("VYOM AI")
print("=" * 45)

print("\nBrain Online!")
print("Type 'exit' to quit.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\nVyom: Goodbye! 👋")
        break

    # -----------------------------
    # Update Brain
    # -----------------------------
    state.set_task(user_input)

    conversation.add_user_message(user_input)
    short_memory.remember("user", user_input)

    intent = detect_intent(user_input)
    state.set_intent(intent)

    action = decision.decide(state)

    print(f"\n[Intent] -> {intent}")
    print(f"[Decision] -> {action}")

    # -----------------------------
    # Handle Previous Question
    # -----------------------------
    if action == "GET_PREVIOUS_QUESTION":

        previous_question = conversation.get_previous_user_message()

        if previous_question is None:
            reply = "You haven't asked a previous question yet."
        else:
            reply = f'Your previous question was:\n"{previous_question}"'

        print(f"\nVyom: {reply}")

        conversation.add_assistant_message(reply)
        short_memory.remember("assistant", reply)
        state.set_last_response(reply)

        continue

# -----------------------------
    # Handle Last User Message
    # -----------------------------
    elif action == "GET_LAST_USER_MESSAGE":

        last_message = short_memory.get_previous_user_message()

        if last_message is None:
            reply = "I couldn't find your last message."
        else:
            reply = f'You just said:\n"{last_message}"'

        print(f"\nVyom: {reply}")

        conversation.add_assistant_message(reply)
        short_memory.remember("assistant", reply)

        state.set_last_response(reply)

        continue


    # -----------------------------
    # Handle Last Assistant Reply
    # -----------------------------
    elif action == "GET_LAST_ASSISTANT_MESSAGE":

        last_reply = short_memory.get_last_assistant_message()

        if last_reply is None:
            reply = "I don't have any previous reply yet."
        else:
            reply = f'My last reply was:\n"{last_reply}"'

        print(f"\nVyom: {reply}")

        conversation.add_assistant_message(reply)
        short_memory.remember("assistant", reply)

        state.set_last_response(reply)

        continue
    # -----------------------------
    # Handle Save Memory
    # -----------------------------
   

    # -----------------------------
    # Handle Recall Memory
    # -----------------------------
# -----------------------------
# AI Memory
    # -----------------------------
    memory_result = extract_memory(user_input)
    print(memory_result)

    if memory_result["intent"] == "remember":

        key = memory_result["entity"]["type"]
        value = memory_result["entity"]["value"]
        confidence = memory_result["entity"].get("confidence", 1.0)

        memory.save(key, value, confidence)

        reply = f"Okay! I'll remember your {key.replace('_', ' ')}."

        print(f"\nVyom: {reply}")

        conversation.add_assistant_message(reply)
        short_memory.remember("assistant", reply)
        state.set_last_response(reply)

        continue


    memory_data = memory.search(user_input)

    if memory_data is not None:

        reply = f"{memory_data}"

        print(f"\nVyom: {reply}")

        conversation.add_assistant_message(reply)
        short_memory.remember("assistant", reply)
        state.set_last_response(reply)

        continue
    
    # -----------------------------
    # Default Chat
    # -----------------------------
    elif action == "CHAT":

        print("\nVyom: ", end="", flush=True)

        assistant_reply = ""

        stream = chat(
            model="qwen3.5:4b",
            messages=conversation.get_messages(),
            think=False,
            stream=True
        )

        for chunk in stream:
            content = chunk["message"]["content"]
            assistant_reply += content
            print(content, end="", flush=True)

        print()

        conversation.add_assistant_message(assistant_reply)
        short_memory.remember("assistant", assistant_reply)
        state.set_last_response(assistant_reply)