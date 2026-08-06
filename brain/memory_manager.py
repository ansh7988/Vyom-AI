from brain.memory import Memory


class MemoryManager:

    def __init__(self):
        self.memory = Memory()

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

    def search(self, query):

        """
        Search memory using a natural language query.
        Version 1:
        Uses Memory Analyzer to understand the query.
        """

        from brain.memory_analyzer import understand_memory

        result = understand_memory(query)

        if result["intent"] != "recall":
            return None

        result = self.semantic_search(result)


    def semantic_search(self, memory_request):

        """
        Placeholder for future embedding search.
        """

        entity = memory_request["entity"]["type"]

        memory = self.recall(entity)

        if memory is None:
            return []

        return [memory]


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
