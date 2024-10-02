from langchain_community.embeddings.ollama import OllamaEmbeddings


## CREATE AN EMBEDDING FUNCTION

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="phi3:3.8b")
    return embeddings

