from brain.embedding_engine import EmbeddingEngine

engine = EmbeddingEngine()

vector = engine.create_embedding(
    "My birthday is 8 June 2007."
)
 
print(type(vector))
print(len(vector))
print(vector[:10])