# Stores FAISS vector stores for each webpage URL

vector_store_cache = {}


def get_vector_store(url: str):
    """
    Returns the cached vector store if available.
    """

    return vector_store_cache.get(url)


def save_vector_store(url: str, vector_store):
    """
    Saves the vector store in memory.
    """

    vector_store_cache[url] = vector_store