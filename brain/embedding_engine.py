from ollama import embeddings


class EmbeddingEngine:

    def __init__(self):

        self.model = "nomic-embed-text"

    def create_embedding(self, text):

        response = embeddings(
            model=self.model,
            prompt=text
        )

        return response["embedding"]