from brain.memory import Memory


class MemoryManager:

    def __init__(self):

        from brain.embedding_engine import EmbeddingEngine

        self.memory = Memory()
        self.embedding = EmbeddingEngine()

    # -----------------------------
    # Save Memory
    # -----------------------------
    def save(self, entity, value, confidence=1.0):

        self.memory.remember(
            key=entity,
            value=value,
            confidence=confidence
        )

    # -----------------------------
    # Recall Memory
    # -----------------------------
    def recall(self, entity):

        memory = self.memory.recall(entity)

        if memory is None:
            return None

        return memory

    # -----------------------------
    # Search (V1)
    # -----------------------------
    def search(self, query):

        from brain.memory_analyzer import understand_memory

        result = understand_memory(query)

        if result["intent"] != "recall":
            return None

        entity = result["entity"]

        return self.semantic_search(entity)

    # -----------------------------
    # Semantic Search (V1)
    # -----------------------------
    def semantic_search(self, entity):

        """
        Temporary semantic search.

        Currently searches by entity name.

        Later this function will use embeddings.
        """

        key = entity["type"]

        memory = self.recall(key)

        return memory

    # -----------------------------
    # Rank Memories (Future)
    # -----------------------------
    def rank_memories(self, query, memories):

        return memories

    # -----------------------------
    # Check Memory
    # -----------------------------
    def exists(self, entity):

        return self.recall(entity) is not None

    # -----------------------------
    # Delete Memory
    # -----------------------------
    def delete(self, entity):

        data = self.memory.load()

        if entity in data:

            del data[entity]

            self.memory.save(data)

            return True

        return False

    # -----------------------------
    # Get All Memories
    # -----------------------------
    def get_all(self):

        return self.memory.load()