from loaders import load_webpage
from splitter import split_documents
from vectorstore import create_vector_store
from cache import get_vector_store, save_vector_store
from llm import get_llm
from prompts import get_prompt
from memory import get_chat_history


def process_query(url: str, question: str):
    """
    Complete RAG pipeline.

    1. Check cache
    2. Load webpage if needed
    3. Split documents
    4. Create FAISS
    5. Save FAISS
    6. Retrieve relevant chunks
    """

    # -----------------------------
    # Check Cache
    # -----------------------------

    vector_store = get_vector_store(url)

    cache_used = True

    if vector_store is None:

        cache_used = False

        print("Building FAISS Index...")

        documents = load_webpage(url)

        chunks = split_documents(documents)

        vector_store = create_vector_store(chunks)

        save_vector_store(url, vector_store)

    else:

        print("Using Cached FAISS Index...")

    # -----------------------------
    # Retrieve Relevant Chunks
    # -----------------------------

    retriever = vector_store.as_retriever(
       search_type="mmr",
       search_kwargs={
          "k": 3,
          "fetch_k": 20
        }
    )

    retrieved_docs = retriever.invoke(question)

    context = ""

    for doc in retrieved_docs:

       context += doc.page_content

       context += "\n\n"


    history = get_chat_history(url)

    prompt = get_prompt()

    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke(
    {
        "context": context,
        "history": history.messages,
        "question": question
    }
    )

    history.add_user_message(question)
    history.add_ai_message(response.content)

    return {

        "cache_used": cache_used,

        "answer": response.content

    }