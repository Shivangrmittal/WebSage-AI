from langchain_core.chat_history import InMemoryChatMessageHistory

# Stores chat history for each webpage
chat_store = {}


def get_chat_history(url: str):
    """
    Returns the chat history object for a webpage.
    Creates one if it doesn't exist.
    """

    if url not in chat_store:
        chat_store[url] = InMemoryChatMessageHistory()

    return chat_store[url]