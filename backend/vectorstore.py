from langchain_community.vectorstores import FAISS

from embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Creates a FAISS vector store from document chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store