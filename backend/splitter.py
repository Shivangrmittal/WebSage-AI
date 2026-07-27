from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Splits LangChain Documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    return chunks