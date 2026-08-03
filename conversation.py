from brain.personality import get_personality


class Conversation:

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": get_personality()
            }
        ]

    # -----------------------------
    # Add Messages
    # -----------------------------
    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_assistant_message(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })

    # -----------------------------
    # Get Full Conversation
    # -----------------------------
    def get_messages(self):
        return self.messages

    # -----------------------------
    # Previous User Question
    # -----------------------------
    def get_previous_user_message(self):

        user_messages = [
            message["content"]
            for message in self.messages
            if message["role"] == "user"
        ]

        if len(user_messages) < 2:
            return None

        return user_messages[-2]

    # -----------------------------
    # Previous Assistant Reply
    # -----------------------------
    def get_previous_assistant_message(self):

        assistant_messages = [
            message["content"]
            for message in self.messages
            if message["role"] == "assistant"
        ]

        if len(assistant_messages) < 2:
            return None

        return assistant_messages[-2]

    # -----------------------------
    # Last N Messages
    # -----------------------------
    def get_last_messages(self, n):
        return self.messages[-n:]

    # -----------------------------
    # Clear Conversation
    # -----------------------------
    def clear(self):
        self.messages = [
            {
                "role": "system",
                "content": get_personality()
            }
        ]
