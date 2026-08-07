import json
import os
from datetime import datetime

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

        now = datetime.now().isoformat()

        # Old format (string)
        if key in data and isinstance(data[key], str):

            old_value = data[key]

            data[key] = {
                "value": old_value,
                "created_at": now,
                "updated_at": now,
                "confidence": 1.0
            }

        # Update existing memory
        if key in data:

            data[key]["value"] = value
            data[key]["updated_at"] = now

        # Create new memory
        else:

            data[key] = {
                "value": value,
                "embedding": embedding,
                "created_at": now,
                "updated_at": now,
                "confidence": 1.0
            }

        self.save(data)

        from brain.embedding_engine import EmbeddingEngine
        engine = EmbeddingEngine()
        embedding = engine.create_embedding(value)

    def recall(self, key):

        data = self.load()

        memory = data.get(key)

        if memory:
            return memory["value"]

        return None