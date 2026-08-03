import json
import os


class ShortMemory:

    def __init__(self):

        self.file = "memory/short_memory.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f, indent=4)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def remember(self, role, message):

        data = self.load()

        data.append({
            "role": role,
            "message": message
        })

        # Keep only last 20 messages
        data = data[-20:]

        self.save(data)

    def recall(self):

        return self.load()

    def get_previous_user_message(self):

        data = self.load()

        user_messages = [
            item["message"]
            for item in data
            if item["role"] == "user"
        ]

        if len(user_messages) < 2:
            return None

        return user_messages[-2]

    def get_last_assistant_message(self):

        data = self.load()

        for item in reversed(data):
            if item["role"] == "assistant":
                return item["message"]

        return None

    def clear(self):

        self.save([])
