import json
import os
from datetime import datetime
from brain.embedding_engine import EmbeddingEngine
class Memory:
    def __init__(self):
        self.file = "memory/user_memory.json"
        if not os.path.exists("memory"):
            os.makedirs("memory")
            
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f, indent=4)

        # Create embedding engine once
        self.embedding_engine = EmbeddingEngine()

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def remember(self, key, value, confidence=1.0):

        data = self.load()

        now = datetime.now().isoformat()


        # Create embedding BEFORE saving
        embedding = self.embedding_engine.create_embedding(value)

        # Convert old memories to new format
        if key in data and isinstance(data[key], str):

            old_value = data[key]

            data[key] = {
                "value": old_value,
                "embedding": self.embedding_engine.create_embedding(old_value),
                "created_at": now,
                "updated_at": now,
                "confidence": confidence
            }

        # Update existing memory
        if key in data:

            data[key]["value"] = value
            data[key]["embedding"] = embedding
            data[key]["updated_at"] = now
            data[key]["confidence"] = confidence

        # Create new memory
        else:

            data[key] = {
                "value": value,
                "embedding": embedding,
                "created_at": now,
                "updated_at": now,
                "confidence": confidence
            }

        self.save(data)

    def recall(self, key):

        data = self.load()

        memory = data.get(key)

        if memory is None:
            return None

        # Support old JSON format
        if isinstance(memory, str):
            return memory

        return memory["value"]
    