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

        data[key] = value

        self.save(data)

    def recall(self, key):

        data = self.load()

        return data.get(key, None)
