import json
import os


class Memory:

    def __init__(self):

        self.file = "memory/user_memory.json"

        if not os.path.exists("memory"):
            os.makedirs("memory")

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f, indent=4)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def remember(self, key, value):

        data = self.load()

        from datetime import datetime

        data[key] = {
            "value": value,
            "type": "preference",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.save(data)

    def recall(self, key):

        data = self.load()

        memory = data.get(key)

        if memory:
            return memory["value"]

        return None